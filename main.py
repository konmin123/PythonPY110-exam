import random
import json

from faker import Faker

from conf import MODEL


faker = Faker()

list_for_title = []

iter_for_title = iter(list_for_title)


def main():
    with open("books.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_for_title.append(line.strip())
    for_write = next(gen_list())
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(for_write, indent=4, ensure_ascii=False))


def title() -> str:
    return next(iter_for_title)


def year() -> int:
    year_in = random.randint(1800, 2021)
    return year_in


def pages() -> int:
    pages_in = random.randint(1, 300)
    return pages_in


def isbn13() -> str:
    isbn13_in = faker.isbn13()
    return isbn13_in


def rating() -> float:
    rating_in = random.uniform(0.0, 5.0)
    return rating_in


def price() -> float:
    price_in = random.uniform(5.0, 1000.0)
    return round(price_in, 2)


def author() -> str:
    author_ = faker.name()
    return author_


def gen_list() -> list:
    list_gen = []
    book_generator = book_gen(1)
    for i in range(100):
        list_gen.append(next(book_generator))

    yield list_gen


def book_gen(pk=1) -> dict:
    while True:
        book_dict = {
            "model": MODEL,
            "pk": pk,
            "Title": title(),
            "year": year(),
            "pages": pages(),
            "price": price(),
            "isbn13": isbn13(),
            "authors": author()+", "+author(),
            "rating": rating()
        }
        yield book_dict
        pk += 1


if __name__ == "__main__":
    main()
