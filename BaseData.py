from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Sale, Stock
from __connect__ import engine

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
publisher2 = Publisher(name='Достоевский')
publisher3 = Publisher(name='Гоголь')

session.add_all([publisher1, publisher2, publisher3])
session.commit()

book1 = Book(title='Сказка о царе Салтане', publisher=publisher1)
book2 = Book(title='Евгений Онегин', publisher=publisher1)

book3 = Book(title='Идиот', publisher=publisher2)
book4 = Book(title='Братья Карамазовы', publisher=publisher2)

book5 = Book(title='Ночь перед Рождеством', publisher=publisher3)
book6 = Book(title='Вий', publisher=publisher3)

session.add_all([book1, book2, book3, book4, book5, book6])
session.commit()

shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Комус')

session.add_all([shop1, shop2])
session.commit()

stock1 = Stock(book_id = book1.id, shop_id=shop1.id, count=30)
stock2 = Stock(book_id = book2.id, shop_id=shop2.id, count=45)
stock3 = Stock(book_id = book3.id, shop_id=shop1.id, count=26)
stock4 = Stock(book_id = book4.id, shop_id=shop2.id, count=54)
stock5 = Stock(book_id = book5.id, shop_id=shop1.id, count=12)
stock6 = Stock(book_id = book6.id, shop_id=shop2.id, count=7)

session.add_all([stock1, stock2, stock3, stock4, stock5, stock6])
session.commit()

sale1 = Sale(price=400, date_sale='10-5-2023', stock_id=stock1.id, count=1)
sale2 = Sale(price=400, date_sale='18-6-2023', stock_id=stock2.id, count=3)
sale3 = Sale(price=400, date_sale='24-6-2023', stock_id=stock3.id, count=4)
sale4 = Sale(price=400, date_sale='13-7-2023', stock_id=stock4.id, count=2)
sale5 = Sale(price=400, date_sale='19-7-2023', stock_id=stock5.id, count=1)
sale6 = Sale(price=400, date_sale='19-7-2023', stock_id=stock6.id, count=1)
sale7 = Sale(price=400, date_sale='24-7-2023', stock_id=stock1.id, count=3)
sale8 = Sale(price=400, date_sale='01-8-2023', stock_id=stock2.id, count=6)
sale9 = Sale(price=400, date_sale='15-8-2023', stock_id=stock3.id, count=1)
sale10 = Sale(price=400, date_sale='19-9-2023', stock_id=stock4.id, count=1)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10])
session.commit()

session.close