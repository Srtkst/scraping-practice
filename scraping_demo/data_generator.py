import random
from faker import Faker

fake = Faker("ja_JP")

def generate_products(n=10):
    return [{
        "title": fake.word(),
        "price": f"¥{random.randint(1000, 5000)}"
    } for _ in range(n)]

def generate_article():
    return {
        "title": fake.sentence(),
        "author": fake.name(),
        "date": fake.date(),
        "content": fake.paragraph(nb_sentences=5)
    }

def generate_reviews(n=5):
    return [{
        "name": fake.name(),
        "rating": random.randint(1, 5),
        "comment": fake.text(max_nb_chars=100)
    } for _ in range(n)]
