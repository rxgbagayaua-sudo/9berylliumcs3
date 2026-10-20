class Publication:
    def __init__(self, title:str, author:str):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def set_title(self, title:str):
        self.__title = title

    def set_author(self, author:str):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)

class Book(Publication):
    def __init__(self,title:str,author:str,number_of_pages:int):
        super().__init__(title,author)
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
