# CS109 Lab 0: Intro to Physical Computing

## Overview

This lab is an introductory project for physical computing using a Raspberry Pi Pico microcontroller (MCU). The goal is to familiarize students with running Python code on a microcontroller and practicing basic programming concepts.

## Learning Objectives

By completing this lab, students will:
- Interact with the Python interpreter on a Raspberry Pi Pico
- Write and run Python programs directly on a microcontroller
- Use the `picozero` module to control hardware components
- Understand basic input/output operations with hardware

## Prerequisites

- VSCode installed
- Micro Pico VSCode extension
- Raspberry Pi Pico
- Lab 0 repository cloned from GitHub Classroom

## Project Components

The lab consists of three main parts:

### 1. Pico Python Interpreter
- Connecting the Pico to a computer
- Running Python commands directly on the microcontroller
- Exploring the `picozero` module
- Controlling the built-in LED

### 2. Running Python Programs
- Creating a `blink.py` script to control the LED
- Using `time.sleep()` to control timing
- Understanding program execution on the Pico

### 3. Hardware Interaction
- Connecting and controlling a buzzer
- Creating a `beep.py` script with variable tone timing

## Challenge: Morse Code Generator

The final challenge involves creating a Morse code generator that:
- Uses the buzzer to send a multi-word message
- Follows Morse code timing specifications
- Can be decoded by an online Morse code decoder

## Submission Requirements

- Video demonstration of the Morse code generator
- Committed `morse.py` code
- Completed `reflection.md`

## Tools and Technologies

- Python
- Raspberry Pi Pico
- `picozero` module
- VSCode
- Micro Pico Extension

## Recommended Resources

- [Morse Code Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)
- VSCode Micro Pico Extension documentation

## Notes

Ensure all code follows best practices:
- Use descriptive variable names
- Add clear comments
- Avoid advanced programming constructs not yet covered in class
