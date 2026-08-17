from collections import OrderedDict


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = OrderedDict()
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.move_to_end(city, True)
        else:
            if len(cache) == cacheSize and cache:
                cache.popitem(False)
            cache[city] = 1
            answer += 5
    return answer