import csv

def offensefunction(offenselist, rowno, crimedict):
    for row in offenselist:
        crime = row[rowno]
        if crime in crimedict:
#            print 'token exists'
            crimedict[crime] = crimedict[crime]  + 1
        else:
#            print 'token does not exists'
            crimedict[crime] = 1
    print crimedict


with open('seattle_incidents_summer_2014.csv', 'rb') as csvfile:
    next(csvfile) # has header
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    crimedict = {}
    offensefunction(spamreader,4, crimedict)

#    for row in spamreader:
#        print row[4]
#        print ', '.join(row)
