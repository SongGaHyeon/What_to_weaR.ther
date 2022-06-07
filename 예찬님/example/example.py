import csv
import random


i = random.randrange(0, 89)
a = []

one_subject = ''
one_address = ''
one_img = ''

def minus4():
    global a
    global one_subject
    global one_address
    global one_img

    a = winter_pants()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

def winter_pants():
    pants_data = []
    f = open('clothes\겨울바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        pants_data.append(line)

    f.close()
    return pants_data[i]

minus4()
print(one_subject)
print(one_address)
print(one_img)