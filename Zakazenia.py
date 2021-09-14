import matplotlib.pyplot as plt
import seaborn as sb
sb.set()
import numpy as np
import pandas as pd
from datetime import date
import Dane


print('Tworzenie raportu. Proszę czekać.')
print("...\n")
start_date = date(2020,3,3)
end_date = date(2021,6,3)

dzien = pd.date_range(start_date, end_date)
dzien = np.array(dzien)

zakazenia = Dane.zakazenia

sr_7_dni = [0,0,0,0,0]
for i in range(5, len(zakazenia)):
    nowa_dana = np.mean(zakazenia[i-6:i+1])

    sr_7_dni.append(nowa_dana)

srednia_7_dniowa_zakazen = np.array(sr_7_dni)


wzrost_proc_tt = [0,0,0,0,0]
for i in range(5,len(zakazenia)):
    if zakazenia[i-7] != 0:
        nowy_proc = (zakazenia[i]-zakazenia[i-7])/zakazenia[i-7]
    else: nowy_proc = np.NaN

    wzrost_proc_tt.append(nowy_proc)

wzrost_proc_tt = np.array(wzrost_proc_tt)



sredni_wzrost_proc_tt = [0,0,0,0,0]
for i in range(5, len(zakazenia)):
    nowa_dana = np.mean(wzrost_proc_tt[i-6:i+1])

    sredni_wzrost_proc_tt.append(nowa_dana)

sredni_wzrost_proc_tt = np.array(sredni_wzrost_proc_tt)

wzrost_proc_tt = wzrost_proc_tt * 100
sredni_wzrost_proc_tt = sredni_wzrost_proc_tt * 100


print('RAPORT ZAKAŻEŃ Z OSTATNICH 8 DNI:')
d = {'dzień':dzien,
     'nowe przypadki':zakazenia,
     'średnia tygodniowa zakażeń':np.round(srednia_7_dniowa_zakazen,0),
     'wzrost procentowy t/t[%]':np.round(wzrost_proc_tt,2),
     'średni wzrost procentowy t/t[%]': np.round(sredni_wzrost_proc_tt,2)}




raport_zakazen = pd.DataFrame(data=d)
raport_zakazen = raport_zakazen.set_index(raport_zakazen.columns[0])
print(raport_zakazen[-8:])


fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)
ax.bar(dzien[182:], zakazenia[182:], color='c',label='Zakażenia')
ax.set_ylabel('Liczba nowych zakażeń', size=15)
ax2 = ax.twinx()
ax2.plot(dzien[182:], wzrost_proc_tt[182:], color='r', label='Wzrost procentowy t/t [%]')
ax2.set_ylabel('Wzrost t/t [%]', size=15)
plt.title('Zakażenia dziennie', size=15)
fig.legend(loc='lower center', ncol=2)
plt.savefig("raport\Zakażenia_dziennie.svg")

fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)
ax.bar(dzien[182:], srednia_7_dniowa_zakazen[182:], color='c',label='Średnia 7-dniowa zakażeń')
ax.set_ylabel('Średnia tygodniowa liczba nowych zakażeń', size=15)
ax2 = ax.twinx()
ax2.plot(dzien[182:], sredni_wzrost_proc_tt[182:], color='r', label='Średni tygodniowy wzrost [%]')
ax2.set_ylabel('Średni tygodniowy wzrost [%]', size=15)
plt.title('Średnia tygodniowa zakażeń', size=20)
fig.legend(loc="lower center", ncol=2)
plt.savefig("raport\Zakażenia_dziennie_średnia_7_dniowa.svg")






