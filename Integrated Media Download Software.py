import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tokenize import String
from pytube import YouTube


def Interactives():

    header = Label(root, text = "Welcome to IMDS",
                padx=15,
                pady=15,
                font="Courier 20 bold",
                bg="#BAAAAA",
                fg="black")
    header.grid(row=1,
                column=1,
                pady=10,
                padx=5,
                columnspan=3)
    link = Label(root,
                 text="Video Link:",
                 bg="#827676",
                 pady=5,
                 padx=5)
    link.grid(row=2,
              column=0,
              pady=5,
              padx=5)

    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
    
    save_label = Label(root,
                       text="Path:",
                       bg="#827676",
                       pady=5,
                       padx=9)
    save_label.grid(row=3,
                    column=0,
                    pady=5,
                    padx=5)
    
    root.saveText = Entry(root,
                           width=27,
                           textvariable=download_Path,
                           font="Arial 14")
    root.saveText.grid(row=3,
                       column=1,
                       pady=5,
                       padx=5)
    
    search_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#827676",
                      relief=RIDGE)
    
    search_B.grid(row=3,
                   column=2,
                   pady=1,
                   padx=1)

    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="white",
                        pady=10,
                        padx=15,
                        relief=RIDGE,
                        font="Georgia, 13")
    
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)

    
def Browse():

    download_Directory = filedialog.askdirectory(
        initialdir="Selected Directory Path", title ="Save Video"
    )

    download_Path.set(download_Directory)

def Download():

    Youtube_link = video_Link.get()

    download_Folder = download_Path.get()

    getVideo = YouTube(Youtube_link)

    videoStream = getVideo.streams.first()

    videoStream.download(download_Folder)

    messagebox.showinfo ("Success!", "Installed and Saved In\n" + download_Folder)


root = tk.Tk()


root.geometry("700x300")
root.resizable(FALSE,FALSE)
root.title("Integrated Media Download Software")
root.config(background="#BAAAAA")

video_Link = StringVar()
download_Path = StringVar()

Interactives()

root.mainloop()
