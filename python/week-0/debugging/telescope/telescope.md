---
title: Debugging a Telescope
author: Makaze
course: CS50 Python
week: 0
topics: "[\"Debugging\", \"Functions\", \"Variables\", \"Scope\"]"
---
# Debugging a Telescope
## Start by watching the Debugging short for CS50
[![CS50 YouTube Link](https://img.youtube.com/vi/2hsn7AxXKmg/0.jpg)](https://www.youtube.com/watch?v=2hsn7AxXKmg)

![Debugging](https://www.youtube.com/watch?v=2hsn7AxXKmg)

## CS50 Week 0 Shorts
<ol>
    <li><a href="https://cs50.harvard.edu/python/2022/shorts/visual_studio_code_for_cs50/">Visual Studio Code for CS50</a></li>
    <li><a href="https://cs50.harvard.edu/python/2022/shorts/functions/">Functions</a></li>
    <li><a href="https://cs50.harvard.edu/python/2022/shorts/return_values/">Return Values</a></li>
    <li><a href="https://cs50.harvard.edu/python/2022/shorts/side_effects/">Side Effects</a></li>
    <li><a href="https://cs50.harvard.edu/python/2022/shorts/variables/">Variables</a></li>
</ol>

## Backgroud
One of the tools beloved by scientists of all kinds is the telescope. The concept of magnifying with glass lenses, both for extremely small things close by and extremely large things very far away, has been an integral part of studying nature from every angle we can.

Today we will be studying the concept of scope in programming with the telescope of a debugger!

## Understanding
A telescope's magnification increases the size of everything in it's field of view by a factor set by the dial. Assume that we have a telescope set up so that at x1 zoom (no magnification), an object that is 1 meter tall fills our view when we are 1 meter away from the object. Suppose we see a friend in the distance who is 1.77 meters tall, and we want to know how far away our friend is. We can calculate it using this relationship with our telescope!

First, we turn the dial until our friend fills up our entire view (their head is at the top and their feet are at the bottom). The formula for that distance is:

$\[
D = \text{Object Height} \times \frac{1 \text{ meter}}{\text{Height at 1 meter with no magnification}} \times M
\]$

We have implemented a program to calculate this distance, given the height of an object (or friend) and the zoom setting it took to make them fill up the view.

There is just one problem. It has bugs! Use the VSCode debugger to fix the bugs and make the program work properly.

## Before You Begin
**Turn off all LSPs, Linters, and Autocompletion help if using a local IDE.** We strongly recommend using the [Codespace](https://cs50.dev/) and/or disabling any extra tools for this exercise to make the most of the opportunity.

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
```bash
$
```
Next execute
```bash
mkdir -p debugging/telescope
```
to make a folder called `telescope` inside of another folder called `debugging` in your codespace. (`debugging` will be created if it does not already exist.)

Then execute
```bash
cd debugging/telescope
```
to change directories into that folder.

You should now see your terminal prompt as `debugging/telescope/ $`. You can now execute
```bash
wget https://raw.githubusercontent.com/alum-challenges/problems/main/python/week-0/debugging/telescope/telescope.py
```
to download the bugged program. Then execute
```bash
code telescope.py
```
to open the new `telescope.py` where you will debug the existing program.

## Specification
The resulting program should implement a function called `zoom` which accepts two `float`s (the size of an object and the magnification level of the telescope), and returns the distance to the object as a `float`.

The program should prompt the user for the magnification level on the dial and the size of the object in meters. It should then calculate the distance and print it as `The object is {value} meters away.` The output should be accurate to 2 decimal places.

<details>
    <summary>Hints</summary>
    <p>More about functions: <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">https://docs.python.org/3/tutorial/controlflow.html#defining-functions</a></p>
</details>

# How to Test
* Run your program with `python telescope.py`. Type `5` and press Enter. At the next prompt, type `3` and press Enter. Your program should output `The object is 15.00 meters away`.
* Run your program with `python telescope.py`. Type `1` and press Enter. At the next prompt, type `1` and press Enter. Your program should output `The object is 1.00 meters away`.
* Run your program with `python telescope.py`. Type `1.77` and press Enter. At the next prompt, type `3.5` and press Enter. Your program should output `The object is 6.20 meters away`.
* Run your program with `python telescope.py`. Type `1.225` and press Enter. At the next prompt, type `1` and press Enter. Your program should output `The object is 1.23 meters away`.

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `telescope` folder and have saved your `telescope.py` file there.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code:
```bash
check50 alum-challenges/problems/main/python/week-0/debugging/telescope/tests
```
* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*
