import webview
import tkinter as tk
from tkinter import *
import threading

# Create the main application window
root = tk.Tk()
root.title('Eaglercraft Launcher')
root.geometry("800x600")  # Set window size

# Set the window icon
root.iconbitmap('Eaglerlogo.ico')  # Replace 'path_to_your_icon.ico' with the actual path to your icon file

# Launcher is still in beta.. let's tell our users that
beta_label = Label(root, text='Launcher in beta phase... More features coming soon!', font=("Arial", 14))
beta_label.pack(pady=20)

# Define client options
options = [
    "Choose Eaglercraft Client",
    "Eaglercraft 1.3",
    "Eaglercraft 1.5.2",
    "Eaglercraft 1.5.2 (Recent Client)",
    "Eaglercraft 1.5.2 (Precision Client)",
    "Eaglercraft 1.8.8",
    'Eaglercraft 1.8.8 (Fuchsiax Client)',
    'Eaglercraft 1.14'
]

# Create a label for client selection
client_label = Label(root, text='Select an Eaglercraft Client:', font=("Arial", 16))
client_label.pack()

# Create a dropdown menu with a cleaner design
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.config(font=("Arial", 14))
drop.pack(pady=15)

# Function to launch the selected client with a transition effect
def launch():
    chosen_client = clicked.get()
    if chosen_client != options[0]:
        root.destroy()
        url = clients[chosen_client]
        webview.create_window(chosen_client, url)
        webview.start()
    else:
        # Display an error message if "Choose Eaglercraft Client" is selected
        error_label = Label(root, text="Please select a valid Eaglercraft client.", foreground="red", font=("Arial", 14))
        error_label.pack(pady=10)

# Create a launch button with a grey background
launch_button = Button(root, text="Launch Eaglercraft Client", command=launch, font=("Arial", 16), bg='grey', fg='white')
launch_button.pack(pady=15)

# Create an Update button with a grey background
def open_github():
    import webbrowser
    webbrowser.open('https://github.com/EaglerDevs/Eaglercraft-launcher.github.io')

update_button = Button(root, text="Update", command=open_github, font=("Arial", 16), bg='grey', fg='white')
update_button.pack(pady=15)

# Function to open the settings menu
def open_settings():
    settings_window = Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("400x300")

    # Add settings options here (customize as needed)
    theme_label = Label(settings_window, text="Select Theme:", font=("Arial", 14))
    theme_label.pack(pady=10)

    theme_options = ["Light Theme", "Dark Theme"]
    theme_var = StringVar()
    theme_var.set(theme_options[0])
    theme_menu = OptionMenu(settings_window, theme_var, *theme_options)
    theme_menu.config(font=("Arial", 12))
    theme_menu.pack()

    font_label = Label(settings_window, text="Font Size:", font=("Arial", 14))
    font_label.pack(pady=10)

    font_scale = Scale(settings_window, from_=10, to=20, orient="horizontal")
    font_scale.set(12)  # Default font size
    font_scale.pack()

    # Add more settings options and functionality here

# Create a Settings button and place it under the Update button
settings_button = Button(root, text="Settings", command=open_settings, font=("Arial", 16), bg='grey', fg='white')
settings_button.pack(pady=15)

# Function to exit the application
def exit_launcher():
    root.destroy()

# Create an Exit button and place it in the bottom left corner
exit_button = Button(root, text="Exit", command=exit_launcher, font=("Arial", 16), bg='grey', fg='white')
exit_button.pack(side=LEFT, anchor=SW, padx=20, pady=20)

# Create a Credits section in the bottom right corner
credits_label = Label(root, text='Made by:\nbtplayzxgit\nFlamePVPCodes\nAR-DEV', font=("Arial", 12))
credits_label.pack(side=RIGHT, anchor=SE, padx=20, pady=20)

# Run the main application loop
root.mainloop()
