import requests as rq
print('please type the url below:')
url = input()
res = rq.head(url)
print(res.headers['Content-Length'])