1. Set up a git repo in that repository. You can refer to [[Making a new Git repo locally]] for that.
2. If you hadn't as part of the previous step, set up a .gitignore and make sure to add anything you wouldn't want committed to it.
3. Make sure a commit has been done and push that.
4. Create an`AGENTS.md` file (standard convention) and a `Docs/` directory in the root of the project directory. There's a bunch of ways to do this, but for now I recommend just making a `project_brief.md` and an `open_questions.md`.
5. In `AGENTS.md`, define the goal of the project and its overall theme and basic structure. In `project_brief.md` add specifications for certain features you already understand and know what they should be shaped as.  In `open_questions.md` put what you're not yet sure about. Commit and push these again, putting as the commit message, "pre-agent commit".
6. You'll now have the agent **read only** for comprehension of the project.  Make sure it does not modify files. It should ask you to resolve existing tensions or conflicts if they consist. Your goal is to get these down to the position where nothing is stopping the agent from building the fundamental scaffold of the project, adjusting the `project_brief.md` and `open_questions.md` as needed. Feel free to use an LLM to help expedite this process.

# Example Project Structure


```
MyProject
-Content
-Source
-Docs
--project_brief.md
--open_questions.md
-.git
-.gitignore
-AGENTS.md
```
