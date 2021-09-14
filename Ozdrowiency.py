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

suma_ozdrowialych = Dane.suma_ozdrowialych

ozdrowiency_w_pop = suma_ozdrowialych/38244000

dziennie_wyzdrowien = [0]
for i in range(1, len(suma_ozdrowialych)):
    dzienne = suma_ozdrowialych[i] - suma_ozdrowialych[i-1]
    dziennie_wyzdrowien.append(dzienne)



print('RAPORT OZDROWIEŃCÓW Z OSTATNICH 8 DNI:')
d = {'data':dzien, 'liczba osób wyzdrowiałych':dziennie_wyzdrowien,
     'łączna liczba wyzdrowiałych':suma_ozdrowialych, 'udział ozdrowieńców w populacji[%]':np.round(ozdrowiency_w_pop*100,2)}



raport_ozdrowiency = pd.DataFrame(data=d)

raport_ozdrowiency = raport_ozdrowiency.set_index(raport_ozdrowiency.columns[0])
print(raport_ozdrowiency[-8:])


fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien[134:], dziennie_wyzdrowien[134:], color='c',label='Wyzdrowień dziennie')
plt.ylabel('Liczba wyzdrowień', size=15)
ax2 = ax.twinx()
plt.plot(dzien[134:], ozdrowiency_w_pop[134:]*100, color='r', label='Ozdrowieńcy w populacji')
plt.ylabel('Ozdrowieńcy w populacji [%]', size=15)
plt.title('Ozdrowieńcy', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Ozdrowiency.svg")

