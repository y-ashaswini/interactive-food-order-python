import time
import pickle
import random
import datetime
import turtle
import sys
from Hippocampi import printslowly as p
from os import remove, rename
from prettytable import PrettyTable


# ART INTEGRATION:

screen = turtle.Screen()
screen.setup(800, 800)
spiral = turtle.Turtle()  # initialising turtle
spiral.ht()


def sqspiral():
    spiral.color('black')
    n = 30  # size
    for i in range(n * 21):  # loop to draw a side
        spiral.forward(i * 1)  # drawing side of length i*10
        spiral.right(90)  # changing direction of pen by 90 degree in clockwise


def movedraw():
    spiral.up()
    spiral.color('orange')
    spiral.goto(-200, 200)
    drawspiral()
    spiral.goto(0, -200)
    spiral.color('red')
    drawspiral()
    spiral.color('yellow')
    spiral.goto(200, 200)
    drawspiral()
    spiral.end_fill()


def drawspiral(flag=300, dist=1):
    spiral.down()
    while flag:  # making pattern
        spiral.forward(dist)  # makes the turtle to move forward
        spiral.left(120)  # makes the turtle to move left
        spiral.left(1)
        dist += 1
        flag -= 1
    spiral.up()


def writin():
    spiral.color('white')
    spiral.up()
    spiral.setpos(-300, 0)
    spiral.down()
    im = 'rsz_mirchi.gif'
    screen.addshape(im)
    turtle.shape(im)
    spiral.up()
    spiral.setpos(-200, 35)
    spiral.down()
    spiral.write('ItSoTASTY!', font=('Jokerman', 40, 'bold'))
    time.sleep(0.3)
    spiral.up()
    spiral.setpos(-280, -70)
    spiral.down()
    spiral.color('yellow')
    time.sleep(0.3)
    spiral.write('ONLINE FOOD DELIVERY', font=('Goudy Stout', 15, 'bold'))
    spiral.up()
    spiral.setpos(-220, -120)
    spiral.color('light blue')
    spiral.down()
    time.sleep(0.3)
    spiral.write('Contact Owner | Yashaswini Shivathaya',
                 font=('Freestyle Script', 25, 'bold'))
    spiral.hideturtle()


screen.bgpic("chaat.gif")
spiral.speed(1000)  # changing speed of turtle
time.sleep(1.5)
sqspiral()
movedraw()
time.sleep(0.7)
writin()
turtle.done()

# MAIN PROGRAMME >>>

udesinumber = 'null'
username = 'initial_value_retained'
user_LastAdress = 'initial_address_value_retained'
user_LastOrder = 'initial_lastorder_value_retained'
user_NumOrders = 'initial_numorder_value_retained'


Discounted_totalPrice = 'initial_disPrice_retained'

# here value = 0 means it is a first timer and 1 means means it isnt.
_isUserFirstTimer = 0
DESINO = 0


# def printslow(x):
#     for i in x:
#         if(i in '.,/?!@#$%^&*()_+=\][;"'):
#             print(i, end = '')
#             time.sleep(0.5)
#         else:
#             print(i,end='')
#             time.sleep(0.05)
#     print()


def greetings_time():
    x = datetime.datetime.now()
    if(x.strftime("%p") == 'AM'):
        p.printslowly(
            'Greetings! And thats hopin you\'re havin a wonderful mornin! ;)')
    elif(int(x.strftime("%H")) >= 12 and int(x.strftime("%H")) <= 15):
        p.printslowly(
            'Greetings! And thats hopin you\'re havin a wonderful afternoon! ;)')
    else:
        p.printslowly(
            'Greetings! And thats hopin you\'re havin a wonderful evenin! ;)')


def firstdisplay():
    p.printslowly('Hello and Welcome to my E - Resturant! ')
    time.sleep(1)


def authorisation(uname='<initialised value of uname to get into while loop>'):
    global username
    while(uname):
        uname = input('Customer, enter your name: ')
        if(uname == '' or uname == False):
            print('username cannot be blank!')
            uname = 1
        elif(' ' in uname):
            print('first name cannot contain space')
            uname = 1
        else:
            username = uname
            print('accepted')
            print()
            break
    time.sleep(0.5)

    p.printslowly('''Do you own a DESICARD YET?

A DESICARD is the card that we gift all our wonderful customers on their very first experience with us!
It is a card which can beget you UNBELIEVABLY LARGE DISCOUNTS and MIND BLOWING DEALS, depending on how frequently you honour us with the opportunity to serve you!
''')

    dcardValidity()
    return


def dcardValidity():

    global DESINO
    global user_LastAdress
    global user_LastOrder
    global user_NumOrders
    global _isUserFirstTimer
    global udno

    x = True

    time.sleep(0.5)
    t = PrettyTable(['click 0', 'click 1', 'click (q)'])
    t.add_row(['ENTER MY DESICARD NO.', 'GET MY OWN DESICARD!', 'QUIT'])
    print(t)
    print()
    y_n = input('You choose>>> ')

    if(y_n == '0'):
        while x:
            try:
                dno = int(input('DESICARD number: '))
                global udesinumber
                udesinumber = int(dno)
                if(len(str(dno)) != 4):
                    p.printslowly(
                        'Oops, Number entered does not match the limit/ Does not match with our records.')
                    x = False
                    break

            except:
                p.printslowly(
                    'Error. Do make sure you are entering numbers only, and not usng any spaces or special characters. Try again.')
                x = False
            else:
                p.printslowly(
                    'Confirming with our database for your DESICARD no...')

                f = open('custrecords.dat', 'rb')

                flag = 0
                try:
                    while True:
                        f1 = pickle.load(f)

                        if(f1['DesiCardNo'] == udesinumber):

                            DESINO = udesinumber
                            flag += 1

                            user_LastAdress = f1['Last Address ']
                            user_LastOrder = f1['Last Order on ']
                            user_NumOrders = f1['No. of Orders']

                except:
                    f.close()

                if(flag != 0):
                    p.printslowly(
                        'Welcome Back! We are pleased to be serving you again.')
                    _isUserFirstTimer = 1
                    input('Press enter to continue.')

                    x = False
                    return

                else:
                    p.printslowly(
                        'Apologies, we do not recognise you. But you can get yourself a DESICARD right now!')
                    x = False
                    input('Press enter to continue.')
                    break
        dcardValidity()
        # above, checking in the existing database if this value exists in our 'custrecords' database

    elif(y_n == '1'):
        udno = assignDNO()

        DESINO = udno

        p.printslowly('Generating DESICARD number...')
        print()
        print(username, ', your new DESI CARD NUMBER IS ', udno, '!')
        print()
        time.sleep(1)
        p.printslowly(
            'A printed form of your new card will be handed over to you along with your bill.')
        time.sleep(1)
        input('Press enter to continue.')
        return

    elif(y_n == 'q'):
        exitprog()
    else:
        print('I\'m afraid this isn\'t an option!')
        dcardValidity()


def exitprog():
    time.sleep(0.7)
    p.printslowly('You have clicked on EXIT')
    print()
    p.printslowly("Wishing you a wonderful day ahead!")
    p.printslowly("Stay Happy, Stay Safe, and SEE YOU SOON!")
    sys.exit()


def assignDNO():
    y = 1
    while y:
        dig1 = random.randint(1, 9)
        dig2 = random.randint(0, 9)
        dig3 = random.randint(0, 9)
        dig4 = random.randint(0, 9)
        dno = dig1*1000+dig2*100+dig3*10+dig4

        f = open('custrecords.dat', 'rb')

        try:
            flag = 0
            while True:
                f1 = pickle.load(f)

                if(f1['DesiCardNo'] == udno):
                    flag += 1

        except:
            f.close()

        if(flag == 0):
            y = 0
        else:
            pass

    # above, to check if this value of dno is duplicated in our 'custrecords' database
    return dno


finaltokri = []

i = 0
tokriinfo = {}


def addtotokri(checkForTheseLetters):
    dtokri = {}

    y = 1
    z = 1

    while y:
        useralpha = input(
            '''[Press "q" to quit] Enter the food alphabet that you want to add to tokri  >>>''')

        if(useralpha in checkForTheseLetters):
            dtokri['Userchoice'] = useralpha
            dtokri['item name'] = tokriinfo[useralpha]
            y = 0

        elif(useralpha == 'q'):
            exitprog()
            y = 0
            z = 0
        else:
            p.printslowly('ERROR -- Apologies, this choice doesnt exist!')

    while z:
        try:
            userqty = input('''Enter the quantity  >>>''')
            dtokri['quantity'] = int(userqty)
            dtokri['price'] = (tokriinfo[useralpha][3])*int(userqty)
            z = 0
        except:
            p.printslowly('ERROR -- Make sure that you are entering a number!')

    else:
        return dtokri


def printmenu(filename):
    f = open(filename, 'rb')

    t = PrettyTable(['CATEGORY', 'FOOD ITEM', 'FLAVOR / SUBCATEGORY',
                    'DESCRIPTION', 'PRICE', 'ADD TO TOKRI (PRESS)'])
    t._max_width = {"CATEGORY": 10, "FOOD ITEM": 10, "FLAVOR / SUBCATEGORY": 10,
                    "DESCRIPTION": 20, "PRICE": 5, 'ADD TO TOKRI (PRESS)': 10}
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    try:

        while True:
            x = pickle.load(f)
            global i

            global tokriinfo
            l = []
            l = [x[0], x[1], x[2], x[4]]

            tokriinfo[alpha[i]] = l

            t.add_row([x[0], x[1], x[2], x[3], x[4], alpha[i]])
            i += 1
            t.add_row(['', '', '', '', '', ''])
    except:
        f.close()
    print(t)
#     print()
#     print('the value of i is now',i)
#     print('your tokri info is',tokriinfo)

    m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:(i)]
    return m

#     print('tokriinfo',tokriinfo)


totalPrice = 0.0


def callmenus():

    global finaltokri
    global totalPrice

    p.printslowly('''We will now be taking you through our menu.
You can add items to your tokri as we proceed.
At the end, you will be able to review your tokri and modify your order.''')
    print()

    temporarytokri = []

    p.printslowly('menu part 1')
    time.sleep(1)
    theSetofletters = printmenu('KathiRolls.dat')
    print()
    ans = input('Add anything to tokri? (y / n) >>>')
    while ans == 'y':
        x = addtotokri(theSetofletters)
        temporarytokri.append(x)
        try:
            totalPrice += x['price']
        except:
            pass  # because of whatever reason, if there's an error

#         print('value returned: ',x)
#         print('your temporary tokri is:')
#         print(temporarytokri)
#         print()

        time.sleep(0.7)
        ans = input('Would you like to continue adding? (y / n) >>>')
    print()
    time.sleep(1.5)

    p.printslowly('menu part 2')
    time.sleep(1)
    theSetofletters = printmenu('PavItems.dat')
    print()
    ans = input('Add anything to tokri? (y / n) >>>')
    while ans == 'y':
        x = addtotokri(theSetofletters)
        temporarytokri.append(x)

        try:
            totalPrice += x['price']
        except:
            pass

#
#         print('value returned: ',x)
#         print('your temporary tokri is: ')
#         print(temporarytokri)
#         print()

        time.sleep(0.7)

        ans = input('Would you like to continue adding? (y / n) >>>')
    print()
    time.sleep(1.5)

    p.printslowly('menu part 3')
    time.sleep(1)
    theSetofletters = printmenu('Golgappe.dat')
    print()
    ans = input('Add anything to tokri? (y / n) >>>')
    while ans == 'y':
        x = addtotokri(theSetofletters)
        temporarytokri.append(x)

        try:
            totalPrice += x['price']
        except:
            pass

#
#         print('value returned: ',x)
#         print('your temporary tokri is: ')
#         print(temporarytokri)
#         print()
        time.sleep(0.7)

        ans = input('Would you like to continue adding? (y / n) >>>')
    print()
    time.sleep(1.5)

    p.printslowly('menu part 4')
    time.sleep(1)
    theSetofletters = printmenu('DesiMishthaan.dat')
    print()
    ans = input('Add anything to tokri? (y / n) >>>')
    while ans == 'y':
        x = addtotokri(theSetofletters)
        temporarytokri.append(x)

        try:
            totalPrice += x['price']
        except:
            pass

#         print('value returned: ',x)
#         print('your temporary tokri is: ')
#         print(temporarytokri)
#         print()

        time.sleep(0.7)

        ans = input('Would you like to continue adding? (y / n) >>>')
    print()
    time.sleep(1.5)

    p.printslowly('Your journey through the menu is complete!')
    p.printslowly('Your tokri is now: ')
    print()
    ifempty = 0
    for i in range(len(temporarytokri)):
        if(i == None or i == '' or i == ' '):
            pass
        else:
            print(temporarytokri[i])
            ifempty += 1
    print()
    if(ifempty == 0):
        p.printslowly(
            'You havent ordered anything. The algorithm automatically takes you to EXIT')
        exitprog()

    else:
        print('Your total price until now: ', totalPrice)
        print()
        finaltokri = temporarytokri
        return temporarytokri


def ask_updateornot(z):
    global finaltokri
    ans = input('Do you want to update your order? (y / n)')
    if ans == 'y':
        tokriafterupdate = updatemenus(ans, z)
        return tokriafterupdate
    else:
        p.printslowly('Accessing your data . . .')
        return finaltokri


def updatemenus(uans, z):

    global finaltokri
    finaltokri = z

    while uans == 'y':
        print('''1. Delete orders
2. Update quantity
3. Order more!

''')

        newtokri = []

        uchoice = input('User, enter your choice >>>')

        if(uchoice == '1'):
            for qq in (finaltokri):
                print(qq)
            print()
            p.printslowly(
                'Enter the alphabet that corresponds to the order you wish to delete')
            udeletechoice = input('>>>')

            for j in finaltokri:
                if(j != None):
                    if(j['Userchoice'] == udeletechoice):
                        pass
                    else:
                        newtokri.append(j)

            if(len(finaltokri) == len(newtokri)):
                print('ERROR -- That is not an option !')
            else:
                finaltokri = newtokri
                print('Changes saved')

        elif(uchoice == '2'):
            for qq in range(len(finaltokri)):
                print(finaltokri[qq])
            print()
            p.printslowly(
                'Enter the alphabet that corresponds to the order you wish to modify')
            uqtychoice = input('>>>')

            for j in finaltokri:
                try:
                    if(j['Userchoice'] == uqtychoice):
                        kkk = 1
                        while kkk:
                            try:
                                unewqty = int(input('Enter new quantity >>>'))
                                kkk = 0
                            except:
                                p.printslowly(
                                    'ERROR -- Make sure youre entering a number!')
                        j['quantity'] = unewqty
                        j['price'] = (j['item name'][3])*unewqty

                        newtokri.append(j)

                    else:
                        newtokri.append(j)

                except:
                    pass
            finaltokri = newtokri
            print('Changes saved')

        elif(uchoice == '3'):

            global i
            i = 0
            global tokriinfo
            tokriinfo = {}
            global totalPrice
            totalPrice = 0.0

            reorderedrokri = callmenus()
            for j in z:
                if(j != None):
                    newtokri.append(j)
            for k in reorderedrokri:
                if(k != None):
                    newtokri.append(k)

            finaltokri = newtokri
            print('Changes saved')

        else:
            print('ERROR --Apologies, this isnt an option!')

        uans = input('Do you want to make more changes to your order? (y / n)')

    return finaltokri


def store_all_info(Tokri, DESINO):
    global Discounted_totalPrice

    x = datetime.datetime.now()
    the_date = str(x.strftime("%d"))+' ' + \
        str(x.strftime("%m"))+' '+str(x.strftime("%Y"))

    discreturn = discountCal()

    p = 0
    for i in Tokri:
        p += i['price']

    dp = 0
    dp = p - ((p*discreturn)/100)

    f = open('current_custdetails.dat', 'ab')
    dcurrentuser = {}
    dcurrentuser['Username'] = username
    dcurrentuser['DesiNumber'] = DESINO
    dcurrentuser['OrderDate'] = the_date
    dcurrentuser['OrderDetails'] = Tokri
    dcurrentuser['TotalPrice'] = p
    dcurrentuser['Discount'] = discreturn
    dcurrentuser['DiscountedPrice'] = dp

    Discounted_totalPrice = dp
    print()
    print('All information stored in current user file.')
    print()
    time.sleep(0.7)
    pickle.dump(dcurrentuser, f)
    f.close()


def discountCal():
    if(_isUserFirstTimer == 0):

        return 0
    else:
        if(int(user_NumOrders) <= 3):
            return 2
        elif(int(user_NumOrders) and user_NumOrders < 10):
            return 3
        elif(int(user_NumOrders) >= 10):
            return 5


def orderDelivery():
    global Discounted_totalPrice
    global user_LastAddress

    input('Press enter to continue')

    if(_isUserFirstTimer == 1):

        p.printslowly(
            'Your order is all set and ready to go, and will be at your doorstep in under 20 minutes!')
        print()
        print(username, 'would you like us to send you your order at your last address at ',
              user_LastAdress, ', or would you like to enter a new one?')
        u = input('Enter new address (y / n) >>>')
        if(u == 'y'):
            newaddress = input('Enter your new address >>>')

            f = open('custrecords.dat', 'rb')
            ff = open('new.dat', 'wb')

            try:
                while True:
                    lkm = pickle.load(f)
                    if(lkm['DesiCardNo'] == DESINO):
                        lkm['Last Address '] = newaddress
                        lkm['No. of Orders'] += 1

                        lll = datetime.datetime.now()
                        the_date = str(lll.strftime(
                            "%d"))+' '+str(lll.strftime("%m"))+' '+str(lll.strftime("%Y"))

                        lkm['Last Order on '] = the_date
                    else:
                        pass
                    pickle.dump(lkm, ff)
            except:
                f.close()
                ff.close()

            remove('custrecords.dat')
            rename('new.dat', 'custrecords.dat')

            p.printslowly('Thank you!')
            time.sleep(0.5)
            p.printslowly(
                'Kindly keep your location on at your device end too, so that we can deliver you your order in lesser time : ')

        else:
            f = open('custrecords.dat', 'rb')
            ff = open('new.dat', 'wb')
            try:
                while True:
                    lkm = pickle.load(f)
                    if(lkm['DesiCardNo'] == DESINO):
                        lkm['No. of Orders'] += 1

                        lll = datetime.datetime.now()
                        the_date = str(lll.strftime(
                            "%d"))+' '+str(lll.strftime("%m"))+' '+str(lll.strftime("%Y"))

                        lkm['Last Order on '] = the_date
                        time.sleep(0.5)
                        print('<custrecords updated!>')
                    else:
                        pass
                    pickle.dump(lkm, ff)
            except:
                f.close()
                ff.close()
            remove('custrecords.dat')
            rename('new.dat', 'custrecords.dat')

        time.sleep(0.7)
        p.printslowly('. . .')
        p.printslowly('Greato! Your food is on its way!')

    else:
        dic = {}
        dic['DesiCardNo'] = DESINO
        dic['No. of Orders'] = 1

        lll = datetime.datetime.now()
        the_date = str(lll.strftime("%d"))+' ' + \
            str(lll.strftime("%m"))+' '+str(lll.strftime("%Y"))

        dic['Last Order on '] = the_date
        uaddress = input('Enter your delivery address here >>>')
        dic['Last Address '] = uaddress

        f = open('custrecords.dat', 'ab')
        pickle.dump(dic, f)
        f.close()

        time.sleep(0.7)
        p.printslowly(
            'Kindly keep you location on at your device too, so that we can deliver you your order in lesser time !')
        p.printslowly('. . .')
        p.printslowly('Greato! Your food is on its way!')

    time.sleep(0.7)
    c = 1
    while c:
        time.sleep(0.7)
        print()
        print('''Dear Customer, would you like to:
    1. Look at your final order receipt
    2. EXIT
    3. Start another order''')

        unun = input('>>> ')
        if(unun == '1'):
            for mnop in finaltokri:
                print(mnop)
            print('Discounted Total Price : ', Discounted_totalPrice)
        elif(unun == '2'):
            c = 0
        elif(unun == '3'):
            main()
        else:
            p.printslowly(
                'ERROR -- Im afraid this option doesnt exist! Enter again: ')
    exitprog()


def main():
    greetings_time()
    time.sleep(1)
    firstdisplay()
    input('Press enter to continue.')
    time.sleep(1)
    authorisation()
    time.sleep(1)

    z = callmenus()
    time.sleep(0.7)
    FinalMostTokri = ask_updateornot(z)
    time.sleep(1)
    print()
    print('YOUR VERY FINAL TOKRI IS (Not yet discounted):')

    global finaltokri
    finaltokri = FinalMostTokri
    try:

        for zi in FinalMostTokri:
            print(zi)
    except:
        pass

    store_all_info(finaltokri, DESINO)
    time.sleep(0.7)
    orderDelivery()


main()
