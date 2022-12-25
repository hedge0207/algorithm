class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        words_logs = []
        digit_logs = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                digit_logs.append(log)
            else:
                words_logs.append(log)

        words_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return words_logs + digit_logs