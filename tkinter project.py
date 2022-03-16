from json import *
from time import *
from tkinter import *
from re import *
from tkinter import messagebox

def submit():
    cancel_button.configure(state='normal')
    delete_button.configure(state='disable')
    login_button.configure(state='disable')
    username = username_Entry.get()
    password = password_Entry.get()
    username_verify = verify_username(username)
    if username_verify:
        messagebox.showwarning('USERnameERROR', 'username already Exist.' + '\n' + 'please Enter another username')
        username_Entry.delete(0, 'end')
        username_Entry.insert(0, 'Enter new username')
    else:
        if (len(username) < 4):
            messagebox.showwarning('USERnameERROR', 'username most be more than 4 characters.')
            username_Entry.delete(0, 'end')
            username_Entry.insert(0, 'Enter username')
        else:
            pattern = compile(r'^[\w._]')
            check_key = 0
            for check in username:
                if pattern.match(check) is None:
                    check_key += 1
                    break
            if check_key == 1:
                messagebox.showwarning('USERnameERROR',
                                       'invalid username.' + '\n' + 'you can only use : alphabets , numbers ,"." and "_"')
                username_Entry.delete(0, 'end')
                username_Entry.insert(0, 'Enter username')
            else:
                if (len(password) < 4):
                    messagebox.showwarning('PASSwordERROR', 'password most be more than 4 characters.')
                    password_Entry.delete(0, 'end')
                    password_Entry.insert(0, 'Enter password')
                else:
                    with open('info.json') as info_file:
                        I_F = load(info_file)
                        I_F[username] = password
                    with open('info.json', 'w') as info_f:
                        dump(I_F, info_f)
                        messagebox.showinfo('Submit Message', 'your account has been registerd! ')
                        delete_button.configure(state='normal')
                        login_button.configure(state='normal')
                        cancel_button.configure(state='disable')
                        username_Entry.delete(0, 'end')
                        password_Entry.delete(0, 'end')
                        username_Entry.insert(0, 'Enter username')
                        password_Entry.insert(0, 'Enter password')

def login():
    cancel_button.configure(state='normal')
    submit_button.configure(state='disable')
    delete_button.configure(state='disable')
    username = username_Entry.get()
    password = password_Entry.get()
    username_verify = verify_username(username)
    if username_verify:
        password_verify = verify_password(username, password)
        if password_verify:
            messagebox.showinfo('Login Message', 'welocme!')
            login_button.configure(state='disabl')
            logout_button.configure(state='normal')
            cancel_button.configure(state='disable')
            username_Entry.delete(0, 'end')
            password_Entry.delete(0, 'end')
            username_Entry.insert(0, 'Enter username')
            password_Entry.insert(0, 'Enter password')
    else:
        messagebox.showerror('USERnameERROR', 'username not Exist.')
        username_Entry.delete(0, 'end')
        username_Entry.insert(0, 'Enter new username')

def delete():
    cancel_button.configure(state='normal')
    submit_button.configure(state='disable')
    login_button.configure(state='disable')
    username = username_Entry.get()
    password = password_Entry.get()
    username_verify = verify_username(username)
    if username_verify:
        password_verify = verify_password(username, password)
        if password_verify:
            d = messagebox.askquestion('Delete Acount', 'Are you sure?')
            if d == 'yes':
                with open('info.json') as info_file:
                    I_F = load(info_file)
                    I_F.pop(username)
                with open('info.json', 'w') as f:
                    dump(I_F, f)
                    messagebox.showinfo('Delete Acount', 'your Acount deleted!')
                    username_Entry.delete(0, 'end')
                    password_Entry.delete(0, 'end')
                    username_Entry.insert(0, 'Enter username')
                    password_Entry.insert(0, 'Enter password')
                    submit_button.configure(state='normal')
                    login_button.configure(state='normal')
                    cancel_button.configure(state='disable')
            else:
                username_Entry.delete(0, 'end')
                password_Entry.delete(0, 'end')
                username_Entry.insert(0, 'Enter username')
                password_Entry.insert(0, 'Enter password')
    else:
        messagebox.showerror('USERnameERROR', 'username not Exist.')
        username_Entry.delete(0, 'end')
        username_Entry.insert(0, 'Enter new username')

def logout():
    if submit_button["state"] == DISABLED and login_button['state'] == DISABLED:
        messagebox.showinfo('Logout Message', 'by!')
        delete_button.configure(state='normal')
        submit_button.configure(state='normal')
        login_button.configure(state='normal')
        logout_button.configure(state='disable')
        return

def cancel():
    password_count.set(3)
    username_Entry.delete(0, 'end')
    password_Entry.delete(0, 'end')
    username_Entry.insert(0, 'Enter username')
    password_Entry.insert(0, 'Enter password')
    delete_button.configure(state='normal')
    submit_button.configure(state='normal')
    login_button.configure(state='normal')
    logout_button.configure(state='disable')
    cancel_button.configure(state='disable')

def verify_username(user):
    with open('info.json') as info_file:
        I_F = load(info_file)
    if user in I_F:
        return True
    else:
        return False

def verify_password(user, pas):
    with open('info.json') as info_file:
        I_F = load(info_file)
    try_left = password_count.get()
    if I_F[user] == pas:
            password_count.set(3)
            return True
    else:
            a = messagebox.askquestion('PASSwordERROR', 'incorrect password.' + '\n' + 'Try again?')
            if a == 'yes':
                password_Entry.delete(0, 'end')
                password_Entry.insert(0, 'NEW password')
                password_count.set(try_left - 1)
                if try_left != 1:
                     return False
                else:
                    messagebox.showwarning('PASSwordERROR', "3 incorrect password." + '\n' + 'try after 4 seconds')
                    sleep(4)
                    password_count.set(3)
            else:
                cancel()
                return


def USERclick(*args):
    username_Entry.delete(0, 'end')

def PASSclick(*args):
    password_Entry.delete(0, 'end')

win = Tk()
win.title('win')
win.geometry('325x225')

password_count = IntVar()
password_count.set(3)

username_label = Label(win, text='username : ', width=9, height=1)
password_label = Label(win, text='password : ', width=9, height=1)

username_Entry = Entry(win, width=22)
password_Entry = Entry(win, width=22)

submit_button = Button(win, text='Submit', command=submit)
login_button = Button(win, text='Log in', command=login)
delete_button = Button(win, text='Delete', command=delete)
logout_button = Button(win, text='Log out', command=logout, state='disable')
cancel_button = Button(win, text='cancel', command=cancel, state='disable')

username_label.place(relx=0.15, rely=0.1)
username_Entry.place(relx=0.38, rely=0.12)
password_label.place(relx=0.15, rely=0.21)
password_Entry.place(relx=0.38, rely=0.22)
submit_button.place(relx=0.1, rely=0.8)
login_button.place(relx=0.3, rely=0.8)
delete_button.place(relx=0.5, rely=0.8)
logout_button.place(relx=0.7, rely=0.8)
cancel_button.place(relx=0.175, rely=0.33)

username_Entry.insert(0, 'Enter username')
password_Entry.insert(0, 'Enter password')

username_Entry.bind('<Button-1>', USERclick)
password_Entry.bind('<Button-1>', PASSclick)

try:
    with open('info.json') as test_file:
        T_file = load(test_file)
except FileNotFoundError:
    messagebox.showinfo('FileNotFound','test account created!')
    I_F = {'test_username': 'test_password'}
    with open('info.json', 'x') as test_file:
        dump(I_F, test_file)
        password_Entry.delete(0, 'end')
        username_Entry.delete(0, 'end')
        username_Entry.insert(0, 'Enter username')
        password_Entry.insert(0, 'Enter password')

win.mainloop()
