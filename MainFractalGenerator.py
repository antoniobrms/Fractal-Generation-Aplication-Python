#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:51:35 2024

@author: antoniobrimesromero
"""

#MAIN MENU FOR THE FRACTAL GENERATOS APLICATION

import os
import sys
import numpy as np
import matplotlib.pyplot as plt



def option1():
    print("Generating Julia Set fractal...")
    cmap = plt.get_cmap('jet')
    def julia_set(width, height, x_min, x_max, y_min, y_max, max_iter, c):
        R = max(abs(c), 2)
        julia = np.zeros((height, width))
        x_range = np.linspace(x_min, x_max, width)
        y_range = np.linspace(y_min, y_max, height)

        for i, x in enumerate(x_range):
            for j, y in enumerate(y_range):
                z = complex(x, y)
                ic = 0

                for k in range(max_iter):
                    z = z**2 + c
                    if abs(z) > R:
                        ic = k
                        break

                julia[j, i] = ic

        return julia

    def plot_julia(width=1600, height=1600, x_min=-2, x_max=2, y_min=-2, y_max=2, max_iter=256, c=complex(-0.8, 0.156)):
        fractal = julia_set(width, height, x_min, x_max, y_min, y_max, max_iter, c)
        plt.imshow(fractal, extent=[x_min, x_max, y_min, y_max], cmap='jet')
        plt.colorbar()
        plt.title("Julia Set")
        plt.show()
        return fractal
    
    # Example Usage
    JuliaSet = plot_julia()
    save_fractal(JuliaSet, 'Julia Set', cmap)
    

def option2():
    exit = False
    cmap = plt.get_cmap('gist_stern') #gist_stern    nipy_spectral
    while exit==False:
        N = input("\nChoose a number between  2 and 7 to generate a modified Mandelbrot fractal based on this: ")
        N = int(N)
        if (1<N<8):
            print("Generating Modified Mandelbrot fractal...")
            def modified_mandelbrot(c, max_iter, n):
                R = max(abs(c), 2)
                z = c
                ic = 0

                for i in range(1, max_iter + 1):
                    z = z**n + c
                    if abs(z) > R:
                        ic = i
                        break
                return ic

            def generate_fractal(area_real, area_imag, n, max_iter=100):
                width, height = len(area_real), len(area_imag)
                fractal_image = np.zeros((height, width))

                for row_index, re in enumerate(area_real):
                    for column_index, im in enumerate(area_imag):
                        c = complex(re, im)
                        ic = modified_mandelbrot(c, max_iter, n)
                        fractal_image[column_index, row_index] = ic
                return fractal_image

            def plot_fractal(area_real, area_imag, n):
                fractal_image = generate_fractal(area_real, area_imag, n)
                plt.imshow(fractal_image, extent=(min(area_real), max(area_real), min(area_imag), max(area_imag)), cmap ='gist_stern')
                plt.colorbar()
                plt.title(f"Modified Mandelbrot Set with z -> z^{n} + c")
                plt.show()
                return fractal_image

            # Example Usage
            area_real = np.linspace(-2, 2, 1600)
            area_imag = np.linspace(-2, 2, 1600)
            MMandelbrot = plot_fractal(area_real, area_imag, N)
            
            #Ask if the user want to save it as PNG
            save_fractal(MMandelbrot, 'Modified Mandelbrot', cmap)
            exit=True
        else:
            print("\nInvalid number. Please try again.")
            
    

def option3():
    print("You have selected Option 3.")
    print("Generating Phoenix fractal...")
    cmap = plt.get_cmap('turbo')
    def phoenix_fractal(width, height, x_min, x_max, y_min, y_max, max_iter, c, p, escape_radius):
        fractal = np.zeros((height, width))
        x_range = np.linspace(x_min, x_max, width)
        y_range = np.linspace(y_min, y_max, height)

        for i, x in enumerate(x_range):
            for j, y in enumerate(y_range):
                z = complex(x, y)
                z_prev = 0  # z_{n-2} starts from 0
                escaped = False

                for k in range(max_iter):
                    z, z_prev = z**2 + c + p * z_prev, z  # Update z and z_prev
                    if abs(z) > escape_radius:
                        fractal[j, i] = k + 1 - np.log(np.log2(abs(z)))
                        escaped = True
                        break
                
                if not escaped:
                    fractal[j, i] = max_iter - 1

        return fractal

    def plot_phoenix_fractal(width=1600, height=1600, x_min=-2, x_max=2, y_min=-2, y_max=2, max_iter=40, c=complex(0.56667, 0.5), p=complex(0.5, 0.007), escape_radius=4):
        fractal_image = phoenix_fractal(width, height, x_min, x_max, y_min, y_max, max_iter, c, p, escape_radius)
        plt.imshow(fractal_image, extent=[x_min, x_max, y_min, y_max], cmap='turbo', origin='lower')
        plt.colorbar()
        plt.title("Phoenix Fractal")
        plt.show()
        return fractal_image

    # Example Usage
    PhoenixFractal = plot_phoenix_fractal()
    
    save_fractal(PhoenixFractal, 'Phoenix Fractal', cmap)
    
    
    

def option4():
    print("You have selected Option 4.")
    print("Generating Multi-step Polynomiograph fractal...")
    cmap = plt.get_cmap('nipy_spectral') #jet

    def iterate_point(z0, p, Iv, Cv, M):
        """
        Iterates a point through a polynomial.

        :param z0: Initial point
        :param p: Polynomial function
        :param Iv: Iteration function
        :param Cv: Convergence test function
        :param M: Maximum number of iterations
        :return: Number of iterations and last computed point
        """
        z = z0
        for i in range(M):
            z = Iv(z, p)
            if Cv(z):
                return i, z
        return M, z



    def multi_step_polynomiography(area, polys, iters, max_iters, conv_tests, area_transforms):
        """
        Generates a multi-step polynomiograph.

        :param area: Area for the polynomiograph (xmin, xmax, ymin, ymax)
        :param polys: Array of polynomial functions
        :param iters: Array of iteration functions
        :param max_iters: Array of maximum iterations
        :param conv_tests: Array of convergence test functions
        :param area_transforms: Array of area transformation functions
        :param color_map: Color map for the polynomiograph
        :return: Multi-step polynomiograph
        """
        
        xmin, xmax, ymin, ymax = area
        width, height = 800, 800  # Resolution of the polynomiograph
        x = np.linspace(xmin, xmax, width)
        y = np.linspace(ymin, ymax, height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        
        polynomiograph = np.zeros((height, width, 3), dtype=np.uint8)

        for poly, Iv, M, Cv, transform in zip(polys, iters, max_iters, conv_tests, area_transforms):
                for i in range(height):
                    for j in range(width):
                        n_iter, _ = iterate_point(Z[i, j], poly, Iv, Cv, M)
                        color = cmap(n_iter / M)  # Use colormap here
                        polynomiograph[i, j] = [int(255 * c) for c in color[:3]]  # Convert to RGB

        return polynomiograph

    def plot_polynomiograph(polynomiograph):
        plt.imshow(polynomiograph, extent=(-2, 2, -2, 2))
        plt.title("Multi-step Polynomiograph")
        plt.colorbar() 
        plt.show()

   
    if __name__ == "__main__":
        
    # Polynomial functions
        polys = [
            lambda z: z**2 + complex(0.285, 0.01),  # Polynomial 1
            lambda z: z**2 - complex(0.8, 0.156),   # Polynomial 2
            lambda z: z**2 + complex(0, -0.8),      # Polynomial 3
            lambda z: z**2 + complex(-0.4, 0.6)     # Polynomial 4
        ]

    # Iteration functions (Standard iteration for each polynomial)
        iters = [lambda z, p: p(z) for _ in polys]

    # Convergence tests (Escape radius of 2)
        conv_tests = [lambda z: abs(z) > 2 for _ in polys]

    # Maximum iterations for each polynomial
        max_iters = [60, 70, 80, 90]

    # Area transformations (No transformation applied)
    area_transforms = [lambda z: z for _ in polys]

    # Define the area of the polynomiograph
    area = (-2, 2, -2, 2)

    # Generate the polynomiograph
    poly_graph = multi_step_polynomiography(area, polys, iters, max_iters, conv_tests, area_transforms)

    # Plot the polynomiograph
    plot_polynomiograph(poly_graph)
    #Ask if the user want to save it as PNG
    save_fractal(poly_graph, 'Multi-step polynomiograp', cmap)
    
    
#Function to ask if the user want to save the fractal image as PNG after generate
def save_fractal(fractal, file_name, colormap='gist_stern'):
    save_option = input("Do you want to save the fractal as a PNG? (yes/no): ").lower()
    if save_option == 'yes':
        script_directory = os.path.dirname(__file__)
        script_directory = script_directory+'/../'
        folder_name = "Fractal Images"
        # Path for the new folder
        new_folder_path = os.path.join(script_directory, folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        print("Fractal saved")
        plt.imsave(new_folder_path+'/Fractal Images'+f"{file_name}.png", fractal, cmap=colormap)
    elif save_option != 'no':
        print("Invalid response. Please type 'yes' or 'no'.")
    
def main_menu():
    while True:
        print("\nChoose what algorithm for fractal generation you want to execute")
        print("1. Julia Set")
        print("2. Modified Mandelbrot")
        print("3. Phoenix Fractal")
        print("4. Multi-step Polynomiograph")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
        elif choice == "0":
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
