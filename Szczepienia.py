import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date
import Dane
import seaborn as sb
sb.set()

print("...\n")
start_date = date(2020,12,28)
end_date = date.today()
end_date = date(2021,6,3)
dzien = pd.date_range(start_date, end_date)

suma_szczepien_I_dawka = Dane.suma_szczepien_I_dawka
suma_szczepien_II_dawka = Dane.suma_szczepien_II_dawka
suma_szczepien = Dane.suma_szczepien

dzienne_szczepienie_I_dawka = [3853]
for i in range(1, len(suma_szczepien_I_dawka)):
    dzienne = suma_szczepien_I_dawka[i] - suma_szczepien_I_dawka[i-1]
    dzienne_szczepienie_I_dawka.append(dzienne)

dzienne_szczepienie_I_dawka = np.array(dzienne_szczepienie_I_dawka)

dzienne_szczepienie_II_dawka = [0]
for i in range(1, len(suma_szczepien_II_dawka)):
    dzienne = suma_szczepien_II_dawka[i] - suma_szczepien_II_dawka[i-1]
    dzienne_szczepienie_II_dawka.append(dzienne)

dzienne_szczepienie_II_dawka = np.array(dzienne_szczepienie_II_dawka)

dzienne_szczepienie = [3853]
for i in range(1, len(suma_szczepien)):
    dzienne = suma_szczepien[i] - suma_szczepien[i-1]
    dzienne_szczepienie.append(dzienne)

dzienne_szczepienie = np.array(dzienne_szczepienie)

procent_populacji_I_dawka = suma_szczepien_I_dawka/38244000
procent_populacji_II_dawka = suma_szczepien_II_dawka/38244000

srednia_7_dniowa_szczepien = []
for i in range(0, len(dzienne_szczepienie)):
    nowa_dana = np.mean(dzienne_szczepienie[i-6:i+1])

    srednia_7_dniowa_szczepien.append(nowa_dana)

srednia_7_dniowa_szczepien = np.array(srednia_7_dniowa_szczepien)


print('RAPORT SZCZEPIEŃ Z OSTATNICH 8 DNI:')
d = {'data':dzien, 'szczepienia wykonane w ciągu doby':dzienne_szczepienie,
     'szczepienia I dawką w ciągu doby':dzienne_szczepienie_I_dawka,
     'zaszczepeni w pełni w ciągu doby':dzienne_szczepienie_II_dawka,
     'łączna liczba liczba szczepień':suma_szczepien,
     'zaszczepieni I dawką':suma_szczepien_I_dawka,
     'w pełni zaszczepieni':suma_szczepien_II_dawka,
     'populacja zaszczepiona I dawką[%]':np.round(procent_populacji_I_dawka*100,2),
     'populacja  w pełni zaszczepiona[%]':np.round(procent_populacji_II_dawka*100,2)}


raport_szczepienia = pd.DataFrame(data=d)
raport_szczepienia = raport_szczepienia.set_index(raport_szczepienia.columns[0])
print(raport_szczepienia[-8:])

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien, dzienne_szczepienie, color='y',label='Dzienna liczba szczepień')
plt.ylabel('Liczba szczepień', size=15)
ax2 = ax.twinx()
plt.plot(dzien, procent_populacji_I_dawka*100, color='b',label='Zaszczepieni I dawką [%]')
plt.plot(dzien, procent_populacji_II_dawka*100, color='r', label='W pełni zaszczepieni [%]')
plt.ylabel('Populacja zaszczepiona [%]', size=15)
plt.title('Szczepienia', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Szczepienia.svg")

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien, srednia_7_dniowa_szczepien, color='y',label='Średnia 7-dniowa liczba szczepień')
plt.ylabel('Liczba szczepień', size=15)
ax2 = ax.twinx()
plt.plot(dzien, procent_populacji_I_dawka*100, color='b',label='Zaszczepieni I dawką [%]')
plt.plot(dzien, procent_populacji_II_dawka*100, color='r', label='W pełni zaszczepieni [%]')
plt.ylabel('Populacja zaszczepiona [%]', size=15)
plt.title('Szczepienia', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Szczepienia_średnia_7_dniowa.svg")





