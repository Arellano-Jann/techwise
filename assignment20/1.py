# ##Assignment - 20 - 01

# ###Count vowels and consonants

# Implement a function to read the content from the "Content.txt" file and return the count of vowels and consonants.

# Example:

#     count_vowel_and_cons("Content.txt") --> (156, 258)

# Content.txt 

#     https://drive.google.com/file/d/1h60E9b3r9ecFLPxnd5lYzDzLiza0NsK3/view?usp=sharing
    
    
def count_vowel_and_cons(filename: str)-> (int, int):
    #write your code here
    vowel = "AEIOUaeiou"
    consonant = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vowel_count = []
    consonant_count = []
    f = open(filename, "r")
    for line in f:
        vowel_count += [character for character in line if character in vowel]
        consonant_count += [character for character in line if character in consonant]
    f.close()
    return len(vowel_count), len(consonant_count)
    
print(count_vowel_and_cons("assignment20/Content.txt"))



# ##Assignment - 20 - 02

# ##Add Rank to the students

# Implement a program to rank the students according to their marks.

# Note: The ranking system:

# If two students of the class get equal marks, they are given the same rank but students with different marks are given the rank as the (number of students above them + 1). See the example for more clarity.

# There are five students in a class. Their marks distribution is: 98 68 74 21 74

# That is first student gets marks 98, second gets 68, and so on. Now , the highest marks is 98. So, the first student gets rank 1. Next higher marks is 74. So student 3 and 5 gets rank 2. Next higher marks is 68 and there are three students (1,3,5) who have got marks higher than him. So he gets rank 4. Similarly , student with marks 21 gets rank 5.

# Sample data in the file

#     John, 84
#     Micheal, 90
#     Peter, 65
#     Jenny, 90
#     Ryan, 77
#     Ashaa, 84
#     Kerry, 52
#     Kingsley, 17
#     Wincy, 95
#     Princy, 95
#     Johnright, 65
#     Mike, 76
#     Peterpot, 64
#     Mark, 98
#     Raj, 76
#     Ashaa, 85
#     Perrt, 53
#     Queen, 15
#     Anshu, 90
#     Amar, 92

# **Expected Output:**

#     1  Mark           98    
#     2  Wincy          95    
#     2  Princy         95    
#     4  Amar           92    
#     5  Micheal        90    
#     5  Jenny          90    
#     5  Anshu          90    
#     8  Ashaa          85    
#     9  John           84    
#     9  Ashaa          84    
#     11  Ryan          77    
#     12  Mike          76    
#     12  Raj           76    
#     14  Peter         65    
#     14  Johnright     65    
#     16  Peterpot      64    
#     17  Perrt         53    
#     18  Kerry         52    
#     19  Kingsley      17    
#     20  Queen         15    


# Sample file: StudentData.txt
# https://drive.google.com/file/d/1dNAPtIZ6McDx9hbXQjPXghjOQ2RoDf9Y/view?usp=sharing


def assign_rank(textfile):
    with open(textfile) as file:
        ranks = [tuple(line.strip().split(", ")) for line in file]
    ranks.sort(key=lambda x: x[1], reverse=True)
    print(ranks)
    for i, marks in enumerate(ranks, 1):
        while ranks[i-2][1] == marks[1]:
            i -= 1
        print(f"{i:3} {marks[0]:10} {marks[1]:>3}")
    
assign_rank("assignment20/Marks.txt")