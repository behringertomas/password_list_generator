#   Python 3.X
########################
#   Coded By           #
#   Pradeep Jairamani  #
########################

########################
#   Password List      #
#   Generator tool     #
########################

import os
import sys

# Declarations
if int(sys.version_info[0]) is 2:
    input = raw_input

dict_months = {"01": "enero", "02": "febrero", "03": "marzo", "04": "abril", "05": "mayo", "06": "junio", "07": "julio",
         "08": "agosto", "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"}

lst_special_characters = ['@', '*', '!', '#', '$']

lst_numeros = ['98765', '9876', '987', '123', '1234', '12345']

password_list = list()
list1 = list()
characters_list = list()
leet_list = list()
unique_list = list()
random_l = list()


######################################################
def datepart(date):
    if (len(date) != 0):
        date, sep, tail = date.partition("/")
        month, sep, year = tail.partition("/")
        list1.append(date)
        list1.append(month)
        list1.append(year)
        try:
            list1.append(dict_months[month])
        except:
            print("Fecha Mal Ingresada")
        list1.append(date[::-1])
        list1.append(month[::-1])
        list1.append(year[::-1])
        list1.append(year[2:])
        list1.append(year[1:])


########################################################

print("[+] Enter User Details")
fname = input("Enter First name: ").lower()
while (len(fname) == 0):
    fname = input("Atleast enter the name of the user: ").lower()
lname = input("Enter Last name: ").lower()
nick = input("Enter Nickname: ").lower()
email = input("Enter Email: ").lower()
dob = input("Enter Date of birth in the format dd/mm/yyyy: ")
while (len(dob) != 0) and (len(dob) != 10):
    dob = input("Enter dob in correct format dd/mm/yyyy: ")
phone = input("Enter Phone number: ")
# vehicle = input("Enter Vehicle number: ")
partner = input("Enter Partner's name: ").lower()
partnick = input("Enter Partner's Nickname: ").lower()
partdob = input("Enter Date of birth of partner dd/mm/yyyy: ")
while (len(partdob) != 0) and (len(partdob) != 10):
    partdob = input("Enter dob in correct format dd/mm/yyyy: ")
bestf = input("Enter Bestfriend's Name: ").lower()
# birthplace = input("Enter birth place: ").lower()
# pet = input("Enter pet's name: ").lower()
child = input("Enter child's name: ").lower()
# childn =input("Enter Child's nick name: ").lower()
# childob = input ("Enter Date of birth of child dd/mm/yyyy: ")
# while(len(childob)!=0) and (len(childob)!=10):
#  childob = input ("Enter dob in correct format dd/mm/yyyy: ")
company = input("Enter Comppany's name: ")
other = input("Enter Any other information for password seperate the words by ',' : ").replace(" ", "")
words2 = other.split(",")
try:
    maxm = int(input("[+] Maxima Cantidad de caracteres de las contraseñas( by default 12 ): "))
except:
    maxm = 12

try:
    minm = int(input("[+] Minima Cantidad de caracteres de las contraseñas( by default 8 ): "))
except:
    minm = 8

spycn = input("[+] Agregar caracteres especiales al final de la lista? : [y/n] ").lower()

if spycn == 'y':
    special = list()
    for spec1 in lst_special_characters:
        special.append(spec1)
        for spec2 in lst_special_characters:
            special.append(spec1 + spec2)
            for spec3 in lst_special_characters:
                special.append(spec1 + spec2 + spec3)

leet = input(
    "[+] Activar modo 1337 ? (Ejemplo:  hello = h3110 ) : [y/n] ").lower()  # 1337 mode can convert the characters to leet speak and hello = h3110
random = input("[+] Agregar numeros aleatorios al final de las contraseñas? : [y/n] ").lower()

################################

funame = fname.title()
nuick = nick.title()
purtname = partner.title()
purtnick = partnick.title()
bustf = bestf.title()
chld = child.title()
# chldn = childn.title()
cumpny = company.title()

##############################3


emails, sep, tail = email.partition("@")

list1 = [fname, lname, nick, emails, funame, nuick, phone, partner, partnick, bestf, purtname, purtnick, bustf, child,
         company, chld, cumpny]
for i in words2:
    list1.append(i)

datepart(partdob)
# datepart(childob)
datepart(dob)

list1 = list(filter(None, list1))  # removing empty data

falela = open("test.txt", "w")



# Algoritmo principal


for i in list1:
    password_list.append(i)
    for j in list1:
        if (i.lower()) != (j.lower()):
            password_list.append(i + j)

if leet == 'y':
    for i in password_list:
        i = i.replace('a', '@')
        i = i.replace('t', '7')
        i = i.replace('l', '1')
        i = i.replace('e', '3')
        i = i.replace('i', '!')
        i = i.replace('o', '0')
        i = i.replace('z', '2')
        i = i.replace('g', '9')
        i = i.replace('s', '5')
        leet_list.append(i)

# Leet Speak chars
# a='@'
# t='7'
# l='1'
# e='3'
# i='!'
# o='0'
# z='2'
# g='9'
# s='5'
####################

if random == 'y':
    for i in password_list:
        for j in lst_numeros:
            random_l.append(i + j)
else:
    random_l = password_list

if spycn == 'y':
    for i in random_l:
        for j in special:
            characters_list.append(i + j)

#######################
count = 0
unique_list = password_list + random_l + characters_list + leet_list
list(set(unique_list))
for i in unique_list:
    if (len(i) >= minm) and (len(i) <= maxm):
        falela.write(i + "\n")
        count += 1

falela.close()

print("[+]Total Words : ", count)
