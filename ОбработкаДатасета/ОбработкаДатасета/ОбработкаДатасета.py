import csv
path_file = "C:/Users/IvanovaAlina/Desktop/Учеба/Диплом/"
r_file = open(path_file + "dataset.csv", encoding ="utf-8")
# Создаем объект reader, указываем символ-разделитель ","
file_reader = csv.reader(r_file, delimiter = ",")
w_file = open(path_file + "dataset_new.csv", 'a',encoding ="utf-8")
csv.register_dialect('my_dialect', delimiter=';', lineterminator="\r")
file_writer = csv.writer(w_file, 'my_dialect')
# Считывание данных из CSV файла
new_data = []
count = 0
for row in file_reader:
    new_data = [row[5]]
    if count > 0: 
        if float(row[6]) <= 2.2:
            new_data.insert(1, '0')
        else:
            new_data.insert(1, '1')
    else:
        new_data.insert(9, 'target')
    file_writer.writerow(new_data)
    count+=1
    #print(row) 