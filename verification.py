import os
import math
import random
import smtplib

def verification(check):
    if check==OTP:
        print("verified")
        return True
        
    else:
        print("Please check the  OTP Again")
        return False

def generate(gmailid):
    digits="0123456789"
    global  OTP
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    
    message= OTP + " is your OTP"
    # bxfxzjnosseuyaei
    # gmailid=input("Enter Gmail ID :")
    
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('av232300@gmail.com','bxfxzjnosseuyaei')
    s.sendmail('av232300@gmail.com',gmailid,message)
    s.quit()
    # return OTP




