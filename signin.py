from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# Functionality Part

def forgot_pass():
    def change_password():
        if userentry.get()=='' or newpassword_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields are required',parent=window)
        elif newpassword_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password and confirm password mismatch!',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='12345',database='userdata')
            mycursor=con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(userentry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpassword_entry.get(),userentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, Please login with new password',parent=window)
                window.destroy()
    window=Toplevel()
    window.title('Change Password')
    
    bgpic=ImageTk.PhotoImage(file='background.jpg')
    
    bgLabell=Label(window,image=bgpic)
    bgLabell.grid()
    
    heading_label=Label(window,text='Reset Password',font=('arial',18,'bold'),bg='white',fg='magenta2')
    heading_label.place(x=500,y=60)
    
    userlabel=Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='orchid1')
    userlabel.place(x=470,y=130)
    userentry=Entry(window, width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    userentry.place(x=470,y=160)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)
    
    passwordLabel=Label(window,text='New Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    passwordLabel.place(x=470,y=210)
    newpassword_entry=Entry(window, width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    newpassword_entry.place(x=470,y=240)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=260)
    
    confirmpassLabel=Label(window,text='Confirm Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    confirmpassLabel.place(x=470,y=290)
    confirmpass_entry=Entry(window, width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    confirmpass_entry.place(x=470,y=320)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=340)
    
    submitbutton=Button(window,text='Submit',bd=0,bg='magenta2',fg='white',font=('Open Sans',16,'bold'),width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',command=change_password)
    submitbutton.place(x=470,y=390)
    
    window.mainloop()


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Field Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='12345')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)


        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome','Login is Successful')


def signup_page():
    login_window.destroy()
    import signup

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)






#GUI Part
login_window=Tk()
login_window.geometry('990x660+50+50')#use with place
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLable=Label(login_window,image=bgImage)
bgLable.place(x=0,y=0) #do not increse window size
# bgLable.pack()
# bgLable.grid(row=0,column=0)

heading=Label(login_window,text='USER LOGIN',font=('Microdoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')

heading.place(x=605,y=120)

usernameEntry=Entry(login_window ,width=25,font=('Microdoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)

usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei Ui Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bg='white',bd=0,activebackground='white',cursor='hand2'
        ,command=hide)
eyeButton.place(x=800,y=255)

forgotButton=Button(login_window,text='Forgot Password?',font=('Microsoft Yahei Ui Light',9,'bold')
,bg='white',fg='firebrick1',bd=0,activebackground='white',
cursor='hand2',activeforeground='firebrick1',command=forgot_pass)
forgotButton.place(x=715,y=295)

login_Button=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
login_Button.place(x=578,y=350)

orLabel=Label(login_window,text='-------------- OR --------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fblabel=Label(login_window,image=facebook_logo,bg='white')
fblabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googlelabel=Label(login_window,image=google_logo,bg='white')
googlelabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterlabel=Label(login_window,image=twitter_logo,bg='white')
twitterlabel.place(x=740,y=440)

signupLabel=Label(login_window,text='Dont Have an Account?',font=('Open Sans',9,'bold'),fg='firebrick',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create New One',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='firebrick1',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)
login_window.mainloop()
