import smtplib
import Encoder
import Contact


def new(usrname, passwrd):
    try:
        # Allows user to type in message
        recipient = addressFilter()
        message = input("Message to send:")
        codedMessage = Encoder.encode(message)

        # IMPORTANT DO NOT CHANGE SUBJECT
        payload = 'Subject:ItsCasual\n\n ' + "!st!" + codedMessage + "!e!"

        # server and message sending
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(usrname, passwrd)
        server.sendmail(usrname, recipient, payload)

        server.quit()

        print("\n ★ Your encrypted message has been Successfully sent to " + recipient + " ★ \n")
    except():
        print("OHHH NO! Something went wrong.")


def addressFilter():
    valid = False
    isContact = False

    while not valid:
        recipient = input("Enter your Contacts email: ")
        isContact = Contact.doesExist(recipient)

        if "@" in recipient:
            end = recipient.split("@")
            accepted = Contact.isAccepted(end[1])

            if accepted:
                valid = True
            else:
                valid = allow(end[1])

        elif isContact:
            recipient = Contact.getContact(recipient.casefold())
            valid = True
        else:
            print("That doesnt seem like an email and its not in your contacts.")
            print("please try again")
            isvalid = False

    if isContact == False:
        print("Would you  like to save this User as a contact?")
        create = input("y/n")
        if "y" in create.casefold():
            save(recipient)

    return recipient


# allows
def allow(add):
    end = add
    print("\n!WARNING!: This seems like its not a Gmail.")
    print("This program was set up to work with Gmail. ")
    print("Unless the recipient has edited the code they may not be able to decode this message.")
    print("Note: If this is a business or school email set up through Gmail feel free to continue on.\n")
    moveForward = input("would you like to send it anyways? (y/n)")

    if "y" in moveForward.casefold():
        print("\nWould you like to always allow emails to " + end + "?")
        save = input("y/n")
        if "y" in save.casefold():
            Contact.addEmailUrls(end)
        else:
            noPurpose = 0
        return True
    else:
        return False


def save(add):
    name = input("Please enter a contact name:")
    exists = Contact.doesExist(name.casefold())
    while exists:
        print("Looks like thats already a contact name please choose another one or type 'cancel' to cancel")
        name = input(":")
        exists = Contact.doesExist(name)
        if "cancel" in name:
            return
    Contact.saveContact(name,add)
    print("\nyour contact has been saved\n")