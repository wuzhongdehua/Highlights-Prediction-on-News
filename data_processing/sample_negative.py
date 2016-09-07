import re, math
from collections import Counter
import random
import itertools
import sys
import csv

csv.field_size_limit(sys.maxsize)

with open('data/28/news_gra_sen_title_loc_final.csv', 'r') as f:
    reader = csv.reader(f)
    reader.next()
    labels = [(int(x[0]),x[1],x[2],x[3],x[4],x[5],x[6]) for x in reader]
    # labels = [x for x in reader]
f.close()
print len(labels)
print labels[0]

ture_labels = []
false_labels = []

for i in range(0, len(labels)):
    if labels[i][0] == 1:
        ture_labels.append(i)
    elif labels[i][0] == 0:
        false_labels.append(i)
print len(ture_labels)
print len(false_labels)

slice = random.sample(false_labels,int(len(ture_labels)*1.5))
# print sorted(slice)
print len(slice)
#
merge_list = ture_labels+slice
merge_list = sorted(merge_list)
print len(merge_list)
# print merge_list

writefile = file('data/28/news_gra_sen_title_loc_sample.csv', 'w')
# myfile = codecs.open('csv_train.csv', 'r', encoding='ascii', errors='ignore')
writer = csv.writer(writefile)
#
j = 0
for i in merge_list:
    j += 1
    writer.writerow((labels[i][0],labels[i][1],labels[i][2],labels[i][3],labels[i][4],labels[i][5],labels[i][6]))
writefile.close()
print j