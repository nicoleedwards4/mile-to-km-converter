from tkinter import *

# mile to km converter with tkinter
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=40, pady=40)  # add window padding

# Entry
input = Entry(width=8)
input.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
# my_label.config(padx=50, pady=50) # add widget padding

# is equal to Label
equal_to_label = Label(text="is equal to", font=("Arial", 12))
equal_to_label.grid(column=0, row=1)

# km output label
km_output_label = Label(text="0", font=("Arial", 12))
km_output_label.grid(column=1, row=1)

# km label
km_label = Label(text="km", font=("Arial", 12))
km_label.grid(column=2, row=2)


# calculate button


def calculate_clicked():
    miles_input = input.get()
    km_output = float(miles_input) * 1.6
    km_output = int(km_output)
    km_output_label.config(text=km_output)
    window.update()


calculate = Button(text="Calculate", command=calculate_clicked)
calculate.grid(column=1, row=2)

window.mainloop()
