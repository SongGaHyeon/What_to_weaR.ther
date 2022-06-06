import csv
import random

i = random.randrange(0, 89)
a = []
one_subject = ''
one_address = ''
one_img = ''

def summer_pants():
    summerpants_data = []
    f = open('templates/clothes/겨울바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        summerpants_data.append(line)

    f.close()
    return summerpants_data[i]

def fifteen_nineteen():
    global a
    global one_subject
    global one_address
    global one_img

    a = summer_pants()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

fifteen_nineteen()
print(one_subject)

