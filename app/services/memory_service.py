import redis

r = redis.Redis(host='localhost', port=6379)

def save_chat(user_id, message):
    r.rpush(user_id, message)

def get_chat(user_id):
    return r.lrange(user_id, 0, -1)