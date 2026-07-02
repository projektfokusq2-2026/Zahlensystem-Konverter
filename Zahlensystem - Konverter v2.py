import customtkinter as ctk

def decimal_to_hexadecimal():
    decimal = int(eingabe_feld1.get())
    if decimal == 0:
        label_ergebnis1.configure(text=f"Hexadezimal: 0")
        return
    letters = ["A", "B", "C", "D", "E", "F"]
    numbers = [10, 11, 12, 13, 14, 15] 
    zuordnung = {}
    for letter, number in zip(letters, numbers):
        zuordnung[number] = letter
    result = ""    
    while decimal > 0:
        rest = decimal % 16
        if rest >= 10:
            final = zuordnung[rest]
        else:
            final = str(rest)
        result = final + result
        decimal = decimal // 16    
              
    label_ergebnis1.configure(text=f"Hexadezimal: {result}")

def hexadecimal_to_decimal():
    hexadecimal = str(eingabe_feld2.get()).upper()
    if hexadecimal == "0":
        label_ergebnis2.configure(text=f"Dezimal: 0")
        return
    letters = ["A", "B", "C", "D", "E", "F"]
    numbers = [10, 11, 12, 13, 14, 15] 
    zuordnung = {}
    for letter, number in zip(letters, numbers):
        zuordnung[letter] = number    
    result = 0
    for index, buchstabe in enumerate(reversed(hexadecimal)):
        if buchstabe.isdigit() == True:
            Ergebnis_dezimal = int(buchstabe) * 16 ** index
            result = result + Ergebnis_dezimal
        elif buchstabe.isalpha() == True:
            Ergebnis_buchstabe = zuordnung[buchstabe] * 16 ** index
            result = result + Ergebnis_buchstabe
    
    label_ergebnis2.configure(text=f"Dezimal: {result}")  

ctk.set_appearance_mode("Dark")     
                           
root = ctk.CTk()
root.title("Dezimal - Hexadezimal - Umrechner")
root.geometry("450x700")
root.configure(fg_color="#000000")

title_label = ctk.CTkLabel(
    root,
    text = "Zahlensystem-Konverter",
    font=("Impact", 24),
    text_color="#6E0A0A"
)    
title_label.pack(pady=5)

label_anweisung1 = ctk.CTkLabel(
    root, 
    text="Gebe Dezimal ein:", 
    font=("Courier New", 14, "bold"), 
    text_color="#888899"
)
label_anweisung1.pack(pady=5)

eingabe_feld1 = ctk.CTkEntry(
    root, 
    placeholder_text="Dezimal",
    font=("Courier New", 16, "bold"),
    width=280,
    height=45,
    corner_radius=20,
    border_width=3,
    border_color="#FF0000",     
    fg_color="#1A1A24",        
    text_color="#FFFFFF",       
    placeholder_text_color="#555566"
)
eingabe_feld1.pack(pady=15)

button_berechnen1 = ctk.CTkButton(
    root, 
    text="Berechnen", 
    font=("Impact", 14),
    width=320,
    height=50,
    corner_radius=25,
    border_width=2,
    border_color="#FF0000",    
    fg_color="#6E0A0A",         
    hover_color="#FF0000",      
    text_color="#FFFFFF"        
)
button_berechnen1.configure(command=decimal_to_hexadecimal)
button_berechnen1.pack(pady=20)

label_ergebnis1 = ctk.CTkLabel(
    root, 
    text="Warte auf Eingabe", 
    font=("Courier New", 20, "bold"), 
    text_color="#FFFFFF" 
)
label_ergebnis1.pack(pady=25)

label_anweisung2 = ctk.CTkLabel(
    root, 
    text="Gebe Hexadezimal ein:", 
    font=("Courier New", 14, "bold"), 
    text_color="#888899"
)
label_anweisung2.pack(pady=5)

eingabe_feld2 = ctk.CTkEntry(
    root, 
    placeholder_text="Hexadezimal",
    font=("Courier New", 16, "bold"),
    width=280,
    height=45,
    corner_radius=20,
    border_width=3,
    border_color="#FF0000",     
    fg_color="#1A1A24",        
    text_color="#FFFFFF",       
    placeholder_text_color="#555566"
)
eingabe_feld2.pack(pady=15)

button_berechnen2 = ctk.CTkButton(
    root, 
    text="Berechnen", 
    font=("Impact", 14),
    width=320,
    height=50,
    corner_radius=25,
    border_width=2,
    border_color="#FF0000",    
    fg_color="#6E0A0A",         
    hover_color="#FF0000",      
    text_color="#FFFFFF"        
)
button_berechnen2.configure(command=hexadecimal_to_decimal)
button_berechnen2.pack(pady=20)

label_ergebnis2 = ctk.CTkLabel(
    root, 
    text="Warte auf Eingabe", 
    font=("Courier New", 20, "bold"), 
    text_color="#FFFFFF" 
)
label_ergebnis2.pack(pady=25)

root.mainloop()