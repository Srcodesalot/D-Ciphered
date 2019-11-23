def getNumOfCodes():
    return len(Codes)


#trys to see if the letter is in the "code" if it isnt it returns the same letter
def getCode(code, char):
    coded = Codes[code]
    try:
        return coded[char]
    except:
        return char


def getDecode(code, char):
    decode = Codes[code]
    for key, value in decode.items():
        if char == value:
            return key
    return char


def getCodeType(list):
    tell = list[-1]
    for codes in Codes:
        if codes[tell] == "tell":
            return codes["code"]
        print("no")
    return 404


# this is the starter code. it will be referenced as index 0 in the codes array
# *Doesnt support caps but wanted to leave the freedom to create codes with capitalizations*
starter = {
    "code": 0,
    ".": "tell",
    "q": "m",
    "w": "n",
    "e": "b",
    "r": "v",
    "t": "c",
    "y": "x",
    "u": "z",
    "i": "l",
    "o": "k",
    "p": "j",
    "a": "h",
    "s": "g",
    "d": "f",
    "f": "d",
    "g": "s",
    "h": "a",
    "j": "p",
    "k": "o",
    "l": "i",
    "z": "u",
    "x": "y",
    "c": "t",
    "v": "r",
    "b": "e",
    "n": "w",
    "m": "q",
    "1": "7",
    "2": "8",
    "3": "9",
    "4": "0",
    "5": "1",
    "6": "2",
    "7": "3",
    "8": "4",
    "9": "5",
    "0": "6"
}

# make sure o add any codes names into this array
Codes = [starter]