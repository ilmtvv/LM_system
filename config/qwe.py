import datetime

now = datetime.datetime.now().astimezone(datetime.timezone.utc)
date = datetime.datetime(2024, 3, 29, 12, 54, 21, 614310, tzinfo=datetime.timezone.utc)


print(now)
print(date)
print(now - date)
print(datetime.timedelta(days=31))
print(datetime.timedelta(days=31) >= now - date)
