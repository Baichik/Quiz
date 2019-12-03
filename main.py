import csv


count = 1
queshnsList = []
aList = []
bList = []
cList = []
correctList = []

with open('Quiz.csv', 'r', newline='') as quiz:
    reder = csv.reader(quiz, delimiter=";")
    for row in reder:
        queshns = row[0]
        a = row[1]
        b = row[2]
        c = row[3]
        corect = row[4]
        points = []
        queshnsList.append(queshns)
        aList.append(a)
        bList.append(b)
        cList.append(c)
        correctList.append(corect)
while count < len(queshnsList):
    print(queshnsList[count])
    option = input("Выберите вариант ответа: " + 'a)' + aList[count] + ' ' +'b)' + bList[count] + ' ' + 'c)' + cList[count] + ' ')
    if option == 'a':
        if aList[count] == correctList[count]:
            points.append(5)
            print('Правильно')
        else:
            print('Не правильно')
    elif option == 'b':
        if bList[count] == correctList[count]:
            points.append(5)
            print('Правильно')
        else:
            print('Не правильно')
    elif option == 'c':
        if cList[count] == correctList[count]:
            points.append(5)
            print('Правильно')
        else:
            print('Не правильно')
    else:
        print('Выберите вариант ответа!')
    count += 1
summ = sum(points)
print('Вы заработали ' + str (summ) + ' баллов')

if summ >= 95:
  print('Поздровляю ваша оценка А')
elif summ >= 90:
  print('Поздровляю ваша оценка А-')
elif summ >= 85:
  print('Поздровляю ваша оценка B+')
elif summ >= 80:
  print('Поздровляю ваша оценка B')
elif summ >= 75:
  print('Поздровляю ваша оценка B-')
elif summ >= 70:
  print('Ваша оценка C')
elif summ >= 65:
  print('Ваша оценка D')
elif summ == 60:
  print('Ваша оценка D-')
elif summ < 60:
  print('Ваша оценка F')