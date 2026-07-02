import customtkinter as ctk
from gui_classes.main_menu import MainMenu
from tracking_system import TrackingSystem

# Sets colour theme of application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Sets title and dimensions of window
root = ctk.CTk()
root.geometry("500x300")
root.title("Student Behaviour Tracker")

# Executed when file is being run
if __name__ == "__main__":
    try:
        app = MainMenu(root) # Creates a new instance of main menu which controls all windows
        TrackingSystem.connect_db()
        root.mainloop()
    except Exception as e: # When the system fails to create a new main menu instance
        print(f"An error occurred: {e}")


