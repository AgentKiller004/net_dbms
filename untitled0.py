print('WELCOME')
print('LET US GET YOU SIGNED IN TO ENHANCE YOUR EXPERIENCE WITH US')
print('-------------------------------------------------------------')
X=str(input('ENTER YOUR NAME: '))
Y=int(input('ENTER YOUR MOBILE NUMBER '))
print('SELSECT WHY YOU CHOOSE THIS PLATFORM ')
print('1.WIFI INSTALLATION')
print('2,UPGRADE YOUR INTERNET PACK')
print('3.UPGRADE PHYSICAL SIM TO E-SIM')
print('4.ADD YOUR LOCATION')
print('5.WHY US ?')
print('\n')
print('6.EXIT')
print('\n')
q=int(input('select your preference: '))
if q==1:
        print('\n')
        print('THESE ARE THE OPTIONS AVAILABLE WITH US:')
        print('1.40mbps-500Rs/month..........it includes exclusive ott platform\n2.60mbps-800Rs/month..........it includes exclusive ott platform\n3.100mbps-100Rs/month..........all ott platform trial available\n4.1gbps-1500/month..........all inclusive')
        print('---------------------------------')
        print('FLAT 40% OFF ON YEARLY PACKAGES')
        print('---------------------------------')
        a1=int(input('SELECT YOUR CHOICE:   '))
        for b in range(1,5):
                if a1==b:
                         a2=str(input('enter your address'))
                         a3=int(input('ENTER YOUR PINCODE'))
                         print('\n')
                         print('SELECT ADD ONS: ')
                         print('1.EXCLUSIVE E-CINEMA(6 month trial)')
                         print('2.INTERNET BOOSTER(physical device) FOR LONG DISTANCES') 
                         print('3.SMART BOX FOR BETTER VIEWING EXPERIENCE')
                         x1=int(input('SELECT (if any) OR TYPE 0: '))
                         for c in range(1,4):
                               if x1==c:
                                    print('\n')
                                    print('ADDED(IF ALREADY SELECTED IN THE WIFI AVAILABILITY MENU IT"LL BE ADDED)')
                                    print('--------------------')
                                    print('HERE IS YOUR BILL:')

        if x1==0:
                print('----------------------------')
                print('YOUR REQUEST IS HELD FURTHER')
                print('----------------------------')
        elif x1!=c:
                print('enter a valid input')
        print('BILLLLLLLLLLLLLL')
        print('------------------------------------------------------------------------------------------')
            
if q==2:
        print('select you current plan:\n')
        print('1.Rs 449/month ,with e cinema (only a device )')
        print('2.999/month , unlimited access to 5g data and e-cinema(multiple devices)')
        print('3.399/month,3gb/day')
        print('-------------------------------------------------------------------------')
        q2=int(input('SELECT A PLAN : '))
        
        if q2==1:
           print('NOW PLEASE SELECT A PACK TO WHICH YOU WANT TO UPGRADE WITH: ''\n')
           print('1.999/month , unlimited access to 5g data and e-cinema(multiple devices)')
           print('2.399/month,3gb/day')
           print('')
           ask=int(input('select:'))
           
           for m in range(1,3):
               if ask==m:
                   print('YOUR PACK WILL BE UPAGRADED ON THE NEXT RECHARGES')
                   
                   print('KINDLY PAY ALL THE REMAINING BILLS( IF ANY )')                        
               if ask!=m:
                   print('SELECT A VALID OPTIOM')
                   ask1=int(input('select:'))
                   print('KINDLY PAY ALL THE REMAINING BILLS( IF ANY )')  
               
        if q2==2:
            print('NOW PLEASE SELECT A PACK TO WHICH YOU WANT TO UPGRADE WITH: ''\n')
            print('1.399/month,3gb/day')
            print('2.Rs 449/month ,with e cinema (only a device )')
            ask11=int(input('SELECT:'))
            for k in range(1,3):
                if ask11==k:
                    print('YOUR PACK WILL BE UPAGRADED ON THE NEXT RECHARGES')
                    
                    print('KINDLY PAY ALL THE REMAINING BILLS( IF ANY )')                        
                if ask11!=k:
                    print('SELECT A VALID OPTIOM')
                    ask1=int(input('select:'))
                    print('KINDLY PAY ALL THE REMAINING BILLS( IF ANY )')  
        if q2==3:
            print('NOW PLEASE SELECT A PACK TO WHICH YOU WANT TO UPGRADE WITH: ''\n')
            print('1.999/month , unlimited access to 5g data and e-cinema(multiple devices)')
            print('2.Rs 449/month ,with e cinema (only a device )')
            ask11=int(input('SELECT:'))
            for k in range(1,3):
                if ask11==k:
                    print('YOUR PACK WILL BE UPAGRADED ON THE NEXT RECHARGES')
                    
                    print('KINDLY PAY ALL THE REMAINING BILLS( IF ANY )')                        
                if ask11!=k:
                    print('SELECT A VALID OPTIOM')
                    ask1=int(input('select:'))
                    print('KINDLY PAY ALL THE REMAINING BILLS( IF ANY )')  
            
         

# tp
if q==3:
  print('1. upgrade physical sim to e-sim')
  print('2. change the e-sim package')
  print('3. FAQs regarding e-sim')
  print('4. benifits of e-sim')
  print('------------------------')
  x=int(input('enter option number :'))
  if x==1:
    print('------------------------')
    print('1. keep same nuber')
    print('2. change number')
    print('3. multiple package')
    print('4. Back')
    print('\n')
    y=int(input('enter option number :'))
    if y==1 :
      print("Price = Rs.500")
    if y==2:
      print('Price to change nuber = Rs.750')
      new=int(input('enter new number :'))
      new2=int(input('conform new nymber :'))
      if new==new2 :
        print("your number is succesfully changed ")
      else: 
        print('reenter new number')
        new=int(input('enter new number :'))
        new2=int(input('conform new nymber :'))
    if y==3:
      print('')

    # if y==4:
    #   print('1. upgrade physical sim to e-sim')
    #   print('2. change the e-sim package')
    #   print('3. FAQs regarding e-sim')
    # print('4. benifits of e-sim')
    #   x=int(input('enter option number :'))

    else:
      print('page not found')
  if x==2:
    print("1. the basic eSIM card plan offering 1GB of global data")
    print("2. the basic eSIM card plan offering 3GB of global data")
    z=int(input("choose package :"))
    if z==1:
      print('charge = $4 (weekly)')
    if z==2:
      print("charge = $12(monthly)")
    else:
      print('package not available')
  if x==3:
    print('1. What is an eSIM?')
    print('2. How is an eSIM different from a physical SIM card?')
    print('3. What devices support eSIM?')
    print('4. Is an eSIM transferable between devices?')
    print('5. Does eSIM support roaming?')
    p=int(input('enter your question num:'))
    if p==1:
      print('An eSIM (embedded SIM) is a digital SIM embedded into your device, allowing you to connect to a mobile network without needing a physical SIM card')
    if p==2:
      print('Unlike a physical SIM card, an eSIM is built into the device and can be programmed remotely, eliminating the need for swapping physical cards.')
    if p==3:
      print('Many modern smartphones, tablets, smartwatches, and IoT devices support eSIM technology, such as the latest iPhone, Samsung Galaxy, Google Pixel devices, and some wearables like Apple Watch.')
    if p==4:
      print('No, eSIM profiles are generally tied to a specific device. You’ll need to contact your carrier to move the eSIM to a new device.')
    if p==5:
      print('Yes, eSIM supports international roaming just like physical SIM cards, as long as your carrier provides the service.')
  if x==4:
    print('benifits of eSIM :\n')
    print('1. Convenience\n2. Supports Multiple Profiles\n3. Dual-SIM Functionality\n4.Durability')
    B=int(input('enter option for which you would like to know more'))
    if B==1:
      print('--> No need to physically insert or swap SIM card.\n--> Easy to set up and activate via QR codes or carrier apps.\n--> Useful for frequent travelers who need to switch between carriers or plans.')
    if B==2:
      print('--> Store multiple carrier profiles on a single eSIM, such as personal and work numbers or international plans.\n--> Switch between profiles without requiring a new SIM card.')
    if B==3:
      print('--> Many devices support using an eSIM alongside a physical SIM, allowing dual-SIM functionality.]n--> Useful for managing two phone numbers or networks simultaneously.')
    if B==4:
      print('--> No moving parts like physical SIMs, which can be damaged, lost, or wear out.\n--> Ideal for rugged devices used in extreme conditions, such as smartwatches and IoT devices.')
  else:
    print('invalid option!!\n reenter')
    # if y==4:
    #   print('1. upgrade physical sim to e-sim')
    #   print('2. change the e-sim package')
    #   print('3. FAQs regarding e-sim')
    # print('4. benifits of e-sim')
    #   x=int(input('enter option number :'))

if q==5:
    def  whyus():
        print('------------')
        print('WHYY USS ??')
        print('------------')
        print('THESE ARE THE REASONS WHY WE BELIEVE WE ARE BETTER THAN OTHERS: \n')
        print(''''A.INTERNET QUALITY: 
              
                  WE ARE THE ONLY ONES WHOSE INTERNET CONNECTIVITY DOES NOT DEPEND UPON THE GEOGRAPHICAL CONDITIONS
                  WE PROVIDE YOU WITH FABULOUS INTERNET CONNECTION THAT TOO INA VERY REASONABLE PRIZE . EVERY NEW FEATURE 
                  OF OUR SERVIC IS FIRST TESTED BY EXPERTS AND THEN PROVIDED TO OUR 'CUSTOMER PANEL' TO REVIEW IT AFTER
                  USING IT FOR 2-6 MONTHS AND THEN IT REACHES YOU.''')
        print('''B.CUSTOMERS:
                 
                  WE STRONGLY BELIEVE THAT WE HAVE ONE OF THE BEST CUSTOMER OWNER CONNECTION AND WE PROVIDE TRANSPERENCY
                  TO OUR USERS.EVERY CITY HAS OUR 3(MINIMUM) CUSTOMER CARE CENTRE WHICH ARE VERY WELL EQUIPPED AND WITH
                  EXPERIENCED ENGINNERS.
                  WE HAVE ONE OF THE BEST RATING ON EACH FACILITY WE PROVIDE(  TO BE CONTINUED    )''')
        print()
        print()
        
   
if q==6:
    print('YOU HAVE EXITED THE PROGRAMME (   TO BE CONTINUED     )')
print('------------------------------------------------')
print('THANK YOU , YOUR INTERACTION WITH US MEANS A LOT')
print('------------------------------------------------')





