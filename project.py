from tkinter import *
import tkinter
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="-----", database="karkeradb")
cursor = mydb.cursor()
root = Tk()
root.geometry('500x500')
sub = IntVar()

#FORM 1
def form1():
    root1 = Tk()
    root1.geometry('500x500')
    label_0 = Label(root1, text="Form 1", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

#NAME
    label_1 = Label(root1, text="Name", width=10, font=("bold", 15))
    label_1.place(x=60, y=150)
    entry_1 = Entry(root1)
    entry_1.place(x=250, y=150)

#AGE
    def only_numbers(char):
        return char.isdigit()

    validation = root1.register(only_numbers)
    label_2 = Label(root1, text="Age", width=10, font=("bold", 15))
    label_2.place(x=53, y=190)
    entry_2 = Entry(root1, width=26, validate="key", validatecommand=(validation, '%S'))
    entry_2.place(x=200, y=190)

#SUBJECTS
    label_3 = Label(root1, text="Subjects", width=10, font=("bold", 15))
    label_3.place(x=63, y=240)
    var = IntVar()
    cbutton = tkinter.Checkbutton(root1, text="Enterprise java", variable=var)
    cbutton.place(x=190, y=240)
    var1 = IntVar()
    cbutton1 = tkinter.Checkbutton(root1, text="Linux", variable=var1)
    cbutton1.place(x=190, y=260)
    var2 = IntVar()
    cbutton2 = tkinter.Checkbutton(root1, text="IOT", variable=var2)
    cbutton2.place(x=190, y=280)
    var3 = IntVar()
    cbutton3 = tkinter.Checkbutton(root1, text="AWP", variable=var3)
    cbutton3.place(x=190, y=300)
    var4 = IntVar()
    cbutton4 = tkinter.Checkbutton(root1, text="SPM", variable=var4)
    cbutton4.place(x=190, y=320)

#MUSIC
    label_4 = Label(root1, text="Interested in music", width=20, font=("bold", 15))
    label_4.place(x=5, y=350)
    var8 = IntVar()
    var9 = IntVar()
    Radiobutton(root1, text="Yes", padx=5, variable=var8, value=1, ).place(x=190, y=350)
    Radiobutton(root1, text="No", padx=5, variable=var9, value=2 ).place(x=250, y=350)

#dropdown list
    variable = StringVar(root1)
    variable.set("Mr")
    w = OptionMenu(root1, variable, "Mrs", "Miss", "Dr")
    w.pack()
    w.place(x=190, y=150)

    def submit():
        cursor.execute('CREATE TABLE IF NOT EXISTS UserInfo(name varchar(200), age int(20))')
        cursor.execute('INSERT INTO UserInfo VALUES(%s,%s)', (entry_1.get(), entry_2.get()))
        mydb.commit()

    b3=Button(root1, text='Submit', width=20, bg='white', fg='black', command=submit)
    b3.place(x=180, y=380)

    b3 = Button(root1, text='Form 2', width=20, bg='white', fg='black', command=form2)
    b3.place(x=180, y=410)

    root1.mainloop()

#FORM2
def form2():
    root2 = Tk()
    root2.geometry('500x500')
    def only_numbers(char):
        return char.isdigit()

    validation = root2.register(only_numbers)

    label_5 = Label(root2, text="Form 2", width=20, font=("bold", 20))
    label_5.place(x=90, y=53)

    label_6 = Label(root2, text="10th Percentage", width=20, font=("bold", 15))
    label_6.place(x=33, y=150)
    entry_4 = Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry_4.place(x=200, y=150)
    label_7 = Label(root2, text="12th Percentage", width=20, font=("bold", 15))
    label_7.place(x=33, y=180)
    entry_5 = Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry_5.place(x=200, y=180)
    label_8 = Label(root2, text="Graduation Percentage", width=20, font=("bold", 15))
    label_8.place(x=15, y=210)
    entry_6 = Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry_6.place(x=200, y=210)
    label_9 = Label(root2, text="P.G Percentage", width=20, font=("bold", 15))
    label_9.place(x=33, y=240)
    entry_7 = Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry_7.place(x=200, y=240)
    label_10 = Label(root2, text="Other :", width=10, font=("bold", 15))
    label_10.place(x=105, y=280)
    label_10 = Label(root2, text="Exam Name", width=10, font=("bold", 15))
    label_10.place(x=190, y=280)
    entry_8 = Entry(root2, width=15)
    entry_8.place(x=300, y=280)
    label_10 = Label(root2, text="Percentage", width=10, font=("bold", 15))
    label_10.place(x=190, y=320)
    entry_9 = Entry(root2, width=15,  validate="key", validatecommand=(validation, '%S'))
    entry_9.place(x=300, y=320)



    def submit_it():
        cursor.execute('CREATE TABLE IF NOT EXISTS UserMarks(10th int(20), 12th int(20), Graduation int(20), PG int(20), OtherExam varchar(200), OtherMarks int(20) )')
        cursor.execute('INSERT INTO UserMarks VALUES(%s,%s,%s,%s,%s,%s)', (entry_4.get(), entry_5.get(), entry_6.get(), entry_7.get(), entry_8.get(), entry_9.get()))
        mydb.commit()

    b4 = Button(root2, text='Submit', width=20, bg='white', fg='black', command=submit_it)
    b4.place(x=180, y=380)

    Button(root2, width=20, bg='white', fg='black', text="Close", command=root2.destroy).place(x=180, y=420).pack()

    root2.mainloop()




l = tkinter.Label(root, text="Select a form ", font=("Helvetica", 19, "bold"))
l.place(x=180, y=100)
b1 = tkinter.Button(root, text='Form 1', height=3, width=19, command=form1)
b1.place(x=100, y=200)
b2 = tkinter.Button(root, text='Form 2', height=3, width=19, command=form2 )
b2.place(x=255, y=200)



root.mainloop()
