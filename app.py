import redis

# Connect to Redis (host = service name in docker-compose.yml)
r = redis.Redis(host='redis', port=6379)

# Increment a counter
count = r.incr('hits')

print(f"Hello, World! This app has been run {count} times.")
