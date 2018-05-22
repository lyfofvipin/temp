from collections import Counter
from collections import defaultdict
from collections import namedtuple
import datetime
import timeit
import re
import system
str = "my name is vipn and i am having a good headwritting and a pagl brother mota."
print(Counter(str))
print(Counter(str.split()))
dict = Counter(str.split())
dict.clear()
print(sum(dict.values()))
print(len(dict))
d = {}
d['one'] = [1]
d['one'].append(23)
print(d)
human = namedtuple('human','name ,age ,mob')
d = human('vipin','19','8875599241')
print(d.name)
t = datetime.time(8,3,29)
print(t)
today = datetime.date.today()
print(today.timetuple())
print(str)