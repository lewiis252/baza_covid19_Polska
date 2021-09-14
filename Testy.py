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

testy = Dane.testy
testy_antygenowe = Dane.testy_antygenowe

procent_dobowy_testow_pozytywnych = Dane.zakazenia/testy
procent_dobowy_testow_pozytywnych = np.array(procent_dobowy_testow_pozytywnych)

suma_zlecen_POZ = Dane.suma_zlecen_POZ

dziennie_zlecenia_POZ = [0]
for i in range(1, len(suma_zlecen_POZ)):
    dzienne = suma_zlecen_POZ[i] - suma_zlecen_POZ[i-1]
    dziennie_zlecenia_POZ.append(dzienne)

dziennie_zlecenia_POZ = np.array(dziennie_zlecenia_POZ)

srednia_7dniowa_zlecen_POZ = [0,0,0,0,0]
for i in range(5, len(dziennie_zlecenia_POZ)):
    nowa_dana = np.mean(dziennie_zlecenia_POZ[i-6:i+1])

    srednia_7dniowa_zlecen_POZ.append(nowa_dana)

srednia_7dniowa_zlecen_POZ = np.array(srednia_7dniowa_zlecen_POZ)

dobowy_procent_testow_antygenowych = np.array(testy_antygenowe/testy)
dobowy_procent_testow_antygenowych = np.round(dobowy_procent_testow_antygenowych*100)

print('RAPORT TESTÓW Z OSTATNICH 8 DNI:')
d = {'data':dzien, 'wykonane testy':testy, 'procent pozytywnych':procent_dobowy_testow_pozytywnych,
     'zlecenia POZ': dziennie_zlecenia_POZ,
     'udział testów antygenowych:': dobowy_procent_testow_antygenowych,
     'średnia 7 dniowa zleceń POZ': np.round(srednia_7dniowa_zlecen_POZ, 2)}



raport_testow = pd.DataFrame(data=d)

raport_testow = raport_testow.set_index(raport_testow.columns[0])
print(raport_testow[-8:])

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien[100:], testy[100:], color='c',label='Wykonane testy')
plt.ylabel('Liczba testów', size=15)
ax2 = ax.twinx()
plt.plot(dzien[100:], procent_dobowy_testow_pozytywnych[100:]*100, color='r', label='Odsetek testów pozytywnych [%]')
plt.ylabel('Testy pozytywne [%]', size=15)
plt.title('Testy', size=20)
fig.legend(loc='lower center', ncol=3)
plt.savefig("raport\Testy.svg")

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien, dziennie_zlecenia_POZ, color='c',label='Zlecenia POZ')
plt.ylabel('Liczba', size=15)
plt.title('Zlecenia POZ', size=20)
fig.legend(loc='lower center', ncol=1)
plt.savefig("raport\Zlecenia_POZ.svg")

fig, ax = plt.subplots(figsize=(20,8))
plt.bar(dzien, srednia_7dniowa_zlecen_POZ, color='c',label='Zlecenia POZ')
plt.ylabel('Liczba', size=15)
plt.title('Zlecenia POZ średnia 7 dniowa', size=20)
fig.legend(loc='lower center', ncol=1)
plt.savefig("raport\Zlecenia_POZ_srednia_7_dniowa.svg")

