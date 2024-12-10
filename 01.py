import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Event Planner")
window.geometry("600x700")

title = tk.Label(window, font=("Comic Sans MS", 20),
                 text="Plan Your Event", fg="blue")
title.pack()

label1 = tk.Label(window, font=("Comic Sans MS", 10),
                  text="Enter the Event Name:")
label1.pack()

ent = tk.Entry(window, font=("Comic Sans MS", 10), width=20)
ent.pack()

label2 = tk.Label(window, font=("Comic Sans MS", 10),
                  text="Select Preferences:")
label2.pack()

chcating = tk.IntVar()
chcat = tk.Checkbutton(window, font=(
    "Comic Sans MS", 10), text="Include Catering", variable=chcating)
chcat.pack(anchor="w")

chmusic = tk.IntVar()
chmus = tk.Checkbutton(window, font=(
    "Comic Sans MS", 10), text="Provide Music", variable=chmusic)
chmus.pack(anchor="w")

chonlinest = tk.IntVar()
chol = tk.Checkbutton(window, font=("Comic Sans MS", 10),
                      text="Enable Online Streaming", variable=chonlinest)
chol.pack(anchor="w")

label3 = tk.Label(window, font=("Comic Sans MS", 10),
                  text="Select Event Type:")
label3.pack()

eventype = tk.StringVar(value="None")
wed = tk.Radiobutton(window, font=("Comic Sans MS", 10), text="Wedding",
                     variable=eventype, value="Wedding").pack(anchor="w")
conf = tk.Radiobutton(window, font=("Comic Sans MS", 10), text="Conference",
                      variable=eventype, value="Conference").pack(anchor="w")
bdp = tk.Radiobutton(window, font=("Comic Sans MS", 10), text="Birthday Party",
                     variable=eventype, value="Birthday Party").pack(anchor="w")


label4 = tk.Label(window, font=("Comic Sans MS", 10), text="Number of Guests:")
label4.pack()

scale = tk.Scale(window, from_=0, to=510, length=1000,
                 orient="horizontal", tickinterval=50)
scale.pack()

label5 = tk.Label(window, font=("Comic Sans MS", 10),
                  text="Select Event Theme:")
label5.pack()

listbox = tk.Listbox(window, width=25, height=8)
listbox.pack()
listbox.insert(0, "Modern")
listbox.insert(1, "Classic")
listbox.insert(2, "Rustic")
listbox.insert(3, "Futuristic")


def reset():
    chmus.deselect()
    chcat.deselect()
    chol.deselect()
    ent.delete(0, tk.END)
    eventype.set(None)
    scale.set(0)
    listbox.select_clear(0, tk.END)


def submit():
    if chcating.get() == 1:
        catering = "Include Catering"
    else:
        catering = ""
    if chmusic.get() == 1:
        music = "Provide Music"
    else:
        music = ""
    if chonlinest.get() == 1:
        streaming = "Enable Online Streaming"
    else:
        streaming = ""
    messagebox.showinfo("Event Summary", f"Event Name: {ent.get()}\nPrefrences: {catering} {music} {streaming}\nEvent Type: {
        eventype.get()}\nNumber of Guests: {scale.get()}\nEvent Theme: {listbox.get(tk.ACTIVE)}")


sub = tk.Button(window, font=("Comic Sans MS", 20),
                text="Submit", command=submit, bg="green", fg="white")
sub.pack()
sub.place(y=560, x=180)

button = tk.Button(window, font=("Comic Sans MS", 20),
                   text="Reset", bg="red", fg="white", command=reset)
button.pack()
button.place(y=560, x=320)
window.mainloop()
