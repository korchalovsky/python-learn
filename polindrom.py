def get_palindrome(str, start, end):
    while end + 1 < len(str) and str[end + 1] == str[start]:
        end += 1

    while start > 0 and end + 1 < len(str) and str[end + 1] == str[start - 1]:
        start -= 1
        end += 1

    return str[start:end + 1]


def longest_palindrome(str):
    long = []
    for i in range(len(str)):
        candidate = get_palindrome(str, i, i)

        if len(candidate) > len(long):
            long = candidate

    return print(long)
