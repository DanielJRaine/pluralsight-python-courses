from pprint import pprint as pprint


words = "why sometimes I have believed as many as six impossible things before breakfast"
words = words.split()

# list comprehension
[len(word) for word in words]

# set comprehension
{len(str(factorial(x))) for x in range(20)}

# dict comprehension
# {key_expr: value_expr for item in iterable }
# iterating over a dict yields keys by default

capital_to_country = {capital: country for country,
                      capital in country_to_capital.items()}

# later keys overwrite earlier keys in the case of duplicates

# optional filtering clauses
# [ expr(item) for item in iterable if predicate(item)]
[x for x in range(101) if is_prime(x)]
