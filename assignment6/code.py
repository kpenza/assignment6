#!/usr/bin/python 

import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
from  Report import Report
from operator import itemgetter

EARLY_MORNING="Early morning"
MORNING="Morning"
AFTERNOON="Afternoon"
NIGHT="Night"

def offensefunction(reportlist):
    crimedict = {}
    for row in reportlist:
        crime = row.offense
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
     

     p1 = plt.barh(N, crimeoccur, align='center', color=jet(np.linspace(0, 1.0, len(crimedesc))), height=0.8, alpha=1)
     plt.yticks(N, crimedesc)
     #plt.yticks(N, crimedesc, rotation=25)
     plt.xlabel('Crimes type')
     plt.ylabel('Occurance')
     plt.yticks(N, crimedesc)
     plt.title('Crime occurance')
     autolabelh(p1, ax)
     plt.tight_layout()
     plt.show()

def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def autolabelh(rects, ax):
    # attach some text labels
    for rect in rects:
        width = rect.get_width()
        height = rect.get_height()
        ax.text(rect.get_x() + 1.05 * width  , rect.get_y() + (height/2) *.98 ,
                '%d' % int(width),
                ha='left', va='center')

def plotgraphchart2(title, earlymorning, morning, afternoon, night):
     
#    for k in range (0, l):
#        print crimedict[k] + " : " + str(crimeoccur[k])

# Final hbar !!
      N = len(title)
      ind = np.arange(N)    # the x locations for the groups
      width = 0.2       # the width of the bars: can also be len(x) sequence
 
      fig, ax = plt.subplots()
      p1 = ax.barh(ind, earlymorning, width, color='r')
      p2 = ax.barh(ind + width, morning, width, color='y')
      p3 = ax.barh(ind + (width * 2), afternoon, width, color='b')
      p4 = ax.barh(ind + (width * 3), night, width, color='g')
     
      ax.set_ylabel('Occurance')
      ax.set_title('Scores by group and gender')
      ax.set_yticks(ind + (width * 3))
      ax.set_yticklabels(title)
      ax.xaxis.set_ticks_position('bottom')
      ax.yaxis.set_ticks_position('left')
      ax.legend((p1[0], p2[0], p3[0], p4[0]), (EARLY_MORNING, MORNING, AFTERNOON,NIGHT))
      autolabelh(p1, ax)
      autolabelh(p2, ax)
      autolabelh(p3, ax)
      autolabelh(p4, ax)
      plt.show()

#     N = len(title)
#     ind = np.arange(N)    # the x locations for the groups
#     width = 0.18       # the width of the bars: can also be len(x) sequence
#
#     fig, ax = plt.subplots()
#     p1 = ax.bar(ind, earlymorning, width, color='r')
#     p2 = ax.bar(ind + width, morning, width, color='y')
#     p3 = ax.bar(ind + (width * 2), afternoon, width, color='b')
#     p4 = ax.bar(ind + (width * 3), night, width, color='g')
#    
#     ax.set_ylabel('Occurance')
#     ax.set_title('Scores by group and gender')
#     ax.set_xticks(ind + width)
#     ax.set_xticklabels((EARLY_MORNING, MORNING, AFTERNOON,NIGHT))
#     ax.xaxis.set_ticks_position('bottom')
#     ax.tick_params(labelsize=13)
#     ax.yaxis.set_ticks_position('left')
#     ax.set_xticklabels(title, rotation=75)
#     ax.legend((p1[0], p2[0], p3[0], p4[0]), (EARLY_MORNING, MORNING, AFTERNOON,NIGHT))
#     autolabel(p1, ax)
#     autolabel(p2, ax)
#     autolabel(p3, ax)
#     autolabel(p4, ax)
#     plt.tight_layout()
#     plt.show()

##     N = len(title)
##     ind = np.arange(N)    # the x locations for the groups
##     width = 0.35       # the width of the bars: can also be len(x) sequence
## 
##     p1 = plt.bar(ind, earlymorning, width, color='r')
##     p2 = plt.bar(ind, morning, width, color='y', bottom=earlymorning)
##     p3 = plt.bar(ind, afternoon, width, color='b', bottom=earlymorning)
##     p4 = plt.bar(ind, night, width, color='g', bottom=earlymorning)
## 
##     plt.ylabel('Scores')
##     plt.title('Scores by group and gender')
##     plt.xticks(ind + width/2., title)
###     plt.yticks(np.arange(0, 81, 10))
##     plt.legend((p1[0], p2[0], p3[0], p4[0]), (EARLY_MORNING, MORNING, AFTERNOON,NIGHT))
##     plt.show()


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

timeconvert =  {0 : EARLY_MORNING,
                1 : EARLY_MORNING,
                2 : EARLY_MORNING,
                3 : EARLY_MORNING,
                4 : EARLY_MORNING,
                5 : EARLY_MORNING,
                6 : MORNING,
                7 : MORNING,
                8 : MORNING,
                9 : MORNING,
               10 : MORNING,
               11 : MORNING,
               12 : AFTERNOON,
               13 : AFTERNOON,
               14 : AFTERNOON,
               15 : AFTERNOON,
               16 : AFTERNOON,
               17 : AFTERNOON,
               18 : NIGHT,
               19 : NIGHT,
               20 : NIGHT,
               21 : NIGHT,
               22 : NIGHT,
               23 : NIGHT,
               24 : NIGHT,
}

def offensetime(reportlist, crim):
    dict = {}
    for row in reportlist:
        if row.offense == crim:
            key = timeconvert[row.reportdate.time().hour]
            if key in dict:
                dict[key] = dict[key] + 1
            else:
                dict[key] = 1
    return dict

# http://stackoverflow.com/questions/19060144/more-efficient-matplotlib-stacked-bar-chart-how-to-calculate-bottom-values
# https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/        
# Stacked Bar Chart
# https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/
# http://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib
# http://matplotlib.org/examples/pylab_examples/scatter_star_poly.html

def chart1(reportlist):
    crimedict = offensefunction(reportlist)
    showtop(crimedict, 20)
    crimedesc, crimeoccur = gettopitems(crimedict, 20)
    plotgraph(crimedesc, crimeoccur)
    print crimedesc
    print crimeoccur

def preparechart2(dict):
    earlymorning = []
    morning = []
    afternoon = []
    night = []
    title = []
    for entry in dict:
        key = entry
        title.append(key) # append heading
        lists = dict[entry]
        if EARLY_MORNING in lists:
            earlymorning.append(lists[EARLY_MORNING])
        else:
            earlymorning.append(0)
        if MORNING in lists:
            morning.append(lists[MORNING])
        else:
            morning.append(0)
        if AFTERNOON in lists:
            afternoon.append(lists[AFTERNOON])
        else:
            afternoon.append(0)
        if NIGHT in lists:
            night.append(lists[NIGHT])
        else:
            night.append(0)
    return title, earlymorning, morning, afternoon, night

def plotgraphchart3(title, districtlist, zonelist, occurancelist, colorlist):
     l = len(zonelist)
     N = range(l)
     jet = plt.get_cmap('jet')
     fig = plt.figure(figsize=(12,8))
     ax = fig.add_subplot(111)

     p1 = plt.barh(N, occurancelist, align='center', color=colorlist, height=0.8, alpha=1)
     plt.yticks(N, zonelist)
     plt.xlabel('Crimes type')
     plt.ylabel('Occurance')
     plt.title('Crime occurance')
     autolabelh(p1, ax)


     plt.tight_layout()
     plt.show()

def preparechart3(dict, offense):
    districtlist = []
    zonelist = []
    occurancelist = []
    for entry in dict:
        if entry.district == "" or entry.district == "99":
              continue
#          print entry.district + " " + entry.zone
        key = entry.offense
        if key == offense:
            district = entry.district
            zone = district + "/" + entry.zone
            if zone in zonelist:
                idx = zonelist.index(zone)
                occurancelist[idx] = occurancelist[idx] + 1
            else:
                districtlist.append(district)
                zonelist.append(zone)
                occurancelist.append(1)
    # sort
    zonelist_s, occurancelist_s, districtlist_s = zip(*sorted(zip(zonelist,occurancelist,districtlist)))

    uniquedistricts = list(set(districtlist_s))
    uniquedistrictslen = len(uniquedistricts)
   
    jet = plt.get_cmap('jet') 
    colors = jet(np.linspace(0, 1.0, uniquedistrictslen))
    colorlist = []
    for k in range(0, len(districtlist_s)):
        d = districtlist_s[k]
        idx = uniquedistricts.index(d)
        colorlist.append(colors[idx])
 
    return districtlist_s, zonelist_s, occurancelist_s,colorlist

def chart2(reportlist):
    dict = {}
    crimedict = offensefunction(reportlist)
    showtop(crimedict, 20)
    crimedesc, crimeoccur = gettopitems(crimedict, 20)
    for crim in crimedesc:
        offensetiming = offensetime(reportlist, crim)
        dict[crim] = offensetiming
    title, earlymorning, morning, afternoon, night = preparechart2(dict)
    plotgraphchart2(title, earlymorning, morning, afternoon, night)
#    print dict
    
#    plotgraph(crimedesc, crimeoccur)
#        print crimedesc
#        print crimeoccur

def chart3(reportlist):
    dict = {}
    crimedict = offensefunction(reportlist)
    crimedesc, crimeoccur = gettopitems(crimedict, 1)
    for crim in crimedesc:
        districtlist, zonelist, occurancelist, colorlist = preparechart3(reportlist, crim)
        plotgraphchart3(crim, districtlist, zonelist, occurancelist, colorlist)
        print districtlist
        print zonelist 
        print occurancelist

def loadcsv(datafile, crimeidx, reportdateidx, districtidx, zoneidx, dateformat):
    reportlist = []
    with open(datafile, 'rb') as csvfile:
        next(csvfile) # has header
        offenselist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in offenselist:
            crime = row[crimeidx]
            reportdate = datetime.datetime.strptime(row[reportdateidx], dateformat)
            district = row[districtidx]
            zone = row[zoneidx]
            reportlist.append(Report(crime,reportdate, district, zone))
    return reportlist

def main():
    reportlist = loadcsv('seattle_incidents_summer_2014.csv', 6, 8,11,12, "%m/%d/%Y %H:%M:%S %p")
#    for r in reportlist:
#        print r
#    chart1(reportlist)
#    chart2(reportlist)
    chart3(reportlist)

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
