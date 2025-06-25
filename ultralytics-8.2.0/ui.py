import tkinter as tk
from tkinter import filedialog, scrolledtext
from stata_analy import parse_ascii_binary_with_ff_separator as parse_ascii_binary
from video_analy import video_analy as va

# Example binary list for demonstration
binary_list = []


def select_file():
    file_path = filedialog.askopenfilename()
    path_text.delete(1.0, tk.END)  # Clear the text box
    path_text.insert(tk.END, file_path)  # Insert the selected file path


def start_display():
    pathfile = path_text.get(1.0, tk.END)  # Get the selected file path
    pathfile = pathfile.rstrip('\n')
    binary_list = va(pathfile)
    content = parse_ascii_binary(binary_list)
    print(content)
    modified_string = "\n" + "\n\n".join("  " + line for line in content)
    result_text.delete(1.0, tk.END)  # Clear the result output box
    result_text.insert(tk.END, modified_string)  # Insert file content


def clear_text():
    result_text.delete(1.0, tk.END)  # Clear the result output box
    path_text.delete(1.0, tk.END)  # Clear the text box


# Create main window
root = tk.Tk()
root.title("LED State Inspection Demo")

# Create file path text box with increased height for two lines
path_text = tk.Text(root, height=2, width=50)  # Using Text widget for multi-line
path_text.grid(row=0, column=0, padx=10, pady=10)

# Create "Select File" button
select_button = tk.Button(root, text="Select File", command=select_file, width=15)
select_button.grid(row=0, column=1, padx=10, pady=10)

# Create result output box with same width as path_text
result_text = scrolledtext.ScrolledText(root, width=70, height=18)
result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create "Start" button with increased width
start_button = tk.Button(root, text="Start", command=start_display, width=15)  # Set width
start_button.grid(row=2, column=0, padx=10, pady=10, sticky='e')

# Create "Clear" button with increased width
clear_button = tk.Button(root, text="Clear", command=clear_text, width=15)  # Set width
clear_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')

# Start the main loop
root.mainloop()