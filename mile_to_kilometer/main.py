import tkinter

window = tkinter.Tk()
window.title("M to Km Converter")
window.minsize(200, 150)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=1, pady=20)
is_equal = tkinter.Label(text="is equal to ")
is_equal.grid(row=1, column=0, padx=(10, 10))
km1 = tkinter.Label(text="0")
km1.grid(row=1, column=1)
km2 = tkinter.Label(text="km")
km2.grid(row=1, column=2)


def click():
    miles_to_convert = int(miles_entry.get())
    km = miles_to_convert * 1.60934
    km1.config(text=(str(round(km))))


button = tkinter.Button(text="Calculate", command=click)
button.grid(row=2, column=1)

miles_entry = tkinter.Entry()
miles_entry.focus()
miles_entry.grid(row=0, column=1)

window.mainloop()
