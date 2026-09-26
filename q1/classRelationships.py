class Member:
    def __init__(self, name, grade_level, role):
        self.name = name
        self.grade_level = grade_level
        self.role = role

    def display_info(self):
            return f"{self.name} | Grade {self.grade_level} | {self.role}"

class Club:
    def __init__(self, name, adviser, no_of_member, active_status):
        self.name = name
        self.adviser = adviser
        self.__number_of_members = 0
        self.active_status = active_status

        self.members = []

    def display_info(self):
            print("Club Name: ", self.name)
            print("Adviser: ", self.adviser)
            print("Number of Members: ", self.__number_of_members)
            print("Active Status: ", self.active_status)

    def add_member(self, member):
         self.members.append(member)
         self.__number_of_members += 1

    def get_number_of_members(self):
           return self.__number_of_members

    def display_members(self):
         for member in self.members:
              print(member.display_info())

club1 = Club("Polaris", "Gerald Paz", 0, True)

member1 = Member("Chrissy", 11, "President")

member2 = Member("JoJo", 7, "Ordinary Member")

member3 = Member("Rafael", 9, "Sgt. At Arms")

print("---Before Relationship---")
club1.display_info()

print("\nMember objects have been created:")
print(member1.display_info())
print(member2.display_info())
print(member3.display_info())

print("\n---Building Relationship")
print("Adding Members to", club1.name,"...")

club1.add_member(member1)
club1.add_member(member2)
club1.add_member(member3)

print("\n---After Relationship---")

club1.display_info()

print("\nMembers of",club1.name,":")

club1.display_members()