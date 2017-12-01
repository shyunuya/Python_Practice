# pre_step.py
import csv
import sys
import random
percent = []
dict_num = {}

def set_num(file_name):
    with open(file_name,'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            perc = int(row[1])
            #print perc
            if perc not in percent:
                percent.append(perc)
                dict_num[perc] = []

            dict_num[perc].append(int(row[0]))
    for key in sorted(dict_num.iterkeys()):
        print "%s : %s" % (key, dict_num[key])


if __name__=="__main__":
    file_name = sys.argv[1]
    set_num(file_name)
    print file_name
