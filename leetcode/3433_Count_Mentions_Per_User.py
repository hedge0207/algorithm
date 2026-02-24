class Solution:
    def _set_var(self, num_users):
        self._num_users = num_users
        self._ans = [0] * num_users
        self._offline_time = [0] * num_users

    def _handle_offline(self, time: str, user_id: str):
        self._offline_time[int(user_id)] = int(time)

    def _handle_mention(self, time: str, users: str):
        time = int(time)
        for user in users.split():
            if user == "ALL":
                for i in range(self._num_users):
                    self._ans[i] += 1
            elif user == "HERE":
                for i in range(self._num_users):
                    if self._offline_time[i] != 0 and self._offline_time[i] + 60 <= time:
                        self._offline_time[i] = 0
                    if self._offline_time[i] == 0:
                        self._ans[i] += 1
            else:
                idx = int(user[2:])
                self._ans[idx] += 1

    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        self._set_var(numberOfUsers)
        events.sort(key=lambda x:(int(x[1]), -ord(x[0][0])))
        for event in events:
            print(event)
            type_, time, target = event
            if type_ == "OFFLINE":
                self._handle_offline(time, target)
            else:
                self._handle_mention(time, target)

        return self._ans