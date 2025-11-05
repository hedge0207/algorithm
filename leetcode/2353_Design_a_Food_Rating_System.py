import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self._food_to_rating = {}
        self._food_to_cuisine = {}
        self._cuisines_to_ratings = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine in self._cuisines_to_ratings:
                heapq.heappush(self._cuisines_to_ratings[cuisine], (-rating, food))
            else:
                self._cuisines_to_ratings[cuisine] = [(-rating, food)]
            self._food_to_rating[food] = [rating, cuisine]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self._food_to_rating[food][1]
        self._food_to_rating[food] = [newRating, cuisine]
        heapq.heappush(self._cuisines_to_ratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while len(self._cuisines_to_ratings[cuisine]) != 0:
            rating, food = heapq.heappop(self._cuisines_to_ratings[cuisine])
            if self._food_to_rating[food][0] == -rating:
                heapq.heappush(self._cuisines_to_ratings[cuisine], (rating, food))
                return food