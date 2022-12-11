# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities
# you found that spaCy gave one of the words of your sentences - did you expect this?

# Importing spacy and loading a model
import spacy
nlp = spacy.load('en_core_web_sm')

# Creating list with garden path sentences
gardenpathSentences = ["The cotton clothing is made of Grows in Mississippi.",
                       "The complex houses married and single soldiers and their families.",
                       "The Sour Drink from the ocean.",
                       "Mary gave the child the dog bit a Band-Aid.",
                       "The dog that I had really loved bones."]


# Preparing sentences for manipulation
doc = map(nlp, gardenpathSentences)


for sentence in doc:
    # Tokenisation
    print([(token, token.orth_, token.orth) for token in sentence])

    # Entity recogniton
    print([(i, i.label_, i.label) for i in sentence.ents])


# Unusual entities
# The Sour Drink recognised as a person
# Grows recognised as a region
# Band-aid wasn't recognised as a brand
