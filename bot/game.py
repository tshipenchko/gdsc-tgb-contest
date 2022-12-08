from random import randint
from typing import List, Tuple


class GameDB:
    def __init__(self):
        self._storage = {}

    def increment_score(self, user_id: int, score: int = 1):
        self._storage[user_id] = self._storage.get(user_id, 0) + score

    def get_score(self, user_id: int) -> int:
        return self._storage.get(user_id, 0)

    def get_top(self, limit: int = 10) -> List[Tuple[int, int]]:
        return sorted(self._storage.items(), key=lambda x: x[1], reverse=True)[:limit]


class Game:
    def __init__(self):
        self._db = GameDB()
        self._current_number = randint(1, 101)

    def check_number(self, user_id: int, number: int) -> str:
        if number == self._current_number:
            self._db.increment_score(user_id)
            self._current_number = randint(1, 101)
            return "You won!"
        elif number >= self._current_number:
            return "Too big"
        else:
            return "Too small"

    def get_score(self, user_id: int) -> int:
        return self._db.get_score(user_id)

    def get_top(self, limit: int = 10) -> List[Tuple[int, int]]:
        return self._db.get_top(limit)
