---
title: Playlist
author: Dana-f559
course: CS50 Python
week: 2
topics: "[\"Functions\", \"Lists\", \"Dict\", \"Loops\"]"
---

# Playlist
## Backgroud
From ancient civilizations to modern times, music has been a big part of human history. Though it has evolved through many centuries it still brings joy to a lot of listeners. Before, not all of the listeners could find the name of the song or the artist who created it. Neither could they make their own playlist, to listen to a list of songs they choose. But now with the new innovation of technology you can do that in a meter of clicks. That's why this problem set is going to be about writing code for a program that will ask for all the songs you want to add for your playlist, and then give the list back to you.

In a file called `playlist.py`, implement a program in Python that prompts the user for the number of songs they want to add to their playlist. Your program should then send that input to a function called `add_songs` that returns a list of dictionaries. Finally print that list as `song by artist`. 

## Understanding
Song - a short musical composition of words and music.

Artist (music artist) -  creates, performs, and often produces music as a form of artistic expression.

Playlist -  a custom compilation of songs and music videos.

## Before You Begin
Execute cd by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
```bash
$
```
Next execute
```bash
mkdir playlist
```
to make a folder called `playlist` in your codespace.

Then execute
```bash
cd playlist
```
to change directories into that folder.

You should now see your terminal prompt as `playlist/ $`. You can now execute
```bash
code playlist.py
```
to make a file called `playlist.py` where you’ll write your program.

## Specification
You will implement two functions: `main` and `add_songs`

In the `main` function you will prompt the user for the number of songs they want to add to the playlist. If the input provided is not a positive number then reprompt the user (0 not included). Then call the `add_songs` function, passing in the value of the songs, and storing the return value of that function in a variable. The it will print the "playlist" in such format `song by artist`

In the `add_songs` function you will take in one input as the function parameters which would be the number of songs they want to add. Then using a loop (in range of the songs number) you will ask them for the song name then the songs artist. If one of the inputs was not provided then reprompt the user for the inputs. After that you will save it as a dictionary where the keys would be `song` and `artist`, and append that dictionary to a list. Then return that list.

<details>
    <summary>Hints</summary>
        <p>More about functions: <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">https://docs.python.org/3/tutorial/controlflow.html#defining-functions</a></p>
        <p>More about lists: <a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">https://docs.python.org/3/tutorial/datastructures.html#more-on-lists</a></p>
        <p>More about dictionaries: <a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">https://docs.python.org/3/tutorial/datastructures.html#dictionaries</a> </p>
</details>

# How to Test
* Run your program with `python playlist.py`. Type `cat` and press Enter. Your program should ask again for the number of songs. 

* Run your program with `python playlist.py`. Type `1` and press Enter. At the next prompt, type `Twenties` and press Enter. Then type `Ghost`. Your program should output `Twenties by Ghost`

* Run your program with `python playlist.py`. Type `3` and press Enter. At the next prompt, type `Twenties` and press Enter. Then type `Ghost` folowed by Enter. Then, type `Valentine` and press Enter. Then type `Maneskin` folowed by Enter. Then, type `Yes, and?` and press Enter. Then type `Ariana Grande` folowed by Enter. Your program should output `Twenties by Ghost` `Valentine by Maneskin` `Yes, and? by Ariana Grande`

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `playlist` folder and have saved your `playlist.py` file there.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code.
> *Coming soon*
* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*