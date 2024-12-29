#CHECK FOR ANY THREATS


#AFTER ADDING OPT 7 IN THE MENU CHECK FOR ANY CYBER SECURITY
userin=1234567890
#REPLACE EMAIL WITH THE ONE WHICH WE USED IN THE MAIN PROGRAMME
e=str(input(('ENTER YOUR EMAIL:  ')))
def thrt(cf,cs):
#    global userin
    s=int(input(cf))
    if s == userin:
        print(f'{s}')
        
        print('YOUR NUMBER IS VERIFIED')
    else:
        print('ENTER YOUR REGISTERED MOBILE NUMBER AGAIN')
  
    print('''\n
             1.CHECK FOR ANY CYBER THREATS 
             2.GET A CYBER  SHEILD FOR YOUR DEVICE
             3.UPGRADE YOUR CYBER SHIELD''')
    x=int(input(cs))
    if x==1:
        print("-------------------------------")
        print('CHECKING FOR THE PROVIDED MOBILE NUMBER AND THE EMAIL ADDRESS:')
        print(userin)
        print(e)
        print('''HAVE YOU GAVE ACCESS OF THE STORAGE OF YOUR DEVICE TO ANY SUSPICIOUS APP OR WEBSITE ? 
              1.YES 
              2.NO''')
        u=int(input('SELECT: '))
        if u in range(1,3):
            if u==1:
                print('THERE IS A RISK TO YOUR DATA')
                print('\n')
                
                print('YOU ARE PROVIDED WITH A FREE CYBER SHIELD FOR A MONTH  (t&c applied)')
                print('''\n
                      IN CASE YOU LIKE TO EXTEND THE CYBER SHIELD JUST VISIT HERE AGAIN ''')
            
            elif u==2:
                print('''IT SEEMS YOU ARE PREETY MUCH AWARE !
                      SCANNING''')
                print('YOUR DEVICE IS FREE ANY THREATS')
                print('''TO ENSURE YOUR DEVICE'S SAFETY WE ALSO HAVE CYBER SHIELD EXCLUSIVELY FOR OUR USERS''')
                
       
                  
            
        else:
            print('SELECT A VALID OPTION')
            
    if x==2:
        print('''HERE ARE THE AVAILABLE OPTIONS FOR THE CYBER SHEILD:
              
              1.RS 499/month    | BASE PACKAGE
              2.RS 599/month    | INTERMIDIATE PACKAGE
              3.RS 999/month    | ADVANCED PACKAGE
              
              FRIENDLY SUGGESTION : BASE PACKAGES --> NORMAL USERS
                                    INTERMIDIATE PACKAGES--> FOR SOMEONE LIKE A GAMER OR A PERSON WORKIN FROM HOME
                                    ADVANCED PACKAGES-->SPECIALLY BUILT FOR CODERS AND SOFTWARE DEVELOPERS
             THIS SHIELD WILL BE ACTIVATED FOR ALL THE DEVICES WHERE THE SAME ACCOUNT IS LOGGED IN ''')
        a=int(input('SELECT: '))
        if a in range(1,4):
            print('''
                  1.MONTHLY
                  2.YEARLY
                  ''')
            a1=int(input('SELECTE :'))
            if a1 in range(1,3):
                
                print('HERE IS YOUR BILL')
                
                print('''THANK YOU
                      ''')
                      
            else:
                print(' ENTER A VALID OPTION ')
                
                
                
                
                
    if x==3:
        print('SELECT YOUR CURRENT PACK: ')
        print('''
              1.RS 499/month    | BASE PACKAGE
              2.RS 599/month    | INTERMIDIATE PACKAGE
              3.RS 999/month    | ADVANCED PACKAGE''')
        b=int(input('select your current plan:  '))
        if b==1:
            print('''
                  SELECT THE PACK :
                  1.RS 599/month    | INTERMIDIATE PACKAGE
                  2.RS 999/month    | ADVANCED PACKAGE''')
            r=int(input('SELECT : '))
            if r in range(1,3):
                print('YOUR SHIELD WILL BE ACTIVATED IN THE NEXT FEW HOURS')
                print('HERE IS YOUR BILL ')
            else:
                print('SELECT A VALID OPTION')
        if b==2:
            print('''
                  1.RS 499/month    | BASE PACKAGE
                  2.RS 999/month    | ADVANCED PACKAGE''')
            r=int(input('SELECT : '))
            if r in range(1,3):
                 print('YOUR SHIELD WILL BE ACTIVATED IN THE NEXT FEW HOURS')
                 print('HERE IS YOUR BILL ')
        if b==3:
            print('''
                  1.RS 499/month    | BASE PACKAGE
                  2.RS 599/month    | INTERMIDIATE PACKAGE
                  ''')
            r=int(input('SELECT : '))
            if r in range(1,3):
                 print('YOUR SHIELD WILL BE ACTIVATED IN THE NEXT FEW HOURS')
                 print('HERE IS YOUR BILL ')
                  
                  
    print('''YOUR INTERACTION WITH US MEANS A LOT 
             PLEASE DO CONSIDER GIVING US A FEEDBACK:
                 1.VERYBAD 
                 2.POOR
                 3.GOOD
                 4.GREAT
                 5.AMAZING''')
    g=int(input('SELECT: '))
    if g in range(1,6):
        print('THANK YOU FOR GIVING US YOUR FEEDBACK')
    else:
        print('SELECT A VALID OPTION')
                
        
        
thrt('ENTER YOUR REGISTERED MOBILE NUMBER','SELCET:')
        
            
            
            
            