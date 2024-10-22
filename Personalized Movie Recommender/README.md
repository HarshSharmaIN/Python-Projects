# Personalized Movie Recommender
This Python program recommends movies based on the user's mood, which is detected through sentiment analysis of the text input. The sentiment can be positive, neutral, or negative, and movies are recommended accordingly.

## Features
* Sentiment Analysis: Analyzes the user's mood using the TextBlob library.
* Movie Recommendations: Recommends a set of movies based on the detected sentiment (positive, neutral, or negative).
* User Interaction: Simple and intuitive interaction where users describe their mood, and the program suggests relevant movies.

## How to Run
Run the movie_recommender.py file:
```bash
python movie_recommender.py
```
You will be prompted to describe your mood, and based on your input, the program will suggest relevant movies.

## Example Usage
```bash
Welcome to the Personalized Movie Recommender!
How are you feeling today? Describe your mood in a few words: I’m feeling a bit down.

Detected mood: Negative
Based on your mood, here are some movie recommendations:

- Schindler's List
- Requiem for a Dream
- Joker
- The Pianist
```

## How It Works
1. User Input: The user provides a short description of their current mood.
2. Sentiment Analysis: The TextBlob library analyzes the input and determines whether the sentiment is:
    * Positive
    * Neutral
    * Negative
3. Movie Recommendation: Based on the detected sentiment, a list of movies is recommended to match the user's mood.

## Movie Lists
1. Positive Movies
    * The Pursuit of Happiness
    * Forrest Gump
    * Up
    * Inside Out
2. Neutral Movies
    * Inception
    * The Matrix
    * Interstellar
    * Arrival
3. Negative Movies
    * Schindler's List
    * Requiem for a Dream
    * Joker
    * The Pianist

## Dependencies
* Python 3.6+
* TextBlob: For sentiment analysis

## Future Improvements
* Add more movies to the recommendation lists.
* Implement an API to fetch live movie recommendations.
* Add an option to get movie details like ratings, synopsis, etc.
* Enhance sentiment analysis with more advanced libraries like VADER or HuggingFace.