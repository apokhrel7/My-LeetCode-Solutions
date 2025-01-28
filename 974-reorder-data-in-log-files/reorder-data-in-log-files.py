class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        output = []

        for stuff in logs:
            if stuff.split(' ')[1].isalpha():
                letter_logs.append(stuff)
            else:
                digit_logs.append(stuff)

        
        sorted_letter_logs = sorted(letter_logs, key=lambda x:(x.split(' ', 1)[1], x.split(' ', 1)[0]))

        return sorted_letter_logs + digit_logs