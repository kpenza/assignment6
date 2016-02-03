class Report:
     
    def __init__(self, offense, reportdate):
        self.offense = offense
        self.reportdate = reportdate

    def __str__(self):
         return "Offense:" + self.offense + " ReportDate: " + str(self.reportdate)
