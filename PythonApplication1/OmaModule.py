def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        a=input('Sisestage riik, mille pealinna soovite teada saada: ')
        print(pealinn_riik.get(a))
    file.close()
    return riik_pealinn,pealinn_riik,riigid


def find_capital():
    a=input('Sisestage riik, mille pealinna soovite teada saada: ')
    riik_pealinn={}
    print(riik_pealinn.get(a))
