##   MarkoMeter	: 	Student Result Management System
##   Author 	: 	Vedant Khandelwal
##   Version 	: 	1.0
##   Github 	: 	https://github.com/TheVedantKhandelwal



def art():#To recall art anywhere in program

    print("███╗░░░███╗░█████╗░██████╗░██╗░░██╗░█████╗░███╗░░░███╗███████╗████████╗███████╗██████╗░")
    print("████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗████╗░████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
    print("██╔████╔██║███████║██████╔╝█████═╝░██║░░██║██╔████╔██║█████╗░░░░░██║░░░█████╗░░██████╔╝")
    print("██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗")
    print("██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░███████╗██║░░██║")
    print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
    print('\t Author:Vedant Khandelwal')
    
#importing Libraries required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def init():#taking input from user
    inp = input("Options:\n1 : Show DataFrame\n2 : View plotted graph\n3 : View bar graph\n4 : View Pie Graph \n5 : Drop a row from DataFrame\n6 : Add Data to Dataframe ")
    if inp=='1':
        import show
    elif inp=='2':
        import pot
    elif inp=='3':
        import bar
    elif inp=='4':
        import pie
    elif inp =='5':
        import drop
    elif inp=='6':
        import marks
    elif inp=='END'or inp=='end':
        print('Closing app')
        input("Press enter to quit...")
        
    else:
        print('Invalid Option chosen, please try again!!!')
        init()
init()
