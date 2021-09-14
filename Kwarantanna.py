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

liczba_osob_na_kwarantannie = Dane.liczba_osob_na_kwarantannie

zmiana_kwarantanny_dd = [0]

for i in range(1, len(liczba_osob_na_kwarantannie)):
    nowe_zajete = liczba_osob_na_kwarantannie[i] - liczba_osob_na_kwarantannie[i-1]
    zmiana_kwarantanny_dd.append(nowe_zajete)

zmiana_hospitalizacji_dd = np.array(zmiana_kwarantanny_dd)



print('RAPORT KWARANTANNY Z OSTATNICH 8 DNI:')
d = {'data':dzien,
     'liczba osób na kwarantannie':liczba_osob_na_kwarantannie,
     'dzienna zmiana osób na kwarantannie': zmiana_kwarantanny_dd}




raport_kwarantanna = pd.DataFrame(data=d)

raport_kwarantanna = raport_kwarantanna.set_index(raport_kwarantanna.columns[0])
print(raport_kwarantanna[-8:])


plt.figure(10)
kwarantanna_wykres_1 = plt.bar(dzien, liczba_osob_na_kwarantannie)
plt.title('Liczba osób na kwarantannie')
plt.savefig("raport\Liczba_osób_na_kwarantannie.svg")

