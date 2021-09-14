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

zajete_lozka = Dane.zajete_lozka

wolne_lozka = Dane.wolne_lozka

procent_zajetych_lozek = zajete_lozka/wolne_lozka
procent_zajetych_lozek = np.array(procent_zajetych_lozek)

zmiana_hospitalizacji_dd = [0]
for i in range(1, len(zajete_lozka)):
    nowe_zajete = zajete_lozka[i] - zajete_lozka[i-1]
    zmiana_hospitalizacji_dd.append(nowe_zajete)

zmiana_hospitalizacji_dd = np.array(zmiana_hospitalizacji_dd)

srednia_7_dniowa_zajetych_lozek = []
for i in range(0, len(zajete_lozka)):
    nowa_dana = np.mean(zajete_lozka[i-6:i+1])

    srednia_7_dniowa_zajetych_lozek.append(nowa_dana)

srednia_7_dniowa_zajetych_lozek = np.array(srednia_7_dniowa_zajetych_lozek)

srednia_7_dniowa_przyrostu_zajetych_lozek = []
for i in range(0, len(zmiana_hospitalizacji_dd)):
    nowa_dana = np.mean(zmiana_hospitalizacji_dd[i-6:i+1])
    srednia_7_dniowa_przyrostu_zajetych_lozek.append(nowa_dana)

srednia_7_dniowa_przyrostu_zajetych_lozek = np.array(srednia_7_dniowa_przyrostu_zajetych_lozek)





print('RAPORT HOSPITALIZACJI Z OSTATNICH 8 DNI:')
d = {'data':dzien[234:], 'zajęte łóżka':zajete_lozka, 'wolne łóżka':wolne_lozka,
     'zmiana hospotalizacji d/d':zmiana_hospitalizacji_dd,
     'średnia 7-dniowa przyrostu zajętych łóżek': np.round(srednia_7_dniowa_przyrostu_zajetych_lozek),
     'zajęte łóżka[%]':np.round(procent_zajetych_lozek*100, 2),
     'średnia 7 dniowa zajętych łóżek': np.round(srednia_7_dniowa_zajetych_lozek, 0),
     }



raport_hospitalizacji = pd.DataFrame(data=d)


raport_hospitalizacji = raport_hospitalizacji.set_index(raport_hospitalizacji.columns[0])
print(raport_hospitalizacji[-8:])

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien[234:], zajete_lozka, color='c',label='Zajęte łóżka')
plt.plot(dzien[234:], wolne_lozka, color='b',label='Wolne łóżka')
plt.ylabel('Liczba łóżek', size=15)
ax2 = ax.twinx()
plt.plot(dzien[234:], procent_zajetych_lozek*100, color='r', label='Zajęte łóżka [%]')
plt.ylabel('Zajęte łóżka [%]', size=15)
plt.title('Hospitalizacja', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Hospitalizacja.svg")






