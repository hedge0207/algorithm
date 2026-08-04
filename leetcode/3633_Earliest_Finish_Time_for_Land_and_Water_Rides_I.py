class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int],
                           waterDuration: list[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        min_land_time = float("inf")
        for i in range(n):
            if landStartTime[i] + landDuration[i] < min_land_time:
                min_land_time = landStartTime[i] + landDuration[i]

        min_water_time = float("inf")
        for i in range(m):
            if waterStartTime[i] + waterDuration[i] < min_water_time:
                min_water_time = waterStartTime[i] + waterDuration[i]

        land_time = sorted([i for i in range(n)], key=lambda x: landDuration[x])
        water_time = sorted([i for i in range(m)], key=lambda x: waterDuration[x])

        land_first = float("inf")
        for i in range(m):
            idx = water_time[i]
            if waterStartTime[idx] <= min_land_time:
                land_first = min(land_first, min_land_time + waterDuration[idx])
            else:
                land_first = min(land_first, waterStartTime[idx] + waterDuration[idx])

        water_first = float("inf")
        for i in range(n):
            idx = land_time[i]
            if landStartTime[idx] <= min_water_time:
                water_first = min(water_first, min_water_time + landDuration[idx])
            else:
                water_first = min(water_first, landStartTime[idx] + landDuration[idx])

        return min(land_first, water_first)
