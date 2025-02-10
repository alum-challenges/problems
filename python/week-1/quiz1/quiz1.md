---
title: Quiz 1
author: Makaze
course: CS50 Python
week: 1
topics: "[\"Quizzes\", \"Conditionals\", \"Control Flow\"]"
---
# This Is Quiz 1
Hello! This is Quiz 1. This quiz is designed to test your knowledge of the structures, syntax and terminology you've learned from Week 1.

The quiz consists of a Python file where each function is a question. The answers will be given in the return values, which will be formatted as directed in the questions' docstrings.

## Before You Begin
**Turn off all LSPs, Linters, and Autocompletion help if using a local IDE.** We strongly recommend using the [Codespace](https://cs50.dev/) and/or disabling any extra tools for this exercise to make the most of the opportunity.

> [!NOTE]
> Double quotes cannot be used inside of double quoted strings without being escaped.

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
```bash
$
```
Next execute
```bash
mkdir quiz1
```
to make a folder called `quiz1` in your codespace.

Then execute
```bash
cd quiz1
```
to change directories into that folder.

You should now see your terminal prompt as `quiz1/ $`. You can now execute
```bash
wget https://github.com/alum-challenges/problems/raw/refs/heads/main/python/week-1/quiz1/quiz1.py
```
to download the Quiz 1 program. Then execute
```bash
code quiz1.py
```
to edit the file called `quiz1.py` where you’ll answer questions in the form of a Python program via the return values.

## Specification
The specification for each function is in each docstring for the functions provided.

Do not edit the function's structures. Dummy data has been provided to demonstrate the format. Each function's return value must match the format in the directions.

<details>
    <summary>Hints</summary>
    <p>Check out the str documentation: <a href="https://docs.python.org/3/library/stdtypes.html#str">https://docs.python.org/3/library/stdtypes.html#str</a></p>
    <p>List of built-in functions: <a href="https://docs.python.org/3/library/functions.html">https://docs.python.org/3/library/functions.html</a></p>
    <p>More about functions: <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">https://docs.python.org/3/tutorial/controlflow.html#defining-functions</a></p>
</details>

# How to Test
You can execute the below to check your code using `check50`, a program that CS50 will use to test your code:
```bash
check50 alum-challenges/problems/main/python/week-1/quiz1/tests
```
If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `quiz1` folder and have saved your `quiz1.py` file there.

* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*
