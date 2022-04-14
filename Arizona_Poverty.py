import csv


file = open('Arizona_Poverty.csv', 'r')
Lines = file.readlines()
row_list = []

for line in Lines:
    my_list = [line[0:2].lstrip(" "), line[3:8].lstrip(" "), line[9:81].lstrip(" "), line[82:90].lstrip(" "), line[91:99].lstrip(" "), line[100:108].lstrip(" "), line[109:130].lstrip(" ")]
    row_list.append(my_list)
    print(row_list)

    file = open('ArizonaPoverty_Cleaned.csv', 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(row_list)
