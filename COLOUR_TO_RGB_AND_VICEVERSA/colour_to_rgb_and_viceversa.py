import tkinter as tk
from tkinter import colorchooser
import random

def display_color(rgb):
    r, g, b = rgb
    color_hex = f'#{r:02x}{g:02x}{b:02x}'
    
    color_display = tk.Toplevel()
    color_display.title("Color Display")
    color_display.geometry("200x200")
    color_display.configure(bg=color_hex)

    label = tk.Label(color_display, text=f'RGB: {rgb}', bg=color_hex, fg='white', font=("Helvetica", 12))
    label.pack(expand=True)

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def rgb_input():
    rgb_string = input("Enter RGB values (comma-separated, e.g., 255,0,0): ")
    try:
        rgb_values = tuple(map(int, rgb_string.split(',')))
        
        if len(rgb_values) == 3 and all(0 <= value <= 255 for value in rgb_values):
            display_color(rgb_values)
        else:
            print("Invalid input! Please enter three values between 0 and 255.")
    except ValueError:
        print("Invalid input! Please ensure you enter integers separated by commas.")

def select_color():
    rgb, color_hex = colorchooser.askcolor()
    if rgb:
        display_color(tuple(map(int, rgb)))

def select_random_color():
    rgb = get_random_color()
    print(f'Random RGB: {rgb}')
    display_color(rgb)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("RGB Color Selector")
    root.geometry("300x200")

    input_button = tk.Button(root, text="Input RGB", command=rgb_input)
    input_button.pack(pady=10)

    palette_button = tk.Button(root, text="Select Random Color", command=select_random_color)
    palette_button.pack(pady=10)

    color_button = tk.Button(root, text="Choose Color from Palette", command=select_color)
    color_button.pack(pady=10)

    root.mainloop()
