class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [0] * len(rooms)
        visited[0] = 1
        queue = rooms[0]
        while queue:
            new_queue = []
            for next_room in queue:
                if visited[next_room] == 1:
                    continue
                new_queue += rooms[next_room]
                visited[next_room] = 1
            queue = new_queue

        return all(visited)