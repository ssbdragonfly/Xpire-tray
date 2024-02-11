import customtkinter as ctk
from backend import handle_input

ctk.set_appearance_mode("Dark")   
ctk.set_default_color_theme("blue")

width, height = 1000, 600
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food Expire-E Program")   #change the name later
        self.geometry(f"{width}x{height}")    

        # Products Label
        self.product_label = ctk.CTkLabel(self, text="Products")
        self.product_label.pack(pady=20, padx=20, anchor="w")
 
        # Product Entry Field
        self.product_entry = ctk.CTkEntry(self,
                            placeholder_text="Comma seperated list!")
        self.product_entry.pack(pady=20, padx=20, anchor="w")

        # Generate Button
        self.gen_results_button = ctk.CTkButton(self,
                                         text="Generate Results",
                                         command=self.create_text)
        self.gen_results_button.pack(pady=20, padx=20, anchor="w")

    @staticmethod
    def filter_input(s: str) -> list[str]:
        s.replace(" ","")
        while s.count(",,"):
            s.replace(",,",",")
        return s.split(",")

    def create_text(self):
        expireitems = self.product_entry.get()
        expireitems = [x for x in self.filter_input(expireitems) if x]
        handle_input(expireitems)

if __name__ == "__main__":
    app = App()
    app.mainloop()
