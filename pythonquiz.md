# Python Quiz - Beginner Level

## What is Python?
Python is a high-level programming language used. It's often used by beginners because it has a human readable syntax structure.

### Video Guide
[Video](https://www.youtube.com/watch?v=mRMmlo_Uqcs&ab_channel=NetworkChuck)

## Why should you learn it?
It's a solid choice for a first programming language. Its versatility makes it useful for a lot of different technologies, and even though it's not the best at one specific thing, python brings you a wide range of practical capabilities. Program scripts, or bots, or automations, or server side software, or games. The only place it could be considered lacking is in the frontend web universe.

## How does this guide/workshop work?
We at EHC have innovated to provide a workshop experience from the workshops we've been to and what we've seen.
1. Live Run-through.
- A major issue for new programmers and even us when we are learning new things is a lack of content. The analogy I like to use is the ikea furniture model. You are building a piece of ikea furniture. You have the instructions. Now what? You follow the instructions and build the furniture. But let's say you have never seen the type of furniture you are building, or how to build a piece of furniture, or how to follow a set of instructions. You will have no clue how to build the furniture. Now replace furniture with code. Our goal with these live run-throughs is to provide that context by doing the workshops by following the instructions in ten minutes or less. 
2. Question Time.
- We want people to ask questions, but we want to keep it under wraps in a large room with 30+ people. We go from a ten minute live run-through where people have high attention spans, to a set of time for pure questions.
3. Instruction Set/Work Time
- Programming is intuitively a solo sport. Even in a collaborative aspect, writing code is still done one person at a line at a time. Instruction sets, like this one, will guide people to building a project and then options for creating customizations.
4. Demo Time
- Demoing your project is great way to feel good about what you have made and to continue to make progress. It’s an amazing feeling to stand up and look back at the work you have done, even if it was only in 20-30 minutes.

## THE START TO THE WORKSHOP
Building a custom python quiz.

### Part 1
**Creating your quiz function**
*There are many ways to solve a problem.*
We will be taking a unique and slightly complex approach to solving the problem of making a python quiz game. We will be programming using functions. The function we have written allows you to write one line of code with a question and an answer and for the magic of a “quiz” to appear. It will print the question along with asking for an input in the python terminal and provide 3 chances for you to get the question right along with keeping score and result messages. We are not going to teach you exactly what the function does because that would take away time from just using it.
```
def do_quiz(question, answer):
  global score
  for attempt in range(3, 0, -1):
    inp = input(question)
    if inp == answer:
      score = score + 1
      print("Correct Answer. " + "Your score is " + str(score) + ".")
      return
    else:
      print("Try again, attempts remaining: ", attempt - 1)
  print("You couldn't figure it out")

```
This is your first block of code. You can just copy and paste it in. The first line declares the code within to be a function. A function is a set of code that can be called to be run. It makes it more efficent to write code since instead of rewriting you can just call it to start work again. A function also aims to process information. The information we need to input is question and answer and it processes that to perform a "function". 

### Part 2
**Adding a score variable**
You need a score, right? Programming IDEs are just like text editors. You are going to create some empty lines above your function so you can create a score variable. 

```
score=0
```
The reason we named it score is because it makes the most sense in English along with the fact that in the quiz function we already incorporate a score feature with a variable called score. We make it =0 because when you start the program in python is goes line by line and we want to declare the score as 0 since you just started. It would be really bad if you didn't reset the score every game. Imagine how high it'd be.

### Part 3
**Calling the quiz function**
Calling a function in python is a simple process with simple syntax. Syntax is basically grammar in English and other languages. It's how ideas are communicated. In python to call a function, write the name along with parenthesis, with whatever parameters the function is expected to recieve. That basically means inputs. Like if your function was for math, you'd probably want to input numbers. 

```
do_quiz(question,answer)
```
Write this line of code below the do_quiz function and replace the question with your question and replace the answer with your answer. To make more questions and answer sets just write another one of these lines.

Play around with adding some questions and answers, and move on once you get bored.

### Part 4
**Researching the basics**
We have build a quiz more or less. You have an ability to add questions to a pre-written function. Now it's time to add some fluff. 

Learn the Print Statement, if Statement, and the idea of the variable. If you feel up for it, learn about nested ifs.

https://www.w3schools.com/python/ref_func_print.asp

https://www.w3schools.com/python/gloss_python_if_statement.asp

https://www.w3schools.com/python/python_variables.asp

https://www.w3schools.com/python/gloss_python_if_nested.asp


### Part 5
**hack**
Use w3schools to decipher the code inside the do_quiz function. Come up with a concept for something you want to make within the limitations of the technology and build it. You might say I have no idea what to make, and to that I say its just a part of the challenge. Higher and Lower Game, Buzzfeed quiz, choose your own adventure story game. All of these are options with just the quiz function, print statements and if statementss. As our motto is: Learn, Code, Hack. By now you have learned, you have programmed, and now its time to hack. Make something into something it wasn't meant to be.

Good luck, I hope our live runthrough and future video makes this more comprehensible, and enjoy our gratitude.

Sincerely, EHC-TEAM.
https://replit.com/@KyleLiao/TiredImpeccableOperation#main.py

```
score = 0

def do_quiz(question, answer):
  # We have attempts from 3 to 1
  # range(start, stop, interval)
  global score
  for attempt in range(3, 0, -1):
    inp = input(question)
    if inp == answer:
      score = score + 1
      print("Correct Answer. " + "Your score is " + str(score) + ".")
      return
    else:
      print("Try again, attempts remaining: ", attempt - 1)
  print("You couldn't figure it out")


do_quiz("What is 5+5 ", "10")
```
Final Sample Code



