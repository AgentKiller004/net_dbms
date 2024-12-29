def feedback():
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



feedback()


