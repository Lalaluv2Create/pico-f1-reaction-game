# F1 Reaction Time Game
- A F1-inspired reaction time game
- I built it using a Raspberry Pi Pico, MicroPython, 5 LEDs, and a push button
- The goal is to press the button as fast as possible once all the lights turn off

## How It Works
1. Press the button to start the game
2. The 5 LEDs turn on one at a time, like the starting lights in an F1 race
3. After a random amount of time between 0.5 and 5.5 seconds, all the lights turn off
4. Press the button as quickly as possible after the lights turn off
5. Your reaction time is measured in milliseconds and displayed in the serial console

## Results
- **Perfect Timing:** Reaction time is 350 ms or less
- **Too Late:** Reaction time is over 350 ms
- **False Start:** The button is pressed before the lights turn off

## Components Used
- Raspberry Pi Pico
- 5 LEDs (red, yellow, blue, green, and white)
-  5 current-limiting resistors
-  Push button
-  Breadboard and jumper wires

## Pin Connections 

- | Component | Pico GPIO Pin |
- | Push Button | GP15 |
- | Red LED | GP20 |
- | Yellow LED | GP21 |
- | Blue LED | GP22 |
- | Green LED | GP16 |
- | White LED | GP17 |

## Files
- 'main.py' - The code for the reaction time game
- "Hardware Setup.pdf"
- "User Instructions.pdf"

## What I Learned
- How to use GPIO pins on the Raspberry Pi Pico
- How to control multiple LEDs and read button input
- How to measure reaction time using milliseconds
- How to use random delays in a game
- How to detect false starts and let the player play again

## How to Run
1. Connect the Raspberry Pi Pico to your computer
2. Open "main.py" in Thonny or another MicroPython-compatible editor
3. Run the code on the Pico
4. Open the serial console to see the instructions and your reaction time
5. Press the button and try to get the fastest reaction time!
