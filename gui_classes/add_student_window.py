import tkinter as tk
import customtkinter as ctk
import tkkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image
import access_data as ad
from tracking_system import TrackingSystem

class AddStudentWindow:
    def __init__(self, root, dimensions = "750x425"):
        self.root = root
        self.dimensions = dimensions

        self.create_ui()

    def create_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.tracker_window = ctk.CTkToplevel(self.root)
        self.tracker_window.geometry(self.dimensions)
        self.tracker_window.title("Add Student Window")

        self.frame = ctk.CTkFrame(master=self.tracker_window)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.title = ctk.CTkLabel(master=self.frame, text="Add New Student", font=("Arial", 24))
        self.title.pack(pady=12, padx=10)

        self.fname_label = ctk.CTkLabel(master=self.frame, text="First Name", font=("Arial", 18))
        self.fname_label.place(x=100, y=100)

        self.first_name = ctk.CTkEntry(master=self.frame, width=300, height=35, font=("Arial", 16), placeholder_text="Enter student's first name...")
        self.first_name.place(x=275, y=100)

        self.lname_label = ctk.CTkLabel(master=self.frame, text="Last Name", font=("Arial", 18))
        self.lname_label.place(x=100, y=175)

        self.last_name = ctk.CTkEntry(master=self.frame, width=300, height=35, font=("Arial", 16), placeholder_text="Enter student's last name...")
        self.last_name.place(x=275, y=175)

        self.email_label = ctk.CTkLabel(master=self.frame, text="Student Email", font=("Arial", 18))
        self.email_label.place(x=100, y=250)

        self.email = ctk.CTkEntry(master=self.frame, width=300, height=35, font=("Arial", 16), placeholder_text="Enter student's school email...")
        self.email.place(x=275, y=250)

        self.submit_button = ctk.CTkButton(master=self.frame, text="Add Student", command=self.submit)
        self.submit_button.place(x=250, y=325)

    def submit(self):
        pass





