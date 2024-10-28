from tkinter import *

class ReSupplyClass:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app  # Reference to the main IMS instance
        self.root.geometry("900x600+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="lightgray")
        self.root.focus_force()

        # Function to validate integer input
        def validate_int(value_if_allowed):
            return value_if_allowed.isdigit() or value_if_allowed == ""  # Allow only digits or empty input

        validate_cmd = self.root.register(validate_int)

        # Create a parent frame to center the grids
        parent_frame = Frame(self.root, bg="lightgray")
        parent_frame.pack(expand=True, anchor="center")  # Center the parent frame within the window

        # Title
        title = Label(parent_frame, text="Resupply Materials", font=("goudy old style", 22, "bold"), bg="#007acc", fg="white")
        title.grid(row=0, columnspan=2, padx=20, pady=20)

        # Section: Papers
        paper_frame = LabelFrame(parent_frame, text="Papers", font=("goudy old style", 15), bg="white", fg="#007acc")
        paper_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        lbl_long_paper = Label(paper_frame, text="Long Bond Paper", font=("goudy old style", 14), bg="white", fg="black")
        lbl_long_paper.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.entry_long_paper = Entry(paper_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_long_paper.grid(row=0, column=1, padx=10, pady=10)

        lbl_short_paper = Label(paper_frame, text="Short Bond Paper", font=("goudy old style", 14), bg="white", fg="black")
        lbl_short_paper.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_short_paper = Entry(paper_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_short_paper.grid(row=1, column=1, padx=10, pady=10)

        lbl_photo_paper = Label(paper_frame, text="Photo Paper", font=("goudy old style", 14), bg="white", fg="black")
        lbl_photo_paper.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.entry_photo_paper = Entry(paper_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_photo_paper.grid(row=2, column=1, padx=10, pady=10)

        # Section: Inks
        ink_frame = LabelFrame(parent_frame, text="Inks", font=("goudy old style", 15), bg="white", fg="#007acc")
        ink_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        lbl_black_ink = Label(ink_frame, text="Black Ink", font=("goudy old style", 14), bg="white", fg="black")
        lbl_black_ink.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.entry_black_ink = Entry(ink_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_black_ink.grid(row=0, column=1, padx=10, pady=10)

        lbl_yellow_ink = Label(ink_frame, text="Yellow Ink", font=("goudy old style", 14), bg="white", fg="black")
        lbl_yellow_ink.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_yellow_ink = Entry(ink_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_yellow_ink.grid(row=1, column=1, padx=10, pady=10)

        lbl_magenta_ink = Label(ink_frame, text="Magenta Ink", font=("goudy old style", 14), bg="white", fg="black")
        lbl_magenta_ink.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.entry_magenta_ink = Entry(ink_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_magenta_ink.grid(row=2, column=1, padx=10, pady=10)

        lbl_cyan_ink = Label(ink_frame, text="Cyan Ink", font=("goudy old style", 14), bg="white", fg="black")
        lbl_cyan_ink.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.entry_cyan_ink = Entry(ink_frame, font=("goudy old style", 12), validate="key", validatecommand=(validate_cmd, '%P'), bd=2, relief="solid")
        self.entry_cyan_ink.grid(row=3, column=1, padx=10, pady=10)

        # Submit Button
        btn_submit = Button(parent_frame, text="Submit", font=("goudy old style", 15, "bold"), bg="#007acc", fg="white", cursor="hand2", command=self.submit)
        btn_submit.grid(row=3, column=0, columnspan=2, padx=20, pady=20, ipadx=10)

    def submit(self):
        try:
            # Get the input values from the entries, converting them to integers, and handle empty inputs
            long_paper = int(self.entry_long_paper.get()) if self.entry_long_paper.get() else 0
            short_paper = int(self.entry_short_paper.get()) if self.entry_short_paper.get() else 0
            photo_paper = int(self.entry_photo_paper.get()) if self.entry_photo_paper.get() else 0
            black_ink = int(self.entry_black_ink.get()) if self.entry_black_ink.get() else 0
            yellow_ink = int(self.entry_yellow_ink.get()) if self.entry_yellow_ink.get() else 0
            magenta_ink = int(self.entry_magenta_ink.get()) if self.entry_magenta_ink.get() else 0
            cyan_ink = int(self.entry_cyan_ink.get()) if self.entry_cyan_ink.get() else 0

            # Call the update_inventory method of the IMS instance to update the labels
            self.main_app.update_inventory(
                long_paper,
                short_paper,
                photo_paper,
                black_ink,
                yellow_ink,
                magenta_ink,
                cyan_ink
            )

            # Save the updated inventory
            self.main_app.save_inventory()

            # Close the ReSupply window after submission
            self.root.destroy()

        except ValueError:
            # Handle the case where a non-integer value is entered
            print("Please enter valid integer values for all fields.")

if __name__ == "__main__":
    root = Tk()
    obj = ReSupplyClass(root, None)  # Pass None for the main_app, but this will not be executed directly
    root.mainloop()
