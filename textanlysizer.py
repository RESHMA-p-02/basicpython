def analyze_text(text):
  # Stop words (common words to be excluded)
  stop_words = ["the", "a", "an", "in", "on", "of", "is", "and", "to", "for"]

  # Clean and process text
  text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
  words = [word for word in text.split() if word not in stop_words]  # Split into words, exclude stop words
  # Calculate analysis results
  characters = len("".join(words))  # Count characters excluding spaces
  sentences = len(text.split(".")) + len(text.split("!")) + len(text.split("?"))  # Count sentences
  average_word_length = round(sum(len(word) for word in words) / len(words), 2) if words else 0 
  word_counts = {word: words.count(word) for word in words}  # Count word frequency
  most_common_word = max(word_counts, key=word_counts.get) if word_counts else None  # Find most frequent word

  # Return analysis results as a dictionary
  return {
      "words": len(words),
      "characters": characters,
      "sentences": sentences,
      "average_word_length": average_word_length,
      "most_common_word": most_common_word
  }

# Get text input from the user
text = input("Enter some text: ")

# Analyze text and print results
analysis = analyze_text(text)
print("Text Analysis Results:")
for key, value in analysis.items():
  print(f"{key.capitalize()}: {value}")
