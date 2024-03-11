#Import pandas
import pandas as pd

# Specify the file path
csv_file_path = 'project_data.csv'

# Read the CSV data set
df = pd.read_csv("C:/Users/ivic2/Downloads/project_data.csv")
print(df)

# Returns movie titles that mention the "United States"
title_df = df[df['title'].str.contains('United States')]
print(title_df)

# Returns the descriptions that mention the "United States"
description_df = df[df['description'].str.contains('United States')]
print(description_df)

# Returns the amount of movies made from the United States
print(df[["country"]].value_counts())

#Exercise Two - Input function
director_name = input("Please enter director's name:")
matching_directors = df[df['director'].fillna('').str.contains(director_name, case=False, na=False)]
if matching_directors.empty:
    print(f"No directors were found with names containing '{director_name}' in this dataset.")
else:
    print(f"There are [{len(matching_directors)}] directors with named {[director_name]} in this dataset.")

#Exercise Three

# Download NLTK stopwords 
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Sort the DataFrame by movie duration 
top_ten_longest_movies = df.sort_values(by='duration_min', ascending=False).head(10)

# Combine descriptions of top ten longest movies 
combined_descriptions = ' '.join(top_ten_longest_movies['description'].dropna())

# Tokenize the words and remove stopwords
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(combined_descriptions)
filtered_words = [word.lower() for word in word_tokens if word.isalpha() and word.lower() not in stop_words]

# Count the occurrences of each word
word_counts = Counter(filtered_words)

# Get the 20 most common words
most_common_words = word_counts.most_common(20)

# Print results
print("20 most common words in the description of the top ten longest movies:")
for word, count in most_common_words:
    print(f"{word}: {count}")

#Exercise 4

#Import Math
import math

# Function to get information on actor
def get_actor_info(actor_name, dataset):
    actor_name = actor_name.lower()  # Convert to lowercase for case-insensitive search

    # Check if any row in the 'cast' column contains the actor's name
    matching_rows = dataset[dataset['cast'].str.lower().str.contains(actor_name, na=False)]

    # Check if the actor is found in any row
    if matching_rows.empty:
        return f"No movie found for the artist: {actor_name}"

    # Calculate the average movie duration rounded up to a whole number
    avg_duration = math.ceil(matching_rows['duration_min'].mean())

    # Get a list of their movies
    movies_list = matching_rows[['title', 'duration_min']].values.tolist()

    return {'average_duration': avg_duration, 'movies_list': movies_list}

# Input Function
actor_name_input = input("Please enter actor's name: ")
result = get_actor_info(actor_name_input, df)

print(result)


