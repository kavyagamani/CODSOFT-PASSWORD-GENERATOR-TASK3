from tkinter import *
import random
import string

root= Tk()
root.geometry("1500x800")
root.title("Password Generator")

root.configure(bg="#000033")




passstr=StringVar()
pwd_len= IntVar()



#function to generate the password
def get_pass():
    pass1= string.ascii_letters+string.digits+string.punctuation
    password=""


    for x in range(pwd_len.get()):#loop to generate the user given length for passwd
        password= password+ random.choice(pass1)
        passstr.set(password)


#tkinter command to generate the gui application
Label(root,text="Password Generator",font="calibri 18 bold",bg="#ac00e6", justify="center",).pack(pady=110)
Label(root,text="Enter Length of the password",bg="#bf00ff",fg="white",padx=20,pady=10,justify="center").pack(pady=9)

Entry(root,textvariable=pwd_len,width=50).pack(pady=2,side=TOP,anchor=N,ipady=5)
Button(root,text="Generate Password",command=get_pass,bg="#bf00ff",fg="white",padx=20,pady=10).pack(pady=9)
Entry(root,textvariable=passstr,width=50).pack(pady=2,side=TOP,anchor=N,ipady=5)

root.mainloop()