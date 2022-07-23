# import modules
import tkinter as tk
from tkinter import *
import whois

# user define function
# Getting Domain information

def Domain_information():
    Domain = whois.whois(str(e1.get()))
    server.set(Domain.whois_server)
    expire_date.set(Domain.expiration_date)
    reg_name.set(Domain.name)
    org.set(Domain.org)
    state.set(Domain.state)
    city.set(Domain.city)
    country.set(Domain.country)
    name_server.set(Domain.name_servers)
    email.set(Domain.emails)
    zip_code.set(Domain.zipcode)


# Object of tkinter
# Background  set for pink
root =tk.Tk()
root.title('Domain_Info')
root.geometry('500x500')
root.configure(bg='light pink')


# Variable Classes in tkinter

server = StringVar()
expire_date = StringVar()
reg_name = StringVar()
org = StringVar()
state = StringVar()
city = StringVar()
country = StringVar()
name_server = StringVar()
email=StringVar()
zip_code = StringVar()


# Creating label for each information
# Name using widget label

Label(root, text="Website URL: ", bg="light pink").grid(row=0, sticky=W)
Label(root, text="Server Name : ",   bg="light pink").grid(row=3,  sticky=W)
Label(root, text="Expiration date : ", bg="light pink").grid(row=4, sticky=W)
Label(root, text="Register name : ",  bg="light pink").grid(row=5,sticky=W)
Label(root, text="Organisation : ", bg="light pink").grid(row=6,sticky=W)
Label(root, text="State : ", bg="light pink").grid(row=7,   sticky=W)
Label(root, text="City : ", bg="light pink").grid(row=8, sticky=W)
Label(root, text="Country: ",  bg="light pink").grid(row=9,  sticky=W)
Label(root,text="Name_server: ", bg="light pink").grid(row=10, sticky=W)
Label(root,text="Email: ", bg="light pink").grid(row=11, sticky=W)
Label(root, text="Zipcode: ", bg="light pink").grid(row=12, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(root, text="", textvariable=server,bg="light pink").grid(row=3, column=1, sticky=W)
Label(root, text="", textvariable=expire_date,bg="light pink").grid(row=4, column=1, sticky=W)
Label(root, text="", textvariable=reg_name, bg="light pink").grid(row=5, column=1, sticky=W)
Label(root, text="", textvariable=org, bg="light pink").grid(row=6, column=1, sticky=W)
Label(root, text="", textvariable=state,bg="light pink").grid(row=7, column=1, sticky=W)
Label(root, text="", textvariable=city,bg="light pink").grid(row=8, column=1, sticky=W)
Label(root, text="", textvariable=country,bg="light pink").grid(row=9, column=1, sticky=W)
Label(root, text="", textvariable=name_server, bg="light pink").grid(row=10,column=1,sticky=W)
Label(root, text="", textvariable=email, bg="light pink").grid(row=11,column=1,sticky=W)
Label(root, text="", textvariable=zip_code, bg="light pink").grid(row=12,column=1,sticky=W)
e1 = Entry(root)
e1.grid(row=0, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(root, text="Hacked", command=Domain_information, activebackground='purple',bg="light pink")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5, )

mainloop()