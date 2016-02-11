#!/usr/bin/python3.4

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


OFFENSENAMING =  {"BIKE THEFT" : "BURGLARY",
                  "CAR PROWL"  : "BURGLARY",
                  "ESCAPE"     : "RUNAWAY",
                  "WARRANT ARREST" : "WARRANTS",
                  "VEHICLE THEFT" : "MAIL THEFT",
                  "WEAPON LAW" :  "WEAPON",
                  "DRUG/NARCOTIC" : "NARCOTICS",
                  "PORNOGRAPHY/OBSCENE MAT" : "PORNOGRAPHY",
                  "EMBEZZLEMENT" : "EMBEZZLE",
                  "WEAPON LAWS" : "WEAPON",
                  "LIQUOR VIOLATION" : "LIQUOR",
                  "LIQUOR LAWS" : "LIQUOR",
                  "FORGERY"   : "FORGERY/COUNTERFEIT",
                  "COUNTERFEIT" : "FORGERY/COUNTERFEIT",
                  "FORGERY/COUNTERFEITING" : "FORGERY/COUNTERFEIT",
                  "LOITERING" : "PROSTITUTION",
                  "PURSE SNATCH" : "ROBBERY",
                  "SHOPLIFTING" : "ROBBERY",
                  "PICKPOCKET" : "ROBBERY",
                  "DRIVING UNDER THE INFLUENCE" : "DUI",
                  "BURGLARY-SECURE PARKING-RES" : "BURGLARY",
                  "VIOLATION OF COURT ORDER" : "WARRANTS",
                  "RECKLESS BURNING" : "ARSON",
                  "THEFT OF SERVICES" : "ROBBERY",
                  "LARCENY/THEFT" : "BURGLARY",
                  "INJURY" : "DISORDERLY CONDUCT",
                  "DISTURBANCE" :  "DISORDERLY CONDUCT",
                  "ELUDING" : "DISORDERLY CONDUCT",
                  "OTHER PROPERTY": "BURGLARY",
                  "FAMILY OFFENSES" :  "DISORDERLY CONDUCT",
                  "FALSE REPORT"  :  "OTHER OFFENSES",
                  "OBSTRUCT"  :  "OTHER OFFENSES",
                  "TRAFFIC"  :  "OTHER OFFENSES",
                  "ANIMAL COMPLAINT" : "OTHER OFFENSES",
                  "LOST PROPERTY" : "NON-CRIMINAL",

}
#OFFENSEREMOVE = ["DRUNKNESS","EXTORTION","GAMBLING","KIDNAPPING","SUICIDE", "BIAS INCIDENT","DISPUTE","FIREWORK","HOMICIDE","ILLEGAL DUMPING","THREATS"]
OFFENSEREMOVE = ["INC - CASE DC USE ONLY"]

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
        print (sorteddict[x][0] + " " + str(sorteddict[x][1]))

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
     

     p1 = plt.barh(N, crimeoccur, align='edge', color=jet(np.linspace(0, 1.0, len(crimedesc))), height=0.8, alpha=1)
     plt.yticks(N, crimedesc)
     #plt.yticks(N, crimedesc, rotation=25)
     plt.ylabel('Crime type')
     plt.xlabel('Occurance')
     plt.yticks(N, crimedesc)
     plt.title('Crime occurance')
     autolabelh(p1, ax)
     ax.xaxis.set_ticks_position('bottom')
     ax.yaxis.set_ticks_position('left')
     plt.axis([0, 6700, l  , 0])
#     plt.axis([0, 10000, l  , 0])
     plt.tight_layout()
     plt.show()

def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height + 4,
                '%d' % int(height), fontsize=10,
                ha='center', va='bottom')

def autolabelh(rects, ax):
    # attach some text labels
    for rect in rects:
        width = rect.get_width()
        height = rect.get_height()
        ax.text(4 +rect.get_x() +  width  , rect.get_y() + (height/2) *.98 ,
                '%d' % int(width), fontsize=10,
                ha='left', va='center')

def plotgraphchart2(title, earlymorning, morning, afternoon, night):
     
#    for k in range (0, l):
#        print crimedict[k] + " : " + str(crimeoccur[k])

# Final hbar !!
      N = len(title)
      ind = np.arange(N)    # the x locations for the groups
      width = 0.22       # the width of the bars: can also be len(x) sequence

 
      fig = plt.figure(figsize=(12,10))
      ax = fig.add_subplot(111)
      p1 = ax.barh(ind, earlymorning, width, color='r')
      p2 = ax.barh(ind + width, morning, width, color='y')
      p3 = ax.barh(ind + (width * 2), afternoon, width, color='b')
      p4 = ax.barh(ind + (width * 3), night, width, color='g')
     
      ax.set_xlabel('Occurance')
      ax.set_xlabel('Crime category')
      ax.set_title('Occurance per category subdivided per occurance period')
      ax.set_yticks(ind + (width * 3))
      ax.set_yticklabels(title)
      ax.xaxis.set_ticks_position('bottom')
      ax.yaxis.set_ticks_position('left')
      ax.legend((p1[0], p2[0], p3[0], p4[0]), (EARLY_MORNING, MORNING, AFTERNOON,NIGHT))
      autolabelh(p1, ax)
      autolabelh(p2, ax)
      autolabelh(p3, ax)
      autolabelh(p4, ax)
      plt.axis([0, 5200, N , 0])
      plt.tight_layout()
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
    print (crimedict)
    print (crimeoccur)

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
    print (crimedesc)
    print (crimeoccur)

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
     fig = plt.figure(figsize=(12,10))
     ax = fig.add_subplot(111)

     p1 = plt.barh(N, occurancelist, align='edge', color=colorlist, height=0.6, alpha=.8)
#     p1 = plt.bar(N, occurancelist, align='center', color=colorlist, width=0.6, alpha=.8)
#     plt.yticks(N, districtlist)
     plt.yticks(N, zonelist)
#     plt.xticks(N, zonelist, rotation=90)
     plt.xlabel('Crime occurance')
#     plt.ylabel('Crime occurance')
     plt.ylabel('District')
#     plt.xlabel('District')
     plt.title('Crime occurance per district')
     ax.xaxis.set_ticks_position('bottom')
     ax.yaxis.set_ticks_position('left')
#    plt.axis([min(x_arr), max(x_arr), max(y_arr), 0])
#     plt.axis([0, 400 ,l, 0])
     plt.axis([0, 2700 ,l, 0])
     autolabelh(p1, ax)
#     autolabel(p1, ax)
#     ax.grid(True)
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
        print (districtlist)
        print (zonelist)
        print (occurancelist)

def loadcsv(datafile, crimeidx, districtidx, datetimeformat=None, zoneidx=None,reportdatetimeidx= None, alternatereportdatetimeidx=None, reportdateidx=None, reporttimeidx=None, reportdateformat=None, reporttimeformat=None, skipoffenses=1 ):
    reportlist = []
    with open(datafile, 'r') as csvfile:
        next(csvfile) # has header
        offenselist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in offenselist:
            crime = row[crimeidx]
            if skipoffenses == 1:
                if crime in OFFENSEREMOVE:
                    continue
            if reportdatetimeidx is not None:
                if row[reportdatetimeidx] == "":
                    rd = row[alternatereportdatetimeidx]
                else:
                    rd = row[reportdatetimeidx]
            if reportdateidx is not None and reporttimeidx is not None:
                rd = row[reportdateidx] + " " + row[reporttimeidx]
            reportdate = datetime.datetime.strptime(rd, datetimeformat)
            district = row[districtidx]
            if zoneidx is not None:
                zone = row[zoneidx]
            else:
                zone = district
            reportlist.append(Report(crime,reportdate, district, zone))
    return reportlist

def allignnaming(reportlist):
    for row in reportlist:
        if row.offense in OFFENSENAMING:
            row.offense = OFFENSENAMING[row.offense]

def getOffenselist(alist):
    lst = []
    for row in alist:
        lst.append(row.offense)
    return lst

def getOffense(alist, offense):
    count = 0
    for row in alist:
        if offense == row.offense:
            count +=1
    return count

def chart4(reportlist_seattle, reportlist_sanfrancisco):
    allignnaming(reportlist_sanfrancisco)
    allignnaming(reportlist_seattle)

    a = getOffenselist(reportlist_sanfrancisco) 
    
    offenses = list(set(getOffenselist(reportlist_sanfrancisco) + getOffenselist(reportlist_seattle)))
    off_sf = []
    off_se = []
    for offense in offenses:
        off_sf.append(getOffense(reportlist_sanfrancisco, offense))
        off_se.append(getOffense(reportlist_seattle, offense))
      
    N = len(offenses)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.4       # the width of the bars: can also be len(x) sequence
 
#    fig = plt.figure(figsize=(14,8))
    fig = plt.figure(figsize=(12,12))
    #    plt.axis([min(x_arr), max(x_arr), max(y_arr), 0])
    ax = fig.add_subplot(111)

    # fig, ax = plt.subplots()
    p1 = ax.barh(ind, off_sf, width, color='r')
    p2 = ax.barh(ind + width, off_se, width, color='b')
#    p1 = ax.bar(ind, off_sf, width, color='r')
#    p2 = ax.bar(ind + width, off_se, width, color='b')
    
    ax.set_ylabel('Crime occurance')
    ax.set_title('Crime reports per state')
    ax.set_yticks(ind + (width ))
    ax.set_yticklabels(offenses)
 #   ax.set_xticks(ind + (width ))
#   ax.set_xticklabels(offenses)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend((p1[0], p2[0] ), ("San Francisco", "Seattle"))
#    autolabelh(p1, ax)
#    autolabelh(p2, ax)
#    autolabel(p1, ax)
#    autolabel(p2, ax)
#    plt.xticks(range(N), offenses, rotation=90)
#    plt.axis([min(x_arr), max(x_arr), max(y_arr), 0])
#    plt.axis([0,N , 0, 15000])
    plt.axis([0,15200 , N, 0])
    ax.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    # 6 Summary Offense Code
    # 8 Date Reported
    # 9 Actual Date (sometimes None)
    # 11 District/Sector
    # 12 Zone/Beat
    reportlist_seattle = loadcsv(datafile='seattle_incidents_summer_2014.csv', crimeidx=6, reportdatetimeidx=9, alternatereportdatetimeidx=8, districtidx=11, zoneidx=12, datetimeformat="%m/%d/%Y %H:%M:%S %p")
#    reportlist_seattle = loadcsv(datafile='seattle_incidents_summer_2014.csv', crimeidx=4, reportdatetimeidx=9, alternatereportdatetimeidx=8, districtidx=11, zoneidx=12, datetimeformat="%m/%d/%Y %H:%M:%S %p")
#    print "Total reports : " + str(len(reportlist_seattle))
    # 2 Category
    # 4 Date
    # 5 Time
    # 8 District
    reportlist_sanfrancisco = loadcsv(datafile='sanfrancisco_incidents_summer_2014.csv', crimeidx=1,reportdateidx=4, reporttimeidx=5, districtidx=6, datetimeformat = "%m/%d/%Y %H:%M")
#    print "Total reports : " + str(len(reportlist_sanfrancisco))
#    for r in reportlist:
#        print r
    reportlist = reportlist_sanfrancisco
#   reportlist = reportlist_seattle
    chart1(reportlist)
#    chart2(reportlist)
#    chart3(reportlist)
#     chart4(reportlist_seattle, reportlist_sanfrancisco)
#    for row in reportlist:
#        print row.offense
#    timeconvert[row.reportdate.time().hour]


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
