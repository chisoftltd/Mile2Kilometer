from tkinter import *

window = Tk()
window.title("Mile 2 Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
mile_label = Label(text="Miles", font=("Arial", 14, "bold"))
mile_label.grid(column=2, row=0)

# Label
equal_label = Label(text="is equal to: ", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

# Label
answer_label = Label(text="0.0", font=("Arial", 14, "bold"))
answer_label.grid(column=1, row=1)

# Label
km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)


# Method
def calculate_distance():
    answer_km = float(input.get()) * 1.609344
    answer_label.config(text=round(answer_km, 2))


# Button
calculate_button = Button(text="Calculate", command=calculate_distance, font=("Arial", 14, "bold"))
calculate_button.grid(column=1, row=2)
window.mainloop()
