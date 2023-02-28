print(20*" ", " Welcome To Athreya Super Market", 20*" ")

from datetime import datetime

name=input("enter your name:")

list= '''
rice                        Rs 50/kg,
sugar                       Rs 20/kg,
bread                       Rs 20/packet,
cheese                      Rs 80/kg,
peanut Buteer               Rs300/kg,
kisan Jam                   Rs 200/kg,
tamarind                    Rs 120/kg,
peanuts                     Rs 120/kg,
jaggery                     Rs 150/kg,
wheat Flour                 Rs 40/kg,
maida                       Rs 40/kg,
cashew Nuts                 Rs 800/kg,
dates                       Rs 150/kg,
baking soda                 Rs 15/packet,
sunrise coffe powder        Rs 3/packet,
coconut Oil                 Rs 120/liter,
cooking oil                 Rs 110/liter,
mysore sandal soaps         Rs 250/3pcs,
dish Wash                   Rs 80/packet,
'''



price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]


items={
'rice'                :       50,
'sugar'               :       20,
'bread'               :       20,
'cheese'              :       80,
'peanutbutter'        :       300,
'kisanjam'            :       200,
'tamarind'            :       120,
'peanuts'             :       120,
'jaggery'             :       150,
'wheatflour'          :       40,
'maida'               :       40,
'cashew Nuts'         :       800,
'dates'               :       150,
'baking soda'         :       15,
'sunrisecoffepowder'  :       3,
'coconutOil'          :       120,
'cookingoil'          :       110,
'mysoresandalsoaps'   :       250,
'dish Wash'           :       80  
}


opt=int(input("enter press 1 for list:"))
if opt==1:
    print(list)
else:
    print("entered wrong key")
    
for i in range (len(items)):
    if i==(len(items)):
        print(i)
    else:
        pass
    opt1=int(input("if you want to buy press 1 or 2 for exit:"))
    if opt1==2:
        break
    if opt1==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append([item,quantity,items,price])
            
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            totalprice+=price
            
            gst=(totalprice*10)/100
            finalprice=gst+totalprice
        else:
            print("sorry item not found")   
    else:
        print("wrong key entered")
                    
inp=input("can i bill items yes or no:")
if inp=='yes':
    pass

if finalprice!=0:
    print(20*"^", "Athreya Supermart",20*"^" )
    print(15*"-", "Guntur",15*"-" )
    print("name :",name,25*" ","date:",datetime.now())
    print(110*" ")
    print("sno",25*" " ,"items",25*" ","quantity",20*" ","price" )
    
    for i in range (len(pricelist)):
        print(i, 28*" ", ilist[i], 28*" ", qlist[i], 24*" ", plist[i])
        if i==(len(pricelist)):
            print(pricelist)
    
  
    print(120*"=")
    
     
    #print(90*"-")
    print(30*" ","totalamount:",40*" ",12*" ","Rs",totalprice)
    print(30*" ","gst:",50*" ",11*" ","Rs",gst)
    print(110*"-")
    print(30*" ","finalprice:",40*" ",13*" ","Rs",finalprice)
    print(110*"-")
    print(30*" ", "---Thanks for Visiting---")
    print(110*" ")
    

    