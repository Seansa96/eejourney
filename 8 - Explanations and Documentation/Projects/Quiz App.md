Tags: [[csharp]]

# Objective

Create a simple console application consisting of 3 questions. Display the questions to the user, get their input for each question, and provide them a grade at the end.

# What I Did

Initially, I scaffolded the project to do just that, and it was very simplistic in nature.  The initial skeleton was designed to run a while loop in the main program and uses if statements that utilized a string `input` to determine which statement to jump to, using the value `exit` to close the program.

This of course was not the best way of handling things, so I moved on to make the version a little more user friendly.

But first, let's discuss the Question class.
## Question Class

The Question class was devised initially with several fields and properties.

These fields were:

```
private const int NumberOfAnswers = 4; //this never got used
private string _questionText = "";
private string[] _answers;
private int _correctAnswerIndex = 0;
private static int nextQuestion = 1;
private readonly int _questionIndex;
```

With public properties made available where necessary.

These were used in the following **Constructor method**:

```
 public Question(int rightAnswer, string QuestionText, string[] args)
 {
     _answers = args;
     _correctAnswerIndex = rightAnswer - 1;
     _questionText = QuestionText;
     _questionIndex = nextQuestion++;
 }

```

Which as you can see, takes in a correct answer, the string containing the actual question, and an array of possible answers.

The question is then constructed of course with those corresponding fields, and its `nextQuestion` field, which the class itself is then incremented by 1, giving each instance of the class its own internal "id", which is primarily used in the program for display purposes for the user.

I then decided to add two methods to this class that were kept coupled and reliant upon each instance of it, instead of making a static method. This is because it was simply easier to do so, and I found it unnecessary to create a more global method that had to taken in parameters when the methods relied on internal state.

The first method was a simple display function to show the question and its answers to the user and prompt them to input their choice.

It was structured to rely upon the `_questionIndex` field to fetch the question number, then used the `_questionText` to show the actual question, then simply used newline characters as well as filler whitespace for the display of each answer.

In retrospect, I should have just used a for loop to go through it since it's an array, but ultimately that wasn't really a performance thing and just more of a convenience thing if anything.

Also, a short note on how I handled answers and their storage:

I probably should have just used enums, and will probably go back and refactor the program slightly to do so just to get used to using them.  After reading up on them and understanding them more, enums are literally built for use-cases such as this, and can vastly simplify working with features such as this in the future.

Anyways, on to the second method.

## Second Method

The second method, at the time I first developed it, just took in the user's answer, compared it to the `_correctAnswerIndex` for the question and then returned true if it was correct. There were side effects in both of the possible paths, with one telling the user they were correct if it returned true, and the other telling the user they were incorrect if it returned false.

This continued even in the finished version. In retrospect, this should be decoupled for tighter design, although in a small program like this it's not a huge deal, as it's fairly simple to diagnose where this comes from.  At the time, I also wasn't thinking or particularly concerned with tracking the user's location in the quiz, so I didn't implement what I later did. Nothing particularly wrong with that, in my opinion, as that went beyond the requirements of the full project and was just more of a stylistic choice.  

# Quiz class

Next, I wanted to implement a class that handled switching between the various scenarios and states of the quiz.  Its sole purpose was for one method, which in retrospect I am not entirely sure if it is good design to create a class who only has one method, but I suppose if anything it keeps the main program class looking much cleaner.

That method is a public static void method `startQuiz` that takes in a `Question[]` array and a string `input`. 

I think at the time I just built each question in the program class, then threw them in a `Question[]` array and then passed that to the `Quiz.startQuiz()` method. I would later use the `QuestionController` class to build questions.

My first version of the `startQuiz` method was a bit messy, especially regarding user input. Honestly, even with my finished version, I'm not particularly happy with how user input was handled and I'll need to research better strategies, as the way Console.ReadLine works when called multiple times, and simply replacing the value of the `input` string on each pass felt very awkward and incorrect, even though it worked, mostly.  I would have to manually clear the value of the string on each pass of the loop, which felt pretty dirty, since it was such a fragile way of tracking input.

Beyond that, it functioned much the way you might expect. Initially, I just used various if statements, which was just because I hadn't researched how to properly use `case` yet.  The basic goal was to get user input, sanitize it, then compare it to the various cases/switches I had built, then perform the corresponding action.  The first iteration just had the simple goal of proceeding through the `QuestionList` if the user entered 'y', which it did more or less.  Of course, the user could not backtrack this way, and at the time I had no storage of answers as the user was given their results in real time as they answered the questions.  When they reached the end, it would simply tell them they finished and close in the same frame.


# Now What?

So, at this point, the quiz hit the goal. It wasn't pretty, but if the user followed the prompts and didn't feel too brave, they'd get to the end mostly in tact. I added in some exception handling to stop the user from crashing the program if they entered things out of bounds of the expected input, and then decided I wanted to expand it a bit since I wasn't happy with the current functionality.

So, the goal was to allow free traversal through the quiz. This meant a few things:

1. The user couldn't get real-time feedback.  Mostly because that wasn't very quiz-like, and secondly to allow them to change their answers and view all the answers they had submitted, as well as see which ones they had yet to submit.
2. I needed to provide more options and thus build more cases.
3. I needed a more robust way to control the user's position, and also, well--that meant I actually needed to know *where the heck they were*. 

So, I needed a handler for that. Enter the `QuestionController` class.

# QuestionController

So, I built this class and sat there for a bit, as I wasn't sure of everything it might need, as well as what it was going to really end up doing.  Then, after thinking about it for a bit, I decided I needed to add a couple of fields to the `Question` class.

The first new field was `_question_answered`. This was just a simple bool that took in the int that was supposed to be the user's answer and signaled if the question had already been answered. I went and added a quick expression in the `CheckAnswer()` method, whether it returned true or false, that set that bool to true, and of course made sure that when the Question was constructed it was set to false by default.

In retrospect, I kept the method as returning a bool and left in the `return true` and `return false` statements, but those are unnecessary and just passes around values that don't do anything, as nothing relies on their evaluation. I also handled feedback to the user in that same method as a side effect, which I probably should decouple just for cleaner design.  

The second new field was `_submitted_answer`, which was a private int that would take in the user's input that was passed in and store it to be graded later.  For some reason, I also cast that to an int with Convert.ToInt32(), which is...I mean, lol. Not sure what I was thinking there, but probably was just at the end of a long session.

Also, had to do some slight offset stuff since the answers the users see are numbered 1 through 4, but of course the answer array is zero-indexed. I do that throughout the program and remembered to do it everywhere, yada yada.

Lastly, I made public properties which default `get;` and `set;` methods for them, nothing fancy.

# The methods

Now that `QuestionController` had everything it needed, it was time to build the methods.  The first one was just a very simple static void method called `GotoQuestion()`.  This simply took in a `Question[]` array and an int representing the index of the question to be shown.  It would then just call the `ShowQuestion()` method of that particular Question object.

In hindsight, perhaps I should have also added a property bool named something like `IsCurrentQuestion` that the `GoToQuestion()` method would set to true when it calls that question's `ShowQuestion()` method to allow the user to simply go back and forward, and then build the corresponding methods.

The next method is `BuildQuestionList`, which is another static method returning type `Question[]`.  This didn't need to take anything in since the questions aren't meant to be mutable in any way during runtime.  If I wanted to, I would have added in functionality to parse a file or something so that a list of questions could be dropped in and whatnot, but that was beyond the scope of this project, so I didn't. BUT...I could have.

Anyways, that was pretty simple to build and nothing really much to optimize there, so yeah.

The last method was a simple `Reset()` method to reset the values of the state trackers `_submitted_answer` and `_question_answered`.  It just takes in the `Question[]` array, iterates through them with a for loop and sets the values of those using the public property to their default states.

# Back to Question

Lastly, I needed one more function to actually evaluate how many correct answers had been given. I made a static method, `GradeQuestions()` in the `Question` class that returned an int. This int was based off of a locally declared int, `num_of_answers_correct`, that was incremented if the for loop in that method encountered a question that had a `_question_answered` of true, AND had a `_submitted_answer` that was equal to the `_correctAnswerIndex`.  

In the `startQuiz()` method, I then simply added a case that would run if the user entered "ready", which would then create a local int `grade` set to the value of the called `GradeQuestions()`, and then print to the user `$"You got {grade} out of {num_of_questions} right! \nWould you like to restart? Type 'restart' if so."`

I then cleaned up some other prints, did some testing to make sure things worked, added a primitive way for the the `startQuiz` method to keep track of the last question the user had answered (it was just a variable that I manually incremented whenever a question case was reached, which of course was not that great, but I was lazy), and did some more clean up. I then lightly sprinkled in unit testing just to get a feel of what that's like and implemented it on the `CheckAnswer()` method. I'll probably use some of that in the future for some of the more annoying things to test just so I don't have to compile and run it.
# Final Thoughts

It was a fun project to build, and I definitely feel that if I did it over again there's a lot that would be done on the first pass, and I would have used enums instead. Overall, I'm still decently happy with how it turned out.