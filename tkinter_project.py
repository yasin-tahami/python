from json import *
from os import remove
from time import *
from tkinter import *
from tkinter import messagebox
from re import *
from math import *

'''
login to use calculator   
use [a-z,A-Z][0-9][. and _ ] to submit   
to Enter the username and password click on them(don't use tab)
while login if you enter 3 incorrect password wait 4 second  
click on cancel button when want to stop submit or login 
your data will save in 'info.json' file on same folder if it doesn't exist; delete it on your own chose before closing 

'''

def submit():
    username = username_Entry.get()
    password = password_Entry.get()
    cancel_button.configure(state='normal')
    login_button.configure(state='disable')
    if click_username == 1 and username != '':
        username_check = check_username(username)
        if username_check:
            messagebox.showwarning('UserNameError', 'username already Exist.' + '\n' + 'please Enter another username.')
            username_Entry.delete(0, 'end')
            username_Entry.insert(0, 'Enter new username')
        else:
            if (len(username) < 4):
                messagebox.showwarning('UserNameError', 'username most be more than 4 characters.')
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
                    messagebox.showwarning('UserNameError','invalid username.' + '\n' + 'you can only use : alphabets , numbers ,"." and "_"')
                    username_Entry.delete(0, 'end')
                    username_Entry.insert(0, 'Enter username')
                else:  
                    if click_password == 1 and password != '' and ' '  not in password :           
                        if (len(password) < 4):
                            messagebox.showwarning('PassWordError', 'password most be more than 4 characters.')
                            password_Entry.delete(0, 'end')
                            password_Entry.insert(0, 'Enter password')

                        else:
                            with open('info.json') as info_file:
                                I_F = load(info_file)
                                name = name_Entry.get()
                                name_check = check_name(name)
                                if name_check != False:
                                    get_gender = gender.get()
                                    new_user ={'username':username, 'password':password,'Name':name_check, 'gender':get_gender}
                                    I_F.append(new_user)                        
                                    with open('info.json', 'w') as info_f:
                                        dump(I_F, info_f)
                                    messagebox.showinfo('Submit Message', 'your account has been registered! ')
                                    login_button.configure(state='normal')
                                    cancel_button.configure(state='disable')
                                    refresh_requirements()
                                    refresh_Entries()  
                                else:
                                    global click_name
                                    click_name = 0               
                    else:
                        messagebox.showerror('PassWordError', 'password required'+ '\n'+ '(don\'t use space)')                
    else:
        messagebox.showerror('UserNameError', 'username required')

def login():
    cancel_button.configure(state='normal')
    submit_button.configure(state='disable')
    username = username_Entry.get()
    password = password_Entry.get()
    if click_username == 1 and username != '':   
        username_check = check_username(username)
        if username_check:
            if click_password ==1 and password != '': 
                password_check = check_password(username, password)
                if password_check:
                    with open('info.json') as info_file:
                            I_F = load(info_file)
                            for i in I_F :
                                if i['username'] == username and i['password'] ==  password:   #after login, disable entries and add them users information.
                                    get_name = i['Name']
                                    get_gender = i['gender']
                                    login_user={'username':username, 'password':password,'Name':get_name, 'gender':get_gender} 
                                    name_Entry.delete(0, 'end')
                                    username_Entry.delete(0, 'end')
                                    password_Entry.delete(0, 'end')
                                    password_Entry.config(show='')
                                    name_Entry.insert(0, login_user['Name'])
                                    username_Entry.insert(0, login_user['username'])
                                    password_Entry.insert(0, login_user['password'])
                                    gender.set(login_user['gender'])
                                    name_Entry.config(state= 'disable')
                                    username_Entry.config(state= 'disable')
                                    password_Entry.config(state= 'disable')
                                    if login_user['gender'] == 'Male':
                                        gender_Female_button.config(state='disable')
                                    elif login_user['gender'] == 'Female':
                                        gender_Male_button.config(state='disable')
                                    else:
                                        gender_Female_button.config(state='disable') 
                                        gender_Male_button.config(state='disable')  

                                    password_show.config(state='disable')    
                                    messagebox.showinfo('Login Message', 'welcome '+ login_user['Name'])
                                    login_button.configure(state='disable')
                                    logout_button.configure(state='normal')
                                    cancel_button.configure(state='disable')    
                                    delete_button.configure(state='normal')
                                    refresh_Entries()
                                    refresh_requirements()
            else:
                messagebox.showerror('PassWordError', 'password required')                                          
        else:
            messagebox.showerror('UserNameError', 'username not Exist.')
            username_Entry.delete(0, 'end')
            username_Entry.insert(0, 'Enter new username')
    else:
        messagebox.showerror('UserNameError', 'username required')

def logout():
    if submit_button["state"] == DISABLED and login_button['state'] == DISABLED:
        messagebox.showinfo('Logout Message', 'by!')
        submit_button.configure(state='normal')
        login_button.configure(state='normal')
        logout_button.configure(state='disable')
        delete_button.configure(state='disable')
        cancel_button.configure(state='disable')
        name_Entry.config(state= 'normal')
        username_Entry.config(state= 'normal')
        password_Entry.config(state= 'normal')
        gender_Female_button.config(state='normal')
        gender_Male_button.config(state='normal')
        password_show.config(state='normal')
        refresh_Entries()
        refresh_requirements()
        return

def delete():
            username = username_Entry.get()
            password = password_Entry.get()
            delete_check = messagebox.askquestion('Delete Account', 'Are you sure?')
            if delete_check == 'yes':
                with open('info.json') as info_file:
                    I_F = load(info_file)
                    for i in I_F :
                        if i['username'] == username and i['password'] ==  password:
                            del I_F[I_F.index(i)]
                            with open('info.json', 'w') as f:
                                dump(I_F, f)
                                
                    messagebox.showinfo('Delete Account', 'your Account deleted!')
                    submit_button.configure(state='normal')
                    login_button.configure(state='normal')
                    logout_button.configure(state='disable')
                    delete_button.configure(state='disable')
                    cancel_button.configure(state='disable')
                    name_Entry.config(state= 'normal')
                    username_Entry.config(state= 'normal')
                    password_Entry.config(state= 'normal')
                    gender_Female_button.config(state='normal')
                    gender_Male_button.config(state='normal')
                    refresh_Entries()

def cancel():
    password_count.set(3)
    submit_button.configure(state='normal')
    login_button.configure(state='normal')
    cancel_button.configure(state='disable')
    refresh_Entries()
    refresh_requirements()

def check_username(user):
        with open('info.json') as info_file:
            I_F = load(info_file)
        for i in I_F:
            if user in i['username']:
                return True 
           
def check_password(user, pas):
    with open('info.json') as info_file:
        I_F = load(info_file)
    try_left = password_count.get()
    for i in I_F:
        if user in i['username']:
            if i['password'] == pas:
                password_count.set(3)
                return True
            else: 
                ask_question = messagebox.askquestion('PassWordError', 'incorrect password.' + '\n' + 'Try again?')
                if ask_question == 'yes':
                    password_Entry.delete(0, 'end')
                    password_Entry.insert(0, 'Enter password')
                    password_count.set(try_left - 1)
                    if try_left != 1:  
                        return False
                    else:     # after 3 wrong password stop working for 4 second.
                        messagebox.showwarning('PassWordError', "3 incorrect password." + '\n' + 'try after 4 seconds')
                        sleep(4)
                        password_count.set(3)
                else:
                    cancel()
                    return

def calculator():
    if login_button['state'] == 'normal' or cancel_button['state'] == 'normal':
        messagebox.showwarning('LoginWarning','login firs.')
    else:    
        calculator = Toplevel(tkinter)
        calculator.title('calculator')
        calculator.geometry('347x315')
        calculator.grab_set() # make tkinter page unusable
        text_input = StringVar()
         
        def button_click(numbers): # add numbers and arithmetic operators to calculator screen
            global operator        
            operator = operator + str(numbers)
            text_input.set(operator)
    
        def square():
            global operator
            try:  
                result =str(sqrt(int(operator)))
                text_input.set(result)
                operator=result
            except ValueError:
                messagebox.showwarning('InvalidInput', 'use Arithmetic numbers. (0,1,2,3...)')

        def equal_button():
            global operator
            try:
                result = str(eval(operator))
                text_input.set(result)
                operator=result
            except SyntaxError:
                messagebox.showwarning('InvalidInput', 'Enter valid value.')

        def backspace():
            try:
                global operator
                operator = operator.rstrip(operator[-1])
                text_input.set(operator)
            except   IndexError: #when there is nothing to delete.
                pass

        def clear_button():
            global operator
            operator =''
            text_input.set("")    

        def on_closing():
            clear_button()
            calculator.destroy() 
            
        txtDisplay = Entry(calculator, font=('arial', 18, 'bold'), width=25, textvariable=text_input, bd=10,bg='#cccccc').grid(columnspan=5)  

        button_0 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='0', command=lambda:button_click(0)).grid(row=4, column=0)
        button_1 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='1', command=lambda:button_click(1)).grid(row=3, column=0)
        button_2= Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='2', command=lambda:button_click(2)).grid(row=3, column=1)
        button_3 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='3', command=lambda:button_click(3)).grid(row=3, column=2)
        button_4 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='4', command=lambda:button_click(4)).grid(row=2, column=0)
        button_5 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='5', command=lambda:button_click(5)).grid(row=2, column=1)
        button_6 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='6', command=lambda:button_click(6)).grid(row=2, column=2)
        button_7 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='7', command=lambda:button_click(7) ).grid(row=1, column=0)
        button_8 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='8', command=lambda:button_click(8)).grid(row=1, column=1)
        button_9 = Button(calculator, padx=13, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='9', command=lambda:button_click(9)).grid(row=1, column=2)

        dot_button = Button(calculator, padx=12, pady=4, bd=4, fg='black', font=('arial', 19, 'bold'), text='.', command=lambda:button_click('.')).grid(row=4, column=1)   
        addition_button = Button(calculator, padx=19, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='+', command=lambda:button_click('+')).grid(row=1, column=3)
        subtraction_button = Button(calculator, padx=20, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='−', command=lambda:button_click('-')).grid(row=2, column=3)
        multiply_button = Button(calculator, padx=20, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='x', command=lambda:button_click('*')).grid(row=3, column=3)
        division_button = Button(calculator, padx=23, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='/', command=lambda:button_click('/')).grid(row=4, column=3)
        Exponent_button = Button(calculator, padx=17, pady=10, bd=4, fg='black', font=('arial', 14, 'bold'), text='xʸ', command=lambda:button_click('**')).grid(row=3, column=4) 
        square_button = Button(calculator, padx=14, pady=3, bd=4, fg='black', font=('arial', 20, 'bold'), text='√', command=square).grid(row=4, column=4)   

        Equals_button = Button(calculator, padx=13, pady=12, bd=4, fg='black', font=('arial', 14, 'bold'), text='=', command=equal_button).grid(row=4, column=2)
        backspace_button = Button(calculator, padx=4, pady=0, bd=4, fg='black', font=('arial', 24, 'bold'),  text='←', command=backspace).grid(row=2, column=4)  
        Clear_button = Button(calculator, padx=18, pady=10, bd=4, fg='black', font=('arial', 15, 'bold'), text='C', command= clear_button).grid(row=1, column=4)

        calculator.protocol("WM_DELETE_WINDOW", on_closing)
        calculator.mainloop()
  
def on_closing():
    delete_check = messagebox.askquestion('Delete file', 'Do you want to delete json file?')
    if delete_check == 'yes':
        try:
            remove("info.json")
            tkinter.destroy()
        except FileNotFoundError: 
            messagebox.showwarning('FileNotFound','The file no longer exists.') 
            tkinter.destroy()  
    else:  #update user_count (delete to reset)
        global user_count
        with open ('info.json') as info_file:
            I_F = load(info_file)
            I_F[0].update({'user_count': user_count})
        with open('info.json','w') as info_file:    
            dump(I_F, info_file)
        tkinter.destroy()      

# by click on entries delete the default input and check if user add requirements(username, password)
def user_click(*args):
    global click_username
    username = username_Entry.get()
    if username == 'Enter username' or username == 'Enter new username':
        username_Entry.delete(0, 'end')
        click_username = 1

def pass_click(*args):
    global click_password
    password = password_Entry.get()    
    if password == 'Enter password':
        password_Entry.delete(0, 'end')
        password_Entry.config(show='*')
        click_password = 1

def name_click(*args):
    global click_name
    name = name_Entry.get()
    if name == 'Enter your name':
        name_Entry.delete(0, 'end') 
        click_name = 1      

def check_name(name):
    if click_name == 1 and name != '' and ' '  not in name :
        return name
    else:
        global user_count   #if user don't want to add name, use 'user' and number of user_count
        user_name = 'user '
        user_name += str(user_count) 
        name_question = messagebox.askquestion('NameError', 'set  ({}) ?'.format(user_name))   
        if name_question == 'yes':
            user_count +=1
            return user_name
        else:
            name_Entry.delete(0, 'end')
            name_Entry.insert(0, 'Enter your name')
            return False

def show_password():
    if show_password_check.get() == 1:
        password_Entry.config(show='')
    else:
        password_Entry.config(show='*')

def refresh_Entries():
    name_Entry.delete(0,'end')
    password_Entry.delete(0, 'end')
    username_Entry.delete(0, 'end')
    name_Entry.insert(0, 'Enter your name')
    username_Entry.insert(0, 'Enter username')
    password_Entry.insert(0, 'Enter password')
    password_Entry.config(show='')
    password_show.deselect()  

def refresh_requirements():
    global click_username
    global click_password
    click_username = 0
    click_password = 0


tkinter = Tk()
tkinter.title('tkinter')
tkinter.geometry('325x225')

password_count = IntVar()
password_count.set(3)
gender = StringVar()
show_password_check = IntVar(value=0)
click_username = 0
click_password = 0
click_name = 0
operator ='' #calculator screen


name_label = Label(tkinter, text='Name : ', width=9, height=1)
username_label = Label(tkinter, text='username : ', width=9, height=1)
password_label = Label(tkinter, text='password : ', width=9, height=1)
gender_label = Label(tkinter, text='gender : ', width=9, height=1)


name_Entry = Entry(tkinter, width= 22)
username_Entry = Entry(tkinter, width=22)
password_Entry = Entry(tkinter, width=22)
gender_Male_button= Radiobutton(tkinter, text='Male', variable= gender, value='Male')
gender_Female_button= Radiobutton(tkinter, text='Female', variable= gender, value='Female')
password_show =Checkbutton(tkinter,text='show password', variable= show_password_check, onvalue =  1, offvalue = 2, command= show_password)


submit_button = Button(tkinter, text='Submit', command=submit)
login_button = Button(tkinter, text='Log in', command=login)
delete_button = Button(tkinter, text='Delete', command=delete, state='disable')
logout_button = Button(tkinter, text='Log out', command=logout, state='disable')
cancel_button = Button(tkinter, text='Cancel', width=7 ,command=cancel, state='disable')
calculate_button = Button(tkinter, text='calculator ', width=7, command=calculator)


name_label.place(relx=0.12, rely=0)
name_Entry.place(relx=0.38, rely=0.015)
username_label.place(relx=0.15, rely=0.1)
username_Entry.place(relx=0.38, rely=0.12)
password_label.place(relx=0.15, rely=0.21)
password_Entry.place(relx=0.38, rely=0.22)
submit_button.place(relx=0.1, rely=0.8)
login_button.place(relx=0.3, rely=0.8)
delete_button.place(relx=0.5, rely=0.8)
logout_button.place(relx=0.7, rely=0.8)
cancel_button.place(relx=0.175, rely=0.47)
calculate_button.place(relx=0.175, rely=0.61)
gender_label.place(relx=0.13, rely=0.33)
gender_Male_button.place(relx=0.37, rely=0.33)
gender_Female_button.place(relx= 0.57, rely=0.33)
password_show.place(relx= 0.4, rely=0.43)


name_Entry.insert(0, 'Enter your name')
username_Entry.insert(0, 'Enter username')
password_Entry.insert(0, 'Enter password')


name_Entry.bind('<Button-1>', name_click)
username_Entry.bind('<Button-1>', user_click)
password_Entry.bind('<Button-1>', pass_click)


try:
    with open('info.json') as test_file:
        T_file = load(test_file)
        user_count = T_file[0]['user_count']  #import user_count from json file
except FileNotFoundError:      #create json file to save data if it doesn't exist.
    messagebox.showinfo('FileNotFound','test account created!')
    I_F = [{'username':'test_username', 'password':'test_password','Name':'test_name', 'gender':'none','user_count':1}]
    with open('info.json', 'x') as test_file:
        dump(I_F, test_file)
        user_count = I_F[0]['user_count']

tkinter.protocol("WM_DELETE_WINDOW", on_closing)
tkinter.mainloop()