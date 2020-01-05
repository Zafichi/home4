def check_palindrome(some_str):
    if some_str.lower().replace(' ', '') == some_str.lower().replace(' ', '')[::-1]:
        return True
    else:
        return False


print(check_palindrome('Never odd or even'))
