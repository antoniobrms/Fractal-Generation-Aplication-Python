# Fractal-Generation-Aplication-Python


```markdown
# Fractal Generation Application - User Manual

## Overview
This Python application generates four different types of fractals: Julia Set, Modified Mandelbrot, Phoenix, and Multi-step Polynomiograph. The user can select which fractal to generate, visualize the result, and optionally save the fractal image as a PNG file.

## Requirements
- Python 3.x
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `sys`
  - `os`

To install dependencies, run:
```bash
pip install numpy matplotlib
```

## How to Use the Application

### 1. Starting the Program
- Run the Python script:
  ```bash
  python fractal_generator.py
  ```
- Alternatively, if you have the executable (for macOS):
  - Double-click the `.exe` file to start the application.

### 2. Main Menu
After starting the program, you will be presented with the following options:

1. Generate Julia Set Fractal
2. Generate Modified Mandelbrot Fractal
3. Generate Phoenix Fractal
4. Generate Multi-step Polynomiograph
0. Exit the program

### 3. Generating Fractals
- **Option 1: Julia Set Fractal**  
  This option generates a Julia Set fractal. The fractal will be displayed on the screen.

- **Option 2: Modified Mandelbrot Fractal**  
  This option generates a Mandelbrot fractal. You will be prompted to enter a number between 2 and 7 to adjust the power of the function.

- **Option 3: Phoenix Fractal**  
  This generates a Phoenix fractal. Adjust the complex constant to change the fractal’s shape.

- **Option 4: Multi-step Polynomiograph**  
  This option generates a visual representation of the roots of a polynomial.

### 4. Saving the Fractal
After generating any fractal, the program will ask:
```
Do you want to save the fractal as a PNG file? (yes/no)
```
- Enter `yes` to save the fractal image in the **Fractal Images** folder located in the same directory as the script.
- Enter `no` to skip saving.

### 5. Exiting the Program
- To exit the program, enter `0` in the main menu.

## Notes
- The saved fractal images will be in `.png` format with a resolution of 1600x1600 pixels for Julia Set and Mandelbrot fractals, and 800x800 pixels for Phoenix fractals.
- The executable version is only available for macOS.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

```

Let me know if you'd like to adjust any part of the manual or description!
