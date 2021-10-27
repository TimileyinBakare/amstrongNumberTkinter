import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300, relief = 'raised')
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

label2 = tk.Label(root, text='Please input your Number?:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

def AmstrongNumber():  
    x1 = entry1.get()
    lengthOfInput = len(x1) #length of the input 
    x1 = int(x1)
    copyOfTheUserInput = x1
    result = 0

    while(x1!=0):
        digit = x1 % 10
        result = result + pow(digit,lengthOfInput)
        x1 = int(x1/10)
    if(result == copyOfTheUserInput):
        label1 = tk.Label(root, text="This is an Amstrong Number")
        label1.config(font=('helvetica', 14))
        canvas1.create_window(200, 230, window=label1)
        print("This is an Amstrong Number")
    else:
        label1= tk.Label(root, text="This is not an Amstrorng Number")
        label1.config(font=('helvetica', 14))
        canvas1.create_window(200, 230, window=label1)
        print("This is not an Amstrong Number")
    
button1 = tk.Button(text='Check if its an Amstrong Number', command=AmstrongNumber,bg='brown', fg='white')
canvas1.create_window(200, 180, window=button1)

root.mainloop()