fileName = "PoultryProjectCalculatorGUI.txt"
accessMode = "a"
with open(fileName, accessMode) as myFile :

    import tkinter
    import tkinter.ttk
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import messagebox
    import datetime 
    CurrentDate = datetime.date.today()
    #label_widget = tkinter.Label(window, text = f"{dt.datetime.now(): %a, %b %d %Y}, fg = 'red', bg = 'black').pack()
    TotalCost = 0
    def clicked():
        TotalCost = 0
        if c.get() == 'USD':
            TotalCost = Var.get() * 5
        elif c.get() == 'Bond' :
            TotalCost = Var.get() * 400
        elif c.get() == 'EcoCash' :
            TotalCost = Var.get() * 450

        messagebox.showinfo("Sue's Chickens Calculator", "Thank you " + n.get() + " " + m.get() + " " + s.get() + " for shopping at Sue's Chickens! The cost for your %d chickens will be " %Var.get() + "%d"%TotalCost + " " + c.get() + ".")
        #res = 'Welcome to ' +  entry_widget1.get()
        #entry_widget1.configure(window, text = res)
        #return

    window = tkinter.Tk()
    window.title("Sue's Chickens Calculator")
    window.geometry('1400x700')
    #button_widget2 = tkinter.Button(window, text = 'Quit', bg = 'red', fg = 'white', font = ('Edwardian Script ITC',15), command = window.quit).place(x = 1000, y = 1)
    icon = tkinter.PhotoImage(file = "C:/Users/MUKAHLERA/Sue's Chickens.png")
    icon2 = tkinter.PhotoImage(file = "C:/Users/MUKAHLERA/Sue's Chickens2.png")

    label_widget = tkinter.Label(window,image = icon).pack(side= LEFT)
    label_widget = tkinter.Label(window,image = icon2).pack(side= RIGHT)


    label_widget = tkinter.Label(window, text = "SUE'S CHICKENS", font = ('Elephant', 40)).pack()
    label_widget = tkinter.Label(window, text = 'Welcome customer, please fill in the details below.', font = ('Edwardian Script ITC',35)).pack()

    n = StringVar()
    n.get()
    m = StringVar()
    m.get()
    s = StringVar()
    s.get()
    label_widget = tkinter.Label(window, text = 'First Name', font = ('Elephant',15)).place(x = 420, y = 150)
    entry_widget1 = tkinter.Entry(window, width = 20, textvariable = n).place(x = 420, y = 200)
    label_widget = tkinter.Label(window, text = 'Middle Name', font = ('Elephant',15)).place(x = 610, y = 150)
    entry_widget2 = tkinter.Entry(window, width = 20, textvariable = m).place(x = 620, y = 200)
    label_widget = tkinter.Label(window, text = 'Last Name', font = ('Elephant',15)).place(x = 820, y = 150)
    entry_widget3 = tkinter.Entry(window, width = 20,  textvariable = s).place(x = 820, y = 200)

    label_widget = tkinter.Label(window, text = '\nHow many chickens do you want to buy? ', font = ('Edwardian Script ITC',30)).place(x = 450, y = 220)
    Var = IntVar()
    Var.get()
    Var.set(1)
    spinbox_widget = tkinter.Spinbox(window, width = 9, from_ = 1, to = 100, font = ('Elephant',12), textvariable = Var).place(x= 620, y = 330)


    p = StringVar()
    p.get()
    p.set('Now')
    label_widget = tkinter.Label(window, text = '''
    Do you want to pay now or later? ''', font = ('Edwardian Script ITC',30)).place(x = 480, y = 350)
    radiobutton_widget = tkinter.Radiobutton(window, text = 'Now', value = 'Now' , variable = p,font = ('Elephant', 15)).place(x = 500, y = 450)
    radiobutton_widget = tkinter.Radiobutton(window, text = 'Later', value ='Later' , variable = p,font = ('Elephant', 15)).place(x = 750, y = 450)
    
    c = StringVar()
    c.get()
    c.set('Bond')
    label_widget = tkinter.Label(window, text = '''
    What currency do you want to use? ''', font = ('Edwardian Script ITC',30)).place(x = 460, y = 500)
    radiobutton_widget = tkinter.Radiobutton(window, text = 'USD', value = 'USD', variable = c,font = ('Elephant', 15)).place(x = 420, y = 600)
    radiobutton_widget = tkinter.Radiobutton(window, text = 'Bond', value = 'Bond', variable = c,font = ('Elephant', 15)).place(x = 630, y = 600)
    radiobutton_widget = tkinter.Radiobutton(window, text = 'EcoCash', value = 'EcoCash', variable = c,font = ('Elephant', 15) ).place(x = 830, y = 600)

    if p.get() == 'Now':
         myFile.write("\n" + "SALE")
         myFile.write(" > " + n.get() + " " + m.get() + " " + s.get()+ " bought " )
         myFile.write(str(Var.get()) + " chickens ") 
         myFile.write(CurrentDate.strftime("on %d %b %Y"))
         myFile.write(" for " + str(TotalCost) + c.get())
    elif p.get() == 'Later':
         myFile.write("\n" + "DEBT")
         myFile.write(" > " + n.get() + " " + m.get() + " " + s.get()+ " took " )
         myFile.write(str(Var.get()) + " chickens ") 
         myFile.write(CurrentDate.strftime("on %d %b %Y"))
         myFile.write(" and owes us " + str(TotalCost) + " " + c.get())
         

    button_widget = tkinter.Button(window, text = 'Done', width = 4 , font = ('Edwardian Script ITC', 18),command = clicked ).pack(side =BOTTOM)

    

    window.mainloop()
