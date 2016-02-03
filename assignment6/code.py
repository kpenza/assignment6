#!/usr/bin/python 

import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt

from operator import itemgetter




def offensefunction(offenselist, rowno):
    crimedict = {}
    for row in offenselist:
        crime = row[rowno]
        if crime in crimedict:
#            print 'token exists'
            crimedict[crime] = crimedict[crime]  + 1
        else:
#            print 'token does not exists'
            crimedict[crime] = 1
    
    sorteddict = sorted(crimedict.items(), key=itemgetter(1),  reverse=True)
    return sorteddict

def showtop(dictionary, noofitems, sorted = True):
    if sorted == True:
        sorteddict = dictionary
    else:
        sorteddict = sorted(dictionary.items(), key=itemgetter(1),  reverse=True)
    for x in range(0, noofitems):
        print sorteddict[x][0] + " " + str(sorteddict[x][1])

def gettopitems(dictionary, noofitems, sorted = True):
    list1 = []
    list2 = []
    if sorted == True:
        sorteddict = dictionary
    else:
        sorteddict = sorted(dictionary.items(), key=itemgetter(1),  reverse=True)
    for x in range(0, noofitems):
        list1.append(sorteddict[x][0])
        list2.append(sorteddict[x][1])
        #print sorteddict[x][0] + " " + str(sorteddict[x][1])
    return list1,list2

def plotgraph(crimedesc, crimeoccur):
     l = len(crimedesc)
#    for k in range (0, l):
#        print crimedict[k] + " : " + str(crimeoccur[k])
     N = range(len(crimedesc))
     jet = plt.get_cmap('jet')
#     plt.bar(range(N), crimeoccur, align='center', color=jet(np.linspace(0, 1.0, N)))
#     plt.xticks(range(N), crimedesc, rotation=25)
#     plt.rcParams.update({'font.size': 14})
     fig = plt.figure(figsize=(12,8))
     ax = fig.add_subplot(111)
     

     plt.barh(N, crimeoccur, align='center', color=jet(np.linspace(0, 1.0, len(crimedesc))), height=0.8, alpha=1)
     plt.yticks(N, crimedesc)
     #plt.yticks(N, crimedesc, rotation=25)
     plt.xlabel('Crimes type')
     plt.ylabel('Occurance')
     plt.yticks(N, crimedesc)
     plt.title('Crime occurance')
     plt.tight_layout()
     plt.show()


def offensefunctionlists(offenselist, rowno, crimedict, crimeoccur):
    for row in offenselist:
        crime = row[rowno]
        if crime in crimedict:
#            print 'token exists'
            idx = crimedict.index(crime)
            crimeoccur[idx] = crimeoccur[idx] + 1
        else:
#            print 'token does not exists'
            crimedict.append(crime)
            crimeoccur.append(1)
    print crimedict
    print crimeoccur

timeconvert =  {0 : "Early morning",
                1 : "Early morning",
                2 : "Early morning",
                3 : "Early morning",
                4 : "Early morning",
                5 : "Early morning",
                6 : "Morning",
                7 : "Morning",
                8 : "Morning",
                9 : "Morning",
               10 : "Morning",
               11 : "Morning",
               12 : "Afternoon",
               13 : "Afternoon",
               14 : "Afternoon",
               15 : "Afternoon",
               16 : "Afternoon",
               17 : "Afternoon",
               18 : "Night",
               19 : "Night",
               20 : "Night",
               21 : "Night",
               22 : "Night",
               23 : "Night",
               24 : "Night",
}

def offensetime(offenselist,offenseidx, reportedidx, crim, csvfile):
    dict = {}
    csvfile.seek(0)
    for row in offenselist:
        csvfile.seek(0)
        offense = row[offenseidx]
        if offense == crim:
            reportdate  = row[reportedidx]
            d = datetime.datetime.strptime( reportdate, "%m/%d/%Y %H:%M:%S %p" )
            t = d.time()
            key = timeconvert[t.hour]
            print key
            if key in dict:
                dict[key] = dict[key] + 1
            else:
                dict[key] = 1
    print dict

# http://stackoverflow.com/questions/19060144/more-efficient-matplotlib-stacked-bar-chart-how-to-calculate-bottom-values
# https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/        
# Stacked Bar Chart
# https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/
# http://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib
# http://matplotlib.org/examples/pylab_examples/scatter_star_poly.html

def chart1(csvfile):
        next(csvfile) # has header
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        crimedict = offensefunction(spamreader, 4)
        showtop(crimedict, 20)
        crimedesc, crimeoccur = gettopitems(crimedict, 20)
        plotgraph(crimedesc, crimeoccur)
        print crimedesc
        print crimeoccur

def chart2(csvfile):
        next(csvfile) # has header
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        crimedict = offensefunction(spamreader, 4)
        showtop(crimedict, 20)
        crimedesc, crimeoccur = gettopitems(crimedict, 20)
        for crim in crimedesc:
            offensetime(spamreader, 4, 8, crim, csvfile)
#       plotgraph(crimedesc, crimeoccur)
#        print crimedesc
#        print crimeoccur

def main():
    with open('seattle_incidents_summer_2014.csv', 'rb') as csvfile:
        #chart1(csvfile)
        chart2(csvfile)

if __name__ == '__main__':
    main()


##     crimedict = []
##     crimeoccur = []
##     offensefunction(spamreader,4, crimedict, crimeoccur)
##     l = len(crimedict)
##     for k in range (0, l):
##         print crimedict[k] + " : " + str(crimeoccur[k])
##     N = len(crimedict)
##     jet = plt.get_cmap('jet')
##     plt.bar(range(N), crimeoccur, align='center', color=jet(np.linspace(0, 1.0, N)))
##     plt.xticks(range(N), crimedict, rotation=25)
##     plt.show()
#    ax = fig.add_subplot(111)
#    ax.bar(len(crimedict),crimedict,0.5, align='center')
    
#|   \ width = 1/1.5
#    plt.bar(10, 10, width, color="blue", crimedict, crimeoccur,)

#    offensetime(spamreader,8, crimedict)

#    for row in spamreader:
#        print row[4]
#        print ', '.join(row)
