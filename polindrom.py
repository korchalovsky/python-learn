def get_palindrome(s, start, end):
    while end + 1 < len(s) and s[end + 1] == s[start]:
        end += 1

    while start > 0 and end + 1 < len(s) and s[end + 1] == s[start - 1]:
        start -= 1
        end += 1

    return s[start:end + 1]


def longest_palindrome(str):
    long = []
    for i in range(len(str)):
        candidate = get_palindrome(str, i, i)

        if len(candidate) > len(long):
            long = candidate

    return print(long)
