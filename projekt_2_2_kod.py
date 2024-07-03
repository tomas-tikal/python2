
"""
projekt_2_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomas TIKAL
email: tikal@3t.cz
discord: ti_to_80805
"""
import projekt_2_2_knihovna

# zadání velikosti čtvercového hracího pole (šachovnice), včetně validace vstupu
while True:
    velikost_sachovnice = input("Zadej velikost strany šachového pole pro hru: ")
    if (not velikost_sachovnice.isdecimal()):
        print('\"Velikost strany\" musí být CELÉ KLADNÉ číslo, větší než 2 (min. 3), zkus to znova :)')
        continue
    else:
        if(int(velikost_sachovnice) <= 2):
            print('\"Velikost strany\" musí být CELÉ KLADNÉ číslo, větší než 2 (min. 3), zkus to znova :)')
            continue
        else:
            break
    break

# zadání počtu prvků v jednom směru, nutného k výhře, včetně validace vstupu
while True:
    print("Zadej počet sousedních polí se stejným znakem, nutných pro výhru.")
    pocet_poli = input("číslo musí být min. 2 a maximálně hodnota velikosti šachového pole: ")
    if(not pocet_poli.isdecimal()):
        print('\"Počet sousedních polí\" musí být CELÉ KLADNÉ číslo, zkus to znova :)')
        continue
    if(not ((int(pocet_poli) >= 2) and (int(pocet_poli) <= int(velikost_sachovnice)))):
        print('\"Počet sousedních polí\" musí být mezi hodnotami 2 a', velikost_sachovnice,  'zkus to znova :)')
        continue
    break

# naplnění prázdného hracího pole (šachovnice)
sachovnice= []
for j in range(int(velikost_sachovnice)):
    sloupecek= []
    for i in range(int(velikost_sachovnice)):
        retezec = str(j)+'.'+str(i)
        sloupecek.append(retezec)
    sachovnice.append(sloupecek)

# pomocná proměnná existujících indexů v hracím poli (šachovnici)
pole_num = []
for j in range(int(velikost_sachovnice)):
    for i in range(int(velikost_sachovnice)):
        souradnice = str(j)+str(i)
        pole_num.append(int(souradnice))

# výpis prázdné šachovnice
projekt_2_2_knihovna.vypis_sachovnice(sachovnice, velikost_sachovnice)

while True:
    radek, sloupec = projekt_2_2_knihovna.vstup(sachovnice, 'X', velikost_sachovnice)
    sachovnice[int(radek)][int(sloupec)] = '.X.'
    projekt_2_2_knihovna.vypis_sachovnice(sachovnice, velikost_sachovnice)
    projekt_2_2_knihovna.kontrola_souseda(sachovnice, radek, sloupec, '.X.', pole_num, pocet_poli, velikost_sachovnice)
    radek, sloupec = projekt_2_2_knihovna.vstup(sachovnice, 'O', velikost_sachovnice)
    sachovnice[int(radek)][int(sloupec)] = '.O.'
    projekt_2_2_knihovna.vypis_sachovnice(sachovnice, velikost_sachovnice)
    projekt_2_2_knihovna.kontrola_souseda(sachovnice, radek, sloupec, '.O.', pole_num, pocet_poli, velikost_sachovnice)


















