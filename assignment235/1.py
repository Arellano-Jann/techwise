def len_last_word(s: str) -> int:
    return len(s.rstrip().split(" ")[-1])# if len(s.split(" ")[-1]) > 0 else len(s.split(" ")[-2])

print(len_last_word("fly me to the moon "))

def length_longest_substring(s: str) -> int:
    