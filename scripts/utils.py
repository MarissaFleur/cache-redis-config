import logging
import pickle
import redis

class RedisUtils:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, password: str = None):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            decode_responses=True
        )

    def get(self, key: str) -> any:
        try:
            return self.client.get(key)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error getting key {key}: {e}")
            return None

    def set(self, key: str, value: any, expire: int = 0) -> bool:
        try:
            return self.client.set(key, value, ex=expire)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error setting key {key}: {e}")
            return False

    def delete(self, key: str) -> bool:
        try:
            return self.client.delete(key)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error deleting key {key}: {e}")
            return False

    def hset(self, key: str, field: str, value: any) -> bool:
        try:
            return self.client.hset(key, field, value)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error setting hash field {field} for key {key}: {e}")
            return False

    def hget(self, key: str, field: str) -> any:
        try:
            return self.client.hget(key, field)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error getting hash field {field} for key {key}: {e}")
            return None

    def hdel(self, key: str, field: str) -> bool:
        try:
            return self.client.hdel(key, field)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error deleting hash field {field} for key {key}: {e}")
            return False

    def exists(self, key: str) -> bool:
        try:
            return self.client.exists(key)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error checking if key {key} exists: {e}")
            return False

    def keys(self, pattern: str) -> list:
        try:
            return self.client.keys(pattern)
        except redis.exceptions.RedisError as e:
            logging.error(f"Error getting keys matching pattern {pattern}: {e}")
            return []