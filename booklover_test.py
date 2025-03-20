import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        lover = BookLover('Kyle', 'kyle_email@gmail.com', 'History')
        lover.add_book('Empire of the Summer Moon', 4)

        expected = 1
        self.assertEqual(lover.num_books, expected)
        self.assertTrue('Empire of the Summer Moon' in lover.book_list['book_name'].tolist())

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        lover = BookLover('Kyle', 'kyle_email@gmail.com', 'History')
        lover.add_book('Empire of the Summer Moon', 4)
        lover.add_book('Empire of the Summer Moon', 4)

        expected = 1
        self.assertEqual(lover.num_books, expected)
        self.assertTrue('Empire of the Summer Moon' in lover.book_list['book_name'].tolist())

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        lover = BookLover('Kyle', 'kyle_email@gmail.com', 'History')
        lover.add_book('Empire of the Summer Moon', 4)

        self.assertTrue(lover.has_read('Empire of the Summer Moon'))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        lover = BookLover('Kyle', 'kyle_email@gmail.com', 'History')
        lover.add_book('Empire of the Summer Moon', 4)

        self.assertFalse(lover.has_read('1984'))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        lover = BookLover('Kyle', 'kyle_email@gmail.com', 'History')
        lover.add_book('Empire of the Summer Moon', 4)
        lover.add_book('1984', 3)
        lover.add_book('Sapiens: A Brief History of Humankind', 5)
        lover.add_book('Black Elk', 3)

        expected = 4
        self.assertEqual(lover.num_books, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        lover = BookLover('Kyle', 'kyle_email@gmail.com', 'History')
        lover.add_book('Empire of the Summer Moon', 4)
        lover.add_book('1984', 3)
        lover.add_book('Sapiens: A Brief History of Humankind', 5)
        lover.add_book('Black Elk', 3)

        favs = lover.fav_books()

        expected = 2
        self.assertEqual(len(favs), expected)

        for index, row in favs.iterrows():
            self.assertTrue(row['book_rating'] > 3)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)