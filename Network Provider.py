def val(pro, valopt):
    while True:
        try:
            userin = int(input(pro))
            if userin in valopt:
                return userin
            else:
                print("Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")
def work4():
    print('Why Choose Us for WiFi Installation?')
    print('1. Expertise and Experience')
    print('2. Customized Solutions')
    print('3. Advanced Technology')
    print('4. Affordable Pricing')
    print('5. Security and Privacy')
    info=val("Enter option:",[1, 2, 3, 4, 5])
    
    if info==1:
        print('1. Highly Qualified Technicians')
        print('2. Proven Track Record')
        O=val("Choose: ",[1, 2])
        
        if O==1:
            print('\t-->Technicians with extensive training and industry certifications.\n \t -->Years of hands-on experience with different WiFi technologies and setups.')
            
        elif O==2:
            print('\t-->Successful installations for residential, commercial, and industrial clients.\n \t -->Positive reviews and testimonials from satisfied customers.')
        
        else:
            print('choosed info is not available ')
    
    elif info==2:
        print('1.Tailored Wi-Fi Setup')
        print('2.Support for Various Devices')
        C=val("Choose: ",[1, 2])
        
        if C==1:
            print('\t--> Analysis of the specific layout and needs of your space before installation.\n \t --> Recommendations for optimal router placement to ensure maximum coverage.')
        
        elif C==2:
            print('\t-->Expertise in connecting a wide range of devices including smartphones, laptops, smart TVs, and IoT devices.\n \t --> Ability to configure both wired and wireless setups depending on your requirements.')
        
        else:
            print('choosed info is not available ')
    
    elif info==3:
        print ('1. Use of Latest Equipment')
        print('2. Seamless Connectivity')
        A=val("Choose: ",[1, 2])
        
        if A==1:
            print ('\t--> Deployment of the latest WiFi routers and repeaters for optimal performance.\n \t-->Integration of advanced technology like WiFi 6 or mesh networks for better speed and coverage')
        
        elif A==2:
            print ('\t-->Solutions designed to ensure smooth, uninterrupted connectivity throughout your space.\n \t -->Tools for analyzing signal strength to fine-tune network performance.')
        
        else:
            print('choosed info is not available ')   
    
    elif info==4:
        print('1. Competitive Pricing Models')
        print('2. Cost-Effective Solutions')
        F=val("Choose: ",[1, 2])
        
        if F==1:
            print("\t-->Transparent and upfront pricing with no hidden fees.\n \t -->Flexible plans based on the scope of your WiFi needs (residential, commercial, enterprise).")
        
        elif F==2:
            print('\t-->Offering value for money with high-quality installation and maintenance services.\n \t -->Discount packages for multi-installation sites (businesses or multiple rooms).')
        
        else:
            print('choosed info is not available ')  
   
    elif info==5:
        print('1. Secure Network Setup')
        print('2. Safe Installation Practices')
        S=val("Choose: ",[1, 2])
        
        if S==1:
            print('\t--> Implementation of strong encryption (WPA3, VPN, etc.) to protect your WiFi from unauthorized access.\n \t--> Advice on network privacy and security best practices.')
        
        elif S==2:
            print('\t--> Adherence to safety standards and regulations during installation.\n \t--> Installation of firewalls and protection against external threats.')
        
        else:
            print('choosed info is not available ')
    opt()
def work3():
    global a
    global p
    print('1.Upgrade physical SIM to E-SIM.')
    print('2.Change the E-SIM package.')
    print('3.FAQs regarding E-SIM.')
    print('4.Benefits of E-SIM.')
    x = val("Enter option:",[1, 2, 3, 4])
    
    if x == 1:
        print('1.Keep same number.')
        print('2.Change number.')
        print('3.View package option.')
        print('4.Back')
        y = val("Enter option:",[1, 2, 3, 4])
        
        if y == 1:
            print("Price = Rs.500")
            p=500
            bill()
        
        elif y == 2:
            print('Price to change number. = Rs.750')
            while True:
                new=input("Enter number: ")
                if new.isdigit():
                    a=str(new)
                    if len(a)==10:
                        print(f"Valid")
                        break
                    else:
                        print("Enter a valid number.")
                else:
                    print("Enter a valid number.")
            while True:
                new2=input("Re-enter number: ")
                if new2.isdigit():
                    k=str(new2)
                    if len(k)==10:
                        if k==a:
                            print("Number changed successfully.")
                            break
                        else:
                            print("Numbers do not match.")
                    else:
                        print("Enter a valid number.")
                else:
                    print("Enter a valid number.")
            p=750
            bill()        
        elif y == 3:
            
            print('1. Basic E-SIM Package (Low Data Use)')
            print('2. Standard E-SIM Package (Moderate Use)')
            print('3. Premium E-SIM Package (High Data Use)')
            package=val("Enter option:",[1, 2, 3])
            
            if package==1:
                print('''Basic E-SIM Package includes:
                        \n \t -->1GB of Data (Valid for 30 days) 
                        \n \t -->Unlimited texting.
                        \n \t -->100 minutes of local calls.\n \t -->Basic customer support.''')
                print("\033[1m\033[4mPrice: ₹50/month\033[0m ") # to make letters bold and underline them
                p=50
                bill()
            if package==2:
                print('''Standard E-SIM Package includes :
                        \n \t -->3GB of Data (Valid for 30 days)
                        \n \t -->Unlimited texting and calls within the registered circle.
                        \n \t -->50 minutes of international calls.\n \t -->Priority customer support.''')
                print("\033[1m\033[4mPrice: ₹150/month\033[0m ") # to make letters bold and underline them
                p=150
                bill()
            if package==3:
                print('''Premium E-SIM Package includes :
                        \n \t -->10GB of High-Speed Data (Valid for 30 days)
                        \n \t -->Unlimited texting and calls within the registered circle.
                        \n \t -->Premium customer support with faster response times.''')
                print("\033[1m\033[4mPrice: ₹300 per month\033[0m ") # to make letters bold and underline them
                p=300
                bill()
        
        elif y == 4:
            # Optional action when going back
            pass
        
        else:
            # If an invalid option for changing sim is entered, do not print "page not found"
            print("Invalid option! Please choose a valid option.")
    
    elif x == 2:
        print("1. The basic E-SIM card plan offering 1GB of global data.")
        print("2. The basic E-SIM card plan offering 3GB of global data.")
        z = val("Enter option:",[1, 2])
        
        if z == 1:
            print('Charge = ₹40 (monthly)')
            p=40
            bill()
        
        elif z == 2:
            print("Charge = ₹120 (monthly)")
            p=120
            bill()
        
        else:
            print("Package not available.")
    
    elif x == 3:
        print('1. What is an E-SIM?')
        print('2. How is an E-SIM different from a physical SIM card?')
        print('3. What devices support E-SIM?')
        print('4. Is an E-SIM transferable between devices?')
        print('5. Does E-SIM support roaming?')
        m = val("Enter question number:",[1, 2, 3, 4, 5])
        
        if m == 1:
            print('An eSIM (embedded SIM) is a digital SIM embedded into your device, allowing you to connect to a mobile network without needing a physical SIM card')
        
        elif m == 2:
            print('Unlike a physical SIM card, an eSIM is built into the device and can be programmed remotely, eliminating the need for swapping physical cards.')
        
        elif m == 3:
            print('Many modern smartphones, tablets, smartwatches, and IoT devices support eSIM technology, such as the latest iPhone, Samsung Galaxy, Google Pixel devices, and some wearables like Apple Watch.')
        
        elif m == 4:
            print('No, eSIM profiles are generally tied to a specific device. You will need to contact your carrier to move the eSIM to a new device.')
        
        elif m == 5:
            print('Yes, eSIM supports international roaming just like physical SIM cards, as long as your carrier provides the service.')

        else:
            print("Invalid question number! Please select a valid option.")
    
    elif x == 4:
        print('benefits of eSIM :\n')
        print('1. Convenience\n2. Supports Multiple Profiles\n3. Dual-SIM Functionality\n4. Durability')
        B = int(input('enter option for which you would like to know more'))
        
        if B == 1:
            print('--> No need to physically insert or swap SIM card.\n--> Easy to set up and activate via QR codes or carrier apps.\n--> Useful for frequent travelers who need to switch between carriers or plans.')
        
        elif B == 2:
            print('--> Store multiple carrier profiles on a single eSIM, such as personal and work numbers or international plans.\n--> Switch between profiles without requiring a new SIM card.')
        
        elif B == 3:
            print('--> Many devices support using an eSIM alongside a physical SIM, allowing dual-SIM functionality.\n--> Useful for managing two phone numbers or networks simultaneously.')
        
        elif B == 4:
            print('--> No moving parts like physical SIMs, which can be damaged, lost, or wear out.\n--> Ideal for rugged devices used in extreme conditions, such as smartwatches and IoT devices.')
        
        else:
            print("Invalid option for benefits. Please choose a valid number.")
    
    else:
        print("Invalid option! Please choose a valid option.")    
    opt()
m='your'
ch=True
def work6():
    global p
    print('Choose plan: ')
    print('1.Data Plan')
    print('2.Talktime Plan')
    x=val("Enter option:",[1, 2])
    if x==1:
        print('i.1GB/existing plan-₹29')
        print('ii.2GB/existing plan-₹49')
        print('iii.5GB/existing plan-₹99')
        print('iv.Unlimited/1 day-₹149')
        print('v.Unlimited/7 days-₹299')
        y=val("Enter option:",[1, 2, 3, 4, 5])
        if y==1:
            print('1GB/existing plan-₹29')
            p=29
            bill()
        elif y==2:
            print('2GB/existing plan-₹49')
            p=49
            bill()
        elif y==3:
            print('5GB/existing plan-₹99')
            p=99
            bill()
        elif y==4:
            print('Unlimited/1 day-₹149')
            p=149
            bill()
        elif y==5:
            print('Unlimited/7 days-₹299')
            p=299
            bill()
    elif x==2:
        print('i.Unlimited talktime, 100 SMS/day, 1GB data/day-₹199')
        print('ii.Unlimited talktime, 100 SMS/day, 2GB data/day-₹299')
        print('iii.Unlimited talktime, 200 SMS/day, 3GB data/day-₹399')
        print('iv.Unlimited talktime, 200 SMS/day, 5GB data/day-₹499')
        print('v.Unlimited talktime, 200 SMS/day, Unlimited data/day-₹599')
        print('vi.Unlimited talktime, Unlimited SMS/day, Unlimited data/day-₹899')
        z=val("Enter option:",[1, 2, 3, 4, 5, 6])
        if z==1:
            print('Unlimited talktime, 100 SMS/day, 1GB data/day-₹199')
            p=199
            bill()
        elif z==2:
            print('Unlimited talktime, 100 SMS/day, 2GB data/day-₹299')
            p=299
            bill()
        elif z==3:
            print('Unlimited talktime, 200 SMS/day, 3GB data/day-₹399')
            p=399
            bill()
        elif z==4:
            print('Unlimited talktime, 200 SMS/day, 5GB data/day-₹499')
            p=499
            bill()
        elif z==5:
            print('Unlimited talktime, 200 SMS/day, Unlimited data/day-₹599')
            p=599
            bill()
        elif z==6:
            print('Unlimited talktime, Unlimited SMS/day, Unlimited data/day-₹899')
            p=899
            bill()
def change():
    global ch
    ch=False
    work1(m)
    pn=pk
    j='new'
    work1(j)
    pm=pk
    print(f"Your previous plan cost: ₹{pn}")
    print(f"Your new plan cost: ₹{pm}")
    if pn>pm:
        print(f"You will be refunded: ₹{pn-pm}")
        ch=True
        opt()
    elif pn<pm:
        print(f"You will be charged: ₹{pm-pn}")
        ch=True
        opt()
    else:
        print("No changes made.")
        ch=True
        opt()
def acc():
    global add
    global num
    global mail
    add=input("Enter address: ")
    while True:
        num=input("Enter number: ")
        if num.isdigit():
            num=int(num)
            k=str(num)
            if len(k)==10:
                print(f"Valid")
                break
            else:
                print("Enter a valid number.")
        else:
            print("Enter a valid number.")
    while True:
        mail=input("Enter email address: ")
        if ('@' in mail and 
            '.' in mail and not 
            mail.startswith('@') and not 
            mail.startswith('.') and not 
            mail.endswith('@') and not 
            mail.endswith('.') and not 
            mail[-1].isdigit() and 
            mail.count("@")==1):
            print(f"Valid")
            break
        else:
            print("Enter a valid email address.")
    print("Thank you for registering with us.")
    opt()
def bill():
    global p
    global pk
    print("Options: ")
    print("1.Monthly")
    print("2.Yearly")
    while True:
        t=input("Enter choice: ")
        if t.isdigit():
            t=int(t)
            if 1<=t<=2:
                print(f"Valid, you chose: {t}")
                break
            else:
                print("Invalid, please enter a option between 1 and 2.")
        else:
            print("Invalid, please enter a option between 1 and 2.")

    if t==1:
        print("Activated at: ",add)
        print("Rgistered number: ",num)
        print("Bill sent to: ",mail)
        print(f"Total bill: ₹{p}")
        pk=p
    elif t==2:
        print("Activated at: ",add)
        print("Rgistered number: ",num)
        print("Bill sent to: ",mail)
        print(f"Total bill: ₹{p*12}")
        print(f"Discounted bill: ₹{int((p*12)*0.8)}")
        pk=int((p*12)*0.8)
    print("Thank you for choosing us.")
    if ch==True:
        opt()
def work():
    if q==1:
        work1(m)
    elif q==7:
        work7()
    elif q==5:
        acc()
    elif q==2:
        change()
    elif q==3:
        work3()
    elif q==4:
        work4()
    elif q==6:
        work6()
def work1(g):
    global p
    print('\n')
    print("Monthly Pricing: ")
    print('1.100 Mbps-₹599')
    print("2.150 Mbps-₹799")
    print("3.200 Mbps-₹899")
    print("4.300 Mbps-₹1299")
    print(f"Friendly reminder, yearly plans offer 20% discount.")
    while True:
        a1=input(f"Enter {g} preference: ")
        if a1.isdigit():
            a1=int(a1)
            if 1<=a1<=4:
                print(f"Valid, you chose: {a1}")
                break
            else:
                print("Invalid, please enter a option between 1 and 4.")
        else:
            print("Invalid, please enter a option between 1 and 4.")
    if a1==1:
        p=599
    elif a1==2:
        p=799
    elif a1==3:
        p=899
    elif a1==4:
        p=1299
    print('\n')
    print('Add-Ons: ')
    print("1.None")
    print('2.Exclusive OTT-₹99')
    print('3.Access Point-₹299') 
    print('4.Router-₹499')
    while True:
        a2=input(f"Enter {g} preference: ")
        if a2.isdigit():
            a2=int(a2)
            if 1<=a2<=4:
                print(f"Valid, you chose: {a2}")
                break
            else:
                print("Invalid, please enter a option between 1 and 4.")
        else:
            print("Invalid, please enter a option between 1 and 4.")
    if a2==1:
        p=p
    elif a2==2:
        p+=99
    elif a2==3:
        p+=299
    elif a2==4:
        p+=499
    bill()
def work7():
    print("Thank you for choosing us.")
    print("We are a leading internet service provider in India. We offer a wide range of services and plans to suit your needs. Our services include Wi-Fi installation, internet plan upgrades, E-SIM activation, and location updates. We also offer a variety of add-ons such as exclusive OTT content, access points, and routers. Our plans are competitively priced and offer great value for money. We are committed to providing you with the best internet experience possible. Choose us for fast, reliable, and affordable internet service.")               
def opt():
    global q
    print("Options: ")
    print("1.Wi-Fi Installation")
    print('2.Update your internet plan.')
    print('3.E-SIM')
    print('4.Why us?')
    print('5.Account')
    print('6.Recharge Number')
    print("7.Exit")
    while True:
        q=input("Select serivce: ")
        if q.isdigit():
            q=int(q)
            if 1<=q<=7:
                print(f"Valid, you chose: {q}")
                work()
                break
            else:
                print("Invalid, please enter a option between 1 and 7.")
        else:
            print("Invalid, please enter a option between 1 and 7.")
acc()