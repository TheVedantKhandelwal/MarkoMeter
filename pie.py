#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def pie():#To display pie graph
    data = pd.read_csv('YOUR PATH HERE')
    print(data)
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    inp = int(input("Plot Graph for? :"))
    Phys = data.loc[inp,'Physics']
    Chem = data.loc[inp,'Chemistry']
    
    math = data.loc[inp,'Maths']
    
    total = Phys.item()+math.item()+Chem.item()
    colours=['blue','red','green','red','yellow','red']
    qlabels = 'Physics','Physics Negative','Maths','Maths Negative','Chemistry','Chemistry Negative'
    print(Phys)
    physneg = 100-Phys
    print(Chem)
    chemneg = 100-Chem
    print(math)
    mathneg = 100-math
    print("\n*50")
    legraph = [Phys,physneg,math,mathneg,Chem,chemneg]
    plt.title("Marks")
    plt.pie(legraph,labels=qlabels,autopct='%1.1f%%',colors=colours)
    
    plt.show()
    print(total)

pie()
import main
