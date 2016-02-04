class Report:
     
    def __init__(self, offense, reportdate, district, zone):
        self.offense = offense
        self.reportdate = reportdate
        self.district = district
        self.zone = zone

    def __str__(self):
         return "Offense:" + self.offense + " ReportDate: " + str(self.reportdate) + "District: " + self.district + "Zone: " + self.zone
