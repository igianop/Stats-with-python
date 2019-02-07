import requests
import sys
from itertools import islice
import pprint


url = "https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=stackoverflow&filter=!9Z(-x)63B"

fromdate = sys.argv[1]
todate = sys.argv[2]

params = {
  'fromdate': fromdate,
  'todate': todate
 }

r = requests.get(url, params=params).json()


a, e = 0, 0
d = {}
re = []
t = []

for i in range(len(r['items'])):
    q = r['items'][i]['score']
    p = [r['items'][i]['is_accepted']]
    d = [r['items'][i]['score'], r['items'][i]['comment_count'], r['items'][i]['answer_id']]
    for d in d:
        re = [r['items'][i]['answer_id'], r['items'][i]['comment_count']]
    t.append(re)
    if p.count(True) == 1:
           e = q + e
           a = a + 1


t.sort(reverse=True)
o = list(islice(t, 10))

v = {'total_accepted_answers:': a, 'top_ten_answers_comment_count:': o,
                 'accepted_answers_average_score:': (float(e/a))}
pprint.pprint(v)
