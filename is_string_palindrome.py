import re

def is_string_palindrome(str):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]','', str.lower())
    return cleaned_string == cleaned_string[::-1]

print(is_string_palindrome("Go hang a salami I'm a lasagna hog.")) # True
print(is_string_palindrome("Was it a rat I saw?")) # True
print(is_string_palindrome("Step on no pets")) # True
print(is_string_palindrome("Sit on a potato pan, Otis")) # True
print(is_string_palindrome("Lisa Bonet ate no basil")) # True