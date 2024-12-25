def work2():
    global p1
    print('\n')
    print("Monthly Pricing: ")
    print('1.100 Mbps-₹599')
    print("2.150 Mbps-₹799")
    print("3.200 Mbps-₹899")
    print("4.300 Mbps-₹1299")
    print(f"Friendly reminder, yearly plans offer 20% discount.")
    while True:
        a1=input("Enter current preference: ")
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
        p1=599
    elif a1==2:
        p1=799
    elif a1==3:
        p1=899
    elif a1==4:
        p1=1299
    print('\n')
    print('Add-Ons: ')
    print("1.None")
    print('2.Exclusive OTT-₹99')
    print('3.Access Point-₹299') 
    print('4.Router-₹499')
    while True:
        a2=input("Enter current preference: ")
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
        p1=p1
    elif a2==2:
        p1+=99
    elif a2==3:
        p1+=299
    elif a2==4:
        p1+=499
    global con1
    global con2
    con1=True
    con2=False
    work1()
    bill()

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
        po=int(p)        
    elif t==2:
        print("Activated at: ",add)
        print("Rgistered number: ",num)
        print("Bill sent to: ",mail)
        print(f"Total bill: ₹{p*12}")
        print(f"Discounted bill: ₹{int((p*12)*0.8)}")
        po=int((p*12)*0.8)
    print("Thank you for choosing us.")
    if con1==True:
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
            print(f"Total bill: ₹{p1}")
            if po>int(p1):
                print(f"₹{(po-p1)} will be deducted from your account.")
            else:
                print(f"₹{p1-po} will be refunded to your account.")
        elif t==2:
            print("Activated at: ",add)
            print("Rgistered number: ",num)
            print("Bill sent to: ",mail)
            print(f"Total bill: ₹{p1*12}")
            print(f"Discounted bill: ₹{int((p1*12)*0.8)}")
            if po>int((p1*12)*0.8):
                print(f"₹{-1*(po-p1*12)} will be refunded to your account.")
            else:
                print(f"₹{int((p1*12)*0.8)-po} will be deducted from your account.")
        print("Thank you for choosing us.")
    opt()
def work():
    if q==1:
        work1()
    elif q==6:
        acc()
    elif q==7:
        work7()
    elif q==2:
        work2()
def work1():
    global p
    print('\n')
    print("Monthly Pricing: ")
    print('1.100 Mbps-₹599')
    print("2.150 Mbps-₹799")
    print("3.200 Mbps-₹899")
    print("4.300 Mbps-₹1299")
    print(f"Friendly reminder, yearly plans offer 20% discount.")
    while True:
        a1=input("Enter your preference: ")
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
        a2=input("Enter your preference: ")
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
    if con2==True:
        bill()
def work7():
    print("Thank you for choosing us.")
    print("We are a leading internet service provider in India. We offer a wide range of services and plans to suit your needs. Our services include Wi-Fi installation, internet plan upgrades, E-SIM activation, and location updates. We also offer a variety of add-ons such as exclusive OTT content, access points, and routers. Our plans are competitively priced and offer great value for money. We are committed to providing you with the best internet experience possible. Choose us for fast, reliable, and affordable internet service.")               
def opt():
    global q
    print("Options: ")
    print("1.Wi-Fi Installation.")
    print('2.Update your internet plan.')
    print('3.Upgrade physical SIM to E-SIM.')
    print('4.Update your location.')
    print('5.Why us?')
    print('6.Account')
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