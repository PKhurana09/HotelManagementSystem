import random
import datetime

# Global variables:
rooms = []

def management():
    print('\t\t\t\tWELCOME TO KHURANA NIWAS')
    print('1.MAKE A BOOKING\n2.ROOM INFO\n3.SERVICES\n4.PAYMENT\n5.RECORDS')

    var = int(input('Please enter your choice'))

    if var == 1:
        makeBooking()
        pass
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
        
    

management()


def makeBooking():
    pass

def service():
    pass

def roomInfo():
    

    pass

def payment():
    pass

def records():
    pass