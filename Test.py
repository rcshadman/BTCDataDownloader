import DataBase
import datetime
import pandas as pd

db=DataBase.MongoDB('localhost',8001)
dbf = db.get_collection('BitfinexUSD2')
d = datetime.datetime(2017, 6, 18, 0)
d2 = datetime.datetime(2017,6,19,0)
print(d)
t1=datetime.datetime.now()
p_a21 = dbf.find({"lu":{"$gt":d}}).sort("lu")
print(p_a21.count())
t_a21 = pd.DataFrame(list(p_a21))
t2=datetime.datetime.now()
print(len(t_a21))
print(t2-t1)