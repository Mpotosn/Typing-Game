# Typing Game 
This is a simple typing game built using Python and Tkinter. Players are challenged to type randomly selected sentences as accurately and quickly as possible within a 120-second time limit.

# Features
120-second countdown timer

Real-time scoring (+1 point for each correct sentence)

Random sentence prompts on each attempt

Keyboard-controlled game start and progression

Simple, clean GUI built with Tkinter

# Requirements
Python 3.x

No external libraries are needed beyond the Python standard library.

# How to Play
Launch the game.

Press 1 to begin.

A sentence will appear — type it exactly into the input box and press Enter.

If your input matches the sentence, your score increases by 1.

The next sentence appears immediately; continue typing as many correct sentences as possible within 120 seconds.

Your current score and remaining time are displayed at the top.

# Notes
Sentences are randomly shuffled each round.

Only the sentence at index 1 of the shuffled list is used (which may seem random to the player).

Input must match exactly (including capitalization and punctuation) to be counted as correct.

The game does not display a final score once the timer ends — you can add this feature if you'd like to enhance it.
