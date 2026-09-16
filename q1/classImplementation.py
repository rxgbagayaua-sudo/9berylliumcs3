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
     print(activity, "has been scheduled for", self.name)

    def updateMembers(self, amount):
        self.__noOfMembers += amount

    def getNoOfMembers(self):
       return self.__noOfMembers

club1 = clubs("Polaris", "Gerald Paz", 40, True)
club2 = clubs("Agham Radio Club", "JC Bartolae", 20, True)

print("---BEFORE---")
print("Object 1: ", club1.name,"-",club1.adviser, "-", club1.getNoOfMembers(), "members")
print("Object 2: ", club2.name,"-",club2.adviser, "-", club2.getNoOfMembers(), "members")

print("\nRemoving 3 members from", club1.name)
club1.updateMembers(-3)

print("\n---AFTER---")
print("Object 1: ", club1.name,"-",club1.adviser, "-", club1.getNoOfMembers(), "members")
print("Object 2: ", club2.name,"-",club2.adviser, "-", club2.getNoOfMembers(), "members")
