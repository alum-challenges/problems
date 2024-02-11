---
title: Buying Cookies 
author: Dana-f559
course: CS50P
week: 0
topics: "[\"Functions\", \"Variables\"]"
---

# Buying Cookies
## Background
With the rapid growth of technology some stores had implemented a self check-out system. Store like Kaufland has its own system, which works like this: in the terminal you say which product are you getting, and the quantaty. Then you put the item on the scale which checks how much the product weights. The reason the scale checks how much the product weights is to know that you put the right product on the scale. 


## Understanding

In a file called `buying.py`, implement a program in Python that will prompt user for how many cookies they want to buy. Your program should then send the input value into a function called `make_cookies` that return the weight in gramms. Finally, print the returned value and tell the user how much the cookies should weight. 


## Before you begin

Execute cd by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
```bash
$
```
Next execute
```bash
mkdir buying
```
to make a folder called `buying` in your codespace.

Then execute
```bash
cd buying
```
to change directories into that folder. You should now see your terminal prompt as `buying/ $`. You can now execute
```bash
code buying.py
```
to make a file called `buying.py` where you’ll write your program.


## Specification
You will implement two functions `main` and `make_cookies`

In the main function you will prompt the user for how many cookies they want to buy(expect the user to enter the correct data for now).Then you will call the make_cookie function which will return the weight of the cookies. After calculating the value, you will display it as such: `The cookies weight: x grams`

The `make_cookie` function is going to take in one input, then calculate how much the cookies weight and return the value. `One cookie is 150 gramms.` 

<details>
    <summary>Hints</summary>
        <p>Don't forget that input returns a string, and you need an int: <a href="https://docs.python.org/3/library/functions.html#int">https://docs.python.org/3/library/functions.html#int</a>
        <p>More about functions: <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">https://docs.python.org/3/tutorial/controlflow.html#defining-functions</a></p>
</details>


## How to test

* Run your program with `python buying.py`. Type `2` and press Enter. Your program should output `300`

* Run your program with `python buying.py`. Type `5` and press Enter. Your program should output `750`

* Run your program with `python buying.py`. Type `10` and press Enter. Your program should output `1500`


You can execute the below to check your code using `check50`, a program that CS50 will use to test your code.
```bash
* Coming soon*
```
* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*
