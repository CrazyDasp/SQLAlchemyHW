from models import Publisher, Book, Shop, Sale, Stock
from datetime import datetime
from __connect__ import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def get_shops(info):
    publisher = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale
    ).select_from(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher).\
        join(Sale)
    if info.isdigit():
        publisher = publisher.filter(Publisher.id == info).all()
    else:
        publisher = publisher.filter(Publisher.name == info).all()
    
    for title, shop_name, price, date in publisher:
        print(f"{title:<40} | {shop_name:<10} | {price:<8} | {date.strftime('%d-%m-%Y')}")

if __name__ == '__main__':
    info = input('Введите имя или id публициста: ')
    get_shops(info)