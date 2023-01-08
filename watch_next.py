import spacy

nlp = spacy.load('en_core_web_md')

# variables to keep track of movies and results
movie_list = []
movie_list_with_identifier = []
movie_comparison_results = []

# reads movies.txt and adds each movie to the movie list
with open("movies.txt", "r") as f:
    for line in f:
        movie_list_with_identifier.append(line.strip())
        movie_list.append(line[9:].strip())

# movie description
hulk_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
                "the Illuminati trick Hulk into a shuttle and lunch him into space to a planet where the Hulk can live" \
                "in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a" \
                "gladiator"
hulk_movie_description = nlp(hulk_movie_description)

# iterates over the movies and adds the score to movie_comparison_results list
for movie in movie_list:
    movie = nlp(movie)
    movie_comparison_results.append(movie.similarity(hulk_movie_description))

# variables to keep track of index and score
score = 0
score_index = 0

# iterates over the score and keeps track of highest score index
for i in range(len(movie_comparison_results)):
    if movie_comparison_results[i] > score:
        score = movie_comparison_results[i]
        score_index = i

# prints statement with the most similar movie
print(f"The most similar movie is: \n{movie_list_with_identifier[score_index]}")
