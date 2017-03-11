# coding: utf-8
get_ipython().magic('run sqlalchemy.py')
get_ipython().magic('paste sqlalchemy.py')
get_ipython().magic('copy sqlalchemy.py')
get_ipython().magic('run sqlalchemy.py --help')
sqlalchemy.create_engine('postgresql://localhost:5432')
from sqlalchemy import *
create_engine('postgresql://localhost:5432')
get_ipython().system('pip install psycopg2')
create_engine('postgresql://localhost:5432')
db.echo =False
db = create_engine('postgresql://localhost:5432')
db
metadata = BoundMetaData(db)
metadata = BoundMetaData(db)
metadata = sqlalchemy.BoundMetaData(db)
metadata = BoundMetaData(db)
get_ipython().magic('write bla.py')
