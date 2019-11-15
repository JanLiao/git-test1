import redis

r = redis.Redis(host='10.22.19.21', port=6379)
v = r.get('hello')
print(v)