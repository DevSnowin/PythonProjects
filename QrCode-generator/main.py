from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import functions


root = Tk()
root.geometry("600x350")
root.title("QR Maker")
root.iconbitmap('icon.ico')


# functions
def showinfo(title, body):
    messagebox.showinfo(title, body)


def showwarning(title, body):
    messagebox.showwarning(title, body)


def showerror(title, body):
    messagebox.showerror(title, body)


def choosePath():
    savingPath_entry.delete(0, END)
    savePath = filedialog.askdirectory(initialdir="/", title="Select a folder")

    if savePath != "":
        savingPath_entry.insert(0, f"{savePath}/QR.jpg")


def saveQR():
    location_value = savingPath_entry.get()
    text_value = link_entry.get()

    if text_value != "" and location_value != "":
        functions.createQR(text_value, location_value)
        showinfo("Success!", "Image has been saved successfully!")
        link_entry.delete(0, END)
        savingPath_entry.delete(0, END)

    elif text_value == "" or location_value == "":
        showwarning("Invaild entries", "Please fill all the fields!")

    else:
        showerror("Error", "Something went wrong please try after sometimes")


# Image
btnSavePath = PhotoImage(file = "btnPah.png")

# Labels
head1_label = Label(root, text="Generate QR Code", font=('Roboto', 18, "bold"))
head1_label.place(x="211", y="32")

link_label = Label(root, text="Paste the link or text here", font=('Roboto', 12, 'normal'))
link_label.place(x="123", y="110")

savingPath_label = Label(root, text="Choose a location_value to save", font=('Roboto', 12, 'normal'))
savingPath_label.place(x="123", y="182")

# Entry
link_entry  = Entry(root, width=40, font=('Roboto', 12, 'normal'))
link_entry.place(x="123", y="139")

savingPath_entry  = Entry(root, width=40, font=('Roboto', 12, 'normal'))
savingPath_entry.place(x="123", y="211")

# Button
btnPathSaving = Button(root, image=btnSavePath, bd=0, command=choosePath)
btnPathSaving.place(x="495", y="215")

btnSave = Button(
            root, text="Save",
            font=('Roboto', 10, 'bold'),
            bg="#1A1A1A",
            fg="#fff",
            bd=0,
            padx=25,
            pady=5,
            command=saveQR
        )
btnSave.place(x="270", y="265")

root.mainloop()
