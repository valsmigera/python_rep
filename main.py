import csv
from typing import List

filename = "log.csv"

descriptor = list()
kolvo_valuta = list()
data_vr = list()
tip_v = list()
tabl_val = ['des', 0, 0, 0, 0, 0, 0, 0, 0, 0]
result_list = list()
valuti = ('Аккаунт', 'Влияние', 'Темные дары', 'Самоцветы', 'Замороженные сокровища', 'Украшения фэйри', 'Сокровища Тирании', 'Героический осколок могущества', 'Осколок могущества странника', 'Осколок могущества завоевателя')

with open("log.csv", "r", encoding='utf8', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        descriptor.append(row[1])
        kolvo_valuta.append(row[6])
        tip_v.append(row[5])
        data_vr.append(row[2])
un_descr = list(set(descriptor))
un_descr.remove('Account Handle')
un_descr.remove('')
for a in range(0, len(un_descr)):
    tabl_val[0] = un_descr[a]
    for b in range(0, len(descriptor)):
        if un_descr[a] == descriptor[b]:
            if tip_v[b] == 'Влияние':
                tabl_val[1] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Темные дары':
                tabl_val[2] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Самоцветы':
                tabl_val[3] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Замороженные сокровища':
                tabl_val[4] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Украшения фэйри':
                tabl_val[5] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Сокровища Тирании':
                tabl_val[6] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Героический осколок могущества':
                tabl_val[7] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Осколок могущества странника':
                tabl_val[8] += int(kolvo_valuta[b])
            elif tip_v[b] == 'Осколок могущества завоевателя':
                tabl_val[9] += int(kolvo_valuta[b])
            else:
                continue
        elif b == len(descriptor) - 1:
            result_list.append(tabl_val)
            tabl_val = ['des', 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            continue
myFile = open('result.csv', 'w', encoding='utf8', newline="")
writer = csv.writer(myFile)
with myFile:
    writer.writerow(valuti)
    for c in range(0, len(result_list)):
        writer.writerow(result_list[c])