import sqlite3
import tkinter as tk
from tkinter import ttk

#link to my repo
db_path = '/storage/emulated/0/MHDM_git/database/recipes.db'

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch data from the database
cursor.execute('SELECT * FROM recipes')
recipe_data = cursor.fetchall()

# Get column names from the table
cursor.execute('PRAGMA table_info(recipes)')
columns = [col[1] for col in cursor.fetchall()]

# Create Tkinter window
root = tk.Tk()
root.title("Recipe Viewer")
root.configure(bg="black")  # Black background

# Frame to hold Treeview and Scrollbars
frame = tk.Frame(root, bg="black")
frame.pack(fill=tk.BOTH, expand=True)

# Create a Treeview widget to display data
tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)

# Custom styles
style = ttk.Style()
style.theme_use("clam")  # More modern theme

# Apply black background and grey cell outlines
style.configure(
    "Treeview",
    background="black",
    foreground="white",
    fieldbackground="black",
    rowheight=65,
    font=("Arial", 4),  # Kept your original font size
    borderwidth=0,
    relief="flat"
)

# Header styling (Fixed Tuple Format)
style.configure(
    "Treeview.Heading",
    background="grey10",
    foreground="white",
    font=("Arial", 5, "bold"),  # Kept your original font size
    relief="flat"
)

# Set column widths dynamically **without modifying font sizes**
for col in columns:
    tree.heading(col, text=col, anchor="center")
    tree.column(col, width=150, anchor="center", stretch=False)  # Fixed width without auto-adjusting font

# Simulating grey cell borders with alternating row colours
def tag_rows():
    for i in range(len(recipe_data)):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", tk.END, values=recipe_data[i], tags=(tag,))

# Default row colours
tree.tag_configure("evenrow", background="grey8")  # Dark background for even rows
tree.tag_configure("oddrow", background="grey10")  # Slightly lighter for odd rows

# Change selection appearance: turquoise text, black background
style.map(
    "Treeview",
    background=[("selected", "black")],  # Cell background turns black when selected
    foreground=[("selected", "#00CED1")]  # Text turns turquoise blue when selected
)

# Insert data with tagging for striping effect
tag_rows()

# Add vertical scrollbar
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=v_scrollbar.set)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

# Add horizontal scrollbar
h_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tree.xview)
tree.configure(xscrollcommand=h_scrollbar.set)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# Bind scroll gestures to improve responsiveness
def scroll_y(event):
    tree.yview_scroll(int(-1 * (event.delta / 60)), "units")

def scroll_x(event):
    tree.xview_scroll(int(-1 * (event.delta / 60)), "units")

tree.bind("<MouseWheel>", scroll_y)
tree.bind("<Shift-MouseWheel>", scroll_x)

# Pack the Treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()