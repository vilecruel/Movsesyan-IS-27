#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:Количество элементов:Произведение элементов:Количество пар, для которых
#произведение элементов делится на 3 (элементы пары в последовательности являются соседними):

fail1 = open("числа.txt", "w", encoding="utf-8")
fail1.write("5 -2 3 9 -4 6")
fail1.close()

fail1 = open("числа.txt", "r", encoding="utf-8")
stroka_chisel = fail1.read()
fail1.close()

kuski = stroka_chisel.split()
spisok = []
for x in kuski:
    spisok.append(int(x))

vsego = len(spisok)

proizvedenie = 1
for x in spisok:
    proizvedenie = proizvedenie * x

pary = 0
for i in range(vsego - 1):
    chislo1 = spisok[i]
    chislo2 = spisok[i + 1]
    if (chislo1 * chislo2) % 3 == 0:
        pary = pary + 1

fail2 = open("отчет1.txt", "w", encoding="utf-8")
fail2.write("Исходные данные: " + stroka_chisel + "\n")
fail2.write("Количество элементов: " + str(vsego) + "\n")
fail2.write("Произведение элементов: " + str(proizvedenie) + "\n")
fail2.write("Количество пар, для которых произведение элементов делится на 3: " + str(pary) + "\n")
fail2.close()

print("Задание 1 выполнено! Результат записан в отчет1.txt")