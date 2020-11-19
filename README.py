# SoccerData
#goal is to create the final table of serieA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Displays all the columns
pd.set_option('display.max_columns', None)
# Makes all the column next to each other as opposed to separating things
pd.set_option("display.expand_frame_repr", False)
values = np.array([
    [16, 2, 1, 50, 10, 3, 5, 33, 83],  # Juve
    [11, 6, 2, 39, 13, 4, 2, 43, 82],  # Inter
    [12, 2, 5, 38, 11, 7, 1, 40, 78],  # Atalanta
    [14, 3, 2, 45, 10, 3, 6, 33, 78],  # Lazio
    [10, 4, 5, 34, 11, 3, 5, 36, 70],  # Roma
    [9, 6, 4, 33, 10, 3, 6, 33, 66],  # Milan
    [10, 3, 6, 33, 8, 5, 6, 29, 62],  # Napoli
    [8, 3, 8, 27, 6, 6, 7, 24, 51],  # Sassuolo
    [9, 5, 5, 32, 3, 8, 8, 17, 49],  # Hellas
    [5, 8, 6, 23, 7, 5, 7, 26, 49],  # Fiorentina
    [7, 2, 10, 23, 7, 5, 7, 26, 49],  # Parma
    [5, 8, 6, 23, 7, 3, 9, 24, 47],  # Bologna
    [6, 6, 7, 24, 6, 3, 10, 21, 45],  # Udinese
    [7, 4, 8, 25, 4, 8, 7, 20, 45],  # Cagliari
    [6, 4, 9, 22, 6, 2, 11, 20, 42],  # Sampdoria
    [7, 4, 8, 25, 4, 3, 12, 15, 40],  # Torino
    [7, 1, 11, 22, 3, 8, 8, 17, 39],  # Genoa
    [4, 5, 10, 17, 5, 3, 11, 18, 35],  # Lecce
    [3, 5, 11, 14, 3, 2, 14, 11, 25],  # Brescia
    [2, 4, 13, 10, 3, 1, 15, 10, 20]  # Spal
])

SerieA2020 = pd.DataFrame(index=['Juventus', 'Inter', 'Atalanta', 'Lazio', 'Roma',
                                 'Milan', 'Napoli', 'Sassuolo', 'Hellas', 'Fiorentina',
                                 'Parma', 'Bologna', 'Udinese', 'Cagliari', 'Sampdoria',
                                 'Torino', 'Genoa', 'Lecce', 'Brescia', 'Spal'],
                          columns=['HomeWin', 'HomeTie', 'HomeLosses', 'HomePoints',
                                   'AwayWins', 'AwayTie', 'AwayLosses', 'AwayPoints',
                                   'TotalPoints'],
                          data=values
                          )
print('\n\n\n')
print(SerieA2020)
print("\n\n\n")

# a = SerieA2020['HomeWin'].std()
# print(a)

description = SerieA2020.describe().transpose()
print(description)

print("-------------------------------------" + "\n\n\n")

print(SerieA2020.loc[['Juventus']])
print("------")

a = list(SerieA2020.iloc(axis=1)[1])
print(a)

print("-------------\n\n\n\n\n\n\n\n")

# for row in SerieA2020.index:
#     print(row, end=" ")

# This one helps you access the index
list1 = SerieA2020.index

points = (SerieA2020.iloc(axis=1)[8])

a = 0

# Interesting way to access just the points
# while (a<20):
#     print("points = " + str(points[a]))
#
#     a+=1


fig = plt.figure()
axes = fig.add_axes([0.05, 0.1, 1, 1])
a = plt.subplots

x = (range(len(points)))
new_x = [2 * i for i in x]

axes.set_title("Serie A")
axes.set_xlabel("Team")
axes.set_ylabel("Points")

plt.xticks(rotation=90)
teamColours = ['#034694', '#001C58', '#5CBFEB', '#D00027',
               '#EF0107', '#DA020E', '#12A0D7', '#ED1A3B',
               '#000000', '#482E92', '#FFD200', '#1A2F48',

               '#7F7F7F', '#AD002A', '#1B5497', '#53162f',
               '#AD1919', '#006086', '#005CA8', '#3697C4']

axes.bar(list1, points, color=teamColours, width=0.7)

plt.ylim(0, max(points))
axes.bar(list1[0], points[0], width=0.7, color='#000000', hatch='||||', edgecolor='#f7f7f7')
axes.bar(list1[1], points[1], width=0.7, color='#0f097d', hatch='||||', edgecolor='#000000')
axes.bar(list1[2], points[2], width=0.7, color='#1732e3', hatch='||||', edgecolor='#000000')
axes.bar(list1[3], points[3], width=0.7, color='#87D8F7')
axes.bar(list1[4], points[4], width=0.7, color='#8E1F2F')
axes.bar(list1[5], points[5], width=0.7, color='#FB090B', hatch='||||', edgecolor='#000000')
axes.bar(list1[7], points[7], width=0.7, color='#00A752', hatch='||||', edgecolor='#000000')
axes.bar(list1[8], points[8], width=0.7, color='#edde11', hatch='||||', edgecolor='#000000')
axes.bar(list1[14], points[14], width=0.7, color='#1B5497', hatch='||', edgecolor='red')









x = []

for i in range(0, 100, 5):
    x.append(i)

plt.yticks(x)
plt.show()
