#import modules
from tkinter import *
from twilio.rest import Client
import os
import random
import bcrypt
#OTP GENERATION SYSTEM
def randomNumberGenerator():
    randomNumber=""
    for i in range(4):
        randomNumber=randomNumber+str(int(random.random()*10))
    return randomNumber
def sendOtp():
    client = Client("AC499d3910607d435f71965d93b85ffd76", "60183ca1a26e642323b8201db0a925bd")
    otpNumber=randomNumberGenerator()
    #sending SMS to number
    client.messages.create(to="+918124098373", 
                       from_="+19143038933", 
                       body=otpNumber)
    return otpNumber
#CRYTOGRAPHY
def encryption(password):
    password=password.encode('utf-8')
    hashed=bcrypt.hashpw(password,bcrypt.gensalt(10))
    return hashed
def decryption(hashed,password):
    hashed=hashed[2:len(hashed)-1]
    password=password.encode('utf-8')
    hashed=hashed.encode('utf-8')
    return bcrypt.hashpw(password,hashed)
#GRAPHICAL USER INTERFACE 
# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1980x1200")
    global username
    global password
    global inputOtp
    global username_entry
    global password_entry
    global inputOtp_entry
    global generatedOtp
    generatedOtp=sendOtp()
    username = StringVar()
    password = StringVar()
    inputOtp=StringVar()
    Label(register_screen, text="Note:OTP WILL BE SEND TO ADMIN MOBILE NUMBER", bg="red", font=("Calibri", 13)).pack()
    Label(register_screen, text="Please enter below details").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ", font=("Calibri", 13))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ", font=("Calibri", 13))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    otp_lable = Label(register_screen, text="OTP * ", font=("Calibri", 13))
    otp_lable.pack()
    inputOtp_entry = Entry(register_screen, textvariable=inputOtp)
    inputOtp_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
# Designing window for login 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1980x1200")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
# Implementing event on register button
def register_user():
    if str(inputOtp.get())==generatedOtp:
        username_info = username.get()
        password_info = password.get()
        password_info=str(encryption(password_info))
        file = open(username_info, "w")
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        inputOtp_entry.delete(0,END)
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        inputOtp_entry.delete(0,END)
        Label(register_screen, text="Enter valid OTP", fg="green", font=("calibri", 11)).pack()
# Implementing event on login button 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if str(decryption(verify[0],password1))==verify[0]:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()
# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x200")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("300x200")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("300x200")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
# Deleting popups
def delete_login_success():
    login_success_screen.destroy()
    main_screen.destroy()
    import Controller
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1980x1200")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop()
main_account_screen()
