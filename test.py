import data
from main import BooksCollector
import pytest


class TestBooksCollector:
    def test_new_book_collector_default_books_genre_is_empty(self):
        default_book_collector = BooksCollector()
        assert default_book_collector.get_books_genre() == {}

    def test_new_book_collector_default_favorites_is_empty(self):
        default_book_collector = BooksCollector()
        assert default_book_collector.get_list_of_favorites_books() == []

    def test_add_new_book_increase_books_genre(self, new_book_collector):
        len_before = len(new_book_collector.get_books_genre())
        new_book_collector.add_new_book('test')
        len_after = len(new_book_collector.get_books_genre())
        assert len_before < len_after

    @pytest.mark.parametrize(
            'book_name',['','41_symbol_name_test_'*2+'!']
    )
    def test_add_new_book_min_max_name_len_not_changin_len(self, book_name, new_book_collector):
        len_before = len(new_book_collector.get_books_genre())
        new_book_collector.add_new_book(book_name)
        len_after = len(new_book_collector.get_books_genre())
        assert len_before == len_after

    @pytest.mark.parametrize(
            'book_genre',data.pre_set_genre
    )
    def test_set_book_genre_upadates_book_genre(self, new_book_collector, book_genre):
        book_name = 'Sample_book'
        new_book_collector.add_new_book(book_name)
        new_book_collector.set_book_genre(book_name, book_genre)
        assert new_book_collector.get_book_genre(book_name) != None

    def test_get_book_genre_book_name_returns_genre(self, new_book_collector):
        book_name = 'Sample_book'
        book_genre = 'Детективы'
        new_book_collector.add_new_book(book_name)
        new_book_collector.set_book_genre(book_name, book_genre)
        assert new_book_collector.get_book_genre(book_name) == book_genre

    @pytest.mark.parametrize(
            'book_genre',data.pre_set_genre
    )
    def test_get_books_with_specific_genre_returns_book_names(self, new_book_collector, book_genre):
        book_name = 'Sample_book'
        new_book_collector.add_new_book(book_name)
        new_book_collector.set_book_genre(book_name, book_genre)
        assert new_book_collector.get_books_with_specific_genre(book_genre) == [book_name]
        
    def test_get_books_for_children_filter_book_by_genre_age_rating(self, generate_all_books):
        children_books = generate_all_books.get_books_for_children()
        for children_book in children_books:
            assert generate_all_books.get_book_genre(children_book) not in data.pre_set_genre_age_rating

    def test_add_book_in_favorites_add_book_to_favorites_list(self, generate_all_books):
        generate_all_books.add_book_in_favorites(data.default_book_names[0])
        assert generate_all_books.get_list_of_favorites_books() == [data.default_book_names[0]]

    def test_add_book_in_favorites_increase_favorites_list(self, generate_all_books):
        len_before = len(generate_all_books.get_list_of_favorites_books())
        generate_all_books.add_book_in_favorites(data.default_book_names[0])
        len_after = len(generate_all_books.get_list_of_favorites_books())
        assert len_before < len_after

    def test_delete_book_from_favorites_decrease_favorites_list(self, generate_all_books):
        generate_all_books.add_book_in_favorites(data.default_book_names[0])
        len_before = len(generate_all_books.get_list_of_favorites_books())
        generate_all_books.delete_book_from_favorites(data.default_book_names[0])       
        len_after = len(generate_all_books.get_list_of_favorites_books())
        assert len_before > len_after