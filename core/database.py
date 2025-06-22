# core/database.py

import mysql.connector as mysql
from tkinter import Tk, Label, Entry, Button, PhotoImage
from PIL import ImageTk
import os

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="your_passwrd"
)
data = db.cursor()

def create_database():
    try:
        data.execute("USE ruhidb")
    except:
        data.execute("CREATE DATABASE ruhidb")
        db.commit()

def create_user_table():
    try:
        data.execute("USE ruhidb")
        data.execute("SELECT id FROM ruhidb")
    except:
        data.execute("USE ruhidb")
        userdata = Tk()
        userdata.geometry('500x270')
        userdata.wm_iconbitmap('resources/winlogo.ico')
        userdata.title("Hello")
        userdata.configure(background="black")

        bgImg = PhotoImage(file="resources/signup.png", master=userdata)
        frame = Label(userdata, image=bgImg)
        frame.image = bgImg
        frame.place(x=0, y=0, relwidth=1, relheight=1)

        nam_ent = Entry(userdata, width=30)
        nam_ent.place(relx=.7, rely=.55, anchor="center")
        pass_ent = Entry(userdata, width=30)
        pass_ent.place(relx=.7, rely=.68, anchor="center")

        def makeDatabase1():
            pas = pass_ent.get()
            nam = nam_ent.get()
            data.execute("CREATE TABLE ruhidb(id INT(5), name VARCHAR(20), password VARCHAR(20), recent VARCHAR(50))")
            data.execute("INSERT INTO ruhidb(id, name, password) VALUES(1, %s, %s)", (nam, pas))
            db.commit()
            userdata.destroy()

        sign_img = PhotoImage(file="resources/sign_button.png", master=userdata)
        but1 = Button(userdata, image=sign_img, bg="#121212", activebackground="#FF5733", bd=0, command=makeDatabase1)
        but1.image = sign_img
        but1.place(relx=.5, rely=.9, anchor="center")
        userdata.mainloop()

def get_username():
    data.execute("USE ruhidb")
    data.execute("SELECT name FROM ruhidb")
    user = data.fetchone()
    return ''.join(user) if user else "User"

def change_username(nm):
    data.execute("USE ruhidb")
    query = "UPDATE ruhidb SET name = %s WHERE id = '1'"
    data.execute(query, (nm,))
    db.commit()

def get_recent():
    data.execute("USE ruhidb")
    data.execute("SELECT recent FROM ruhidb")
    rec = data.fetchone()
    return rec[0] if rec else ""

def update_recent(text):
    data.execute("USE ruhidb")
    query = "UPDATE ruhidb SET recent = %s WHERE id = '1'"
    data.execute(query, (text,))
    db.commit()

def create_history_table():
    try:
        data.execute("USE ruhidb")
        data.execute("SELECT user FROM recent_data")
    except:
        data.execute("CREATE TABLE recent_data(time VARCHAR(50), user VARCHAR(20), query VARCHAR(50), date VARCHAR(50))")
        db.commit()

def insert_history(time, user, query, date):
    data.execute("USE ruhidb")
    data.execute("INSERT INTO recent_data VALUES (%s, %s, %s, %s)", (time, user, query, date))
    db.commit()

def fetch_history():
    data.execute("USE ruhidb")
    data.execute("SELECT * FROM recent_data")
    return data.fetchall()

def delete_history():
    data.execute("USE ruhidb")
    data.execute("DELETE FROM recent_data")
    db.commit()
