import urllib.request as rq
import json
response = rq.urlopen('https://xxx/review_portal/bo/v1/reports/reviews')
body = response.read()
json_obj = json.loads(body)
print(body)
print(json_obj)
print('this a code ' + json_obj['code'])