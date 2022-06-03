# Implement a function which accepts two strings (player_one and player_two)⁠ as arguments and returns an integer stating the winner of the game - Rock, Paper, Scissors.

# Each argument will contain a single string: "Rock", "Paper", or "Scissors". Return the winner according to the following rules:

# Rock beats Scissors

# Scissors beats Paper

# Paper beats Rock

# If player_one wins, return 1

# If player_two wins, return -1 and

# If both player_one and player_two are the same, return 0
def rps(player_one, player_two):
    Choices = {"rock": "scissors", 
               "scissors": "paper",
               "paper": "rock"
               }
    if player_one == player_two:
        return "Draw"
    if Choices[player_one] == player_two:
        return "Player One Wins"
    else:
        return "Player Two Wins"

print(rps("rock", "rock"))
print(rps("scissors", "paper"))
print(rps("rock", "paper"))



# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"

# Output: 3 Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"

# Output: 1

# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"

# Output: 3

# Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is not a substring.

def length_longest_substring(s: str) -> int:
    #Write your code Here
    longest = ""
    current_substring = ""
    for i in s:
      if i not in current_substring:
        current_substring += i
      elif len(longest) < len(current_substring):
        longest = current_substring
        current_substring = "" + i
      else:
        current_substring = ""
    return len(current_substring) if len(current_substring) > len(longest) else len(longest)

print(length_longest_substring("pwwkew"))
print(length_longest_substring("bbb"))
print(length_longest_substring("a"))
print(length_longest_substring(""))
print(length_longest_substring("  "))
print(length_longest_substring("abc abcbb "))
print()

def length2(s):
    longs = []
    if len(s) == 0:
        return 0
    for i in range(len(s)):
        substring = s[i]
        j = i+1
        while j <= len(s)-1 and s[j] not in substring:
            substring += s[j]
            j += 1
        longs.append(len(substring))
    return max(longs)

print(length2("pwwkew"))
print(length2("bbb"))
print(length2("a"))
print(length2(""))
print(length2("  "))
print(length2("abc abcbb "))