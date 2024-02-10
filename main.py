import tkinter as tk
import customtkinter as ctk
from backend import get_food_info
ctk.set_appearance_mode("Dark")   
ctk.set_default_color_theme("blue")
appWidth, appHeight = 600, 700
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food Expire-E Program")   #change the name later
        self.geometry(f"{appWidth}x{appHeight}")    

        #Name Entry
        self.nameLabel = ctk.CTkLabel(self,
                                text="Name")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text="Shaurya")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Products Label
        self.productLabel = ctk.CTkLabel(self, text="Products")
        self.productLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Product Entry Field
        self.productEntry = ctk.CTkEntry(self,
                            placeholder_text="e.x:Potato")
        self.productEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results",
                                         command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")
 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self,
                                         width=400,
                                         height=200)
        self.displayBox.grid(row=6, column=0,
                             columnspan=4, padx=20,
                             pady=20, sticky="nsew")
    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)
    def createText(self):
        expireitems = self.productEntry.get()
        expireitems1 = ""
        for x in expireitems:
            if not x.isalpha():
                expireitems1 += "1"
            else:
                expireitems1 += x
        expireitems1 = expireitems1.split("1")
        newexpireitems = []
        for x in expireitems1:
            if expireitems1 != "" and expireitems1 != " " and expireitems1 != "  ":
                newexpireitems.append(x)
        text = str(self.nameEntry.get()) + ":" 
        for x in newexpireitems:
            text+= "\nYour " + x + " expires in " + get_food_info(x) + " days, "
        return text

if __name__ == "__main__":
    app = App()
    app.mainloop()