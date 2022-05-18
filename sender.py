import smtplib, ssl #Importing the libraries smtplib(Starts the email handling) and ssl(For your connection with the server)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Enter your email address (Like my@gmail.com): ")  # Enter your address
receiver_email = input("Enter the receiver address (Like your@gmail.com): ")  # Enter receiver address
password = input("Type your password and press enter: ")
text=input("Enter the message you want to send: ")
message = input("""\ 
Subject: Hi there! """ + text)

context = ssl.create_default_context() #creates the connection and handles the cleanup afterwards
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password) #Logs into your account using the email and password you gave
    server.sendmail(sender_email, receiver_email, message) #Sends from your email the message you've created t the email you've written out