from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#heading
Label(root,text="python registration form", font="ar 15 bold").grid(row=0 , column=3)

#fieldname 
name = Label(root,text="name")
Phone = Label(root,text="Phone")
Gender = Label(root,text="Gender")
Emergency= Label(root,text="Emergency")
paymentmood = Label(root,text="paymentmood")

#packingfield
name.grid(row=1 , column=2)
Phone.grid(row=2 , column=2)
Gender.grid(row=3 , column=2)
Emergency.grid(row=4 , column=2)
paymentmood.grid(row=5 , column=2)

#variable for store data
namevalue = StringVar
Phonevalue = StringVar
Gendervalue = StringVar
Emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

#create entry feild
nameentry = Entry(root, textvariable= namevalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Emergencyentry = Entry(root, textvariable=Emergencyvalue)
paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

#packing entryfield
nameentry.grid(row=1, column=3)
Phoneentry.grid(row=2, column=3)
Genderentry.grid(row=3, column=3)
Emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#create check box 
checkbtn = Checkbutton(text= "remember me?", variable=checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="submit", command=getvals).grid(row=7,column=3)


root.mainloop()