import csv

with open('C:/users/exiz/documents/datascience/StatInference/STATISTICS_PROJECT.git/raw_data/Hostel.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    shit = []
    for line in readCSV:
        if line[0] == '' :
            shit.append(line)
        else:
            distance = line[4]
            x = True
            count = 1
            print(distance)
            while x:
                print(distance[0:count])
                try:
                    y = float(distance[0:count])
                    print(distance[0:count])
                    count += 1
                except ValueError:
                    out = distance[0:count-1]
                    print(out)
                    line[4] = out
                    shit.append(line)
                    x = False

fuck = open('C:/users/exiz/documents/datascience/StatInference/STATISTICS_PROJECT.git/raw_data/Hotel_Japan.csv',"w+", newline="")
thing = csv.writer(fuck, delimiter = ",")
for line in shit:
    print(line)
    thing.writerow(line)