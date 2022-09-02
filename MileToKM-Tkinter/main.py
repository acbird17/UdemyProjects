import tkinter

def button_clicked():
    new_get=int(input.get())
    new_text=round(new_get*1.609,2)
    km_label.config(text=new_text)

window = tkinter.Tk()
window.title("Miles to Kilometer")
window.minsize(500,300)
window.config(padx=20, pady=20)

equal_label = tkinter.Label(text="Label", font=("Arial", 20))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = tkinter.Label(text="Label", font=("Arial", 20))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Label", font=("Arial", 20))
km_label.config(text="0")
km_label.grid(column=1, row=1)

kms_label = tkinter.Label(text="Label", font=("Arial", 20))
kms_label.config(text="Km")
kms_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


input = tkinter.Entry(width=10, text="0")
print(input.get())
input.grid(column=1, row=0)

window.mainloop()