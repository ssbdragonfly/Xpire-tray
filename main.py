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
        self.name_label = ctk.CTkLabel(self,
                                text="Name")
        self.name_label.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.name_entry = ctk.CTkEntry(self,
                          placeholder_text="Your name here!")
        self.name_entry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Products Label
        self.productLabel = ctk.CTkLabel(self, text="Products")
        self.productLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Product Entry Field
        self.product_entry = ctk.CTkEntry(self,
                            placeholder_text="Comma seperated list!")
        self.product_entry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")

        # Generate Button
        self.gen_results_button = ctk.CTkButton(self,
                                         text="Generate Results",
                                         command=self.generate_results)
        self.gen_results_button.grid(row=5, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")
 
        # Text Box
        self.display_box = ctk.CTkTextbox(self,
                                         width=400,
                                         height=200)
        self.display_box.grid(row=6, column=0,
                             columnspan=4, padx=20,
                             pady=20, sticky="nsew")
    def generate_results(self):
        self.display_box.delete("0.0", "200.0")
        text = self.create_text()
        self.display_box.insert("0.0", text)

    def create_text(self):
        expireitems = self.product_entry.get()
        expireitems.replace(" ","")
        expireitems.replace(",,",",")
        expireitems = expireitems.split(",")
        newexpireitems = []
        for x in expireitems:
            if x != "":
                newexpireitems.append(x)
        text = str(self.name_entry.get()) + ":" 
        for x in newexpireitems:
            text+= "\nYour " + x + " expires in " + get_food_info()[x] + " days, "
        return text

if __name__ == "__main__":
    app = App()
    app.mainloop()
