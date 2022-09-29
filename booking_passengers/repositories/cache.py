import redis
from utils.login_redis import SetRedisHost
from datetime import timedelta


class CacheRepository(SetRedisHost):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings

    def get(self, key: str):
        result = self.redis_client.get(key)
        return result
    
    def set(self, key, value, expiration_time=timedelta(seconds=1800)):
        return self.redis_client.set(key,value,expiration_time)
    
    def delete(self, key: str):
        self.redis_client.delete(key)

    def is_cache(self, key:str):
        result = False
        try:
            if self.get(key):
                result = True
            else:
                self.set(key, "True")
                result = False
        except:
            """Si el cache llegara a fallar deja procesar la reserva"""
            result = False
        return result

        



