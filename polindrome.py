def get_palindrome(string, start, end):
    while end + 1 < len(string) and string[end + 1] == string[start]:
        end += 1

    while start > 0 and end + 1 < len(string) and string[end + 1] == string[start - 1]:
        start -= 1
        end += 1

    return string[start:end + 1]


def longest_palindrome(string):
    long = []
    for i in range(len(string)):
        candidate = get_palindrome(string, i, i)

        if len(candidate) > len(long):
            long = candidate

    return print(long)