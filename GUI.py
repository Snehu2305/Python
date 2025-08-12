import tkinter as tk

def addNum():
  num1 = int(entry1.get())
  num2 = int(entry2.get())

  result = num1 + num2
  result_label.condig(text="Result: " +str(result))

  root = tk.Tk()
  root.title("It's my first calculator with GUI")

  entry1 = tk.Entry(root)
  
