from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('postgresql://matthew:password@localhost:5432/test')

Base = declarative_base()

class cars(Base):
    __tablename__ = 'mtcars'

    car = Column(String, primary_key=True)
    mpg = Column(Float)
    wt = Column(Float)

    def __repr__(self):
       return "<cars(car='%s', mpg='%s', wt='%s')>" % (
                            self.car, self.mpg, self.wt)
   
#cars.__table__ 
#Table('users', MetaData(bind=None),
#    Column('car', String(), table=<users>, primary_key=True, nullable=False)
#    Column('mpg', Float, table=<users>),
#    Column('wt', Float, table=<users>)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = db)

session = Session()

# Now create an instance and work on it

foo = cars(car = 'Fiat Uno', mpg = '50', wt = '75')
session.add(foo)
session.commit()

# Example queries

foo_q = session.query(cars).filter(cars.wt > 2.465)

foo_q.all()

foo_q1 = foo_q.filter(cars.mpg < 20).all()

foo_q2 = foo_q.filter(cars.mpg < 20).filter(cars.car.contains('Merc')).all()
