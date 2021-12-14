import random
import json
from faker import Faker

from conf import MODEL


faker = Faker()


def main():
    for_write = next(gen_list(1))
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(for_write, indent=4, ensure_ascii=False))
        

def title():
    with open("books.txt", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def year():
    year_in = random.randint(1800, 2021)
    yield year_in


def pages():
    pages_in = random.randint(1, 300)
    yield pages_in


def isbn13():
    isbn13_in = faker.isbn13()
    yield isbn13_in


def rating():
    rating_in = random.uniform(0.0, 5.0)
    yield rating_in


def price():
    price_in = random.uniform(5.0, 1000.0)
    yield round(price_in)


def author():
    author_in = faker.name()
    yield author_in


def gen_list():
    list_gen = []
    book_generator = book_gen(1)
    for i in range(100):
        list_gen.append(next(book_generator))
        
    yield list_gen
    
    
def book_gen(pk=1):
    while True:
        book_dict = {
            "model": MODEL, 
            "pk": pk, 
            "Title": next(title()), 
            "year": next(year()),  
            "pages": next(pages()), 
            "isbn13": next(isbn13()), 
            "rating": next(rating())
        }
        yield book_dict
        pk += 1


if __name__ == "__main__":
    main()

