
#Реализовать консольное приложение заметки, с сохранением, чтением,
#добавлением, редактированием и удалением заметок. Заметка должна
#содержать идентификатор, заголовок, тело заметки и дату/время создания или
#последнего изменения заметки. Сохранение заметок необходимо сделать в
#формате json или csv формат (разделение полей рекомендуется делать через
#точку с запятой). Реализацию пользовательского интерфейса студент может
#делать как ему удобнее, можно делать как параметры запуска программы
#(команда, данные), можно делать как запрос команды с консоли и
#последующим вводом данных, как-то ещё, на усмотрение студента.

import csv
import datetime

def readMyCsv():
    with open("notes.csv", encoding="utf-8") as file_reader:
        notes = csv.reader(file_reader, delimiter = ";")
        count = 0
        arrNotes = []
        for row in notes:
            arrNotes.append(row)
            count += 1

    return arrNotes

def writeMyCsv(notes):
    with open("notes.csv", 'w', encoding="utf-8", newline='') as csv_file_writer:
        writer = csv.writer(csv_file_writer, delimiter =";", quotechar='|')
        for row in notes:
            writer.writerow(row)
    print('Запись сделана')


command = input("Это программа для заметок, введите команду - all, new, red, del: ")

if (command == "all"):
    notes = readMyCsv()

    for row in notes:
        print(f'{row[0]} : {row[1]} {row[2]} {row[3]} ' )

    print(f'Количество записей в файле: {len(notes)}')


if (command == "new"):
    header = input("Введите заголовок: ")
    text = input("Введите текст: ")
    current_date_time = datetime.datetime.now()
    current_date = current_date_time.date()
    #current_time = current_date_time.time()
    notes = readMyCsv()

    notes.append([len(notes)+1, header, text, current_date])

    writeMyCsv(notes)

if (command == "red"):

    notes = readMyCsv()
    num = input("Введите номер записи для изменений: ")
    tmp_notes = notes

    for row in notes:
        if (row[0] == num):
                index = int (row[0])-1
                header = input("Введите заголовок: ")
                text = input("Введите текст: ")
                current_date_time = datetime.datetime.now()
                current_date = current_date_time.date()
                tmp_notes[index] = [num, header, text, current_date]
                writeMyCsv(tmp_notes)

if (command == "del"):

    notes = readMyCsv()
    num = input("Введите номер записи для удаления: ")
    tmp_notes = notes

    for row in notes:
        if (row[0] == num):
            tmp_notes.remove(row)
            writeMyCsv(tmp_notes)



