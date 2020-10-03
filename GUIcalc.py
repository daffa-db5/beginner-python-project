# this app is the part of https://github.com/daffa-db5/beginner-python-project
# Project : GUI Calculator using Python Tkinter
# Author : Daffa Rahman
# Date : 10/3/2020
# 
# requirements
# - tkinter


import tkinter as tk


def listToString(arr):
	result = ""
	for i in arr:
		result += str(i)
	return result

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		
		self.parent = parent

		self.cEntry = tk.Entry(self.parent)
		self.cEntryString = []
		self.bWidth = 10
		self.bHeight = 5

		self.ContentView()

	def ContentView(self):
		tk.Label(self.parent, text="PyCalculator").pack()

		self.cEntry.pack(fill="x")
		
		bFrame = tk.Frame(self)
		bFrame.pack(fill="both", expand=True)

		b1 = tk.Button(bFrame, text="7", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("7"))
		b2 = tk.Button(bFrame, text="8", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("8"))
		b3 = tk.Button(bFrame, text="9", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("9"))

		b4 = tk.Button(bFrame, text="4", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("4"))
		b5 = tk.Button(bFrame, text="5", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("5"))
		b6 = tk.Button(bFrame, text="6", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("6"))

		b7 = tk.Button(bFrame, text="1", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("1"))
		b8 = tk.Button(bFrame, text="2", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("2"))
		b9 = tk.Button(bFrame, text="3", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("3"))

		for i in range(9):
			eval(f"b{i+1}.grid(column={i % 3}, row={i // 3})")

		b0 = tk.Button(bFrame, text="0", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("0"))
		b0.grid(column=1, row=3)

		bE = tk.Button(bFrame, text="=", width=self.bWidth, height=self.bHeight, command=lambda:self.sendResult())
		bE.grid(column=0, row=3)

		bD = tk.Button(bFrame, text=".", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("."))
		bD.grid(column=2, row=3)

		bPlus = tk.Button(bFrame, text="+", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("+"))
		bMin = tk.Button(bFrame, text="-", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("-"))
		bMul = tk.Button(bFrame, text="x", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("*"))
		bDiv = tk.Button(bFrame, text="/", width=self.bWidth, height=self.bHeight, command=lambda:self.addToEntry("/"))

		bPlus.grid(column=3, row=0)
		bMin.grid(column=3, row=1)
		bMul.grid(column=3, row=2)
		bDiv.grid(column=3, row=3)

		bS = tk.Button(self, text="<x", command=lambda:self.popEntry())	
		bS.pack(fill="x")
		

	def insertEntry(self, entry, text):
		entry.delete(0, tk.END)
		entry.insert(0, text)

	def addToEntry(self, text):
		self.cEntryString.append(str(text))
		self.insertEntry(self.cEntry, listToString(self.cEntryString))

	def popEntry(self):
		try:
			self.cEntryString.pop()
			self.insertEntry(self.cEntry, listToString(self.cEntryString))
		except IndexError:
			print("No More Math!")

	def sendResult(self):
		text = self.cEntry.get()
		try:
			print(eval(text))
			self.cEntryString = []
			self.addToEntry(eval(text))
		except:
			print("sorry, i cant do that")
	
	
if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
