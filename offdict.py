from tkinter import *
import os
import glob
from PIL import Image,ImageTk
app = Tk()
app.resizable(0, 0)
app.geometry("600x225")
app.title("TRA TỪ ANH - VIỆT - ANH   ")


nen = Image.open("nen.png")
nenz=  ImageTk.PhotoImage(nen)

def opensource3(file):
	root = Tk()
	root.title("Dịch")
	root.resizable(0,0)
	scrollbar = Scrollbar(root)
	f =  open("Dict/" +file,"r",encoding ='utf8')
	scrollbar.pack(side = RIGHT,fill = Y)
	text = Text(root,wrap =WORD,yscrollcommand = scrollbar.set,fg = 'white',font = 'Ariel 13',bg = 'black')
	text.pack()
	text.insert(END,f.read())
	scrollbar.config(command = text.yview)
	root.mainloop()

def search():
	word = wordText.get()
	for file in os.listdir("Dict/"):
		if word+'.txt' == file:
			opensource3(file)		
def hideText(click):
    if  wordText.get() == u"Nhập từ và nhấn Enter để tra ":
        wordText.delete(0, "end")
        wordText.insert(0, '')


Label = Label(app,image = nenz,height = 225,width = 600)
Label.image= nenz
Label.place(x =0,y = 0)


keyWord = StringVar()
meaning = StringVar()
wordText = Entry(app,width=57,textvariable=keyWord,font=('Verdana',11),fg='red',justify='center')
wordText.grid(row=0, column=1, padx=3, pady=4)

wordText.insert(0, u"Nhập từ và nhấn Enter để tra ")
wordText.bind('<FocusIn>', hideText)
wordText.bind("<Return>", (lambda event: search()))



# searchButton = Button(app, text ="Search", command = search).pack()

app.mainloop()