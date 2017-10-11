from datetime import datetime

now = datetime.now()
print(now, type(now))

dt = datetime(2017, 10, 20, 14, 20, 30)
print(dt)
print(dt.timestamp())