import tkinter
import random

windows = tkinter.Tk()

def RandomNum():
	MyRand = random.randint(1,1024)
	byte_thrown.configure(text="I threw a byte : " + str(MyRandom))
	
MyTitle = tkinter.Label(window, text="Random byte generator",font="calibri 16 bold")

MyButton = tkinter.Button(window, text="All Right!", command=RandNum)

byte_thrown = tkinter.Label(window, font="calibri 14 bold")
byte_thrown.pack()

window.mainloop()