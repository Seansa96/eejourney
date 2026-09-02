# Rebuilding CIR Assessment Maker From Scratch

## A Guided Learning Curriculum Based on the First Working Version

This guide is for rebuilding CIR Assessment Maker yourself, deliberately and in small
working increments. It is not intended to reproduce the current repository by copying
files. Its purpose is to teach you how the application fits together, why its boundaries
exist, and how to reason through each decision.

The historical starting point is Git commit:

```text
1559b2f basic core mvp established
```

That commit, created June 7, 2026, is the first complete runnable version in the
repository history. Earlier commits contain planning and repository setup but not a
functional application.

The first working version already supported the essential loop:

```text
Load assessment
-> start attempt
-> answer questions
-> complete attempt
-> review results
-> optionally commit grade
```

Your first objective is to rebuild only that loop. Do not begin with SQLite, symbolic
mathematics, code execution, circuit editing, adaptive recommendations, LAN hosting, or
the current collection of assessment types. Those features are valuable precisely
because they were added to a stable core.

---

## 1. How to Use This Guide

### Build in a separate workspace

Do not learn by repeatedly deleting pieces from the main repository. Create a sibling
directory and initialize a new Git repository:

```powershell
New-Item -ItemType Directory C:\Users\SeanS\Downloads\cir_app_rebuild
Set-Location C:\Users\SeanS\Downloads\cir_app_rebuild
git init
```

Keep the original repository available as a reference, but do not copy entire files from
it. When you are stuck, inspect a historical file intentionally:

```powershell
git -C C:\Users\SeanS\Downloads\cir_app show 1559b2f:path/to/file
```

Use this order when asking for help:

1. State what you believe the component should do.
2. Show the smallest failing example.
3. Explain what you already tried.
4. Ask for a hint before asking for a full implementation.
5. After receiving help, rewrite the idea in your own words.

### Keep a build journal

Create a simple `LEARNING.md` in the rebuild repository. After each session, record:

- What you implemented.
- What surprised you.
- One bug and its cause.
- One design decision you would make differently.
- One question you still have.

### Use checkpoints

Every stage in this guide ends with a suggested commit. Do not move forward while the
current stage is broken. A small working commit is more useful than a week of half-wired
features.

### Do not optimize the first pass

The first implementation should be explicit and a little repetitive. You are learning
the data flow. Abstract only after you can point to concrete duplicated behavior.

---

## 2. The System You Are Rebuilding

The first working application had three main layers and one frontend:

```text
Browser
  |
  | HTTP/JSON
  v
QuizApp.Api
  |
  | calls services through domain contracts
  v
QuizApp.Core
  |
  | repository interfaces
  v
QuizApp.Infrastructure
  |
  | reads/writes YAML and JSON
  v
data/
```

### Core

Core describes what the application means:

- What is an assessment?
- What is a question?
- What is an attempt?
- What makes an answer correct?
- When may a grade be committed?
- What repository behavior does the application require?

Core should not know how YAML is parsed, where files are stored, which HTTP route is
used, or how a button looks.

### Infrastructure

Infrastructure performs technical work:

- Deserialize YAML and JSON.
- Map file DTOs into domain models.
- Read categories and settings.
- Save attempts.
- Save grade-log entries.

### API

The API translates HTTP requests into service calls:

- Parse route and body values.
- Call a service.
- Convert expected failures into useful status codes.
- Configure dependency injection and serialization.

The API should not contain scoring rules or manually parse assessment YAML.

### Frontend

The Astro frontend:

- Calls the API.
- Maintains the currently selected assessment and attempt.
- Renders question controls.
- Submits answers.
- Displays feedback according to practice/scored rules.

It does not decide authoritative correctness.

---

## 3. Prerequisites

You do not need mastery before beginning, but you should be able to explain these ideas as
you encounter them.

### C# and .NET

- Classes and records
- Enums
- Interfaces
- Generic collections
- `async` and `await`
- LINQ basics
- Dependency injection
- Nullable reference types
- Pattern matching

### Web fundamentals

- HTTP methods
- Status codes
- JSON request and response bodies
- Browser fetch requests
- CORS during local development
- Client state versus server state

### TypeScript and Astro

- Interfaces
- Union types
- DOM query and event listeners
- Template strings
- Form submission
- Async fetch calls
- Basic responsive CSS

### Testing

- Arrange, Act, Assert
- Unit tests versus integration tests
- Fake/in-memory repositories
- Testing behavior rather than private implementation

---

# Part I: Rebuild the First Working MVP

## 4. Stage Zero: Define the Boundary

Before creating projects, write down the smallest product.

### Required behavior

- Load categories.
- List assessments for a category.
- Load one assessment.
- Start a practice or scored attempt.
- Randomize question order when configured.
- Answer multiple-choice questions.
- Answer select-all questions.
- Enter a free response and self-check it.
- Complete an attempt.
- Review results.
- Commit a completed score to a grade log.
- Read and update basic settings.
- Validate assessment definitions.

### Explicitly excluded

- Authentication
- Database
- Search
- Assessment creation UI
- Timers
- Math rendering
- Code execution
- Multiple users
- Rich analytics

### Questions to answer

1. Which information describes an assessment permanently?
2. Which information belongs to one learner's attempt?
3. Which decisions must be authoritative on the backend?
4. Which data must survive a browser refresh?
5. Which IDs must remain stable?

The crucial distinction is:

```text
Assessment definition != attempt state
```

An assessment says what questions exist and what answers are expected. An attempt says
which learner session answered what, in which order, and when.

Suggested commit:

```text
docs: define MVP scope and domain boundaries
```

---

## 5. Stage One: Scaffold the Solution

Create the backend projects:

```powershell
New-Item -ItemType Directory backend\src
New-Item -ItemType Directory backend\tests

dotnet new sln -n QuizApp -o backend
dotnet new classlib -n QuizApp.Core -o backend\src\QuizApp.Core
dotnet new classlib -n QuizApp.Infrastructure -o backend\src\QuizApp.Infrastructure
dotnet new webapi -n QuizApp.Api -o backend\src\QuizApp.Api
dotnet new xunit -n QuizApp.Tests -o backend\tests\QuizApp.Tests
```

Add references:

```powershell
dotnet sln backend\QuizApp.sln add backend\src\QuizApp.Core\QuizApp.Core.csproj
dotnet sln backend\QuizApp.sln add backend\src\QuizApp.Infrastructure\QuizApp.Infrastructure.csproj
dotnet sln backend\QuizApp.sln add backend\src\QuizApp.Api\QuizApp.Api.csproj
dotnet sln backend\QuizApp.sln add backend\tests\QuizApp.Tests\QuizApp.Tests.csproj

dotnet add backend\src\QuizApp.Infrastructure\QuizApp.Infrastructure.csproj reference backend\src\QuizApp.Core\QuizApp.Core.csproj
dotnet add backend\src\QuizApp.Api\QuizApp.Api.csproj reference backend\src\QuizApp.Core\QuizApp.Core.csproj
dotnet add backend\src\QuizApp.Api\QuizApp.Api.csproj reference backend\src\QuizApp.Infrastructure\QuizApp.Infrastructure.csproj
dotnet add backend\tests\QuizApp.Tests\QuizApp.Tests.csproj reference backend\src\QuizApp.Core\QuizApp.Core.csproj
dotnet add backend\tests\QuizApp.Tests\QuizApp.Tests.csproj reference backend\src\QuizApp.Infrastructure\QuizApp.Infrastructure.csproj
```

Add YamlDotNet to Infrastructure. Do not add it to Core.

### Think about

- Why may Infrastructure reference Core, while Core should not reference Infrastructure?
- Why should tests reference both?
- Why is the API the composition root?

### Checkpoint

```powershell
dotnet build backend\QuizApp.sln
dotnet test backend\QuizApp.sln
```

Suggested commit:

```text
chore: scaffold layered backend solution
```

---

## 6. Stage Two: Model the Domain

Start with domain records and enums. Do not start with controllers.

### Enums

Define:

- `AssessmentType`: Quiz, Test
- `AssessmentMode`: Practice, Scored
- `QuestionType`: MultipleChoice, SelectAll, FreeResponse
- `QuestionOrderMode`: Randomized, Static

Include an `Unknown` value for enums loaded from external files. It gives validation a
chance to report a useful error instead of silently accepting bad input.

### Definition models

Model:

- `Category`
- `SubCategory`
- `AppSettings`
- `AssessmentDefinition`
- `QuestionDefinition`
- `ChoiceOption`
- `AnswerDefinition`
- `AssessmentSummary`

### Attempt models

Model:

- `Attempt`
- `AttemptAnswer`
- `SubmittedAnswer`
- `AnswerEvaluation`
- `AttemptResults`
- `QuestionResult`
- `GradeLogEntry`
- `GradeLogSummary`

### Stable IDs

Use string IDs:

```text
calculus-2
area-between-curves
area-between-curves-basic
q001
```

Do not use a question's position as its identity. Positions change under randomization.

### A useful design exercise

For every property, label it as one of:

- authored definition
- runtime state
- derived result
- persistence metadata

If a property seems to belong to two categories, investigate whether two models are being
collapsed together.

### Questions to answer

1. Why does `Attempt` store question IDs instead of copied questions?
2. Why does `SubmittedAnswer` support several nullable answer shapes?
3. Why is `AnswerEvaluation` stored with an attempt answer?
4. Which fields should be immutable after attempt creation?

Suggested commit:

```text
feat: define assessment attempt and grade domain models
```

---

## 7. Stage Three: Validate Assessment Definitions

Treat assessment files as untrusted input, even though they are local.

Create:

```text
ValidationIssue
AssessmentValidationResult
AssessmentValidator
```

Validate:

- missing assessment ID
- missing category ID
- missing question prompt
- duplicate question IDs
- invalid assessment type
- invalid question type
- multiple choice without choices
- answer choice ID not found
- select-all answer IDs not found
- quiz over 50 questions
- test over 200 questions
- negative timers

### Why validation is separate from parsing

Parsing answers:

> Can this text become an object?

Validation answers:

> Is this object meaningful and safe for the application to use?

A syntactically valid YAML file may still reference a nonexistent answer choice.

### Write tests first

Create one valid assessment factory in tests. Change one property per test and assert the
specific issue code.

Avoid tests that only assert `IsValid == false`. Verify why validation failed.

### Questions to answer

1. Should the validator throw exceptions or return issues?
2. Which failures can be reported together?
3. Why validate again when starting an attempt?
4. What should happen to one invalid file when listing many files?

Suggested commit:

```text
feat: validate assessment definitions
```

---

## 8. Stage Four: Define Repository Interfaces

Core needs data but should not know about files.

Define:

- `ISettingsRepository`
- `ICategoryRepository`
- `IAssessmentRepository`
- `IAttemptRepository`
- `IGradeLogRepository`

Keep interfaces based on application needs, not generic CRUD.

Examples:

```csharp
Task<IReadOnlyList<Category>> ListAsync(...);
Task<IReadOnlyList<AssessmentSummary>> ListByCategoryAsync(string categoryId, ...);
Task<AssessmentDefinition?> GetByIdAsync(string assessmentId, ...);
Task SaveAsync(Attempt attempt, ...);
```

### Why not one generic repository?

Settings, assessments, attempts, and grade logs have different access patterns. A generic
repository often hides those differences behind vague methods and leaks persistence
assumptions into Core.

### Questions to answer

1. Does Core need a filename, or does it need an assessment ID?
2. Should listing assessments return full definitions or summaries?
3. Which operation must be idempotent?
4. What will make a later SQLite implementation possible?

Suggested commit:

```text
feat: define persistence contracts
```

---

## 9. Stage Five: Build the File Format Boundary

Create file DTOs that resemble YAML and JSON closely. Keep them separate from the domain
models.

### Why DTOs exist

The file schema may use:

```yaml
assessmentType: quiz
type: multipleChoice
```

The domain uses enums and explicit defaults. Mapping is where external strings become
internal meaning.

Implement:

- `FileDtos.cs`
- `FileDtoMapper.cs`
- `FileFormat.cs`

`FileFormat` should:

- recognize `.json`
- otherwise parse YAML
- serialize JSON and YAML
- use camel-case naming

### Mapping rules

Map every external enum string explicitly. Do not scatter string comparisons throughout
services.

Decide how missing lists behave:

- `null` from a file should usually become an empty collection in the domain.
- missing optional text may remain `null`.
- missing required data should be reported by validation.

### Security and correctness detail

When accepting a filename for validation, reduce it to `Path.GetFileName(fileName)` before
searching. This prevents a caller from traversing outside the assessment directory.

### Tests

- YAML assessment loads.
- JSON assessment loads.
- enum strings map correctly.
- missing optional collections do not crash.
- validation finds bad references after mapping.

Suggested commit:

```text
feat: map YAML and JSON files into domain models
```

---

## 10. Stage Six: Implement File Repositories

Create `FileStorageOptions` with paths derived from one data root:

```text
data/
  settings.yaml
  categories/
  assessments/
  attempts/
  grades/
  samples/
```

Implement each repository narrowly.

### Settings

- Return defaults when the file does not exist.
- Save a complete settings document.

### Categories

- Enumerate category YAML/JSON files.
- Return sorted categories.

### Assessments

- Enumerate both `assessments/` and `samples/`.
- Map each file to the domain.
- List summaries by category.
- Get a definition by stable ID.
- Validate a selected file.

### Attempts

- Store one JSON file per attempt ID.
- Replace the file when the attempt changes.
- Use a generated GUID-like stable attempt ID.

### Grade log

- Store a list of grade entries.
- Avoid duplicate commits for one attempt.

### Think about failure behavior

The historical first version returned `null` for unreadable files in some paths. As a
learning exercise, decide whether listing should:

- fail the whole request,
- skip the bad file and log it,
- or return both valid records and diagnostics.

There is no universally correct answer. State your chosen contract.

Suggested commit:

```text
feat: add file-backed repositories
```

---

## 11. Stage Seven: Implement Scoring

Build scoring before attempt orchestration.

### Multiple choice

Compare stable choice IDs case-insensitively.

### Select all

Compare sets, not list order:

```text
[a, b, c] == [c, a, b]
```

Also ensure duplicates do not accidentally change the result.

### Free response

The first MVP uses human self-check:

```text
selfCheckCorrect == true
```

Do not attempt semantic grading.

### Result visibility

Practice mode shows feedback after answering.

Scored mode hides:

- correctness
- expected answer
- explanation

until completion.

This rule belongs in backend result construction. The frontend may hide data for display,
but the API must not leak answers it claims to hide.

### Score calculation

```text
correct count / total questions * 100
```

Use the stored question order for the denominator and result order.

### Tests

- correct and incorrect multiple choice
- select-all order independence
- missing select-all choice
- free-response self-check true/false
- practice feedback visible
- scored feedback hidden before completion
- scored feedback visible after completion

### Questions to answer

1. Why does scoring accept a question definition and submitted answer?
2. Why should result construction be separate from answer evaluation?
3. What happens when a question is unanswered?
4. Should unanswered questions count in the denominator?

Suggested commit:

```text
feat: score MVP question types and build results
```

---

## 12. Stage Eight: Implement the Attempt Lifecycle

`AttemptService` coordinates repositories, validation, settings, randomization, and
scoring.

### Start

1. Load assessment by ID.
2. Validate it.
3. Load settings.
4. Select explicit mode or assessment default.
5. Copy question IDs into a new list.
6. Shuffle when both the assessment and settings allow it.
7. Create an attempt.
8. Save it.

Use a Fisher-Yates shuffle. Store the result once.

### Submit answer

1. Load the attempt.
2. Reject completed attempts.
3. Load and validate the assessment.
4. Find the question by stable ID.
5. Score the answer.
6. Replace any previous answer for that question.
7. Save the updated attempt.

Replacing an answer makes navigation and editing possible without duplicate answer rows.

### Complete

1. Set `CompletedAt` if it is not already set.
2. Save the attempt.
3. Build results.

Make completion idempotent. Repeating it should not continually change the completion
time or duplicate data.

### Randomization reasoning

Never reshuffle while displaying an attempt. The attempt's `QuestionOrder` is the
authoritative order for:

- navigation
- results
- review
- refresh

### Tests

Use in-memory fake repositories to test:

- start creates an attempt
- randomization preserves all IDs
- submission stores evaluation
- resubmission replaces the answer
- unknown question is rejected
- completed attempts reject submissions
- completion is idempotent
- results follow saved order

Suggested commit:

```text
feat: implement assessment attempt lifecycle
```

---

## 13. Stage Nine: Implement Grade Commit

`GradeLogService` should commit only a completed attempt.

Flow:

1. Get attempt results.
2. Reject incomplete attempts.
3. Check for an existing grade with the same attempt ID.
4. Return the existing entry or create one.
5. Save the log.

This makes grade commit idempotent.

Compute summary:

- number of entries
- average percent
- entries ordered by commit time

### Think about

- Is a grade a snapshot or a live view of an attempt?
- What happens if an assessment title changes later?
- Why store both assessment ID and title?
- Should practice attempts be committable?

For the MVP, permit explicit practice commits and optionally auto-commit scored attempts
according to settings.

Suggested commit:

```text
feat: add grade-log commit and summary
```

---

## 14. Stage Ten: Expose the Web API

Configure in `Program.cs`:

- JSON camel case
- string enum serialization
- Swagger in development
- dependency injection
- data-root calculation
- local frontend CORS

### MVP endpoints

```text
GET  /api/settings
PUT  /api/settings
GET  /api/categories
GET  /api/assessments?categoryId=...
GET  /api/assessments/{assessmentId}
POST /api/assessments/validate
POST /api/attempts
POST /api/attempts/{attemptId}/answers
POST /api/attempts/{attemptId}/complete
GET  /api/attempts/{attemptId}/results
POST /api/grades/commit
GET  /api/grades/summary
```

### Keep request contracts separate

Create API request DTOs such as:

- `StartAttemptRequest`
- `SubmitAnswerRequest`
- `ValidateAssessmentFileRequest`
- `CommitGradeRequest`

Map them to domain models. HTTP-specific concerns should not be added to Core.

### Error semantics

Return structured errors:

```json
{
  "error": {
    "code": "ATTEMPT_NOT_FOUND",
    "message": "..."
  }
}
```

Use:

- `400` for invalid requested operations
- `404` for missing resources
- `201` when creating an attempt
- `200` for successful reads and updates

### Manual API test

Before creating a frontend, use Swagger or an HTTP file to:

1. List categories.
2. List assessments.
3. Start an attempt.
4. Submit one answer.
5. Complete it.
6. Commit the grade.

If this flow does not work without a frontend, the backend is not ready.

Suggested commit:

```text
feat: expose core assessment API
```

---

## 15. Stage Eleven: Author Minimal Data

Create one category:

```yaml
schemaVersion: 1
id: calculus-2
title: Calculus 2
subcategories:
  - id: area-between-curves
    title: Area Between Curves
```

Create one assessment containing exactly:

- one multiple-choice question
- one free-response self-check question
- one select-all question

Create settings with practice/scored defaults and randomization.

### Why only one assessment?

Content volume can hide architecture bugs. One assessment is enough to prove:

- parsing
- validation
- category filtering
- all three question controls
- scoring
- review

### Authoring checks

- IDs are unique.
- Answer IDs exist.
- Every prompt is meaningful.
- The explanation teaches why.
- The schema version is present.

Suggested commit:

```text
content: add first category and sample assessment
```

---

## 16. Stage Twelve: Scaffold the Astro Frontend

Create the Astro project and keep the first UI simple.

The historical version used:

```text
frontend/src/pages/index.astro
frontend/src/styles/global.css
```

For learning, you may begin in one page, but divide code into conceptual sections:

- types
- API helper
- state
- navigation
- rendering
- event binding

### Frontend state

Track:

- settings
- categories
- assessment summaries
- selected category
- selected assessment
- current attempt
- current question index
- latest results
- grade summary

### API helper

Write one generic helper:

```ts
async function api<T>(path: string, init?: RequestInit): Promise<T>
```

It should:

- prepend the API base
- set JSON content type
- throw useful errors
- parse an empty `204` safely

### Think about

- Which state originates from the server?
- Which state is transient UI state?
- What must be reloaded after a mutation?
- What should happen when a request fails?

Suggested commit:

```text
feat: scaffold Astro application shell
```

---

## 17. Stage Thirteen: Build the Load Flow

Implement:

1. Fetch settings and categories on startup.
2. Select a category.
3. Fetch assessments for that category.
4. Select an assessment.
5. Fetch its complete definition.
6. Choose practice or scored mode.
7. Start an attempt.

Do not let the frontend invent the question order. Use the order returned in the attempt.

### Render loading and empty states

Every asynchronous section should handle:

- loading
- successful data
- no data
- error

### Questions to answer

1. When should assessment summaries be enough?
2. When is the full definition needed?
3. Should changing categories discard an active attempt?
4. Which buttons should be disabled while a request is running?

Suggested commit:

```text
feat: load categories and start assessments
```

---

## 18. Stage Fourteen: Render and Submit Questions

Create one renderer that switches by question type.

### Multiple choice

Use radio inputs in the learning rebuild, even if the current app uses cards. Native
controls let you understand semantics before styling.

### Select all

Use checkboxes and collect selected IDs.

### Free response

Use a textarea and a self-check checkbox in the historical MVP. Later, you will improve
this flow.

### Submit

Build a `SubmittedAnswer` matching the active type and send it to:

```text
POST /api/attempts/{attemptId}/answers
```

Reload results after submission. In practice mode, display feedback. In scored mode,
verify the API does not provide hidden feedback.

### Navigation

Add Previous and Next. The current question is determined from:

```text
attempt.questionOrder[currentIndex]
```

Do not reorder the assessment's authored question list itself.

### Common bug

Rendering new HTML destroys old DOM nodes and their listeners. Bind events after every
render or use event delegation.

Suggested commit:

```text
feat: answer and navigate MVP questions
```

---

## 19. Stage Fifteen: Complete, Review, and Commit

Add:

- Complete button
- final results view
- correct count
- total questions
- percent score
- per-question answer and explanation
- explicit practice-grade commit
- automatic scored commit when configured

### Completion confirmation

Warn if unanswered questions remain. The backend may still allow completion, but the user
should understand the consequence.

### Grade log view

Display:

- assessment title
- mode
- score
- committed date

At this stage, do not add sorting, analytics, bulk deletion, or charts.

Suggested commit:

```text
feat: complete attempts and review grade log
```

---

## 20. Stage Sixteen: Settings

Implement controls for:

- default mode
- randomized/static order
- default quiz length
- default test length
- optional timers
- auto-commit scored attempts

Even though timers are stored, do not enforce them yet. A field existing in configuration
does not mean its behavior is implemented.

### Important lesson

Distinguish:

- schema support
- persistence support
- UI support
- runtime behavior

A feature is not complete until all required layers agree.

Suggested commit:

```text
feat: add basic settings management
```

---

## 21. Stage Seventeen: Verify the MVP

Run:

```powershell
dotnet test backend\QuizApp.sln

Set-Location frontend
npm run build
```

Manual flow:

1. Start backend.
2. Start frontend.
3. Load the assessment.
4. Begin practice mode.
5. Answer all three question types.
6. Confirm immediate feedback.
7. Complete and commit.
8. Begin scored mode.
9. Confirm feedback is hidden.
10. Complete and confirm feedback appears.
11. Restart both processes.
12. Confirm file-backed attempts and grades remain.

### Definition of done

You should be able to explain, without opening code:

- how a YAML choice ID becomes a scored answer
- how an attempt finds its assessment
- where randomized order is stored
- why practice and scored results differ
- how dependency injection chooses file repositories
- why committing the same attempt twice does not duplicate the grade

Suggested commit:

```text
feat: complete core assessment MVP
```

This is your equivalent of historical commit `1559b2f`.

---

# Part II: Rebuild the Project's Evolution

Do not implement every chapter automatically. Each chapter is a separate learning cycle:

```text
problem -> design -> contract -> tests -> backend -> frontend -> content -> review
```

## 22. Assessment Creation

Historical reference:

```text
3e021b6 Added test creation flow and api endpoints
```

Learn:

- save/update repository methods
- frontend forms
- validation before persistence
- generated IDs
- preview versus authoritative backend validation

Start with only quiz/test metadata and one multiple-choice editor.

Think about:

- How do you prevent overwriting an existing assessment?
- Should drafts be valid assessments?
- Is YAML the source of truth or merely an export format?

---

## 23. Markdown, Math, and Media

Historical reference:

```text
cac7900 Added image, LaTex, and markdown schema support
```

Learn:

- additive schema evolution
- media metadata and alt text
- Markdown rendering
- KaTeX pipeline
- safe handling of authored content
- YAML escaping rules

Implement media first, then Markdown, then math.

Do not render arbitrary unsanitized HTML.

---

## 24. Resumable Attempt Sessions

Historical reference:

```text
48c2843 added sessions and attempt management
```

Add:

- attempt status
- pause
- resume
- delete
- review
- explicit lifecycle timestamps

Draw a state machine before coding:

```text
inProgress -> paused -> inProgress
inProgress -> completed
inProgress -> deleted
paused     -> deleted
completed  -> deleted
```

Define which operations are legal in each state.

---

## 25. Numeric and Symbolic Answers

Historical reference:

```text
9c419b6 Added symbolicResponse and LaTex friendly math input
```

Build in this order:

1. numeric response with tolerance
2. MathLive input
3. symbolic response schema
4. symbolic engine interface
5. local Compute Engine adapter
6. timeout and parse-error handling

The backend remains authoritative. The frontend provides input assistance, not final
grading.

---

## 26. Worked Examples

Historical reference:

```text
4427728 Added whole new assessment type...
```

This is your first major lesson in assessment-type-specific state.

Add:

- worked-example definition
- ordered steps
- locked progression
- hints
- failed-step remediation
- previous-step review
- completion after final correct step

Do not force worked examples through quiz semantics merely because both contain questions.

---

## 27. Analytics and Memory-First Attempts

Historical reference:

```text
04594b1 Updated Grade Log functionality and frontend
```

Add:

- in-memory active attempt store
- durable paused/completed attempts
- areas
- category/subcategory aggregation
- question-type statistics
- weak-topic summaries

Questions:

- Which calculations use committed grades?
- Which diagnostics may use practice attempts?
- How do you avoid counting one attempt twice across memory and persistence?

---

## 28. Code Questions and CodeMirror

Historical progression:

```text
code question/Piston work
6c0973f CodeMirror 6 editor
317478a editor completion
```

Separate:

- editor experience
- submitted source schema
- harness generation
- execution adapter
- result interpretation
- security limits

Never let the browser call the code runner directly.

---

## 29. Guided Projects

Historical reference:

```text
3281fa7 Added guided project assessment type
```

Add:

- editable file definitions
- session file state
- required and bonus checks
- app-managed compilation
- project completion rules

Begin with the historical header-concatenation model, then explain why real multi-file
projects need a workspace runner.

---

## 30. Recall Drills

Historical reference:

```text
8bf7078 Added new assessment type recallDrill
```

Model a different loop:

```text
prompt -> attempt recall -> reveal -> self-rate -> next item
```

Learn:

- rating enums
- per-item progress
- weak-tag summaries
- unscored instructional sessions

Do not add scheduling until the base recall session is stable.

---

## 31. Question-Bank Sampling

Historical reference:

```text
b1a5edd attemptQuestionCount
```

Add an authored bank size and served attempt size.

Sample once when starting the attempt, then persist selected IDs in question order.

Test:

- no duplicates
- requested count
- stable resume
- results contain only sampled questions

---

## 32. SQLite Retention and Assessment Catalog

Historical reference:

```text
dd71e0b SQLite catalog and guided navigation
```

Migrate in two separate conceptual steps:

1. attempts/grades to SQLite
2. authored assessment metadata to a queryable SQLite catalog

Keep authored YAML as source of truth.

Learn:

- schema initialization
- idempotent migration
- import metadata
- hybrid repositories
- fallback behavior
- preserving the last valid imported record

Never delete legacy data during the first successful migration.

---

## 33. Circuit Questions

Historical reference:

```text
dd71e0b circuit assessments
```

This chapter teaches structured visual answers:

- circuit component catalog
- diagram schema
- SVG renderer
- pointer events
- topology scoring
- meter placement
- retained visual state

Keep visual representation separate from electrical meaning.

---

## 34. Concept Lessons and Interactive Explorations

Historical reference:

```text
58db774 concept lesson and interactive exploration
```

Concept lessons add sequential instructional sections.

Interactive explorations add:

- declarative controls
- derived views
- persisted control state
- interaction completion rules

Do not permit arbitrary authored JavaScript. Evaluate a constrained expression model.

---

## 35. Multipart Questions and Adaptive Navigation

Historical reference:

```text
317478a multipart scoring and adaptive navigation
```

Multipart questions introduce fractional points:

```text
parent question = 1 point
each of N parts = 1/N point
```

Adaptive navigation introduces recommendations based on learning history.

Keep these separate internally:

- scoring calculates evidence
- recommendation service interprets evidence
- UI labels suggestions

Do not let the recommendation UI silently change grades.

---

## 36. LAN Server Distribution

This is the current branch's next evolution. Treat it as deployment and security work,
not merely changing `localhost` to `0.0.0.0`.

Learn:

- same-origin static frontend hosting
- HTTPS certificates
- authentication cookies
- token verification
- CSRF protection
- rate limiting
- host firewall scope
- shared versus user-owned data

The first LAN version remains one shared trusted workspace. User ownership is a later
schema and authorization change.

---

# Part III: How to Think While Rebuilding

## 37. Trace One Feature Vertically

For any feature, trace:

```text
YAML/JSON
-> file DTO
-> mapper
-> domain model
-> validator
-> repository
-> service
-> API contract
-> frontend type
-> renderer/input
-> submitted request
-> persistence
-> result/review
-> tests
```

If a feature breaks, identify the first boundary where the expected value changes.

---

## 38. Ask Ownership Questions

For every rule, ask:

- Does the browser own this decision?
- Does the API own this translation?
- Does Core own this rule?
- Does Infrastructure own this mechanism?

Examples:

- "Multiple choice A is correct" belongs to assessment data.
- "Compare submitted choice ID" belongs to scoring.
- "Read YAML" belongs to Infrastructure.
- "Show a green card" belongs to the frontend.

---

## 39. Prefer Invariants Over Patches

An invariant is a statement that should always be true:

- question IDs are unique
- answer choice IDs exist
- completed attempts cannot accept answers
- attempt order never changes after start
- one attempt has at most one committed grade

When a bug appears, ask which invariant was missing or unenforced.

---

## 40. Test the Risk, Not the Line Count

High-risk behavior:

- scoring
- state transitions
- persistence migration
- hidden feedback
- destructive deletion
- external code execution
- authentication

Low-risk behavior:

- changing a label
- adding one validated content file
- adjusting a nonfunctional color

Match test effort to the blast radius.

---

## 41. Recognize Cross-Layer Feature Cost

A new question type is not one enum value. It usually requires:

- schema
- DTO mapping
- validation
- submitted answer shape
- scoring
- attempt persistence
- API serialization
- input UI
- review UI
- analytics
- tests
- sample content

Write this checklist before estimating a feature.

---

## 42. Debug Systematically

When something fails:

1. Reproduce with the smallest case.
2. Identify whether failure is parse, validation, state, scoring, persistence, API, or UI.
3. Inspect the value at one boundary at a time.
4. Write a focused test when the failure is backend behavior.
5. Fix the cause, not only the visible symptom.
6. Rerun the narrow test.
7. Run the relevant build.

Examples:

- YAML error: parse the one file directly.
- Wrong score: call `ScoringService` in a unit test.
- Resume bug: inspect persisted attempt and state transition.
- UI selection bug: inspect DOM state and submitted request separately.

---

# Part IV: Suggested Study Schedule

## 43. Twelve-Session MVP Track

### Session 1

- Write scope.
- Draw architecture.
- Scaffold projects.

### Session 2

- Define domain enums and records.
- Classify definition versus state.

### Session 3

- Write validator and validation tests.

### Session 4

- Define repository interfaces.
- Create file DTOs and mapper.

### Session 5

- Implement YAML/JSON reading.
- Implement settings/category/assessment repositories.

### Session 6

- Implement scoring and tests.

### Session 7

- Implement attempts and randomization.

### Session 8

- Implement grade log.
- Expose API endpoints.

### Session 9

- Create minimal content.
- Exercise complete API flow without frontend.

### Session 10

- Scaffold Astro.
- Load categories and assessments.

### Session 11

- Render questions.
- Submit answers.
- Navigate attempts.

### Session 12

- Complete/review/commit.
- Add settings.
- Run full manual MVP flow.

Do not measure success by finishing in twelve calendar days. Repeat a session when its
mental model is still blurry.

---

## 44. Questions You Should Eventually Answer

### Domain

- Why are records a good fit for these models?
- When would a class be preferable?
- Why are stable IDs better than indexes?
- Why is an assessment definition immutable during an attempt?

### Architecture

- What dependency direction does the solution enforce?
- Why do repository interfaces live in Core?
- Why do file DTOs live in Infrastructure?
- Why is `Program.cs` called the composition root?

### Persistence

- What corruption risks exist with direct file replacement?
- When does SQLite become preferable?
- What makes a migration idempotent?
- Why should authored content and attempt state remain separate?

### Frontend

- Why should the frontend not score authoritative answers?
- What state survives a render?
- What state survives a refresh?
- What state survives a server restart?

### Security

- Which data is untrusted?
- Which endpoints mutate state?
- What must never be exposed to the browser?
- Why does LAN access still require HTTPS?

---

## 45. A Good Definition of Learning

You have learned a component when you can:

1. Explain why it exists.
2. Rebuild a smaller version without looking.
3. Predict how it fails.
4. Write a focused test for its contract.
5. Change it without breaking an unrelated layer.
6. Describe what a future implementation could replace.

The objective is not to memorize this repository. It is to acquire the ability to design
another application with similar constraints and recognize the same architectural
problems when they appear in a different form.

---

## 46. Historical Reference Map

Use these commits only after attempting the relevant stage yourself:

| Commit | Milestone |
| --- | --- |
| `1559b2f` | First complete core MVP |
| `3e021b6` | Assessment creation flow |
| `cac7900` | Markdown, LaTeX, and media |
| `48c2843` | Attempt sessions and management |
| `9c419b6` | Symbolic responses and MathLive |
| `4427728` | Worked Examples |
| `04594b1` | Analytics and memory-first attempts |
| `6c0973f` | CodeMirror editor and expanded content |
| `3281fa7` | Guided Projects |
| `8bf7078` | Recall Drills |
| `b1a5edd` | Sampled question banks |
| `dd71e0b` | SQLite catalog, navigation, and circuits |
| `58db774` | Concept Lessons and Interactive Explorations |
| `317478a` | Multipart scoring, recommendations, and completion |

Useful commands:

```powershell
git -C C:\Users\SeanS\Downloads\cir_app show --stat 1559b2f
git -C C:\Users\SeanS\Downloads\cir_app show 1559b2f:path/to/file
git -C C:\Users\SeanS\Downloads\cir_app diff 1559b2f 3e021b6 -- path/to/file
git -C C:\Users\SeanS\Downloads\cir_app log --reverse --oneline
```

Try to predict the diff before reading it. That turns repository history into a design
exercise rather than an answer key.

