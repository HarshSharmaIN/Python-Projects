from textblob import TextBlob

# Predefined movie lists for each sentiment
positive_movies = ["The Pursuit of Happiness", "Forrest Gump", "Up", "Inside Out"]
neutral_movies = ["Inception", "The Matrix", "Interstellar", "Arrival"]
negative_movies = ["Schindler's List", "Requiem for a Dream", "Joker", "The Pianist"]


# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Get sentiment polarity
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


# Function to recommend movies based on sentiment
def recommend_movies(sentiment):
    if sentiment == "positive":
        return positive_movies
    elif sentiment == "negative":
        return negative_movies
    else:
        return neutral_movies


# Main program
def main():
    print("Welcome to the Personalized Movie Recommender!")
    user_input = input("How are you feeling today? Describe your mood in a few words: ")

    # Analyze the user's mood
    sentiment = analyze_sentiment(user_input)
    print(f"\nDetected mood: {sentiment.capitalize()}")

    # Recommend movies based on the sentiment
    movies = recommend_movies(sentiment)
    print(f"Based on your mood, here are some movie recommendations:\n")
    for movie in movies:
        print(f"- {movie}")


# Run the main function
if __name__ == "__main__":
    main()
