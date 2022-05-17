import random
from random import randrange
import names
from datetime import datetime, timedelta


list_1 = list(range(0,70)) # 1
print(list_1)

list_2 = list() # 2
for i in range (0, 70):
    y = random.randrange(2, 100, 2)
    list_2.append(y)
print(list_2)

list_3 = list() # 3
for i in range (0, 70):
    z = random.randrange(1, 100, 2)
    list_3.append(z)
print(list_3)

def chet_ch(lst):   # 4
    return [x for x in lst if not x % 2]
print(chet_ch(list_1))

def nechet_ch(lst):     # 5
    return [x for x in lst if x % 2]
print(nechet_ch(list_1))

def delen_na_5(lst):     # 6
    return [x for x in lst if not x % 5]
print(delen_na_5(list_1))

def delen_na_5_2(lst):     # 7
    return [x for x in lst if not x % 2 and not x % 5]
print(delen_na_5_2(list_1))

list_4 = [i for i in range(1,71)]   # 8
print(list_4)
a = list_4


def split(arr, size):   #9
   arrs = []
   while len(arr) > size:
      pice = arr[:size]
      arrs.append(pice)
      arr = arr[size:]
   arrs.append(arr)
   return arrs
print(split(list_4, 5))


def hw10(lst):  # 10
    return [x for x in lst if not x % 2], [x for x in lst if x % 2]
print(hw10(list_4))

five_stars = list() # 11
for i in range(0,14):
   hw11 = list(range(1,6))
   five_stars.append(hw11)
print(five_stars)

for i in range(0, len(hw11)): # 12
   a = sum(five_stars[i])
   print(a)

def hw13(lst):    # 13
   for i in range(0, len(lst)):
      if a >= 100:
         return
      elif a < 100:
         return lst
      else:
         print('No lists')
print(hw13(five_stars))

def hw14(age):  # 14
   if age <= 15:
      1200
   elif age >= 16 and age <= 18:
   elif age >=19 and age <= 25:
   elif age >=26 and age <= 35:
   elif age >= 36 and age <= 45:
   elif age >=46 and age >= 70:
   else:


hw16 = list()  # 16
for i in range(0, 70):

   hw16_1 = names.get_full_name()
   hw16.append(hw16_1)
print(hw16)

hw17 = list()  # 17
hw17_1 = 'name_of_file'
for i in range(1, 71):
   hw17_2 = hw17_1+str(i), i
   hw17.append(hw17_2)
print(hw17)

def datetimegenerator(start, end):  # функция для генерации даты
   delta = end - start
   int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
   random_second = randrange(int_delta)
   return start + timedelta(seconds=random_second)
d1 = datetime.strptime('1/1/2005 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

def password_genenerator():
   chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
   password = str()
   length = random.randint(10, 20)
   for i in range(length):
      password += random.choice(chars)
   return password

def namegenerator(gender):
   if gender == 'male':
      random_name = names.get_full_name(gender='male')
   if gender == 'female':
      random_name = names.get_full_name(gender='female')
   else:
      random_name = names.get_full_name()
   return random_name

def logingenerator():
   login_symbol = random.randint(5, 15)
   login = str()
   chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
   for i in range(login_symbol):
      login += random.choice(chars)
   return login

def mailgenerator():
   chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
   email = str()
   email_pre = str()
   email_post = str()
   symbol_email = random.randint(5, 15)
   for i in range(symbol_email):
      email_pre += random.choice(chars)
   if symbol_email % 2:
      email_post = '@mail.ru'
   elif symbol_email % 3:
      email_post = '@gmail.ru'
   else:
      email_post = '@yandex.ru'
   return email_pre + email_post

Employees = list()   # 19
hw19_6 = list()
for i in range(70):
   hw19_1 = namegenerator('Any')
   hw19_2 = logingenerator()
   hw19_3 = password_genenerator()
   hw19_4 = mailgenerator()
   hw19_5 = datetimegenerator(d1, d2)
   hw19_6.extend([hw19_1, hw19_2, hw19_3, hw19_4, hw19_5])
   Employees.append(hw19_6)
   hw19_6 = list()
print(Employees)

family = list()
hw20_4 = list()   # 20
for i in range(70):
   hw20_1 = logingenerator()
   hw20_2 = namegenerator('Any')
   hw20_3 = random.randint(1, 100)
   hw20_5 = True
   if hw20_3 % 2 == 0:
      hw20_5 = True
   else:
      hw20_5 = False
   hw20_4.extend([hw20_1, hw20_2, hw20_5])
   family.append(hw20_4)
   hw20_4 = list()
print(family)

gender = list()   # 21
hw21_5 = list()

for i in range(70):
   hw21_1 = logingenerator()
   hw21_2 = random.randint(1, 2)
   hw21_3 = str()
   if hw21_2 == 1:
      hw21_3 = 'male'
   else:
      hw21_3 = 'female'
   hw21_4 = namegenerator(hw21_3)
   hw21_5.extend([hw21_1, hw21_4, hw21_3])
   gender.append(hw21_5)
   hw21_5 = list()
print(gender)

salary = list()   # 22
hw22_4 = list()

for i in range(70):
   hw22_1 = logingenerator()
   hw22_2 = namegenerator('Any')
   hw22_3 = random.randint(300, 5000)
   hw22_4.extend([hw22_1, hw22_2, hw22_3])
   salary.append(hw22_4)
   hw22_4 = list()
print(salary)

hw23 = list()  # 23
for i in salary:
   if i[2] >= 1500 and i[2] <= 3000:
      hw23.append(i[1])
print(hw23)

hw24 = list()  # 24
for i in gender:
   if i[2] == 'male':
      hw24.append(i[1])
print(hw24)

hw25 = list()  # 25
for i in gender:
   if i[2] == 'female':
      hw25.append(i[1])
print(hw25)

hw26 = list()  # 26
for i in family:
   if i[2] == False:
      for i in gender:
         if i[2] == 'male':
            hw26.append(i[1])
   else:
      continue
print(hw26)