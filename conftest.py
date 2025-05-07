import pytest
from main import BooksCollector
import data

@pytest.fixture(scope='function')
def new_book_collector():
    new_book_collector = BooksCollector()
    return new_book_collector

@pytest.fixture(scope='function')
def generate_all_books(new_book_collector):
    for index,book_name in enumerate(data.default_book_names):
        new_book_collector.add_new_book(book_name)
        new_book_collector.set_book_genre(book_name, data.pre_set_genre[index])
    return new_book_collector