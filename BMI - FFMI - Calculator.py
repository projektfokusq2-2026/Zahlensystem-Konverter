import customtkinter as ctk

def fenster_anpassen():
    root.update_idletasks()
    aktuelle_hoehe = root.winfo_reqheight()
    aktuelle_breite = root.winfo_reqwidth()
    root.geometry(f"{aktuelle_breite}x{aktuelle_hoehe}")

def update_combobox_color(choice):
    if choice != "Geschlecht":
        geschlecht_box._entry.configure(state="normal")
        geschlecht_box.set(choice)
        geschlecht_box.configure(text_color="#FFFFFF")   
        geschlecht_box._entry.configure(state="readonly")
        geschlecht_box.update() 

def umrechnen():
    try:
        geschlecht = str(geschlecht_box.get())
        groeße = float(eingabe_feld2.get().replace(",", "."))
        groeße_quadrat = groeße * groeße
        gewicht = float(eingabe_feld1.get().replace(",", "."))
        bmi = gewicht/groeße_quadrat
        kfa_text = eingabe_feld3.get().strip('%')
        tabelle_maennlich = [(20, "Untergewicht", "#5CE6E6"),
                    (24.9, "Normalgewicht", "#2ECC71"),
                    (29.9, "Übergewicht", "#F1C40F"),
                    (34.9, "Adipositas Grad I", "#E67E22"),
                    (39.9, "Adipositas Grad II", "#E74C3C"),
                    (float("Inf"), "Adipositas Grad III", "#962D22")]
        tabelle_weiblich = [(19, "Untergewicht", "#5CE6E6"),
                            (23.9, "Normalgewicht", "#2ECC71"),
                            (29.9, "Übergewicht", "#F1C40F"),
                            (34.9, "Adipositas Grad I", "#E67E22"),
                            (39.9, "Adipositas Grad II", "#E74C3C"),
                            (float("Inf"), "Adipositas Grad III", "#962D22")]
        tabelle_ffmi = [(18, "Sehr wenig Muskelmasse", "#5CE6E6"),
                        (20, "Durchschnittliche Muskelmasse", "#2ECC71"),
                        (23, "Sportliche Muskelmasse", "#2ECC71"), 
                        (25, "Sehr hohe Muskelmasse", "#2ECC71"),
                        (float("Inf"), "Natürliches Limit überschritten", "#F1C40F")]
        bmi_tat = ""
        anteil_muskelmasse= ""
        farbe_normal = "#FFFFFF"
        farbe_ffmi = "#FFFFFF"
        if kfa_text == "":
            if geschlecht == "Männlich":
                for grenze, klasse, hex_farbe in tabelle_maennlich:
                    if bmi <= grenze:
                        bmi_tat = klasse
                        farbe_normal = hex_farbe
                        break
                label_ergebnis.configure(text=f"-> BMI: {bmi:.2f}\n -> Kategorie: {bmi_tat}", text_color=farbe_normal)
                label_muskeln.configure(text=f"")    
            elif geschlecht == "Weiblich":
                for grenze, klasse, hex_farbe in tabelle_weiblich:
                    if bmi <= grenze:
                        bmi_tat = klasse
                        farbe_normal = hex_farbe
                        break
                label_ergebnis.configure(text=f"-> BMI: {bmi:.2f}\n -> Kategorie: {bmi_tat}", text_color=farbe_normal) 
                label_muskeln.configure(text=f"")   
        else:
            kfa = float(kfa_text.replace(",", "."))
            ffm = gewicht * (1 - kfa/100)
            ffmi = ffm/groeße_quadrat
            if geschlecht == "Männlich":
                    for grenze, klasse, hex_farbe in tabelle_maennlich:
                        if bmi <= grenze:
                            bmi_tat = klasse
                            farbe = hex_farbe
                            break
                    for f_grenze, f_klasse, f_hex_farbe in tabelle_ffmi:
                        if ffmi <= f_grenze:
                            anteil_muskelmasse = f_klasse
                            farbe_ffmi = f_hex_farbe
                            break    
                    label_ergebnis.configure(text=f"-> BMI: {bmi:.2f}\n -> Kategorie: {bmi_tat}", text_color=farbe)
                    label_muskeln.configure(text=f"-> Muskelmasse: {anteil_muskelmasse}", text_color=farbe_ffmi)    
            elif geschlecht == "Weiblich":
                        for grenze, klasse, hex_farbe in tabelle_weiblich:
                            if bmi <= grenze:
                                bmi_tat = klasse
                                farbe = hex_farbe
                                break
                        for f_grenze, f_klasse, f_hex_farbe in tabelle_ffmi:
                            if ffmi <= f_grenze:
                                anteil_muskelmasse = f_klasse
                                farbe_ffmi = f_hex_farbe
                                break    
                        label_ergebnis.configure(text=f"-> BMI: {bmi:.2f}\n -> Kategorie: {bmi_tat}", text_color=farbe)
                        label_muskeln.configure(text=f"-> Muskelmasse: {anteil_muskelmasse}", text_color=farbe_ffmi)    
    except:
            label_ergebnis.configure(text="Ungültige Eingabe!")        
                
    fenster_anpassen()    

ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.title("BMI - Rechner")
root.geometry("400x650")
root.configure(fg_color="#000000")
root.bind("<Return>", lambda event: umrechnen())
root.resizable(False, False)

title_label = ctk.CTkLabel (
    root,
    text="BMI - Rechner",
    font=("Impact", 24),
    text_color="#95CBF5",
)
title_label.pack(pady=5)

label_anweisung1 = ctk.CTkLabel(
    root,
    text="Geschlecht",
    font=("Courier New", 18, "bold"),
    text_color="#FFFFFF"
)
label_anweisung1.pack(pady=5)    

geschlecht_box = ctk.CTkComboBox(
    root,
    values=["Männlich", "Weiblich"],
    width=280,
    height=45,
    corner_radius=20,
    border_width=3,
    font=("Courier New", 16, "bold"),
    text_color="#555566",
    border_color="#95CBF5",
    fg_color="#0A2438",
    button_color="#95CBF5",
    dropdown_fg_color="#0F2B48",            
    dropdown_text_color="#FFFFFF",           
    dropdown_hover_color="#1A3A5C",
    command=update_combobox_color
)
geschlecht_box.pack(pady=15)
geschlecht_box.set("Geschlecht")

label_anweisung2 = ctk.CTkLabel(
    root, 
    text="Körpergewicht in Kg", 
    font=("Courier New", 18, "bold"), 
    text_color="#FFFFFF"
)
label_anweisung2.pack(pady=5)

eingabe_feld1 = ctk.CTkEntry(
    root, 
    placeholder_text="Körpergewicht",
    font=("Courier New", 16, "bold"),
    width=280,
    height=45,
    corner_radius=20,
    border_width=3,
    border_color="#95CBF5",     
    fg_color="#0A2438",        
    text_color="#FFFFFF",       
    placeholder_text_color="#555566"
)
eingabe_feld1.pack(pady=15)

label_anweisung3 = ctk.CTkLabel(
    root, 
    text="Größe in m", 
    font=("Courier New", 18, "bold"), 
    text_color="#FFFFFF"
)
label_anweisung3.pack(pady=5)

eingabe_feld2 = ctk.CTkEntry(
    root, 
    placeholder_text="Größe",
    font=("Courier New", 16, "bold"),
    width=280,
    height=45,
    corner_radius=20,
    border_width=3,
    border_color="#95CBF5",     
    fg_color="#0A2438",        
    text_color="#FFFFFF",       
    placeholder_text_color="#555566"
)
eingabe_feld2.pack(pady=15)

label_anweisung4 = ctk.CTkLabel(
    root,
    text="Optional: Kfa (FFMI)",
    font=("Courier New", 18, "bold"),
    text_color="#FFFFFF"
)
label_anweisung4.pack(pady=5)

eingabe_feld3 = ctk.CTkEntry(
    root,
    placeholder_text="Körperfettanteil in %",
    font=("Courier New", 16, "bold"),
    width=280,
    height=45,
    corner_radius=20,
    border_width=3,
    border_color="#304D63",
    fg_color="#05121C",
    text_color="#FFFFFF",
    placeholder_text_color="#304D63"
)
eingabe_feld3.pack(pady=15)

button_berechnen = ctk.CTkButton(
    root, 
    text="Berechnen", 
    font=("Impact", 14),
    width=320,
    height=50,
    corner_radius=25,
    border_width=2,
    border_color="#95CBF5",    
    fg_color="#0A2438",         
    hover_color="#95CBF5",      
    text_color="#FFFFFF"        
)
button_berechnen.configure(command=umrechnen)
button_berechnen.pack(pady=20)

label_ergebnis = ctk.CTkLabel(
    root, 
    text="Warte auf Eingabe", 
    font=("Courier New", 20, "bold"), 
    text_color="#FFFFFF" 
)
label_ergebnis.pack(pady=25)

label_muskeln = ctk.CTkLabel(
     root,
     text="",
     font=("Courier New", 20, "bold"),
     text_color="#FFFFFF"
)
label_muskeln.pack(pady=5)

root.mainloop()