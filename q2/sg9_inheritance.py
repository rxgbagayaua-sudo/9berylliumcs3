class Publication: #Create the class Publication
    def __init__(self, title:str, author:str): #initializes the attributes of the objects of the Publication Class
        self.__title = title #stores the title attribute for the created object
        self.__author = author #stores the author attribute for the created object

    def get_title(self): #defines the getter method to return the title of the created object of the Publication class
        return self.__title #returns the title of the created object of the Publication class
    
    def get_author(self): #defines the getter method to return the author of the created object of the Publication class
        return self.__author #returns the author of the created object of the Publication class
    
    def set_title(self, title:str): #defines the setter method to change or set the value to the title attribute for the created object of the Publication class
        self.__title = title #sets or changes the title of the created object of the Publication class

    def set_author(self, author:str): #defines the setter method to change or set the value to the author attribute for the created object of the Publication class
        self.__author = author #sets or changes the author of the created object of the Publication class

    def display_info(self): #defines the method to display the information of the created object of the Publication Class
        print("Title:", self.__title) #prints the title of the created object of the Publication Class
        print("Author:", self.__author) #prints the author of the created object of the Publication class

class Book(Publication): #Create the class Book, which inherits from Publicatiom
    def __init__(self,title:str,author:str,number_of_pages:int):
        super().__init__(title,author) #calls the initializer in the PUblication class to set up the tile and author attribute within the Book Class
        self.__number_of_pages = number_of_pages
        
    def get_number_of_pages(self):
        return self.__number_of_pages
    
    def set_number_of_pages(self,number_of_pages:int):
        if number_of_pages < 0:
            print("The number of pages must be positive")
        else:
            self.__number_of_pages = number_of_pages

class Magazine(Publication):
    def __init__(self, title:str, author:str, issue_number:int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self,issue_number):
        if issue_number <= 0:
            print("The issue number must be positive")
        else:
            self.__issue_number = issue_number

pub1 = Publication("Journal of Experimental Psychology","Ratchiff R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("=====Library Information=====")

print("\n===Publication Information===")
pub1.display_info()

print("\n===Book Information===")
book1.set_number_of_pages(-310)
book1.display_info()
print("Number of pages:",book1.get_number_of_pages())

print("\n===Magazine Information===")
mag1.display_info()
print("Issue Number:",mag1.get_issue_number())
