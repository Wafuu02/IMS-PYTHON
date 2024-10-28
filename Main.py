import tkinter as tk
from tkinter import Label, Frame, Button, Toplevel, BOTTOM, X, RIDGE
import time
from datetime import datetime
from Encoding import EncodeClass
from Resupply import ReSupplyClass
from History import HistoryClass  # Import the new History class

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Xanje Print Track")
        self.root.config(bg="#f0f0f0")
        
        self.inventory = {
                "long_paper": 0,
                "short_paper": 0,
                "photo_paper": 0,
                "black_ink": 0,
                "yellow_ink": 0,
                "magenta_ink": 0,
                "cyan_ink": 0
            }

        super().__init__()
        self.load_inventory()

        # Title
        title = Label(self.root, text="Xanje Print - Track", font=("Times New Roman", 34, "bold"), bg="#2c3e50", fg="white")
        title.place(x=0, y=0, relwidth=1, height=70)

        # Clock
        self.lbl_clock = Label(self.root, text="", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()

        # Left Menu
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#ecf0f1")
        LeftMenu.place(x=0, y=102, width=200, height=600)
        lbl_Menu = Label(LeftMenu, text="Menu", font=("Times New Roman", 20, "bold"), bg="#1abc9c", fg="white").pack(side="top", fill="x")
        Button(LeftMenu, text="Encoding", command=self.Encoding, font=("Times New Roman", 20, "bold"), bg="white", bd=3, cursor="hand2", fg="#2c3e50").pack(side="top", fill="x")
        Button(LeftMenu, text="ReSupply", command=self.ReSupply, font=("Times New Roman", 20, "bold"), bg="white", bd=3, cursor="hand2", fg="#2c3e50").pack(side="top", fill="x")
        Button(LeftMenu, text="History", command=self.show_history, font=("Times New Roman", 20, "bold"), bg="white", bd=3, cursor="hand2", fg="#2c3e50").pack(side="top", fill="x")

        # Content
        lbl_paper = Label(self.root, text="Types of Papers", font=("goudy old style", 15), bg="#2980b9", fg="white").place(x=250, y=150, width=1000)
        self.lbl_LBP = Label(self.root, text=f"Long Bond Paper \n [ {self.inventory['long_paper']} ]", bd=5, relief=RIDGE, bg="#3498db", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_LBP.place(x=300, y=220, height=80, width=150)
        self.lbl_SBP = Label(self.root, text=f"Short Bond Paper \n [ {self.inventory['short_paper']} ]", bd=5, relief=RIDGE, bg="#3498db", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_SBP.place(x=650, y=220, height=80, width=150)
        self.lbl_PP = Label(self.root, text=f"Photo Paper \n [ {self.inventory['photo_paper']} ]", bd=5, relief=RIDGE, bg="#3498db", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_PP.place(x=1000, y=220, height=80, width=150)

        lbl_inks = Label(self.root, text="Ink Colors", font=("goudy old style", 15), bg="#2980b9", fg="white").place(x=250, y=350, width=1000)
        self.lbl_Blck = Label(self.root, text=f"Black \n [ {self.inventory['black_ink']} ]", bd=5, relief=RIDGE, bg="#2c3e50", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_Blck.place(x=300, y=420, height=80, width=150)
        self.lbl_Yllw = Label(self.root, text=f"Yellow \n [ {self.inventory['yellow_ink']} ]", bd=5, relief=RIDGE, bg="#f39c12", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_Yllw.place(x=650, y=420, height=80, width=150)
        self.lbl_Mgnt = Label(self.root, text=f"Magenta \n [ {self.inventory['magenta_ink']} ]", bd=5, relief=RIDGE, bg="#e74c3c", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_Mgnt.place(x=650, y=520, height=80, width=150)
        self.lbl_Cyn = Label(self.root, text=f"Cyan \n [ {self.inventory['cyan_ink']} ]", bd=5, relief=RIDGE, bg="#1abc9c", fg="white", font=("goudy old style", 12, "bold"))
        self.lbl_Cyn.place(x=1000, y=420, height=80, width=150)

        # Footer
        self.lbl_footer = Label(self.root, text="Xanje Print - Track Inventory Management System Developed By:(STATE UR GROUP)\n For Any Technical Issues(Contact this number)", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
        self.lbl_footer.pack(side=BOTTOM, fill=X)

        self.history = HistoryClass(Toplevel(self.root))  # Create an instance of the History class

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        current_date = datetime.now().strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f"Welcome to Xanje Print - Track \t\t Date: {current_date} \t\t Time: {current_time}")
        self.root.after(1000, self.update_clock)

    def Encoding(self):
        self.new_win = Toplevel(self.root)
        encoding_obj = EncodeClass(self.new_win, self)

    def ReSupply(self):
        self.new_win = Toplevel(self.root)
        inventory_obj = ReSupplyClass(self.new_win, self)


    def load_inventory(self):
        try:
            with open("C:\\Users\\MyPC\\Pictures\\New folder\\PROJECT 1-20241005T115651Z-001\\PROJECT 1\\Data\\inventory.txt", "r") as file:
                for line in file:
                    item, quantity = line.strip().split(":")
                    if item in self.inventory:
                        self.inventory[item] = int(quantity)
        except FileNotFoundError:
            print("Inventory file not found. Starting with empty inventory.")
            
    def save_inventory(self):
        with open("C:\\Users\\MyPC\\Pictures\\New folder\\PROJECT 1-20241005T115651Z-001\\PROJECT 1\\Data\\inventory.txt", "w") as file:
            for item, quantity in self.inventory.items():
                file.write(f"{item}:{quantity}\n")

    def update_inventory(self, long_paper, short_paper, photo_paper, black_ink, yellow_ink, magenta_ink, cyan_ink):
        self.inventory['long_paper'] += long_paper
        self.inventory['short_paper'] += short_paper
        self.inventory['photo_paper'] += photo_paper
        self.inventory['black_ink'] += black_ink
        self.inventory['yellow_ink'] += yellow_ink
        self.inventory['magenta_ink'] += magenta_ink
        self.inventory['cyan_ink'] += cyan_ink
        self.update_labels()
        self.save_inventory()
        action = f"Resupplied: Long={long_paper}, Short={short_paper}, Photo={photo_paper}, Black={black_ink}, Yellow={yellow_ink}, Magenta={magenta_ink}, Cyan={cyan_ink} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.history.log_action(action)  # Log the action

    def deduct_inventory(self, long_paper, short_paper, photo_paper, black_ink, yellow_ink, magenta_ink, cyan_ink):
        self.inventory['long_paper'] -= long_paper
        self.inventory['short_paper'] -= short_paper
        self.inventory['photo_paper'] -= photo_paper
        self.inventory['black_ink'] -= black_ink
        self.inventory['yellow_ink'] -= yellow_ink
        self.inventory['magenta_ink'] -= magenta_ink
        self.inventory['cyan_ink'] -= cyan_ink
        self.update_labels()
        self.save_inventory()
        action = f"Deducted: Long={long_paper}, Short={short_paper}, Photo={photo_paper}, Black={black_ink}, Yellow={yellow_ink}, Magenta={magenta_ink}, Cyan={cyan_ink} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.history.log_action(action)  # Log the action

    def show_history(self):
        self.history.master.deiconify()  # Show the history window

    def update_labels(self):
        self.lbl_SBP.config(text=f"Short Bond Paper \n [ {self.inventory['short_paper']} ]")
        self.lbl_LBP.config(text=f"Long Bond Paper \n [ {self.inventory['long_paper']} ]")
        self.lbl_PP.config(text=f"Photo Paper \n [ {self.inventory['photo_paper']} ]")
        self.lbl_Blck.config(text=f"Black \n [ {self.inventory['black_ink']} ]")
        self.lbl_Yllw.config(text=f"Yellow \n [ {self.inventory['yellow_ink']} ]")
        self.lbl_Mgnt.config(text=f"Magenta \n [ {self.inventory['magenta_ink']} ]")
        self.lbl_Cyn.config(text=f"Cyan \n [ {self.inventory['cyan_ink']} ]")

if __name__ == "__main__":
    root = tk.Tk()
    ims = IMS(root)
    root.mainloop()
