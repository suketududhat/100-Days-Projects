from tkinter import *

GRID_PADX = 5
GRID_PADY = 5

window = Tk()
window.title("Mile to Km Coverter")
window.configure(bg="white")
window.config(padx=GRID_PADX, pady=GRID_PADY)
# window.minsize(width=500, height=500)

label = Label(text="is equal to")
label.grid(column=0, row=1, padx=GRID_PADX, pady=GRID_PADY)

entry = Entry(width=10)
entry.grid(column=1, row=0, padx=GRID_PADX, pady=GRID_PADY)

result_label = Label(text="0")
result_label.grid(column=1, row=1, padx=GRID_PADX, pady=GRID_PADY)


def action():
    miles = entry.get()
    km = float(miles) * 1.609
    result_label.config(text=f"{km}")


button = Button(text="Calculate", command=action)
button.grid(column=1, row=2, padx=GRID_PADX, pady=GRID_PADY)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=GRID_PADX, pady=GRID_PADY)

km_label = Label(text="Km")
km_label.grid(column=2, row=1, padx=GRID_PADX, pady=GRID_PADY)

window.mainloop()
