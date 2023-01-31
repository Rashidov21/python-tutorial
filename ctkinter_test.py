import customtkinter

def button_event():
    print("Button")
    
    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{600}x{500}")
        self.title("CTk example")
        
        frame = customtkinter.CTkFrame(master=self,
                               width=200,
                               height=200,
                               corner_radius=10)
        frame.pack(padx=20, pady=20)
        
        entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        entry.pack(padx=20, pady=10)



app = App()
# app.configure(fg_color="#fff")
app.minsize(400,300)
app.maxsize(900,800)
# app.iconify()
app.mainloop()