from random import *
from OmaModule import *
riik_pealinn={}
pealinn_riik={}
riigid=[]

print(failist_to_dict('riigid_pealinnad.txt'))
a=input('Sisestage riik, mille pealinna soovite teada saada: ')
print(pealinn_riik.get(a))

print(find_capital('riigid_pealinnad.txt'))