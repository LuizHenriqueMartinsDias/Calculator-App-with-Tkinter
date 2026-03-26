from tkinter import *
display_value = ""

#Window Config
window = Tk()
window.title("Calculator")
window.geometry("320x450")
window.config(background="gray")


#Display
Label(window,text=display_value ,height=6, justify="right").grid(row=0, column=0, columnspan=10, sticky="nsew")


#Buttons
Button(window,text="1",width=10,height=4).grid(row=4, column=1)
Button(window,text="2",width=10,height=4).grid(row=4, column=2)
Button(window,text="3",width=10,height=4).grid(row=4, column=3)
Button(window,text="4",width=10,height=4).grid(row=3, column=1)
Button(window,text="5",width=10,height=4).grid(row=3, column=2)
Button(window,text="6",width=10,height=4).grid(row=3, column=3)
Button(window,text="7",width=10,height=4).grid(row=2, column=1)
Button(window,text="8",width=10,height=4).grid(row=2, column=2)
Button(window,text="9",width=10,height=4).grid(row=2, column=3)
Button(window,text="0",width=10,height=4).grid(row=5, column=2)
Button(window,text="+",width=10,height=4).grid(row=4, column=4)
Button(window,text="-",width=10,height=4).grid(row=3, column=4)
Button(window,text="x",width=10,height=4).grid(row=2, column=4)
Button(window,text="+/-",width=10,height=4).grid(row=5, column=1)
Button(window,text="=",width=10,height=4).grid(row=5, column=4)
Button(window,text=".",width=10,height=4).grid(row=5, column=3)
Button(window,text="C",width=10,height=4).grid(row=1, column=2)
Button(window,text="<",width=10,height=4).grid(row=1, column=3)
Button(window,text="/",width=10,height=4).grid(row=1, column=4)
Button(window,text="x²",width=10,height=4).grid(row=1, column=1)

window.mainloop()

