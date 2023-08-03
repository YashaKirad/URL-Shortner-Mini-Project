from tkinter import *
import pyshorteners


root = Tk()
root.title("URL Shortener")
root.geometry("650x300")
root.resizable(False,False)

def my_url():
    url_entry = url.get()
    result = pyshorteners.Shortener().tinyurl.short(url_entry)
    urlEntry.insert(END, result)

Label(root,text="URL Shortner",font=("georgia",20,"bold"),fg="black").pack(pady=10)

frame1 = Frame(root)
Label(frame1,text="Enter URL Here: ",font=("georgia",15,"bold")).pack(side=LEFT)
url = Entry(frame1,width=35,font=("cambria",15),bg="white")
url.pack()
frame1.pack(pady=10)


Button(root,text="Generate Link",font=("cambria",15,"bold"),fg="black",bg="sky blue",command=my_url).pack(pady=10)

frame2 = Frame(root)
Label(frame2,text="Shortened URL: ",font=("georgia",15,"bold")).pack(side=LEFT)
urlEntry = Entry(frame2,width=35,font=("cambria",15,"bold"),bg="white")
urlEntry.pack()
frame2.pack(pady=10)

root.mainloop()