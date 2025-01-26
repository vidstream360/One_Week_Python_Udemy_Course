def count_vowels(a):
    count = 0
    for vowel in a:
        if vowel in "aeiou":
            count += 1
    return count

print(count_vowels("hell world"))