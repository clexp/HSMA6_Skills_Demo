# To run this code, you should use the supplied nlp_sa virtual environment.
# You will also need to have a trained model saved by running sa_1.py first.

# Import tensorflow and elements of keras (the API to access tensorflow) that
# we need
import tensorflow as tf

from tensorflow import keras

# Specify the filename of the model we want to open.  You'll need to change this
# if the model you want to load is named something else.
filename = 'winning_model.keras'

# Load the model in as trained_sa_model
trained_sa_model = keras.models.load_model(filename)

# Threshold for classifying as positive or negative
threshold = 0.5

# Load reviews into list
sarcastic_reviews = []

for i in range(1, 11):
    with open(f"sarcastic_{i}.txt", "r") as f:
        raw_review = f.read()
        sarcastic_reviews.append(raw_review)

# If we're using Windows, we have to convert the list of text to a Tensor first.
# We don't have to do this if we're using a Unix OS as it does it for us (though
# you can still run the code as it is).  You can add that to your growing list
# of why Windows is rubbish for data science.
tensor = tf.convert_to_tensor(sarcastic_reviews)

# Call the predict method of our trained model on the tensor.  This will
# output a number between 0 and 1 from our sigmoid activation layer.
predicted_confidence = trained_sa_model.predict(tensor)

# Choose review to ignore
ignore_index = int(input("Choose review to ignore (1-10)")) - 1

# Dictionary of review numbers to PSGs
review_dict = {
    1:"Agnus",
    2:"ANTIC",
    3:"ARM",
    4:"Denise",
    5:"Motorola 68000",
    6:"Paula",
    7:"POKEY",
    8:"SID",
    9:"TIA",
    10:"Zilog Z80"
}

# Counter to store number of negative predictions
negative_predictions = 0

# Print the output for each review
for review_index in range(len(sarcastic_reviews)):
    if review_index != ignore_index:
        print (f"Review {review_index+1} : {review_dict[review_index+1]}")
        print (sarcastic_reviews[review_index])
        print (f"Output : {predicted_confidence[review_index]}")

        # Check the output against the threshold we specified above.  If it's higher
        # than the threshold, classify the text as positive, otherwise classify it
        # as negative.
        if predicted_confidence[review_index] > threshold:
            print ("Predicted POSITIVE")
        else:
            print ("Predicted NEGATIVE")
            negative_predictions += 1

        print ("---")

print ()
print (f"Total Negative Predictions : {negative_predictions}")

