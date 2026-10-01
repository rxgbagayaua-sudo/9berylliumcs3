class Member:
  def __init__(self, name, grade_level, role):
    self.name = name
    self.grade_level = grade_level

  def display_info(self):
    return f"{self.name} | Grade {self.grade_level} | {self.role}"
      
class Officer(Member):
  def __init__(self, name, grade_level, position):
    super().__init__(name, grade_level)
    self.position = position
  def display_info(self):
   return f"{self.name} | Grade {self.grade_level} | {self.position}"

class Adviser:
  def __init__(self, name, department):
    self.name = name
    self.department = department
  def display_info(self):
    return f"{self.name} | {self.department}"

class Club:
    def __init__(self, name, adviser, active_status):
      self.name = name
      self.active_status = active_status
      self.adviser = adviser
      self.members = []
    def add_members(self, member):
      self.members.append(member)
    def display_info(self)
      print("Club Name: ", self.name)
      print("Adviser: ", self.adviser.name)
      print("Department:", self.adviser.department)
      print("Number of Members: ", len(self.members))
      print("Active Status: ", self.active_status)
    def display_members(self):
      for member in self.members:
        print(member.display_info())

adviser1 = Adviser("Geralf Paz", "Science Department")
club1 = Club("Polaris, adviser1, True")
member1 = Member("JoJo", 7)
officer1 = Officer("Chrissy", 10, "President")
officer2 = Officer("Rafael", 9, "Sgt at Arms")
      
  
