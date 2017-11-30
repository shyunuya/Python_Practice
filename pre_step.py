# pre_step.py
import csv
percent = []
dict_num = {}
with open("num_data.txt",'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        perc = int(row[1]) / 101.0
        print perc
        if perc not in percent:
            percent.append(perc)
            dict_num[perc] = []
        
        dict_num[perc].append(int(row[0]))
        
print ""
print ""
print percent
print ""
print ""
print dict_num
