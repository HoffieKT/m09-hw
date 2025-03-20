import pandas as pd

class BookLover():

    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self, book_name, rating):
        if (rating < 0) or (rating > 5):
            print('Book has not been added. Rating needs to be an integer from 0 to 5.')
        else:
            if book_name not in self.book_list['book_name'].tolist():
                new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
                self.num_books+=1
            else:
                print(str(book_name) + ' is already in the list.')

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].tolist()

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list.loc[self.book_list['book_rating'] > 3]
