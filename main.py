import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='ไม่ควรใส่')
        return 

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคุณแม่')
title_label.pack(pady=20)

number_input = tk.Entry(master=window, width=15)
number_input.pack()

go_button = tk.Button(
    master=window, text='มีอะไร',
    command=show_output, width=15, height=2
)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()