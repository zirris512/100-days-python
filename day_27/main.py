from tkinter import *

FONT = ("Arial", 12, "bold")


def convert_to_km():
    km_conversion = round(float(miles_input.get()) * 1.609, 2)
    conversion_label["text"] = km_conversion


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

miles_input = Entry(width=5, font=FONT)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

conversion_label = Label(text="0", font=FONT)
conversion_label.grid(column=1, row=1)

button = Button(text="Calculate", font=FONT, command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
