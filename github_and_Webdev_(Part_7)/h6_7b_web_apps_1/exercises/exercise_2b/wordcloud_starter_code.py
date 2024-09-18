from wordcloud import WordCloud, STOPWORDS
import string
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def make_wordcloud(text_input, filename="wordcloud.png"):
    stopwords = set(STOPWORDS)
    tokens = text_input.split()
    punctuation_mapping_table = str.maketrans('', '', string.punctuation)
    tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]
    lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

    joined_string = (" ").join(lower_tokens)

    wordcloud = WordCloud(width=1800,
                      height=1800,
                      stopwords=stopwords,
                      min_font_size=20).generate(joined_string)

    plt.figure(figsize=(30,40))
    # Turn off axes
    plt.axis("off")
    # Display (essential to actually get the wordcloud in the image)
    plt.imshow(wordcloud)
    # Save the wordcloud to a file
    plt.savefig(filename)


###################################################
# EXAMPLE USE: With string, which will be the output
# of st.text_input() or st.text_area()
###################################################

penguin_text = """
Penguins are a group of aquatic flightless birds from the family Spheniscidae
of the order Sphenisciformes.
They live almost exclusively in the Southern Hemisphere: only one species,
the Galapagos penguin, is found north of the Equator. Highly adapted for life in the ocean water,
penguins have countershaded dark and white plumage and flippers for swimming. Most penguins feed
on krill, fish, squid and other forms of sea life which they catch with their bills and swallow
whole while swimming. A penguin has a spiny tongue and powerful jaws to grip slippery prey.

They spend about half of their lives on land and the other half in the sea.
The largest living species is the emperor penguin (Aptenodytes forsteri):
on average, adults are about 1.1 m (3 ft 7 in) tall and weigh 35 kg (77 lb).
The smallest penguin species is the little blue penguin (Eudyptula minor),
also known as the fairy penguin, which stands around 30–33 cm (12–13 in) tall and
weighs 1.2–1.3 kg (2.6–2.9 lb).
Today, larger penguins generally inhabit colder regions, and smaller penguins inhabit regions
with temperate or tropical climates. Some prehistoric penguin species were enormous:
as tall or heavy as an adult human.There was a great diversity of species in subantarctic regions,
and at least one giant species in a region around 2,000 km south of the equator 35 mya, during
the Late Eocene, a climate decidedly warmer than today.
"""

make_wordcloud(penguin_text, "penguin_sample_wordcloud.png")


###################################################
# EXAMPLE USE: With .txt file
###################################################

# Read text in for which we want to generate word cloud
# The read() method of the file object simply reads in the contents of the file
# as one, single continuous string of text.
with open("bttf_reviews.txt", "r") as f:
    bttf_text = f.read()

make_wordcloud(bttf_text, "bttf_sample_wordcloud.png")



###################################################
###################################################
# Advanced wordcloud function
# This accepts an optional additional image to act
# as a 'mask'
# It also allows users to pass in additional
# parameters that are accepted by the wordcloud
# function itself
###################################################
###################################################

def make_wordcloud_with_image_mask(
        text_input,
        filename="wordcloud.png",
        mask_image=None,
        **kwargs
        ):
    stopwords = set(STOPWORDS)
    tokens = text_input.split()
    punctuation_mapping_table = str.maketrans('', '', string.punctuation)
    tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]
    lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

    joined_string = (" ").join(lower_tokens)

    plt.figure(figsize=(30,40))
    plt.axis("off")

    if mask_image is not None:
        mask_image_opened = Image.open(mask_image)
        mask_array = np.array(mask_image_opened)

        wordcloud = WordCloud(width=mask_array.shape[1],
                    height=mask_array.shape[0],
                    stopwords=stopwords,
                    mask=mask_array,
                    **kwargs).generate(joined_string)

        plt.imshow(wordcloud, interpolation='bilinear')

    else:
        wordcloud = WordCloud(width=1800,
                    height=1800,
                    stopwords=stopwords,
                    **kwargs).generate(joined_string)

        plt.imshow(wordcloud)

    plt.savefig(filename)



make_wordcloud_with_image_mask(penguin_text,
                               "penguin_sample_wordcloud_mask.png",
                               mask_image="penguin.jpg"
                               )

make_wordcloud_with_image_mask(penguin_text,
                               "penguin_sample_wordcloud_mask_smaller_text.png",
                               mask_image="penguin.jpg",
                               min_font_size=6
                               )

make_wordcloud_with_image_mask(bttf_text,
                               "bttf_sample_wordcloud_blue.png",
                               colormap='Blues'
                               )

make_wordcloud_with_image_mask(bttf_text,
                               "bttf_sample_wordcloud_pink_background_blue_text.png",
                               colormap='Blues',
                               background_color='pink'
                               )
