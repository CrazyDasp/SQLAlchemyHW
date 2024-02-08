import sqlalchemy as sq

DSN = 'postgresql://postgres:postgres@localhost:5432/SQLPy'

engine = sq.create_engine(DSN)
