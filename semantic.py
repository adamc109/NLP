import spacy

nlp = spacy.load('en_core_web_md')

# variables for words to compare
word1 = nlp("car")
word2 = nlp("lorry")
word3 = nlp("passenger")

# prints comparison of words
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""
Cat, Monkey, Banana
Cat and Monkey had the most similarity, seemingly because they are animals
Monkey and banana had some similarity as monkeys are assumed to like banana
Cat and Banana had the least similarities as there is no obvious connection
"""

"""
Car, Lorry, Passenger
Car and lorry had the most similarity as they are both vehicles.
Passenger had a slightly higher similarity with lorry, however you would expect it to have a higher similarity to car
"""

"""
When using sm model it showed a low similarity of 0.43 between car and lorry, the highest similarity was passenger and
car with 0.63
"""