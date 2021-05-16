import smtplib


def run_main(): 
    sendersEmail = ""  # you must enter your email here
    recieversEmail = "" # you must enter the recievers email here
    password = "" # you must enter the password to your email here.

    message = "Avaneesh was detected in keylogger"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sendersEmail, password)
    print("login success")
    server.sendmail(sendersEmail, recieversEmail, message)
    print("email has been sent to {}".format(recieversEmail))
