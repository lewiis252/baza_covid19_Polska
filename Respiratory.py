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

zajete_respiratory = Dane.zajete_respiratory

wolne_respiratory = Dane.wolne_respiratory

procent_zajetych_respiratorow = (zajete_respiratory)/(wolne_respiratory)

dzienne_zmiana_zajetych_respiratorow = [0]
for i in range(1, len(zajete_respiratory)):
    dzienne = zajete_respiratory[i] - zajete_respiratory[i-1]
    dzienne_zmiana_zajetych_respiratorow.append(dzienne)

dzienne_zmiana_zajetych_respiratorow = np.array(dzienne_zmiana_zajetych_respiratorow)

srednia_7_dniowa_zajetych_respiratorow = []
for i in range(0, len(zajete_respiratory)):
    nowa_dana = np.mean(zajete_respiratory[i-6:i+1])

    srednia_7_dniowa_zajetych_respiratorow.append(nowa_dana)

srednia_7_dniowa_zajetych_respiratorow = np.array(srednia_7_dniowa_zajetych_respiratorow)

srednia_7_dniowa_zmiany_zajetych_respiratorow = []
for i in range(0, len(dzienne_zmiana_zajetych_respiratorow)):
    nowa_dana = np.mean(dzienne_zmiana_zajetych_respiratorow[i-6:i+1])

    srednia_7_dniowa_zmiany_zajetych_respiratorow.append(nowa_dana)

srednia_7_dniowa_zmiany_zajetych_respiratorow = np.array(srednia_7_dniowa_zmiany_zajetych_respiratorow)


print('RAPORT RESPIRATORÓW Z OSTATNICH 8 DNI:')
d = {'data':dzien[234:], 'zajęte respiratory':zajete_respiratory,
     'wolne respiratory':wolne_respiratory, 'zmiana zajętych respiratorów d/d':dzienne_zmiana_zajetych_respiratorow,
     'średnia 7-dniowa zmiana zajętych respiratorów': np.round(srednia_7_dniowa_zmiany_zajetych_respiratorow),
     'zajęte respiratory[%]':np.round(procent_zajetych_respiratorow*100,2),
     'średnia 7-dniowa zajętych respiratorów': np.round(srednia_7_dniowa_zajetych_respiratorow,2)}



raport_respiratorow = pd.DataFrame(data=d)


raport_respiratorow = raport_respiratorow.set_index(raport_respiratorow.columns[0])
print(raport_respiratorow[-8:])

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien[234:], zajete_respiratory, color='c',label='Zajęte respiratory')
plt.plot(dzien[234:], wolne_respiratory, color='b',label='Wolne respiratory')
plt.ylabel('Liczba respiratorów', size=15)
ax2 = ax.twinx()
plt.plot(dzien[234:], procent_zajetych_respiratorow*100, color='r', label='Zajęte respiratory [%]')
plt.ylabel('Zajęte respiratory [%]', size=15)
plt.title('Respiratory', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Respiratory.svg")


