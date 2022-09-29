import redis

class SetRedisHost:
    def __init__(self, settings):
        self.redis_client = redis.Redis(
            host = settings.REDIS_HOST,
            port = settings.REDIS_PORT,
            ssl = settings.REDIS_SSL,
            password = settings.REDIS_PASSWORD,
            connection_pool = settings.REDIS_POOL)
