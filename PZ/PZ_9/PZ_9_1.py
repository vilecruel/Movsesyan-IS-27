#Практическая работа 9

#Даны имена девочек. Определить, какие из этих имен встречаются в группах
#на всех вторых курсах, какие есть только в некоторых группах и какие
#не встречаются ни в одной из групп.

vse_imena = {"Анна", "Елена", "Мария", "Дарья", "Ольга", "Ирина"}

grup1 = {"Анна", "Елена", "Мария"}
grup2 = {"Анна", "Мария", "Дарья"}
grup3 = {"Анна", "Мария", "Ольга"}

vse_gruppy = grup1 & grup2 & grup3
otvet1 = vse_imena & vse_gruppy

obshiy_spisok = grup1 | grup2 | grup3

otvet2 = vse_imena - obshiy_spisok

otvet3 = (vse_imena & obshiy_spisok) - otvet1

print("Во всех группах:", otvet1)
print("Только в некоторых:", otvet3)
print("Нет ни в одной:", otvet2)