


#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def bar():#To display Bar Graph
    graph = pd.read_csv('YOUR PATH HERE')  #Path to CSV 
    inp = input('Choice: \nPhysics: 1\nChemistry: 2\nMaths: 3')
    if inp=='1':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Physics marks")
        a.plot(y='Physics',title="Physics",kind="bar")
        plt.show()
    elif inp=='2':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Chemistry marks")
        a.plot(y='Chemistry',title="Chemistry",kind="bar")
        plt.show()
    elif inp=='3':
        input("Press ENTER to continue to Maths marks")
        a.plot(y='Maths',title="Maths",kind="bar")
        plt.show()
    elif inp=='END':
        input("Press ENTER to close")
    else:
        print("Invalid Option entered, Please try again!!!")
        bar()
    import main
bar()
