from tkinter import *
from PIL import ImageTk

def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()

signup_window.title('SignUp Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()


frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',
        font=('Microsoft Yahei Ui Light',18
        ,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='firebrick1',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=25,font=('Microsoft Yahei Ui Light',10
        ,'bold'),bg='firebrick1',fg='white')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

termsandconditions=Checkbutton(frame,text='I agree to the Term & Conditions',
        font=('Microsoft Yahei Ui Light',9
        ,'bold'),bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1',
        cursor='hand2')
termsandconditions.grid(row=9,column=0,padx=15,pady=10)

signupButton=Button(frame,text='Signup',font=('Open Sans',16
        ,'bold'),bd=0,bg='firebrick1',fg='white',
        activebackground='firebrick1',activeforeground='white',
        width=17)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Don't have an Account?",
        font=('Open Sans',9,'bold'),
        bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

LoginButton=Button(frame,text='Log In',
        font=('Open Sans',9,'bold underline')
        ,bg='white',fg='blue',bd=0
        ,cursor='hand2',activebackground='white',
        activeforeground='blue',command=login_page)
LoginButton.place(x=170,y=404)

signup_window.mainloop()