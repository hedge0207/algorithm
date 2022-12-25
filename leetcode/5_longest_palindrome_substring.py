def longestPalindrome(s: str) -> str:
    longest_palindrome = ""
    n = len(longest_palindrome)
    for i in range(len(s)):
        for j in range(i, len(s)):
            word = s[i:j+1]
            word_len = len(word)
            # 시간 제약에 맞추기 위해 추가한 코드
            # 그럼에도 턱 걸이로 통과했다.
            if word_len < n:
                continue
            if word == word[::-1] and word_len > n:
                longest_palindrome = word
                n = word_len
    return longest_palindrome


# best practice
def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int):
        # 회문을 찾으면 회문으로부터 좌우로 한 칸씩 확장시키면서 최대 길이의 회문을 찾는다.
        while s[left] == s[right] and left >= 0 and right < len(s):
            left -= 1
            right += 1
        return s[left + 1:right]

    # s가 한 자리 문자거나, 그 자체로 회문이면 바로 return
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    for i in range(len(s)-1):
        # 회문이 짝수인 경우(expand(i, i + 1))와 홀수인 경우(expand(i, i + 2))를 중 최댓값을 구한다.
        # 짝수 포인터와 홀수 포인터가 슬라이딩 윈도우처럼 앞으로 나아간다.
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

