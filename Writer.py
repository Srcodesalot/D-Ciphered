import smtplib
import Encoder

def new(usrname, passwrd):
    try:
        # Allows user to type in message
        recipient = input("Enter your Contacts email: ")
        message = input("Message to send:")
        codedMessage = Encoder.encode(message)

        #IMPORTANT DO NOT CHANGE SUBJECT
        payload = 'Subject:ItsCasual\n\n ' + "!start!" + codedMessage + "!end!"

        # server and message sending
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(usrname, passwrd)
        server.sendmail(usrname, recipient, payload)

        server.quit()

        print("\n ★ Your encrypted message has been Successfully been sent to " + recipient + " ★ \n")
    except():
        print("OHHH NO! Something went wrong.")
