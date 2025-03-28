import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import time
import os

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(db_directory, "recipes.db")

#Make sure the reconnection is made

import sqlite3

#look up a recepy
#with autocomplte
#once a recipe is identifies i want to check if it has a cooking_time value
#if doesnt have one create it
# id it has, average with previous valies


def spaced_text(text: str) -> str:
    """Adds spaces between each character in a string for a spaced-out look."""
    return " ".join(text.upper())


class Stopwatch:
    def __init__(self, root, recipe):
        # Stopwatch state variables
        self.running = False  # Indicates if the stopwatch is running
        self.start_time = 0  # Records the start time of the stopwatch
        self.elapsed_time = 0  # Tracks the total elapsed time

        # Configure the main application window
        root.geometry("400x500")  # Set the fixed window size
        root.resizable(False, False)  # Disable resizing
        root.configure(bg="#000000")  # Set the background colour to black (dark mode)

        # Configure custom scrollbar style
        # Customise the appearance of the scrollbar to fit the dark theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background="#000000",
            darkcolor="#000000",
            lightcolor="#000000",
            troughcolor="#000000",
            bordercolor="#FFFFFF",
            arrowsize= 1,  # Reduce the size of the scroll buttons
        )

        # Recipe display
        # Displays the name of the recipe (e.g., "Egg Sandwich") at the top of the window
        self.recipe_label = tk.Label(
            root,
            text=spaced_text(f"{recipe}"),
            font=("Consolas", 12, "normal"),
            bg="#000000",
            fg="#FFFFFF",
        )
        self.recipe_label.place(relx=0.5, rely=0.1, anchor="center")  # Centre-align the label

        # Stopwatch time display
        # Displays the elapsed time in "HH:MM:SS" format
        self.time_display = tk.Label(
            root,
            text="0:00:00",  # Initial display text
            font=("Consolas", 30, "normal"),
            bg="#000000",
            fg="#FFFFFF",
        )
        self.time_display.place(relx=0.5, rely=0.25, anchor="center")  # Positioned below the recipe label

        # Start/Stop button
        # A button that toggles the stopwatch between running and stopped states
        self.toggle_button = tk.Button(
            root,
            text=spaced_text("START"),  # Initial button text
            font=("Consolas", 14, "normal"),
            bg="#000000",
            fg="#FFFFFF",
            command=self.toggle,  # Call the toggle method on click
            relief="flat",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground="#FFFFFF",
        )
        self.toggle_button.place(relx=0.5, rely=0.5, anchor="center", width=380, height=150)

        # Console log
        # A scrolled text box that logs stopwatch actions (e.g., "Stopwatch started", "Stopwatch stopped")
        self.console = ScrolledText(
            root,
            height=2,  # Compact height
            font=("Consolas", 3),
            state="disabled",  # Read-only mode
            wrap="word",  # Wrap text at word boundaries
            bg="#000000",
            fg="#FFFFFF",
            relief="flat",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground="#FFFFFF",
        )
        self.console.place(relx=0.5, rely=0.7, anchor="center", width=380)

        # Attach a smaller scrollbar to the console
        console_scrollbar = ttk.Scrollbar(root, command=self.console.yview, style="Vertical.TScrollbar")
        self.console.config(yscrollcommand=console_scrollbar.set)

        # Save button
        # A placeholder button for saving stopwatch data (functionality to be implemented)
        self.save_button = tk.Button(
            root,
            text=spaced_text("SAVE"),  # Button text
            font=("Consolas", 14, "normal"),
            bg="#000000",
            fg="#FFFFFF",
            command=self.save,  # Call the save method on click
            relief="flat",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground="#FFFFFF",
        )
        self.save_button.place(relx=0.5, rely=0.85, anchor="center", width=380, height=150)

        # Start the stopwatch's time updater
        self.update_time()

    def toggle(self):
        """Toggle the stopwatch between start and stop states."""
        if self.running:
            self.stop()
        else:
            self.start()

    def start(self):
        """Start the stopwatch."""
        self.running = True
        self.start_time = time.time() - self.elapsed_time  # Adjust for paused time
        self.toggle_button.config(
            text=spaced_text("STOP"),  # Update button text to "STOP"
            bg="#FFFFFF",  # White background when active
            fg="#000000",  # Black text when active
        )
        self.log_message("Stopwatch started.")  # Log the start action
        self.update_time()

    def stop(self):
        """Stop the stopwatch."""
        self.running = False
        self.elapsed_time = time.time() - self.start_time  # Calculate elapsed time
        self.toggle_button.config(
            text=spaced_text("START"),  # Update button text to "START"
            bg="#000000",  # Black background when inactive
            fg="#FFFFFF",  # White text when inactive
        )
        self.log_message(f"Stopwatch stopped at {self.format_time(self.elapsed_time)}.")  # Log the stop action

    def save(self):
        """Log a placeholder message for the save button."""
        self.log_message("Save button clicked. (No action implemented yet)")

    def update_time(self):
        """Update the stopwatch's time display."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time  # Calculate elapsed time
            self.time_display.config(text=self.format_time(self.elapsed_time))  # Update the display
        root.after(100, self.update_time)  # Call this method every 100 milliseconds
   

    def format_time(self, elapsed_time):
        """Convert elapsed time into HH:MM:SS format."""
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        return f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"

    def log_message(self, message):
        """Add a message to the console log."""
        self.console.config(state="normal")  # Enable editing to insert the message
        self.console.insert("end", message + "\n")  # Append the message
        self.console.see("end")  # Scroll to the latest log entry
        self.console.config(state="disabled")  # Disable editing


# Recipe input from outside the class
recipe_name = "Egg Hello!" # Recipe name to display in the app header

# Create the GUI application
root = tk.Tk()  # Create the main application window
root.title("Stopwatch")  # Set the window title
stopwatch = Stopwatch(root, recipe=recipe_name)  # Instantiate the Stopwatch class
root.mainloop()  # Run the application