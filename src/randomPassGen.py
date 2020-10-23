import os
import string
import random
import json

# check if file exist or not
def checkFile():
    if (os.path.exists('data.json')):
        randGen()
    else:
        emptyData = {}
        writeJSON(emptyData)

# write to JSON file
def writeJSON(data, filename='data.json'):
    with open(filename, 'w') as writeFile:
        json.dump(data, writeFile, indent=4)


def randGen():
    userName = input("Username: ")
    aboutPass = input("For: ")

    with open('data.json', 'r') as readFile:
        dataFile = json.load(readFile)

        # If file is empty
        if (not dataFile):
            length = int(input("Enter the length of randomize password: "))
            passWord = string.ascii_letters + string.digits + string.punctuation
            randPass = ''.join(random.choice(passWord) for i in range(length))
            userData = { "My password": [{
                "username": userName,
                "about": aboutPass,
                "password": randPass
                }
            ]}
            writeJSON(userData)
            readFile.seek(0)
        else:
            # If data already existed
            for i in dataFile['My password']:
                if (aboutPass.lower() in i['about'].lower()):
                    print('Password is {}'.format(i['password']))
                    break
            else:
                length = int(input("Enter the length of randomize password: "))
                passWord = string.ascii_letters + string.digits + string.punctuation
                randPass = ''.join(random.choice(passWord) for i in range(length))
                temp = dataFile['My password']

                newData = {
                    "username": userName,
                    "about": aboutPass,
                    "password": randPass
                    }
                temp.append(newData)
                writeJSON(dataFile)

if __name__ == "__main__":
    checkFile()