# To run this code, you should use the supplied nlp_sa virtual environment.
# You will also need to have a trained model saved by running sa_1.py first.

# Import tensorflow and elements of keras (the API to access tensorflow) that
# we need
import tensorflow as tf

from tensorflow import keras

# Specify the filename of the model we want to open.  You'll need to change this
# if the model you want to load is named something else.
filename = 'trained_sa_model.keras'

# Load the model in as trained_sa_model
trained_sa_model = keras.models.load_model(filename)

# Threshold for classifying as positive or negative
threshold = 0.5

# A list containing text on which to test our trained sentiment analysis model
test_reviews = ["""
Tenet is simply an incredible film with deep complex concepts to unravel well
after the credits roll. Low ratings with criticism of the film's "over the top 
confusion" is more indicative of an audience that has been spoon-fed brainlessly
 simple ideas for far too long, than any legitimate flaw in Nolan sculpture of a
flowing and seamless narrative thread. Despite its complexity (which I believe 
is an asset) the film is perfectly paced, the actors bring a fluid confidence 
that assures the audience that at the very least the characters understand 
"inversion" (even if we don't fully), and the cinematography and score also hold
 up their weight alongside the driving narrative. There is a understandable 
concern that the mix was not inducive to assisting the audience in understanding
 the various exposition dumps that occur throughout the film, however this could
 vary widely depending on the sound system used when viewing and in any event it
 did not detract from my overall enjoyment of the film. This is a film that 
challenges conventional story arcs, and was a breath of fresh air in a landscape
 that for years has featured repetitively unimaginative action films such as 
those presented under the Avengers franchise. Hopefully this movie gains the 
recognition it deserves and Nolan is rewarded for breaking the mould in 
difficult year for large-budget cinema-based films. Perhaps Tenet is 
demonstrating a brilliant stroke of commercial genius on Nolan's part; 
make a movie so confusing yet enjoyable that viewers MUST go back for a second 
viewing!
""",
"The movie was a load of rubbish!"
]

# If we're using Windows, we have to convert the list of text to a Tensor first.
# We don't have to do this if we're using a Unix OS as it does it for us (though
# you can still run the code as it is).  You can add that to your growing list
# of why Windows is rubbish for data science.
tensor = tf.convert_to_tensor(test_reviews)

# Call the predict method of our trained model on the tensor.  This will
# output a number between 0 and 1 from our sigmoid activation layer.
predicted_confidence = trained_sa_model.predict(tensor)

# Print the output for each review
for review_index in range(len(test_reviews)):
    print (f"Review {review_index} : {predicted_confidence[review_index]}")

    # Check the output against the threshold we specified above.  If it's higher
    # than the threshold, classify the text as positive, otherwise classify it
    # as negative.
    if predicted_confidence[review_index] > threshold:
        print ("Predicted POSITIVE")
    else:
        print ("Predicted NEGATIVE")

    print ()

