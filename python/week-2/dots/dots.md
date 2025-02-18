---
title: Dots
author: Dana-f559
course: CS50 Python
week: 2
topics: "[\"Functions\", \"Lists\", \"Dict\", \"Loops\"]"
---

# Dots
## Background
...

## Understanding
In a file called `dots.py`, implement a program that prompts the user for input, then decodes the input:
the amout of dots before an alphanumeric charachter is its position in a string. The decoding algorighm should be coded inside the `decode` function. The function should except a string, then return the decoded version of it.


Note: the indexes are starting from 1! 

The input of `...5.C..S....0` would result in the output of `CS50`

`...5` means that the charachter `5` has the position number `3` in the string.

`.C` means that the charachter `C` has the position number `1` in the string.

`..S` means that the charachter `S` has the position number `2` in the string.

`....0` means that the charachter `0` has the position number `4` in the string.

You can assume that there will be no 0 indexes letters, no repeated indexes.

## Before You Begin
Execute cd by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
```bash
$
```
Next execute
```bash
mkdir dots
```
to make a folder called `dots` in your codespace.

Then execute
```bash
cd dots
```
to change directories into that folder.

You should now see your terminal prompt as `dots/ $`. You can now execute
```bash
code dots.py
```
to make a file called `dots.py` where you’ll write your program.

## Specification


Use this code as a template. Edit only the body of `decode`:
```python
def main():

    text = input(": ")
    print(decode(text))

def decode(text):
    raise NotImplementedError

if __name__ == "__main__":
    main()
```

<details>
    <summary>Hints</summary>
        <p>More about functions: <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">https://docs.python.org/3/tutorial/controlflow.html#defining-functions</a></p>
        <p>More about lists: <a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">https://docs.python.org/3/tutorial/datastructures.html#more-on-lists</a></p>
        <p>More about dictionaries: <a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">https://docs.python.org/3/tutorial/datastructures.html#dictionaries</a> </p>
</details>

# How to Test
* Run your program with `python dots.py`. Your program should ask for input. Type in `..o...t.d` and press Enter. Your program should output `dot`.


* Run your program with `python dots.py`. Type `....k..u.d...c.....y` and press Enter. Your program should output:
```
ducky
```

* Run your program with `python dots.py`. Type `..S.C...5....0` and press Enter. Your program should output:
```
CS50
```
* Run your program with `python dots.py`. Type `......,.....o...l..e................y............... ..........w.............r....l..............e.........o........h....... .................o...................?..................u............a........... .H` and press Enter. Your program should output:
```
Hello, how are you?
```

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `dots` folder and have saved your `dots.py` file there.

If you get an error saying `python` is not found, try replacing it with `python3` in the terminal command instead.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code:
```bash
check50 alum-challenges/problems/main/python/week-2/dots/tests
```
* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*
