import tkinter as tk

root = tk.Tk()
root.title('Infinity')
root.geometry('600x400+500+200')
# root.iconbitmap('bomb.ico')

label_1 = tk.Label(font=('Arial', 20,'bold'),
                   text = 'Miracle',
                   bg = 'blue',
                   fg = 'black',
                   padx = 60,
                   pady = 37,
                   width = 8,
                   height = 2,
                   anchor = 'ne',
                   relief= tk.RAISED,
                   bd = 20)
label_1.pack()

root.mainloop()