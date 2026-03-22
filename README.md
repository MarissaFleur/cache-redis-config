# cache-redis-config
=======================

## Description
---------------

A modular and configurable Redis cache configuration management tool for your Node.js applications. This software provides a simple and intuitive interface for setting up and managing Redis cache servers.

## Features
------------

* **Modular Architecture**: cache-redis-config is designed to be highly extensible and customizable, allowing you to add new Redis providers and cache strategies as needed.
* **Redis Connections Management**: Easily connect to and manage multiple Redis instances with a unified interface.
* **Cache Strategies**: Choose from a variety of cache strategies, including `cache-redis` (a simple cache), `cache-redis-cluster` (for Redis clusters), `cache-redis-sentinel` (for Redis Sentinel), and custom strategies.
* **Configurable Options**: Configuration options are available for Redis client settings, cache expiration, and more.

## Technologies Used
-------------------

* **Node.js**: cache-redis-config is built with Node.js and uses the latest versions of the following dependencies:
	+ [redis](https://www.npmjs.com/package/redis)
	+ [cache-manager](https://www.npmjs.com/package/cache-manager)
	+ [ioredis](https://www.npmjs.com/package/ioredis)
* **ES6+**: cache-redis-config uses modern JavaScript features for a cleaner, more maintainable codebase.

## Installation
--------------

To get started with cache-redis-config, run the following command in your terminal:

```bash
npm install cache-redis-config
```

### Usage

```javascript
const cacheRedisConfig = require('cache-redis-config');

const cache = cacheRedisConfig.create({
  providers: [
    {
      connector: 'redis',
      host: 'localhost',
      port: 6379,
    },
  ],
  cacheStrategy: 'cache-redis',
  options: {
    maxConnections: 10,
  },
});

const cacheManager = cache.getCacheManager();
```

### Example Use Cases:

* Create a new Redis connection instance with a specific cache strategy
```javascript
const cache = cacheRedisConfig.create({
  providers: [
    {
      connector: 'redis',
      host: 'localhost',
      port: 6379,
    },
  ],
  cacheStrategy: 'cache-redis-cluster',
});
```

* Use a custom cache strategy
```javascript
const cache = cacheRedisConfig.create({
  providers: [
    {
      connector: 'redis',
      host: 'localhost',
      port: 6379,
    },
  ],
  cacheStrategy: 'my-cache-strategy',
});
```

### Development

If you'd like to contribute to the development of cache-redis-config, please feel free to fork this repository and submit a pull request with your changes.

### License

cache-redis-config is licensed under the MIT License.

### Author

cache-redis-config was created by [Your Name].