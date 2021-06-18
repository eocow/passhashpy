import hashlib, sys, codecs

loginqna = input("Are you logging in or registering?: ")
if loginqna == "logging in":
        logintof = True
elif loginqna == "registering":
        logintof = False 
else:
        print("Invalid Response")
        sys.exit()

usrinp = input("Enter your Password: ")

usrinpd = usrinp.encode("utf-8")

usrhash = hashlib.sha256()

usrhash.update(usrinpd)

temphash = usrhash.hexdigest()

#print(temphash)
#print(logintof)

if logintof == True:
        passwrd = open("/home/eo/vs-work/py/working-project-1/hashpassreg/passwrd.txt", "r")
        flag = 0
        index = 0
        for line in passwrd:
                index += 1 
                if temphash in line:
                        flag = 1
                        break 
        if flag == 1: 
                print("Correct Password!")
                passwrd.close
                sys.exit
        else:
                print("Incorrect Password.")
                passwrd.close()
                sys.exit
elif logintof == False:
        passwrda = open("/home/eo/vs-work/py/working-project-1/hashpassreg/passwrd.txt", "a")
        passwrda.write("\n" + temphash)
        passwrda.close()
        sys.exit()
