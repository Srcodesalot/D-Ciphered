import imaplib
import email
import Decoder


potentialEmails = []


# Queues a list of mail would work better async
def mailQueue(usrname, passwrd):
    global potentialEmails

    try:
        # message reading
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(usrname, passwrd)
        mail.select('inbox')

        typ, data = mail.search(None, 'All')
        emailstring = data[0]
        emailList = emailstring.split()

        for i in emailList:
            ty, data = mail.fetch(i, '(RFC822)')
            for response in data:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = msg['subject']
                    if subject == "ItsCasual":
                        potentialEmails.append(msg)
        return potentialEmails
    except():
        print("OHH NO! Something went wrong.")


# returns decoded string
def decipher():
    global potentialEmails
    x=0
    for mail in potentialEmails:
        print(str(x) + ". " + mail['from'] + mail["Date"] + "\n")
        x += 1

    selector = input("input the number associated with the message you wish to decode:")
    if int(selector) < 0 or int(selector) > len(potentialEmails):
        print("\n  ∆˚Whoa there Bucko thats not on the list!˚∆")
        return ''
    print("")
    print("Message:")
    selected = potentialEmails[int(selector)]
    body = str(selected).split("!start!")
    message = body[1].split("!end!")
    decodedMessage = Decoder.decode(message[0])
    potentialEmails = []

    return decodedMessage

