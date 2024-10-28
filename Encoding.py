from tkinter import *
from tkinter import ttk

class EncodeClass:
    def __init__(self, root, ims_instance):
        self.root = root
        self.ims_instance = ims_instance  # Store the instance of IMS
        self.root.geometry("800x450+220+130")  # Adjusted window size
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_pages = IntVar()  # To store number of pages
        self.var_Type_Print = StringVar()  # To store type of print
        self.var_Size = StringVar()  # To store size of paper

        # Title
        title = Label(self.root, text="Print Details", font=("goudy old style", 22, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=0, y=0, relwidth=1, height=60)  # Title spans the entire width of the window

        # Labels
        lbl_size = Label(self.root, text="Size of Paper", font=("goudy old style", 16, "bold"), bg="white", fg="#0f4d7d")
        lbl_size.place(x=100, y=100)

        lbl_type_print = Label(self.root, text="Type of Print", font=("goudy old style", 16, "bold"), bg="white", fg="#0f4d7d")
        lbl_type_print.place(x=400, y=100)

        lbl_no_pages = Label(self.root, text="No. of Pages to Print", font=("goudy old style", 16, "bold"), bg="white", fg="#0f4d7d")
        lbl_no_pages.place(x=100, y=200)

        # Dropdowns for size and type of print
        self.size_dropdown = ttk.Combobox(self.root, textvariable=self.var_Size, values=["Select", "Short", "Long", "Photo Paper"], font=("goudy old style", 14), state="readonly")
        self.size_dropdown.place(x=100, y=130, width=220, height=30)
        self.size_dropdown.current(0)  # Set "Select" as default value

        self.type_print_dropdown = ttk.Combobox(self.root, textvariable=self.var_Type_Print, values=["Select", "Colored", "Black & White"], font=("goudy old style", 14), state="readonly")
        self.type_print_dropdown.place(x=400, y=130, width=220, height=30)
        self.type_print_dropdown.current(0)  # Set "Select" as default value

        # Validation function to ensure only integers in Entry widget
        def validate_int(value_if_allowed):
            return value_if_allowed.isdigit() or value_if_allowed == ""  # Accept digits only

        validate_cmd = self.root.register(validate_int)

        # Entry widget for number of pages (integer input only)
        entry_no_pages = Entry(self.root, textvariable=self.var_pages, font=("goudy old style", 14), validate="key", validatecommand=(validate_cmd, '%P'))
        entry_no_pages.place(x=100, y=230, width=220, height=30)

        # Submit button
        submit_btn = Button(self.root, text="Submit", font=("goudy old style", 16, "bold"), bg="#0f4d7d", fg="white", cursor="hand2", bd=0, command=self.deduct_inventory)
        submit_btn.place(x=325, y=320, width=150, height=40)

        # Styling the submit button to look modern
        submit_btn.config(highlightbackground="#0f4d7d", activebackground="#07496d", activeforeground="white")

    def deduct_inventory(self):
        # Get the number of pages, type of print, and size of paper
        total_pages = self.var_pages.get()
        print_type = self.var_Type_Print.get()
        paper_size = self.var_Size.get()

        # Initialize deductions
        yellow_deduction = 0
        magenta_deduction = 0
        cyan_deduction = 0
        black_deduction = 0
        long_paper_deduction = 0
        short_paper_deduction = 0
        photo_paper_deduction = 0

        # Deduction logic based on type of print
        if print_type == "Colored":
            if total_pages >= 350:
                yellow_deduction = total_pages // 350
                magenta_deduction = total_pages // 350
                cyan_deduction = total_pages // 350
        elif print_type == "Black & White":
            if total_pages >= 600:
                black_deduction = total_pages // 600

        # Deduct paper size based on the number of pages printed
        if paper_size == "Short":
            short_paper_deduction = total_pages  # Deduct pages from short paper
        elif paper_size == "Long":
            long_paper_deduction = total_pages  # Deduct pages from long paper
        elif paper_size == "Photo Paper":
            photo_paper_deduction = total_pages  # Deduct pages from photo paper

        # Call the update method in IMS
        self.ims_instance.deduct_inventory(long_paper_deduction, short_paper_deduction, photo_paper_deduction, black_deduction, yellow_deduction, magenta_deduction, cyan_deduction)

        # Log action in history
        action = f"Encoded Print - Pages: {total_pages}, Type: {print_type}, Size: {paper_size}"
        self.ims_instance.history.log_action(action)  # Log action

        # Optionally, you can close the encoding window after submission
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = EncodeClass(root, None)  # Pass None for ims_instance, but this will not be executed directly
    root.mainloop()
