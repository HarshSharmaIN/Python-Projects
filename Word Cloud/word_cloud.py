from wordcloud import WordCloud, STOPWORDS
import random

with open ("words.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = str(data[i].replace("\n", ""))

random.shuffle(data)

for word in data:
    string = " ".join(data)

wc = WordCloud(
    background_color="black",
    stopwords=STOPWORDS,
    height=400,
    width = 400
)

wc.generate(string)

wc.to_file("generated/wordcloud_image.png")
print("Word Cloud Generated!")