m='your'
ch=True
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
        if '@' in mail and '.' in mail and not mail.startswith('@') and not mail.startswith('.') and not mail.endswith('@') and not mail.endswith('.') and not mail[-1].isdigit() and mail.count("@")==1:
            print(f"Valid")
            break
        else:
            print("Enter a valid email address.")
    print("Thank you for registering with us.")
    opt()
def bill():
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
    elif q==6:
        work6()
    elif q==5:
        acc()
    elif q==2:
        change()
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
def work6():
    print("Thank you for choosing us.")
    print("We are a leading internet service provider in India. We offer a wide range of services and plans to suit your needs. Our services include Wi-Fi installation, internet plan upgrades, E-SIM activation, and location updates. We also offer a variety of add-ons such as exclusive OTT content, access points, and routers. Our plans are competitively priced and offer great value for money. We are committed to providing you with the best internet experience possible. Choose us for fast, reliable, and affordable internet service.")               
def opt():
    global q
    print("Options: ")
    print("1.Wi-Fi Installation.")
    print('2.Update your internet plan.')
    print('3.Upgrade physical SIM to E-SIM.')
    print('4.Why us?')
    print('5.Account')
    print("6.Exit")
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