import customtkinter as ctk
from gui_classes.add_student_window import AddStudentWindow
from gui_classes.add_record_window import AddRecordWindow

# GUI Class for managing properties of main menu interface
class MainMenu:
    root = ''

    def __init__(self, root):
        self.root = root
        self.create_ui()

    # Creates user interface with all necessary elements
    def create_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Defines space within which elements may be positioned
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Sets the title of this application
        self.title = ctk.CTkLabel(master=self.frame, text="Main Menu", font=("Arial", 24))
        self.title.pack(pady=12, padx=10)

        # Allows user to navigate to create account window
        self.add_student_button = ctk.CTkButton(master=self.frame, text="Add a New Student", command=self.add_student)
        self.add_student_button.pack(padx=20, pady=20)

        # Allows user to navigate to login window
        self.add_record_button = ctk.CTkButton(master=self.frame, text="Add a New Record", command=self.add_record)
        self.add_record_button.pack(padx=20, pady=20)
    
    # Will be executed once create account button is pressed
    def add_student(self):
        AddStudentWindow(self.root)
        self.root.withdraw()

    # Will be executed once login button is pressed
    def add_record(self):
        AddRecordWindow(self.root)
        self.root.withdraw()

    



