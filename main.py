import random
import string
import smtplib
nos=[]
nos.extend(list(string.digits))
random.shuffle(nos)
otp="".join(nos[0:6])
msg=otp+" is your otp"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Id", "password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,otp)
a = input("Enter Your OTP >>: ")
if a == otp:
    print("Verified")
else:
    print("Please Check your OTP again")