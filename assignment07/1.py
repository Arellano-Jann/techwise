# Camel case is often used as a naming convention in computer programming, but is an ambiguous definition due to the optional capitalization of the first letter. Some programming styles prefer camel case with the first letter capitalised, others not. For clarity, this article calls the two alternatives upper camel case (initial uppercase letter, also known as Initial Capitals, Initial Caps, InitCaps or Pascal case) and lower camel case (initial lowercase letter, also known as dromedary case). Some people and organizations, notably Microsoft, use the term camel case only for lower camel case, designating Pascal case for the upper camel case.

# -- from the wikipedia

# We will also use the convention that the term camel case stands for first letter lower and the term pascal case stands for first letter also capitals

# We will first address two situations:

#   1. converting a variable name which has underscores separating the parts to  camel case

#   2. Converting a string whiich has spaces punctuation etc to a camel case variable name

# ## Convert a variable name to camel case.

# variable_to_camel_case("basic_salary_in_dollar") => basicSalaryInDollar

def variable_to_camel_case(text: str) -> str:
    #Write your code Here
    text = text.lower()
    toUpper = False
    final_string = ""
    for x in text:
        if not toUpper:
            if x == ' ' or x == '_':
                toUpper = True
            else:
                final_string += x
        else:
            final_string += x.upper()
            toUpper = False
    return final_string

print(variable_to_camel_case("basic_salary_in_dollar"))
print(variable_to_camel_case("basic salary in dollar"))


# Convert a variable name from camel case

import re

def camel_case_to_snake_case(camel: str) -> str:
    #Write your code Here
    camel = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel) #  this is fucking genius. holy shit
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel).lower()
    # final_string = ""
    # for x in camel:
    #     if x.isupper():
    #         final_string += '_' + x.lower()
    #     else:
    #         final_string += x
    # return final_string

print(camel_case_to_snake_case("basicSalaryInDollar"))
print(camel_case_to_snake_case("snakeToCamel"))