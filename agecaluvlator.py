# import the tkinter library
from calendar import calendar
from re import I
import re
from time import strftime
from tkinter import font, messagebox
from tkinter import *
import datetime
from babel.dates import get_month_names
from tkcalendar import *


# Creating the frame
window = Tk()

# defing variable
heading = StringVar()

# Constants for the window
'''
Taking screen width and height of the use and subtracting it with the window's width and height
to align the window box in the center of the screen
'''
user_window_Width = window.winfo_screenwidth()
user_window_Height = window.winfo_screenheight()

window_height = 600
window_width = 700

position_right = (user_window_Width/2)-(window_width/2)
position_down = (user_window_Height/2)-(window_height/2)


# Characters of the windowo
window.title("Age Calculator")
window.geometry(
    f'{window_width}x{window_height}+{int(position_right)}+{int(position_down)}')
window.resizable(width=False, height=False)
window.iconbitmap(
    r'C:\Users\97798\Desktop\Python\GUI\Age_calculator\Resource\icon.ico')
window.config(bg="#353238")


def exit():
    window.destroy()


def people_birthday():
    if date_split[1] == 1:
        messagebox.showinfo("Birthdays In Janurary",
                            "Elvis Presley: January 8\nSimone de Beauvoir: January 9 \nAlexander Hamilton: January 11\nMartin Luther King Jr.: January 15\nMuhammad Ali: January 17 ")

    elif date_split[1] == 2:
        messagebox.showinfo("Birthdays In Feburary",
                            "Cristiano Ronaldo. Feb 05\nNeymar. Feb 05\nOle Gunnar Solskjær. Feb 26")

    elif date_split[1] == 3:
        messagebox.showinfo("Birthdays In March",
                            "Justin Bieber\nQuentin Tarantino.\nShaquille O'neal")

    elif date_split[1] == 4:
        messagebox.showinfo("Birthdays In April",
                            "Robert Downey Jr\nCobie Smulders\nRussell Crowe")

    elif date_split[1] == 5:
        messagebox.showinfo("Birthdays In May",
                            "Jamie Dornan\nGeorge Clooney\nStephen Amell")

    elif date_split[1] == 6:
        messagebox.showinfo("Birthdays In June",
                            "Sundar Pichai\nGeorge Orwell\nDisha Patani")

    elif date_split[1] == 7:
        messagebox.showinfo("Birthdays In July",
                            "Dalai Lama\nGregory Isaacs\nPriyanka Chopra")

    elif date_split[1] == 8:
        messagebox.showinfo("Birthdays In August",
                            "Jason Momoa\nMary Louise Parker\nVera Farmiga")

    elif date_split[1] == 9:
        messagebox.showinfo("Birthdays In September",
                            "Zendaya\nSalma Hayek\nKeanu Reeves")

    elif date_split[1] == 10:
        messagebox.showinfo("Birthdays In October",
                            "Dakota Johnson\nCamilla Belle\nMatt Damon")

    elif date_split[1] == 11:
        messagebox.showinfo("Birthdays In November",
                            "Toni Collette\nFamke Janssen\nDavid Schwimmer")

    else:
        messagebox.showinfo("Birthdays In December",
                            "Zoe Kravitz\nPaula Patton\nLucy Liu")


def select_date():
    mydate = cal.get_date()
    convert_date_listtointeger(mydate)


def convert_date_listtointeger(mydate):
    global date_split
    date_split = mydate.split("/")
    for i in range(len(date_split)):
        date_split[i] = int(date_split[i])
    conversion(date_split)


def conversion(date_split):

    get_year = int(str(20)+(strftime('%y')))
    get_month = (strftime('%m'))
    get_day = (strftime('%d'))
    age_of_user_year = (get_year-date_split[0])
    age_of_user_month = abs((int(get_month)-date_split[1]))
    age_of_user_day = abs((int(get_day)-date_split[2]))
    display_age(age_of_user_year, age_of_user_month, age_of_user_day)


def display_age(age_of_user_year, age_of_user_month, age_of_user_day):
    messagebox.showinfo("Age caluclator", "You are = " + str(age_of_user_year) +
                        " YEARS "+str(age_of_user_month)+" MONTH AND "+str(age_of_user_day)+" DAYS OLD")


cal = Calendar(window, selectmode="day", year=2021,
               month=7, day=30, date_pattern='yyyy/mm/dd')
cal.place(x=0, y=230)


# desiging the age window


heading_text = Label(window, text="Age Calculator",
                     fg="#92140C", bg="#BE7C4D", padx=20,
                     pady=20, font=('Times', 20))
heading_text.pack(side=TOP)

# displayin todays date
global today_date
today_date = datetime.date.today()
td = Label(window, text="Today Date: "+str(today_date),
           bg="#C1B4AE", font=('Helvetica', 16), pady=30, padx=7)
td.place(x=2, y=120)

# picking today's date


# '''buttons for Caluclating and clearing


b_clear = Button(window, text="Exit",
                 font=('Helvetica', 10), width=20, height=4, background="#fa7921", activebackground="#fa7921", command=exit)
b_clear.place(x=0, y=450)
b_calculate = Button(window, text="Calculate",
                     font=('Helvetica', 10), width=20, height=4, background="#fa7921", activebackground="#fa7921", command=select_date)
b_calculate.place(x=200, y=450)
b_fpb = Button(window, text="Famous People Birthday",
               font=('Helvetica', 10), width=20, height=4, background="#fa7921", activebackground="#fa7921", command=people_birthday)
b_fpb.place(x=400, y=450)


window.mainloop()
