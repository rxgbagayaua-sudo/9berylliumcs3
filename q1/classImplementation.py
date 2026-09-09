class clubs:
    def __init__(self, name, adviser, noOfMembers, activeStatus):
        self.name = name
        self.adviser = adviser
        self.__noOfMembers = noOfMembers
        self.activeStatus = activeStatus

    def displayInfo(self):
        print("Club Name: ", self.name)
        print("Adviser: ", self.adviser)
        print("Number of Members: ", self.noOfMembers)
        print("Active Status: ", self.activeStatus)

    def scheduleActivity(self, activity):
     print(Activity, "has been scheduled for", self.name)

    def updateMembers(self, amount):
        if self.__noOFMembers 

    def getNoOfMembers(self):
