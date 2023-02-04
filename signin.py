from tkinter import *
from PIL import ImageTk
# Functionality Part
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
    eyeButton.config(command=show)


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
cursor='hand2',activeforeground='firebrick1')
forgotButton.place(x=715,y=295)

login_Button=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19)
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
