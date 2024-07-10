from tkinter import *                                                   # importiere den Standard von tkinter
from tkinter import messagebox                                          # importiere auch die messagebox

# Plan für heute:
# - Testen des Layouts, Verbesserungspotentiale erkennen
# - Analyse des Codes (wdh). 
# - Neuerungen: ipad, columnspan, title und geometry
# - Erster Einblick in Variablen
# - Umstellen des Layouts auf Variablen durch die TN
# - Falls noch Zeit: Auslesen des Inhalts von Texten und String-Verkettung


# Layout
# Vorname: ___________ Nachname: ______________
# Strasse: ____________________________________
# PLZ: _______         Ort: ___________________
# E-MAIL:  ____________________________________
#  <OK>  <Abbrechen>

# Event handler für die Buttons
def onOKClick():
    messagebox.showinfo(title = "Hinweis", message="OK Clicked")

def onCancelClick():
    messagebox.showinfo(title = "Hinweis", message="Auf wiedersehen!")
    exit()
    
# Anwendungsfenster
win_anwendung = Tk()                                                                                  
frame_person = Frame(master=win_anwendung, background="lightgrey")
 
label_vorname = Label(master = frame_person, text = "Vorname:", background="lightgrey")         
entry_vorname = Entry(master = frame_person)
label_nachname = Label(master = frame_person, text = "Nachname:", background="lightgrey")
entry_nachname = Entry(master = frame_person)
label_strasse = Label(master = frame_person, text = "Strasse:", background="lightgrey")
entry_strasse = Entry(master = frame_person)
label_plz = Label(master = frame_person, text = "PLZ:", background="lightgrey")
entry_plz = Entry(master = frame_person)
label_ort = Label(master = frame_person, text = "Ort:", background="lightgrey")
entry_ort = Entry(master = frame_person)
label_email = Label(master = frame_person, text = "E-Mail:", background="lightgrey")
entry_email = Entry(master = frame_person)

button_ok = Button(master = frame_person, text="OK", command = onOKClick)
button_cancel = Button(master = frame_person, text="Cancel", command = onCancelClick)
# grid-Layout
label_vorname.grid(column = 0, row = 0, padx = 10, pady = 5, sticky="W")
entry_vorname.grid(column = 1, row = 0, padx = 10, pady = 5,  sticky="WE")
label_nachname.grid(column = 2, row = 0, padx = 10, pady = 5, sticky="W")
entry_nachname.grid(column = 3, row = 0, padx = 10, pady = 5, sticky="WE")
label_strasse.grid(column=0, row=1, padx = 10, pady = 5, sticky="W")
entry_strasse.grid(column=1, row=1, padx = 10, pady = 5, columnspan=3, sticky="EW")
label_plz.grid(column=0, row=2, padx = 10, pady = 10, sticky="W")
entry_plz.grid(column=1, row=2, padx = 10, pady = 10, ipady=2, sticky="W") # sieht besser aus mit innerem padding, oder?
label_ort.grid(column=2, row=2, padx = 10, pady = 10, sticky="W")
entry_ort.grid(column=3, row=2, padx = 10, pady = 10, sticky="EW")
label_email.grid(column=0, row=3, padx = 10, pady = 10, sticky="W")
entry_email.grid(column=1, row=3, padx = 10, pady = 10, sticky="EW", columnspan=3)
button_ok.grid(column = 0, row = 4, pady=10)
button_cancel.grid(column = 1, row = 4, pady=10)
frame_person.grid(row = 0, column = 0, sticky = "NSEW")

# responsives Design einschalten
frame_person.columnconfigure(0, weight = 1)
frame_person.columnconfigure(1, weight = 1)
frame_person.columnconfigure(2, weight = 1)
frame_person.columnconfigure(3, weight = 1)
frame_person.rowconfigure(0, weight = 2)
frame_person.rowconfigure(1, weight = 2)
frame_person.rowconfigure(2, weight = 2)
frame_person.rowconfigure(3, weight = 2)
frame_person.rowconfigure(4, weight = 0)

win_anwendung.columnconfigure(0, weight = 1)
win_anwendung.rowconfigure(0, weight = 1)
win_anwendung.title("Adressverwaltung")
win_anwendung.geometry("450x280")
win_anwendung.mainloop()                                                      # Endlossschleife bis Fenster geschlossen wird
