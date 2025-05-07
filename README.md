# SPRINT 4

## Описание тестов
1. `test_new_book_collector_default_books_genre_is_empty` - проверка создания нового класса с пустым значением `books_genre`
2. `test_new_book_collector_default_favorites_is_empty` - проверка создания нового класса с пустым значением `favorites`
3. `test_add_new_book_increase_books_genre` - функция `add_new_book` должна увеличивать длину словаря `books_genre`
4. `test_add_new_book_min_max_name_len_not_changin_len` - параметризированный тест на проверку валидации входных параметров функции `add_new_book`. Передается пустая строка и строка длиной 41 символ. Ожидается что длина словаря `books_genre` не изменится.
5. `test_set_book_genre_upadates_book_genre` - параметризированный тест функции `set_book_genre`. Тест добваляет новую книгу и получает её жанр с помощью функции `get_book_genre`.
6. `test_get_book_genre_book_name_returns_genre` - тест проверки возвращаегомого значения функции `get_book_genre`.
7. `test_get_books_with_specific_genre_returns_book_names` - параметризированный тест функции `get_books_with_specific_genre`. Тест добавляет новую книгу и получает её название по жанру.
8. `test_get_books_for_children_filter_book_by_genre_age_rating` - тест создает книги всех типов жанров, проверяет что книги полученные в функции `get_books_for_children` не попадают под возрастные ограничения.
9. `test_add_book_in_favorites_add_book_to_favorites_list` - тест добавления книги в избранный список, проверяется увелечение списка `favorites`.
10. `test_get_list_of_favorites_books_retuns_book_names` - проверка возвращаемого значения функции `get_list_of_favorites`, проверяется что возвращаемое название книги соответсвует переданному в функцию `add_book_in_favorites`.
11. `test_add_book_in_favorites_increase_favorites_list` - добавление книги в избранный список должно увеличить длину списка.
12. `test_delete_book_from_favorites_decrease_favorites_list` - удаление книги в избранный список должно уменьшать длину списка.
13. `test_get_books_genre_returns_books_genre` - тест проверки возвращаемого значения функции `get_books_genre`. Через фикстуру создаются книги всех жанров.


## Покрытие тестами
Для оценки покрытия тестами можно использовать следущуюю комнаду
```shell
pytest test.py --cov --cov-branch --cov-report=html 
```