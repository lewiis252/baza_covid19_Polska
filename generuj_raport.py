import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import Zakazenia
import Zgony
import Testy
import Hospitalizacja
import Respiratory
import Kwarantanna
import Ozdrowiency
import Szczepienia
import seaborn as sb
sb.set()


print('Tworzenie raportu.')
print('...')

fig, ax = plt.subplots(figsize=(20,8))
plt.plot(Zakazenia.dzien[234:], (np.log(Zakazenia.srednia_7_dniowa_zakazen[234:])), color='c',label='Zakażenia średnia 7-dniowa')
plt.plot(Zakazenia.dzien[234:], (np.log(Zgony.srednia_7_dniowa_zgonow[234:])), color='b',label='Zgony średnia 7-dniowa')
plt.plot(Zakazenia.dzien[234:], (np.log(Hospitalizacja.zajete_lozka)), color='r',label='Zajęte łóżka')
plt.plot(Zakazenia.dzien[234:], (np.log(Respiratory.zajete_respiratory)), color='g',label='Zajęte respiraotry')
plt.title('Zakażenia,zgony,hospitalizacja,respiratory (skala logarytmiczna)', size=20)
fig.legend(loc='lower center', ncol=4)
plt.savefig("raport\Zakażenia,zgony,hospitalizacja,respiratory.svg")

fig, ax = plt.subplots(figsize=(20,8))
plt.plot(Zakazenia.dzien[234:], (np.log(Zakazenia.srednia_7_dniowa_zakazen[234:])), color='c',label='Zakażenia średnia 7-dniowa')
plt.plot(Zakazenia.dzien[234:], (np.log(Testy.srednia_7dniowa_zlecen_POZ[234:])), color='b',label='Zlecenia POZ średnia 7-dniowa')
plt.plot(Zakazenia.dzien[234:], (np.log(Hospitalizacja.zajete_lozka)), color='r',label='Zajęte łóżka')
plt.plot(Zakazenia.dzien[234:], (np.log(Respiratory.zajete_respiratory)), color='g',label='Zajęte respiraotry')
plt.title('Zakażenia,zgony,hospitalizacja,respiratory (skala logarytmiczna)', size=20)
fig.legend(loc='lower center', ncol=4)
plt.savefig("raport\Zakażenia,zlecenia POZ,hospitalizacja,respiratory.svg")

fig, ax = plt.subplots(figsize=(20,8))
plt.plot(Zakazenia.dzien[234:], (Zgony.srednia_7_dniowa_zgonow[234:]), color='b',label='Zgony ')
plt.plot(Zakazenia.dzien[234:], (Respiratory.srednia_7_dniowa_zmiany_zajetych_respiratorow), color='g',label='Zmiana zajętych respiraotorów')
plt.title('Zgony i respiratory', size=20)
fig.legend(loc='lower center', ncol=4)
plt.savefig("raport\Zgony i respiratory.svg")

Zakazenia.raport_zakazen.to_excel("raport\Raport_covid19.xlsx",
             sheet_name='Zakażenia')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Zgony.raport_zgonow.to_excel(writer, sheet_name='Zgony')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Hospitalizacja.raport_hospitalizacji.to_excel(writer, sheet_name='Hospitalizacja')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Respiratory.raport_respiratorow.to_excel(writer, sheet_name='Respiratory')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Testy.raport_testow.to_excel(writer, sheet_name='Testy')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Kwarantanna.raport_kwarantanna.to_excel(writer, sheet_name='Kwarantanna')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Ozdrowiency.raport_ozdrowiency.to_excel(writer, sheet_name='Ozdrowieńcy')

with pd.ExcelWriter('raport\Raport_covid19.xlsx',
                    mode='a') as writer:
    Szczepienia.raport_szczepienia.to_excel(writer, sheet_name='Szczepienia')


raport_dnia = [
('Dane na dzień ' + str(date.today()) + ':'),
('Nowych zakażeń: ' + str(Zakazenia.zakazenia[-1]) + ', zmiana t/t: ' + str(np.round(Zakazenia.wzrost_proc_tt[-1],2)) + ' %.'),
('Zgony: ' + str(Zgony.zgony[-1]) + ', łącznie ' + str(Zgony.zgony_lacznie[-1]) + ' zgonów od początku trwania pandemii.'),
('Zajęte łóżka: ' + str(Hospitalizacja.zajete_lozka[-1]) + ' zmiana d/d: ' + str(Hospitalizacja.zmiana_hospitalizacji_dd[-1]) + '.'),
('Zajęte respiratory: ' + str(Respiratory.zajete_respiratory[-1]) + ' zmiana d/d: ' + str(Respiratory.dzienne_zmiana_zajetych_respiratorow[-1]) + '.'),
('Wykonane testy: ' + str(Testy.testy[-1]) + ', pozytywnych: ' + str(np.round(Testy.procent_dobowy_testow_pozytywnych[-1]*100,2)) + ' %.'),
('Udział testów antygenowych: ' + str(Testy.dobowy_procent_testow_antygenowych[-1]) + '%.'),
('Zlecenia POZ: ' + str(Testy.dziennie_zlecenia_POZ[-1]) + ',') + ' zlecenia POZ tydzień temu:' + str(Testy.dziennie_zlecenia_POZ[-7]),
('Wyzdrowiali: ' + str(Ozdrowiency.dziennie_wyzdrowien[-1]) + ', udział ozdrowieńców w populacji: ' + str(np.round(Ozdrowiency.ozdrowiency_w_pop[-1]*100,2)) + ' %.'),
('Osoby na kwarantannie: ' + str(Kwarantanna.liczba_osob_na_kwarantannie[-1]) + ', dzienna zmiana osób na kwarantannie: ' + str(Kwarantanna.zmiana_kwarantanny_dd[-1]) + '.'),
('Wykonanych szczepień: ' + str(Szczepienia.dzienne_szczepienie[-1]) + ', populacja zaszczepiona I dawką: '
      + str(np.round((Szczepienia.procent_populacji_I_dawka[-1]*100),2)) + ' %, populacja w pełni zaszczepiona: ' +
      str(np.round((Szczepienia.procent_populacji_II_dawka[-1]*100),2)) + ' %.')]

with open("raport\dzienny_raport.txt", "w") as output:
    output.write('')

for i in range(0, len(raport_dnia)):
    with open("raport\dzienny_raport.txt", "a") as output:
        output.write(str(raport_dnia[i] + '\n'))




a = input('Generowanie raportu zakończone. Wykresy i raport zostały zapisane w folderze "raport". Wciśnij enter aby wyjść.')