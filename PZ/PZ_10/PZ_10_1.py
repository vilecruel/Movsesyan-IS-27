# Практическая 10

#Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить
#текст в стихотворной форме предварительно поставив последнюю строку между первой и второй.

ishodny_fail = open("text18-17.txt", "w", encoding="utf-8")
ishodny_fail.write("Да, были люди в наше время,\n")
ishodny_fail.write("Могучее, лихое племя:\n")
ishodny_fail.write("Богатыри — не вы.\n")
ishodny_fail.write("Плохая им досталась доля:\n")
ishodny_fail.write("Немногие вернулись с поля.\n")
ishodny_fail.write("Когда б на то не божья воля,\n")
ishodny_fail.write("Не отдали б Москвы!\n")
ishodny_fail.close()

f = open("text18-17.txt", "r", encoding="utf-8")
tekst_stiha = f.read()
f.close()

print("Содержимое файла text18-17.txt:")
print(tekst_stiha)
print("-" * 30)

znaki = ".,!?;:—"
skolko_znakov = 0
for simvol in tekst_stiha:
    if simvol in znaki:
        skolko_znakov = skolko_znakov + 1

print("Количество знаков препинания:", skolko_znakov)

f = open("text18-17.txt", "r", encoding="utf-8")
stroki = f.readlines()
f.close()

pervaya_stroka = stroki[0]
poslednyaya_stroka = stroki[-1]

if not poslednyaya_stroka.endswith("\n"):
    poslednyaya_stroka = poslednyaya_stroka + "\n"

noviy_stih = []
noviy_stih.append(pervaya_stroka)
noviy_stih.append(poslednyaya_stroka)

for s in stroki[1:-1]:
    noviy_stih.append(s)

f_noviy = open("otvet2.txt", "w", encoding="utf-8")
for s in noviy_stih:
    f_noviy.write(s)
f_noviy.close()

print("Задание 2 выполнено! Проверь файл otvet2.txt")