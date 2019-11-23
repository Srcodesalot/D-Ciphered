import DIEUWKGF
def encode(message):
    messageL = list(message)
    codedMessage= ''
    code = 0
    # Code used to scramble is always the default until you add more yourself
    if DIEUWKGF.getNumOfCodes() > 1:
        code = input("choose a setting based on Index: ")

    #scrambles everyletter
    for mes in messageL:
        i = DIEUWKGF.getCode(code,mes)
        codedMessage += i

    # this is where you add your decryptor (or tell)
    # when it sees the extra period itll know im using code 1
    if code == 0:
        codedMessage += "."


    return codedMessage

