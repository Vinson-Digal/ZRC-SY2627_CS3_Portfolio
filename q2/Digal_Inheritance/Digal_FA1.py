class Publication:
    """Parent class: every library material has a title and an author."""

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    """Child class of Publication. A book also has a number of pages."""

    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = None  
        self.set_number_of_pages(number_pages)  

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        """Accept only positive whole numbers; otherwise keep the old value."""
        if not isinstance(number_pages, int):
            print("Number of pages must be a whole number.")
        elif number_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.__number_of_pages = number_pages

    def display_info(self):
        super().display_info()  
        print(f"Number of pages: {self.__number_of_pages}")


class Magazine(Publication):
    """Child class of Publication. A magazine also has an issue number."""

    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        """Accept only positive whole numbers; otherwise keep the old value."""
        if not isinstance(issue_number, int):
            print("Issue number must be a whole number.")
        elif issue_number <= 0:
            print("Issue number must be positive.")
        else:
            self.__issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.__issue_number}")

if __name__ == "__main__":
    pub1 = Publication("Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H.")
    pub2 = Publication("Introduction to Algorithms", "Cormen, T. et al.")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = Book("Noli Me Tangere", "Jose Rizal", 438)
    mag1 = Magazine("National Geographic", "Various Authors", 202)
    mag2 = Magazine("TIME", "Various Authors", 45)

    print("Publication Information:")
    pub1.display_info()
    print()
    pub2.display_info()

    print("\nBook Information:")
    book1.set_number_of_pages(-310) 
    book1.display_info()
    print(book1.get_number_of_pages())
    print()
    book2.display_info()

    print("\nMagazine Information:")
    mag1.display_info()
    print(mag1.get_issue_number())
    print()
    mag2.set_issue_number(0)  
    mag2.display_info()
