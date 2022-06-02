import arrow
from datetime import datetime, timedelta

print('\n#####################################################')
# Date time basics

# input manual date
d = datetime(2010, 7, 4, 12, 15, 58)
# date of today
d = datetime.now()
print(f"Format of date variable: {type(d)}")
print(f"Print date var directly: {d}")

# first way formatting
sDate = '{:%Y-%m-%d %H:%M:%S}'.format(d)
print(f"Formated date variable type: {type(sDate)}")
print(f"String date printed: {sDate}")

# second way formatting
sDate2 = d.strftime('Local date foramt: %x | Local time format: %X')
print(f"Formated date variable type: {type(sDate2)}")
print(f"String date printed: {sDate2}")

print('\n#####################################################')
# parsing dates with strptime

# first way
sDate = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
print(f"1st way = Var format: {type(sDate)} | Parsed date:", sDate)

# second way
sDate = datetime.fromisoformat("2012-12-12 10:10:10")
print(f"2nd way = Var format: {type(sDate)} | Parsed date:", sDate)

print('\n#####################################################')
# timedelta

d1 = datetime(1983, 1, 17)
d2 = datetime(2022, 4, 21)
delta = d2 - d1
print(f"Date delta between {d1} and {d2} is equal to: {delta}")
delta = d2 + timedelta(days=10)
print(f"Date {d2} + 10 days equals to: {delta}")

print('\n#####################################################')
# using arrow library to humanize dates
# pip install -U arrow

t1 = arrow.Arrow(2021, 1, 23)  # manual method
print("Arrow: manual date: ", t1.format('YYYY-MM-DD'))
t2 = arrow.get(d1)
print("Arrow: taking datetime object: ", t2.format('YYYY-MM-DD'))
t3 = arrow.utcnow()  # gets utc
t3 = arrow.now()
# ZZZ prints "Hora oficial do Brasil"
print("Arrow: now:", t3.format('YYYY-MM-DD HH:mm:ss ZZ'))
print("Arrow: humanize now:", t3.humanize())
print(f"Arrow: humanize {t2.format('YYYY-MM-DD')}:", t2.humanize())
print(f"Arrow: humanize t1 var date {t1.format('YYYY-MM-DD')}:", t1.humanize())

# add or subtract days, months or...
t1 = t1.shift(months=5)
print(
    f"Arrow: Shift and humanize t1 var date {t1.format('YYYY-MM-DD')}:", t1.humanize())
