import numpy as np
from datetime import date
import pandas as pd

df1 = pd.read_excel('Dane_covid19.xlsx', sheet_name='Zakażenia', engine='openpyxl')

df2 = pd.read_excel('Dane_covid19.xlsx', sheet_name='Hospitalizacja', engine='openpyxl')

df3 = pd.read_excel('Dane_covid19.xlsx', sheet_name='Szczepienia', engine='openpyxl')



zakazenia = np.array(df1['nowe przypadki'])
zgony = np.array(df1['nowe zgony'])
testy = np.array(df1['wykonane testy'])
testy_antygenowe = np.array((df1['dzienna liczba testów antygenowych']))
liczba_osob_na_kwarantannie = np.array(df1['liczba osób na kwarantannie'])
suma_ozdrowialych = np.array(df1['liczba osób wyzdrowiałych'])
zajete_lozka = np.array(df2['zajęte łóżka'])
wolne_lozka = np.array(df2['dostępne łóżka'])
zajete_respiratory = np.array(df2['zajęte respiratory'])
wolne_respiratory = np.array(df2['dostępne respiratory'])
suma_zlecen_POZ = np.array(df1['suma zleceń POZ'])
suma_szczepien_I_dawka = np.array(df3['szczepienia I dawką'])
suma_szczepien_II_dawka = np.array(df3['szczepienia II dawką'])
suma_szczepien = np.array(df3['suma wykonanych szczepień'])
