import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date
import Dane
import seaborn as sb
sb.set()

print("...\n")
start_date = date(2020,3,3)
end_date = date.today()
end_date = date(2021,6,3)

dzien = pd.date_range(start_date, end_date)

zgony = Dane.zgony

sr_7_dni = [0,0,0,0,0]
for i in range(5, len(zgony)):
    nowa_dana = np.mean(zgony[i-6:i+1])


    sr_7_dni.append(nowa_dana)

srednia_7_dniowa_zgonow = np.array(sr_7_dni)


zgony_lacznie = [0]

for i in range(1, len(zgony)):
    nowa_suma = zgony[i] + zgony_lacznie[i-1]
    zgony_lacznie.append(nowa_suma)

zgony_lacznie = np.array(zgony_lacznie)




print('RAPORT ZGONÓW Z OSTATNICH 8 DNI:')
d = {'data':dzien, 'nowe zgony':zgony, 'średnia tygodniowa zgonów':np.round(srednia_7_dniowa_zgonow,0),
     'zgony łącznie':zgony_lacznie}



raport_zgonow = pd.DataFrame(data=d)
raport_zgonow = raport_zgonow.set_index(raport_zgonow.columns[0])
print(raport_zgonow[-8:])


fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien, zgony, color='c',label='Liczba zgonów')
plt.ylabel('Zgony', size=15)
ax2 = ax.twinx()
plt.plot(dzien, zgony_lacznie, color='r', label='Zgony łącznie')
plt.ylabel('Zgony łącznie', size=15)
plt.title('Zgony', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Zgony.svg")

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien, srednia_7_dniowa_zgonow, color='c',label='Liczba zgonów średnia 7-dniowa')
plt.ylabel('Zgony', size=15)
ax2 = ax.twinx()
plt.plot(dzien, zgony_lacznie, color='r', label='Zgony łącznie')
plt.ylabel('Zgony łącznie', size=15)
plt.title('Zgony', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Zgony średnia 7-dniowa.svg")
