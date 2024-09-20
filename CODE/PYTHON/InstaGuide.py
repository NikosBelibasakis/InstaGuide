#version 1

import customtkinter as ctk


# Create the main window
root = ctk.CTk()
root.title("InstaGuide")

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window geometry to cover 100% of the screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Function to clear the entry form
def clear_entry():
    url_entry.delete(0, 'end')

# Create a header label
header_label = ctk.CTkLabel(root, text="InstaGuide", font=("Arial", 64, "bold"), text_color="#65bbff")
header_label.pack(pady=20)  # Adds some padding at the top

# Create a frame to hold the label and entry field
frame1 = ctk.CTkFrame(root, fg_color=root.cget("fg_color"))  # Set frame color same as background
frame1.pack(pady=50, padx=50, anchor="w")  # Move the frame to the left

# Add label for the URL entry
url_label = ctk.CTkLabel(frame1, text="Please enter the URL of the accommodation page:", font=("Arial", 24, "bold"), text_color="#65bbff")
url_label.grid(row=0, column=0, padx=10, pady=10)

# Add entry form for the URL
url_entry = ctk.CTkEntry(frame1, width=400, fg_color=root.cget("fg_color"), border_color="#65bbff")
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a frame for the buttons
button_frame = ctk.CTkFrame(frame1, fg_color=root.cget("fg_color"))
button_frame.grid(row=1, column=1, pady=10)

# Add a button to clear the entry form
clear_button = ctk.CTkButton(button_frame, text="Clear", command=clear_entry, text_color="#65bbff",
                             fg_color=root.cget("fg_color"), border_color="#65bbff", border_width=2,
                             font=("Arial", 16, "bold"))
clear_button.pack(side="left", padx=15)

# Add a button to get the reviews
get_reviews_button = ctk.CTkButton(button_frame, text="Get Reviews", text_color="#65bbff",
                                   fg_color=root.cget("fg_color"), border_color="#65bbff", border_width=2,
                                   font=("Arial", 16, "bold"))
get_reviews_button.pack(side="right", padx=15)  # Place next to the Clear button 

# Start the main loop of the application
root.mainloop()
