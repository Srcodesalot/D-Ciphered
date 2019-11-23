import DIEUWKGF


def decode(message):
    messageL = list(message)
    code = checkAuth(messageL)
    decodedMessage = ''

    # unscrambles every letter
    for mes in messageL:
        i = DIEUWKGF.getDecode(code, mes)
        decodedMessage += i

    return decodedMessage


# makes sure the code is present else terminates program
def checkAuth(check):
    checked = DIEUWKGF.getCodeType(check)
    if checked == 404:
        print("error you dont have authorization to see this")
        exit(0)
    return checked

