from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("Calculator")
root.configure(bg='pink')
root.geometry('650x400')
upload=Image.open('Ls 54\Activity 1\Untitled.png')
upload=upload.resize(300,300)
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg='pink')
label.place(x=180,y=20)
label1=Label(root,text="Hi my dear User,Take your Payment",bg='pink')
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    Msgbox=messagebox.showinfo("Alert,Do you want to have your Transaction?")
    if Msgbox=='ok':
        topwin()
button1=Button(root,text="Let's get Started",command=msg,bg='brown',fg='white')
button1.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='light gray')
    top.geometry('600x350+50+50')
    label=Label(top,text="Total amount",bg='light gray')
    entry=Entry(top)
    lbl=Label(top,text="Here are the number of notes for each denomination",bg='light gray')
    l1=Label(top,text="1000",bg='light gray')
    l2=Label(top,text="500",bg='light gray')
    l3=Label(top,text="100",bg='light gray')
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
def calculator():
    try:
        global amount
        amount=int(entry.get())
        note1000=amount//1000
        amount%=1000
        note500=amount//500
        amount%=500
        note100=amount//100

        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)

        t1.insert(END, str(note1000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    except ValueError:
        messagebox.showerror("Please enter a valid number")

    btn=Button(top,text="Calculate",command=calculator,bg='brown',fg='white')
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place