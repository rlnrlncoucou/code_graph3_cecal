# graphique violon cecal
#on importe la bibliothèque adaptée

import matplotlib.pyplot as plt
import math

#on utilise uniquement les données "cecal" de l'expérience
graph = "ileal"

# initialiser les données
x=[]
y1=[]
y2=[]

# remplir avec les données issues du document
fIN = open('data_filtrer.csv', 'r')
line = fIN.readline()

#on ajoute au fur et à mesure nos données
count = 0
while line != '':
    line = fIN.readline()
    if line == '':
        break 
    # split line (séparer les données dans les lignes par ":")
    valueList = line.split(':')
        
    # récupérer les données
    sample_type = valueList[0]
    print(valueList)
    #Comme la population de souris cecal sont étudié qu'au 21 ème jour, nous ne prenons pas en compte le facteur "jour"
    #Nous étudions d'une part les souris placebo et d'autes part les souris ABX c'est pourquoi on est censé obtenir deux zones différentes
    treatment = valueList[2]
    bacteria = math.log(float(valueList[4]))/math.log(10)

    # filtrer les lignes
    if treatment == 'ABX' and sample_type == graph :
        y1.append(bacteria)
    else:
        y2.append(bacteria)
count=count+1
        
fIN.close()

# create graph data (instanciate graph) : crée la base du graphique (le corps)
figure, axes = plt.subplots()

# nommer les titres et les axes
axes.set_title('Bactérie vivante dans le caecum')
axes.set_ylabel('Bactérie vivante en log10')
axes.set_xlabel('Traitements')
# adapter les axes pour un graphique de type violon
axes.violinplot([y1,y2])
    
figure.savefig('Résultat graphique des bactéries dans l'iléum.png', dpi=300)
