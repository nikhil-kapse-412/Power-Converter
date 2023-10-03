from tkinter import*
from tkinter.messagebox import*
import re

root = Tk()
root.title("Power Converter")
root.geometry("600x600+50+50")
f = ("Arial", 30, "bold", 'italic')

lab_header = Label(root, text="Power Converter", font=f)
lab_header.pack(pady=6)

conversion_factors = {
    "Horsepower to Watts": 745.7,
    "Watts to Horsepower": 1 / 745.7
}

conversion_type_var = StringVar(root)
conversion_type_var.set("Horsepower to Watts")  # Default selection
conversion_type_menu = OptionMenu(root, conversion_type_var, *conversion_factors.keys())
conversion_type_menu.config(font=f)
conversion_type_menu.pack(pady=3)

lab_hp = Label(root, text="Enter Value", font=f)
lab_hp.pack(pady=5)
ent_hp = Entry(root, font=f)
ent_hp.pack(pady=5)

special_char_pattern = r'[!@#$%^&*()+=/\|""'',?]'

def convert():
    try:
        hp = ent_hp.get()
        conversion_type = conversion_type_var.get()

        if hp == "":
            showerror("Issue", f"{conversion_type} Horsepower cannot be empty")
        elif re.search(special_char_pattern, hp):
            showerror("issue", f"{conversion_type}Horsepower cannot be special character")
        elif " " in hp:
            showerror("Issue", f"{conversion_type}Horsepower cannot be spaces")
        elif float(hp)< 0:
            showerror("issue", f"{conversion_type}Horsepower should be positive")
        elif not hp.replace(".", "").isdigit():
            showerror("Issue", f"{conversion_type}Horsepower cannot be text")
        else:
        
            hp_float = float(hp)
            wa = hp_float * conversion_factors[conversion_type]
            
            lab_wa.configure(text=f"Conversion {wa:.4f}")
    except Exception as e:
        showerror("Issue", "Horsepower should be a number")

lab_wa = Label(root, text="Conversion", font=f)
lab_wa.pack(pady=5)

btn_convert = Button(root, text="Convert", font=f, command=convert)
btn_convert.pack(pady=5)

root.mainloop()
