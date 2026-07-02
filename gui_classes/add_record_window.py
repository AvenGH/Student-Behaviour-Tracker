import tkinter as tk
import customtkinter as ctk
import tkkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image
import access_data as ad
from tracking_system import TrackingSystem

class AddRecordWindow:
    def __init__(self, root, dimensions = "750x650"):
        self.root = root
        self.dimensions = dimensions

        self.ap_text_variable = ctk.StringVar()
        self.ap_text_variable.set("0")

        self.bp_text_variable = ctk.StringVar()
        self.bp_text_variable.set("0")

        self.names = [
            "Avaneesh Kumar", 
            "Shay Patel", 
            "Varchas Ravishankar", 
            "Rahul Joshi", 
            "Venuk Perera", 
        ]

        self.record_types = [
            "Achievement Point", 
            "Behaviour Point", 
            "R1",
            "R2",
            "R3",
            "R4",
            "R5",
            "R6",
            "R7"
        ]

        self.create_ui()

    
    def create_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        style = tb.Style(theme="darkly")

        self.tracker_window = ctk.CTkToplevel(self.root)
        self.tracker_window.geometry(self.dimensions)
        self.tracker_window.title("Student Behaviour Tracker")

        self.frame = ctk.CTkFrame(master=self.tracker_window)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.title = ctk.CTkLabel(master=self.frame, text="Welcome to the Student Behaviour Tracker!", font=('Arial', 24))
        self.title.pack(pady=12, padx=10)

        self.student_name_label = ctk.CTkLabel(master=self.frame, text="Student Name", font=("Arial", 18))
        self.student_name_label.place(x=100, y=100)

        self.student_name = ctk.CTkComboBox(master=self.frame, values=self.names, width=240, height=35, font=("Arial", 16), state="readonly")
        self.student_name.set("Select Student Name")
        self.student_name.place(x=275, y=100)

        self.record_type_label = ctk.CTkLabel(master=self.frame, text="Type", font=("Arial", 18))
        self.record_type_label.place(x=100, y=175)

        self.record_type = ctk.CTkComboBox(master=self.frame, values=self.record_types, width=240, height=35, font=("Arial", 16), state="readonly")
        self.record_type.set("Select Type")
        self.record_type.place(x=275, y=175)

        self.reason_label = ctk.CTkLabel(master=self.frame, text="Reason", font=("Arial", 18))
        self.reason_label.place(x=100, y=250)

        self.reason = ctk.CTkEntry(master=self.frame, width=300, height=35, font=("Arial", 16), placeholder_text="Enter reason...")
        self.reason.place(x=275, y=250)

        self.date_label = ctk.CTkLabel(master=self.frame, text="Date", font=("Arial", 18))
        self.date_label.place(x=100, y=325)

        self.date = tb.DateEntry(master=self.frame, bootstyle="darkly")
        self.date.place(x=345, y=410)

        # Field that takes in the number of APs
        self.achievement_points_label = ctk.CTkLabel(master=self.frame, text="APs", font=("Arial", 18))
        self.achievement_points_label.place(x=100, y=400)

        # Allows the user to increment the number of APs
        self.ap_increment_button = ctk.CTkButton(master=self.frame, corner_radius=0, text="+", width=40, font=("Arial", 20), command=lambda : self.increment("ap", self.achievement_points.get()))
        self.ap_increment_button.place(x=275, y=400)

        # Value gets updated every time the user clicks on a '+' or '-' button
        self.achievement_points = ctk.CTkEntry(master=self.frame, corner_radius=0, textvariable = self.ap_text_variable, width=60, font=("Arial", 18), state="disabled")
        self.achievement_points.place(x=215, y=400)

        # Allows the user to decrement the number of APs
        self.ap_decrement_button = ctk.CTkButton(master=self.frame, corner_radius=0, text="-", width=40, font=("Arial", 20), command=lambda : self.decrement("ap", self.achievement_points.get()), state = ctk.DISABLED)
        self.ap_decrement_button.place(x=175, y=400)

        # Field that takes in the number of BPs
        self.behaviour_points_label = ctk.CTkLabel(master=self.frame, text="BPs", font=("Arial", 18))
        self.behaviour_points_label.place(x=375, y=400)

        # Allows the user to increment the number of BPs
        self.bp_increment_button = ctk.CTkButton(master=self.frame, corner_radius=0, text="+", width=40, font=("Arial", 20), command=lambda : self.increment("bp", self.behaviour_points.get()))
        self.bp_increment_button.place(x=550, y=400)

        # Value gets updated every time the user clicks on a '+' or '-' button
        self.behaviour_points = ctk.CTkEntry(master=self.frame, corner_radius=0, textvariable = self.bp_text_variable, width=60, font=("Arial", 18), state="disabled")
        self.behaviour_points.place(x=490, y=400)

        # Allows the user to decrement the number of BPs
        self.bp_decrement_button = ctk.CTkButton(master=self.frame, corner_radius=0, text="-", width=40, font=("Arial", 20), command=lambda:self.decrement("bp", self.behaviour_points.get()), state = ctk.DISABLED)
        self.bp_decrement_button.place(x=450, y=400)

        # Field that allows user to submit all their booking details
        self.submit_button = ctk.CTkButton(master=self.frame, fg_color="green", text="Add Student Record", command=self.submit)
        self.submit_button.place(x=250, y=475)


# Will be executed once '+' button is clicked
    def increment(self, type, value):
        if type == "ap" and self.record_type.get() == "Achievement Point":
            # Increments the value and then enables the decrement button
            self.ap_text_variable.set(str(int(value) + 1))
            self.ap_decrement_button.configure(state=ctk.NORMAL)
        elif type == "bp" and self.record_type.get() == "Behaviour Point":
            self.bp_text_variable.set(str(int(value) + 1))
            self.bp_decrement_button.configure(state=ctk.NORMAL)
        

    # Will be executed once '-' button is clicked
    def decrement(self, type, value):
        # Checks if the value is greater than zero, otherwise cannot be decremented as it results in a negative value
        if int(value) > 0:
            if type == "ap" and self.record_type.get() == "Achievement Point":
                # Decrements the value
                self.ap_text_variable.set(str(int(value) - 1))
            elif type == "bp" and self.record_type.get() == "Behaviour Point":
                self.bp_text_variable.set(str(int(value) - 1))

            # Disables the decrement buttons if the values cannot be decremented further
            if self.ap_text_variable.get() == "0":
                self.ap_decrement_button.configure(state=ctk.DISABLED)
            if self.bp_text_variable.get() == "0":
                self.bp_decrement_button.configure(state=ctk.DISABLED)

    def ap_valid(self):
        if self.record_type.get() == "Achievement Points":
            if self.achievement_points.get() == "0":
                return False
            
    def bp_valid(self):
        if self.record_type.get() == "Behaviour Points":
            if self.behaviour_points.get() == "0":
                return False

    # Will be executed once 'submit' button is clicked
    def submit(self):
        if self.student_name.get() == "" or self.record_type.get() == "" or self.reason.get() == "":
            tk.messagebox.showerror("Error", "All fields are required!")
            return
        
        if not self.ap_valid:
            tk.messagebox.showerror("Error", "Minimum of 1 AP is required!")
            return
        
        if not self.bp_valid:
            tk.messagebox.showerror("Error", "Minimum of 1 BP is required!")
            return
        
        achievement_points = self.achievement_points.get()
        behaviour_points = self.behaviour_points.get()

        if self.record_type.get() != "Achievement Point":
            achievement_points = 0
        if self.record_type.get() != "Behaviour Point":
            behaviour_points = 0
        
        TrackingSystem.add_student_record(self.student_name.get(), self.record_type.get(), self.reason.get(), self.date, achievement_points, behaviour_points)
        tk.messagebox.showinfo("Record added successfully", f"Your record has successfully been added.")
        return True

# Executed when file is being run
if __name__ == '__main__':
    root = ctk.CTk()
    TrackingSystem.connect_db()
    app = AddRecordWindow(root)
    root.mainloop()

