import random
import datetime

# Global variables:
rooms = []
avail_rooms = []
phone_numbers = []
adrs = []
names = []
email_adrs = []
check_ins = []
check_outs = []



def management():
    print('\t\t\t\tWELCOME TO KHURANA NIWAS')
    print('1.MAKE A BOOKING\n2.ROOM INFO\n3.SERVICES\n4.PAYMENT\n5.RECORDS')

    var = int(input('Please enter your choice'))

    if var == 1:
        makeBooking()
    elif var == 2:
        service()
        pass
    elif var == 3:
        roomInfo()
        pass
    elif var == 4:
        payment()
        pass
    elif var == 5:
        records()
        pass
    else:
        print('Wrong choice.\nTry Again')
        


def makeBooking():
    print("\t\t\t\tLet us proceed with Booking\n")


    while 1: 
        name1 = str(input("Please Enter you Name: "))
        ph1 = str(input("Please enter you Phone Number: "))
        adr1 = str(input("Please enter your Home Address: "))
        eadr1 = str(input("Please enter you email address: "))
    # check if any of the fields is empty:
        if name1 != '' and ph1 != '' and adr1 != '' and eadr1 != '':
            phone_numbers.append(ph1)
            names.append(name1)
            adrs.append(adr1)
            email_adrs.append(eadr1)
            break
        else:
            print("Name, Phone Number, Address and Email Address can not be empty!!")
    



def service():
    pass

def roomInfo():
    pass

def payment():
    pass

def records():
    pass


management()