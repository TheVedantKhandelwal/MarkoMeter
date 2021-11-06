import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def pot():#to display a plotted graph
    graph = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    inp = input('Options: \nPhysics: 1\nChemistry: 2\nMaths: 3\nMy Choice:')
    if inp=='1':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Physics marks")
        a.plot(y='Physics',title="Physics")
        plt.show()
    elif inp=='2':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Chemistry marks")
        a.plot(y='Chemistry',title="Chemistry")
        plt.show()
    elif inp=='3':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Maths marks")
        a.plot(y='Maths',title="Maths")
        plt.show()
    elif inp=='END':
        input("Press ENTER to close")
    else:
        print("Invalid Option entered, Please try again!!!")
        pot()
        
pot()
import main
