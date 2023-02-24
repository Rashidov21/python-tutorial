from tkinter import Tk, Entry, Button, Label


window = Tk() # yangi tkinter oyna obyekti
window.title("Converter") # oyna sarlavhasi
window.geometry('400x250')  # oyna hajmi

# App body 
def convert_value():
    value = entry.get()
    lbl = Label(bg="#FAFAFA",text=f"Converted value : {value}" ,font=("Poppins SemiBold",16))
    lbl.grid(column=0, row=1)


entry = Entry(bg="#FAFAFA", font=("Poppins SemiBold",16))
btn = Button(text="Convert", bg="#232323", 
             foreground="#FAFAFA",
             font=("Poppins SemiBold",10),
             command=convert_value)

entry.grid(column=0, row=0)
btn.grid(column=1, row=0)


window.mainloop() # oynani ishga tushirish