Contact={
    "Pankaj":(9919531903,"iamsexy4uh@gmail.com","kushinagar"),
    "kartikey":(7042866240,"kartikeykakran56@gmail.com","Rohini18"),
    "abhishek":(9087563989,"bhopdu76@gmail.com","Badali"),
    "ashiwini":(8178413790,"ashiq786@gmail.com","Avantika")
}
class CONTACT():
    def add(self):
        self.name=input("Enter your name ")
        self.MobileNO=input("Enter your mobile number ")
        self.Email=input("Enter your email address ")
        self.address=input("Enter your place ")
        Contact[self.name]=self.MobileNO,self.Email,self.address
        print("your contact has been Saved ")
    def show(self):
        for key,value in Contact.items():
            print(key," ",value)
    def remove(self):
        self.name=input("Enter your contact to proceed ")
        if self.name in Contact:
            del Contact[self.name]
        else:
            print("contact is unvailable ")
    def find(self):
        self.name=input("Enter your name ")
        for key,value in Contact.items():
            if key==self.name:
                print(key,value)
            else:
                print("Contact Not found ")
            break
Cumming=CONTACT()
choice=int(input("Enter your choice "))
if choice==1:
    Cumming.add()
elif choice==2:
    Cumming.show()
elif choice==3:
    Cumming.remove()
elif choice==4:
    Cumming.find()
else:
    print("invalid choice")

