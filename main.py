from tkinter import *

window = Tk()
window.title("Mile 2 Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

input = Entry(width=10)
input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=("Arial", 14, "bold"))
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to: ", font=("Arial", 14, "bold"))
equal_label.grid(column=0, row=1)

answer_label = Label(text="0.0", font=("Arial", 14, "bold"))
answer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)


def calculate_distance():
    answer_km = float(input.get()) * 1.609344
    answer_label["text"] = round(answer_km, 2)


calculate_button = Button(text="Calculate", command=calculate_distance)
calculate_button.grid(column=1, row=2)
window.mainloop()
