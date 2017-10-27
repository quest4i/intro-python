from datetime import date


now = date.today()
now_str = now.isoformat()
with open('today', 'wt') as output:
    print(now_str, file=output)


with open('today', 'rt') as input:
    today_string = 
