import time
import redis

r = None
for i in range(5):  # retry 5 times
    try:
        r = redis.Redis(host='redis', port=6379)
        r.ping()  # check if Redis is ready
        break
    except redis.exceptions.ConnectionError:
        print("Redis not ready, retrying...")
        time.sleep(2)

if not r:
    raise Exception("Cannot connect to Redis")

count = r.incr('hits')
print(f"Hello, World! This app has been run {count} times.")
