import json

with open('addressBook.json') as data_file:
    loaded = json.load(data_file)

def saveContact(name, address):
    global loaded
    nme = name
    add = address

    book = loaded["address_book"]

    if name not in book:
        book[name] = address
    else:
        print("whoa looks Like you already have a contact named " + name)

    with open("addressBook.json", 'w') as outfile:
        json.dump(loaded, outfile, sort_keys=True, indent=4)



def getContacts():
    global loaded
    book = loaded["address_book"]

    return book

def getContact(name):
    global loaded
    book = loaded["address_book"]
    address = book[name]
    return address

def doesExist(name):
    global loaded
    exists = False
    book = loaded["address_book"]

    if name in book:
        exists = True

    return exists


def addEmailUrls(url):
    global loaded
    urlend = url
    urls = loaded["excepted_emails"]
    urls[urlend] = True

    with open("addressBook.json", 'w') as outfile:
        json.dump(loaded, outfile, sort_keys=True, indent=4)


def isAccepted(url):
    global loaded
    urlend = url
    accepted = True

    urls = loaded["excepted_emails"]

    if urlend not in urls:
        accepted = False

    return accepted

