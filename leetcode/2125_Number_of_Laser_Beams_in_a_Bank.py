class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        last_num_devices = 0
        for row in bank:
            num_device = row.count("1")
            if num_device == 0:
                continue
            ans += num_device * last_num_devices
            last_num_devices = num_device
        return ans