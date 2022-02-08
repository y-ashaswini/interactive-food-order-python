import pickle
from os import remove,rename
#ME: Below, the current cust details you can input through the "def current_custdetails_binfile():" fn, because everytime you run it, it'll be refreshed. it is renewed every time one runs the code.
'''
{'Username': 'ilo', 'OrderDetails': [{'Userchoice': 'A', 'item name': ['Desi Chatpata', 'KathiRolls', 'Paneer', 20], 'quantity': 4, 'price': 80}, {'Userchoice': 'G', 'item name': ['Desi Chatpata', 'Golgappe', 'Black Grape Paani', 20], 'quantity': 4, 'price': 80}, {'Userchoice': 'K', 'item name': ['Desi Mishthaan', 'Gulab Jamun', 'Gulab Jamun', 25], 'quantity': 1, 'price': 25}], 'DesiNumber': 4000, 'OrderDate': '27 07 2020', 'TotalPrice': 65, 'Discount': 0, 'DiscountedPrice': 65.0}

{'Username': 'gimopunti', 'DesiNumber': 6650, 'OrderDate': '28 07 2020', 'OrderDetails': [{'Userchoice': 'A', 'item name': ['Desi Chatpata', 'KathiRolls', 'Paneer', 20], 'quantity': 8, 'price': 160}, {'Userchoice': 'C', 'item name': ['Desi Chatpata', 'PavItems', 'Pav Bhaaji', 15], 'quantity': 1, 'price': 15}, {'Userchoice': 'D', 'item name': ['Desi Chatpata', 'PavItems', 'Dabeli', 15], 'quantity': 1, 'price': 15}, {'Userchoice': 'H', 'item name': ['Desi Chatpata', 'Golgappe', 'Chaas Paani', 20], 'quantity': 1, 'price': 20}, {'Userchoice': 'J', 'item name': ['Desi Chatpata', 'Golgappe', 'Khatta Aam Paani', 20], 'quantity': 1, 'price': 20}, {'Userchoice': 'K', 'item name': ['Desi Mishthaan', 'Gulab Jamun', 'Gulab Jamun', 25], 'quantity': 1, 'price': 25}, {'Userchoice': 'L', 'item name': ['Desi Mishthaan', 'Srikhand', 'Srikhand', 25], 'quantity': 1, 'price': 25}], 'TotalPrice': 280, 'Discount': 0, 'DiscountedPrice': 280.0}

{'Username': 'hawaiian', 'DesiNumber': 8842, 'OrderDate': '28 07 2020', 'OrderDetails': [{'Userchoice': 'A', 'item name': ['Desi Chatpata', 'KathiRolls', 'Paneer', 20], 'quantity': 2, 'price': 40}, {'Userchoice': 'M', 'item name': ['Desi Mishthaan', 'Kulfi', 'Kulfi', 25], 'quantity': 1, 'price': 25}], 'TotalPrice': 65, 'Discount': 2, 'DiscountedPrice': 63.7}

{'Username': 'cmon', 'DesiNumber': 8421, 'OrderDate': '28 07 2020', 'OrderDetails': [{'Userchoice': 'A', 'item name': ['Desi Chatpata', 'KathiRolls', 'Paneer', 20], 'quantity': 2, 'price': 40}, {'Userchoice': 'E', 'item name': ['Desi Chatpata', 'PavItems', 'Misal Pav', 15], 'quantity': 1, 'price': 15}, {'Userchoice': 'K', 'item name': ['Desi Mishthaan', 'Gulab Jamun', 'Gulab Jamun', 25], 'quantity': 1, 'price': 25}], 'TotalPrice': 80, 'Discount': 0, 'DiscountedPrice': 80.0}

'''
def custrecords_binfile():
    #there are 5 records in it now
    d={}
    f = open('custrecords.dat','ab')
    n = int(input('enter n '))
    for i in range(n):
        dcardno = int(input('desi card no (four digits) : '))
        pastorders = int(input('no of orders in past :  '))
        date_lastorder = input('date month year \n')
        address_lastorder = input('enter address \n')
        d['DesiCardNo'] = dcardno
        d['No. of Orders'] = pastorders
        d['Last Order on '] = date_lastorder
        d['Last Address '] = address_lastorder
        pickle.dump(d,f)
    f.close()
    
def custrecords_display():
    try:
        f=open('custrecords.dat','rb')
        try:
            while True:
                f1=pickle.load(f)
                print(f1)
        except:
            f.close()
    except:
        print('such a file doesnt exist ')

def current_custdetails_binfile():
    ans = 'y'
    f = open('current_custdetails.dat','wb')
    while ans == 'y':
        l = eval(input('enter what you want to enter: '))
        pickle.dump(l,f)
        ans = input('cont? (y/n)>')
    f.close()
    print('file created')

'''
def createchaatfiles():
    
    f= open('KathiRolls.dat','wb')

    a=['Desi Chatpata','KathiRolls','Paneer','Popular Indian street-food, Paneer Kathi rolls are warm, layered parathas filled with spicy, creamy and soft paneer, mixed peppers and sweet caramelized onions.' , 20]
    b=['Desi Chatpata','KathiRolls','Spicy','This North Indian recipe is a beautifully synced performance of mashed potatoes, tomatoes, onions, green chutney and a melange of spices- all set to give your taste buds a thrill ride!', 20]
    pickle.dump(a,f)
    pickle.dump(b,f)
    
    print('done')
    f.close()



    f1 = open('PavItems.dat','wb')

    c=['Desi Chatpata','PavItems','Pav Bhaaji' , 'A plate for two' , 15]
    d=['Desi Chatpata','PavItems','Dabeli' , 'A plate for two' , 15]
    e=['Desi Chatpata','PavItems','Misal Pav' , 'A plate for two' , 15]
    pickle.dump(c,f1)
    pickle.dump(d,f1)
    pickle.dump(e,f1)
    print('done')
    f1.close()


    f2 = open('ChaatItems.dat','wb')

    f=['Desi Chatpata','ChaatItems','Dahi Vada' , 'A plate for two' , 15]
    g=['Desi Chatpata','ChaatItems','Paapadi Chaat' , 'A plate for two' , 15]
    h=['Desi Chatpata','ChaatItems','Samosa Chaat' , 'A plate for two' , 15]
    i=['Desi Chatpata','ChaatItems','Bhel Puri' , 'A plate for two' , 15]
    j=['Desi Chatpata','ChaatItems','Rabadi' , 'A plate for two' , 15]
    pickle.dump(f,f2)
    pickle.dump(g,f2)
    pickle.dump(h,f2)
    pickle.dump(i,f2)
    pickle.dump(j,f2)
    
    print('done')
    f2.close()


    f3 = open('Golgappe.dat','wb')

    k=['Desi Chatpata','Golgappe','Meetha Paani' ,'Not everyone likes their panipuri tangy- ; a few enjoy it sweet! Made with deep tamarind, date chutney, green chilly and lemon juice. Served chilled. 1 plate 5' , 20]
    l=['Desi Chatpata','Golgappe','Black Grape Paani' , 'The perfect blend of black grape juice, ground mint leaves, coriander leaves, green chillies, tamarind pulp, black salt, red chili powder and lemon juice. Served Chilled. 1 plate 5', 20]
    m=['Desi Chatpata','Golgappe','Chaas Paani' , 'Rich and creamy buttermilk mixed with a paste of coriander leaves, mint leaves and green chilies, this unique blend of flavours is sure to have a lasting impact on your taste buds! Served Chilled. 1 plate 5' , 20]
    n=['Desi Chatpata','Golgappe','Orange Juice Paani' , 'A beautiful blend of orange juice, roasted cumin powder, panipuri masala, chopped pudina, lemon juice and amchur powder.1 plate 5', 20]
    o=['Desi Chatpata','Golgappe','Khatta Aam Paani' , 'With fresh mangoes boiled, mashed and mixed with mint leaves, ginger, green chilies, and sugar, this paani is the favourite of all mango lovers! Served chilled. 1 plate 5' , 20]
    pickle.dump(k,f3)
    pickle.dump(l,f3)
    pickle.dump(m,f3)
    pickle.dump(n,f3)
    pickle.dump(o,f3)
    
    print('done')
    f3.close()

    f4 = open('DesiMishthaan.dat', 'wb')

    p=['Desi Mishthaan','Gulab Jamun', 'Gulab Jamun', 'Deep fried milk balls stuffed with pistachio and soaked in rose infused syrup. Here, we serve them topped with beautiful edible gemstones. 1 bowl contains 3',25]
    q=['Desi Mishthaan','Srikhand', 'Srikhand', 'The rich and delicious dessert, prepared using hung curd sweetened with sugar, flavoured with a tinge of cardamom and saffron and topped with edible gold foil is one of our most loved! 1 bowl serves 2' ,25]
    r=['Desi Mishthaan','Kulfi', 'Kulfi', 'Sweetened milk cooked until caramalization, with utmost patience and care gives birth to the legendary kulfi. Here we serve it topped with exotic nuts and edible pearls. 1 bowl serves 2',25]

    pickle.dump(p,f4)
    pickle.dump(q,f4)
    pickle.dump(r,f4)

    print('done')
    f4.close()
'''

def display():
    try:
        f=open('current_custdetails.dat','rb')
        try:
            while True:
                f1=pickle.load(f)
                print(f1)
                print()
        except:
            f.close()
    except:
        print('such a file doesnt exist ')

def del_unwanted(filename):
    f=open(filename,'rb')
    f2=open('new.dat','wb')
    flag=0
    print('deleting unwanted records :')
    m=1
    while m:
        if(flag<8):
            f1=pickle.load(f)
            pickle.dump(f1,f2)
            flag+=1
        else:
            m=0
    f.close()
    f2.close()
    print('Done')
    remove(filename)
    rename('new.dat',filename)

# current_custdetails_binfile()
custrecords_display()
# del_unwanted('custrecords.dat')
# display()