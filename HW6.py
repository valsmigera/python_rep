import csv
import fileinput
import random
import names
import datetime
import time


digits_file = open('digits.csv', 'w', newline="")    # 1.1
writer = csv.writer(digits_file)
for i in range(150):
    task_1_1 = random.randint(0, 150)
    task_1_1 = str(task_1_1)
    writer.writerow([task_1_1])

names_file_1 = open('names.csv', 'w', newline="")     # 1.2
writer = csv.writer(names_file_1)
for i in range(100):
    task_1_2 = names.get_full_name()
    writer.writerow([task_1_2])

email_file_1 = open('emails.csv', 'w', newline="")     # 1.3
writer = csv.writer(email_file_1)
for i in range(100):
    task_1_3 = 'name' + str(i) + 'gmail.com'
    writer.writerow([task_1_3])

nne_file_1 = open('nne.csv', 'w', newline="")     # 1.4
writer = csv.writer(nne_file_1)
for i in range(100):
    task_1_4_1 = random.randint(0, 150)
    task_1_4_1 = str(task_1_4_1)
    task_1_4_2 = names.get_full_name()
    task_1_4_3 = task_1_4_2 + 'gmail.com'
    writer.writerow([task_1_4_1, task_1_4_2, task_1_4_3])

digits_2_list = list()    # 2.1
for i in range(300):
    task_2_1 = random.randint(10, 310)
    task_2_1 = str(task_2_1)
    digits_2_list.append(task_2_1)

digits_file_2 = open('digits_2.csv', 'w', newline="")
writer = csv.writer(digits_file_2)
with digits_file_2:
    writer.writerow(['number'])
    for i in digits_2_list:
        writer.writerow([i])

names_2_list = list()     # 2.2
for i in range(400):
    task_2_2 = names.get_full_name()
    names_2_list.append(task_2_2)

names_file_2 = open('names_2.csv', 'w', newline="")
writer = csv.writer(names_file_2)
with names_file_2:
    writer.writerow(['name'])
    for i in names_2_list:
        writer.writerow([i])

emails_2_list = list()     # 2.3
for i in range(400):
    task_2_3 = 'Pochta' + str(i) + '@gmail.com'
    emails_2_list.append(task_2_3)

emails_file_2 = open('emails_2.csv', 'w', newline="")
writer = csv.writer(emails_file_2)
with emails_file_2:
    writer.writerow(['email'])
    for i in emails_2_list:
        writer.writerow([i])

nne_2_list = list()       # 2.4
nne_2_2_list = list()
for i in range(450):
    number_var = random.randint(10, 310)
    number_var = str(number_var)
    names_var = names.get_full_name()
    email_var = names_var + '@gmail.com'
    nne_2_2_list.extend([number_var, names_var, email_var])
    nne_2_list.append(nne_2_2_list)
    nne_2_2_list = list()

nne_2_file = open('nne_2.csv', 'w', newline="")
writer = csv.writer(nne_2_file)
with nne_2_file:
    writer.writerow(['number', 'name', 'Email'])
    for i in nne_2_list:
        writer.writerow(i)


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

date_list = ['Date']
for i in range(50):     # a
    task_a = random_date("1/1/1980 12:00 AM", "1/1/1990 12:00 AM", random.random())
    date_list.append(task_a)
for i in range(100):    # b
    task_b = random_date("1/1/1991 12:00 AM", "1/1/2000 12:00 AM", random.random())
    date_list.append(task_b)
for i in range(150):    # c
    task_c = random_date("1/1/2001 12:00 AM", "1/1/2010 12:00 AM", random.random())
    date_list.append(task_c)
for i in range(150):    # d
    task_d = random_date("1/1/2011 12:00 AM", "1/1/2021 12:00 AM", random.random())
    date_list.append(task_d)


nne_2_temp_list_1 = list()
nne_2_temp_list_2 = list()
a = 0

with open('nne_2.csv', 'r', newline='') as f:   # a
    reader = csv.reader(f)
    for row in reader:
        nne_2_temp_list_1.extend(row + [date_list[a]])
        nne_2_temp_list_2.append(nne_2_temp_list_1)
        a += 1
        nne_2_temp_list_1 = list()
print(nne_2_temp_list_2)

nne_2_file = open('nne_2.csv', 'w', newline="")
writer = csv.writer(nne_2_file)
with nne_2_file:
    for i in nne_2_temp_list_2:
        writer.writerow(i)

names_list_4 = list()
name_and_date_list_4_1 = list()
name_and_date_list_4_2 = list()

with open('nne_2.csv', 'r', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        names_list_4.append(row[1])
        name_and_date_list_4_1.extend([row[1], row[3]])
        name_and_date_list_4_2.append(name_and_date_list_4_1)
        name_and_date_list_4_1 = list()

name_and_date_list_4_2[0].remove('name')
name_and_date_list_4_2[0].remove('Date')
names_list_4.remove('name')

for i in range(550):    # b
    name_get = names.get_full_name()
    names_list_4.append(name_get)

names_list_4.sort()     # c
email_list_4 = list()
phone_list_4 = list()
gender_list_4 = list()
salary_list_4 = list()
date_list_4 = list()

for i in range(1000):   # d
    mail_var = 'Mail' + str(i) + 'gmail.com'
    email_list_4.append(mail_var)
for i in range(1000):
    rand_var = random.randint(100000, 999999)
    phone_list_4.append(rand_var)
for i in range(1000):
    gender_var = random.randint(1, 2)
    if gender_var == 1:
        gender_list_4.append('Male')
    else:
        gender_list_4.append('Female')
for i in range(1000):
    salary_var = random.randint(1000, 5000)
    salary_list_4.append(salary_var)
for i in range(1000):
    date_var = "Data_net"
    date_list_4.append(date_var)
combo_list_4_1 = list()
combo_list_4_2 = list()


for i in range(0, 1000):   # e
    combo_list_4_1.extend([names_list_4[i], date_list_4[i], email_list_4[i], phone_list_4[i], gender_list_4[i]])
    combo_list_4_2.append(combo_list_4_1)
    combo_list_4_1 = list()

combo_list_1 = list()
combo_list_2 = list()


for i in range(0, len(combo_list_4_2)):
    for a in range(1, len(name_and_date_list_4_2)):
        if combo_list_4_2[i][0] == name_and_date_list_4_2[a][0]:
            combo_list_4_2[i][1] = name_and_date_list_4_2[a][1]

for i in range(0, len(combo_list_4_2)):
    for a in range(1, len(name_and_date_list_4_2)):
        if combo_list_4_2[i][1] == 'Data_net':
            combo_list_4_2[i][1] = random_date("1/1/1980 12:00 AM", "1/1/2020 12:00 AM", random.random())


combo_file_2 = open('combo.csv', 'w', newline="")   # f
writer = csv.writer(combo_file_2)
with combo_file_2:
    writer.writerow(['name', 'date', 'email', 'phone', 'gender'])
    for i in combo_list_4_2:
        writer.writerow(i)