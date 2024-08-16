---
title: Match Adventure
author: Makaze
course: CS50 Python
week: 2
topics: "[\"Conditionals\", \"Loops\", \"Pattern Matching\", \"Match\", \"Case\", \"Dictionaries\"]"
---
# Match Adventure
## Backgroud
When it comes to programming, one of the classic examples is a text-based adventure game where you type in commands and explore your environment. In a text adventure, you type in commands such as "Go west" and "Pick up an apple", and get responses back based on the command the subjects chosen.

We are going to explore using the magic of Structural Pattern Matching, as introduced in PEP 636.

## Understanding
Your player will need to have an inventory, stored as a `dict` containing the items as keys and the quantity as values. Your player will move in one of the four cardinal directions (north/south/east/west), and can pick things up if they are standing in front of them.

Your starting values:
```py
INVENTORY = {
    "apples": 0,
    "herbs": 0,
    "water": 0,
    "firewood": 0,
}

direction = None
```

Your program should accept the following commands, and have the following outputs. Words in curly braces `{}` can be any value in the list separated by a `/`.
#### `Go {north/south/east/west/home}`
The response for each choice should be:

`north`: `You walk north and arrive at an orchard of apple trees.`

`south`: `You walk south and arrive at a field of healings herbs.`

`east`: `You walk east and arrive at a spring full of drinking water.`

`west`: `You walk west and arrive at a lumber yard full of firewood.`

Valid directions should change the `direction` variable to the matched value.

`home`: `You go home, ending your adventure here. Goodbye!`

Going home should print end the game and exit the program.

If the word after Go is not a valid option, the response is `You cannot go {choice 1}. Valid directions are north, south, east, west, and home.`
#### `Take {an/some} {apple/apples/herbs/water/firewood}`
Response: `You take {choice 1} {choice 2} and add to your inventory.`
1 of the chosen item should be added to the inventory.
#### `Count {item}`
Response: `You have {item count} {item} in your inventory.`

## Before You Begin
Execute cd by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
```bash
$
```
Next execute
```bash
mkdir adventure
```
to make a folder called `adventure` in your codespace.

Then execute
```bash
cd adventure
```
to change directories into that folder.

You should now see your terminal prompt as `adventure/ $`. You can now execute
```bash
code adventure.py
```
to make a file called `adventure.py` where you’ll write your program.

## Specification
Your program should run outside of a function at the global level, making use of loops and match-case instead of functions to achieve the desired behavior.

Your program should begin with the following values:

```py
INVENTORY = {
    "apples": 0,
    "herbs": 0,
    "water": 0,
    "firewood": 0,
}

direction = None
```

Your program should start by printing the following line and then a prompt for input. Each prompt in the program should be at the beginning of its own line with a right angle bracket followed by a space: `> `
```
Your adventure has begun. You see an empty field in all directions. Your inventory is empty. Choose "Go home" to end your adventure.
> 
```
Finally, there should be an empty line between each input and the response that follows.

Your program should follow the response pattern described in the Understanding section of the problem.

#### Example Sequence:
Your program should produce results as follows:
```
Your adventure has begun. You see an empty field in all directions. Your inventory is empty. Choose "Go home" to end your adventure.
> Go north

You go north and arrive at an orchard of apple trees.
> Take an apple

You take an apple and add to your inventory.
> Go south

You walk south and arrive at a field of healings herbs.
> Take some herbs

You take some herbs and add to your inventory.
> Count herbs

You have 1 herbs in your inventory.
>
```

After the above sequence, your inventory and direction values should now be:
```py
INVENTORY = {
    "apples": 1,
    "herbs": 1,
    "water": 0,
    "firewood": 0,
}

direction = "south"
```

If the command the user gives is not a valid a case covered by the Understanding, the program should print:
```
Invalid directions, please try again.
```
And reprompt for input with the same `> `.

Your program should continue until the user enters a command to `Go home`.

**The catch:** Your program should be able to handle all of these cases without using a single if statement! Only match-case statements.

<details>
    <summary>Hints</summary>
        <p>Don't forget that input returns a str: <a href="https://docs.python.org/3/library/stdtypes.html#str">https://docs.python.org/3/library/stdtypes.html#str</a></p>
        <p>More about pattern matching: <a href="https://peps.python.org/pep-0636/">https://peps.python.org/pep-0636/</a></p>
        <p>Remember that the dict documentation has some helpful methods, like dict.get(): <a href="https://docs.python.org/3/library/stdtypes.html#dict">https://docs.python.org/3/library/stdtypes.html#dict</a></p>
</details>

# How to Test
Run your program with `python adventure.py` and enter `Go north`, `Take an apple`, `Go south`, `Take some herbs`, `Count herbs`, and `Go home`. You should see the following sequence and end up back on the command line.
```
Your adventure has begun. You see an empty field in all directions. Your inventory is empty. Choose "Go home" to end your adventure.
> Go north

You go north and arrive at an orchard of apple trees.
> Take an apple

You take an apple and add to your inventory.
> Go south

You walk south and arrive at a field of healings herbs.
> Take some herbs

You take some herbs and add to your inventory.
> Count herbs

You have 1 herbs in your inventory.

> Drop herbs

Invalid directions, please try again.
> Go home

You go home, ending your adventure here. Goodbye!
```

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `adventure` folder and have saved your `adventure.py` file there.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code:
```bash
check50 alum-challenges/problems/main/python/week-2/adventure/tests
```
* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*

