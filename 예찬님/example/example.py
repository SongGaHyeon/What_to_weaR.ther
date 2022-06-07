import csv

f = open('겨울바지_data.csv', 'r')
rdr = csv.reader(f)

data = []

for line in rdr:
    data.append(line)

f.close()

print(data)

data[i][]