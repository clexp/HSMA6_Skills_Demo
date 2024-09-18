### IMPORTANT - SOMETIMES WHEN RUNNING IN THE INTERACTIVE TERMINAL OF VSCODE,
### THE NEXT ENCOUNTER WILL NOT SHOW UP BEFORE IT ASKS YOU WHETHER YOU WANT TO
### FIGHT.  IF THAT HAPPENS, SIMPLY TYPE r TO REPEAT THE ENCOUNTER WITH ANOTHER
### PIRATE - YOU WON'T BE PENALISED FOR THIS.

# To run this code, you should use the supplied nlp_sa virtual environment.
# You will also need to have a trained model saved by running sa_1.py first.

# Import tensorflow and elements of keras (the API to access tensorflow) that
# we need
import tensorflow as tf

from tensorflow import keras

# Import pandas
import pandas as pd

# Import random library
import random

# Import time library
import time

# Specify the filename of the model we want to open.  You'll need to change this
# if the model you want to load is named something else.
filename = 'trained_sa_model.keras'

# Load the model in as trained_sa_model
trained_sa_model = keras.models.load_model(filename)

# Threshold for classifying as positive or negative
threshold = 0.5

# We're going to use the Reviews Dataset from
# https://www.kaggle.com/datasets/ahmedabdulhamid/reviews-dataset
# which contains over 4000 labelled positive and negative reviews from various
# industries.
# Here, we'll read in the reviews and their associated labels (0 or 1) from the
# csv.  You need to ensure that the sword_fighting_dataset.csv file is in the
# same directory as this .py file (it is by default).
# Read in csv and store as a Pandas dataframe
swordfight_review_df = pd.read_csv('sword_fighting_dataset.csv')

# Set up list of pirates
# Names randomly generated using :
# https://www.imagineforest.com/blog/pirate-name-generator/
pirates = [
    "Poopdeck Pete",
    "Handsome Jimmy",
    "Evie Shark-Bait",
    "Bill Bones",
    "Randell Rummy",
    "Maximus Dark-Skull",
    "Jack Red-Locks",
    "Davey Dark-Skull",
    "Roger Starky",
    "Captain Patty Price",
    "Sadie Waters",
    "Clara Shadows",
    "Silver-Tooth Samuel",
    "Dirty Danny",
    "Shiverin Shelley",
    "Admiral Spike",
    "Captain McFilthy",
    "Captain Blackbeard",
    "Nancy Lobster-Legs",
    "Captain Vera Brave",
    "Lazy-Eye Louie",
    "Martha One-Eyed",
    "Captain Vex Totem",
    "Theo Stinkalot",
    "Captain Scurvyshorts",
    "Jonas Rattler",
    "Captain Redbeard",
    "Musclemouth Mike",
    "Glory Jones",
    "Crimson Seadog",
    "Misty Winters",
    "Finn O Fish",
    "Joy McStubby",
    "Vera Sparrow",
    "Liza Mcgee",
    "Ruth O Patches",
    "Pistol-Grin Gary",
    "Mary Jane Death-Bringer",
    "Captain Drake Deranged",
    "Silvera Snake-Eyes",
    "Captain Justeene",
    "Captain Puffypants",
    "Capn Chipper Toes",
    "Betty Tuna-Breath",
    "George Balding"
]

# Set up the score counter
sa_sword_fighting_score = 0

# Print intro message
print ("I'm Danbrush Chalkwood, and I want to be a data scientist.")

# Set encounter counter
encounter = 1

# Begin encountering and fighting pirates
while encounter < 51:
    time.sleep(1)

    print ()
    print (f"ENCOUNTER {encounter}")

    # Pick a random pirate name
    random_pirate = random.choice(pirates)
    
    # Pick a random review for them to give, and grab the review and the
    # correct classification
    random_review_index = random.randint(1, len(swordfight_review_df)-1)
    review = swordfight_review_df.loc[random_review_index]["review"]
    r_class = swordfight_review_df.loc[random_review_index]["class"]

    print (f"You have encountered {random_pirate}.  They want to fight.")
    print ("They exclaim : ")
    print (review)
    print ('"ARRRRRRR"')
    
    # Check correct classification and print appropriate message
    if r_class == 1:
        print ('"And I say twas a POSITIVE experience!  Shall we fight?"')
    else:
        print ('"And I say twas a NEGATIVE experience!  Shall we fight?"')

    print ()

    # Check if user wants to fight this pirate (cast input as lowercase to
    # catch input of capital Y)
    fight_input = input(
        "Fight? Type y to fight, r to repeat, or anything else to run").lower()
    
    # If the user does want to fight
    if fight_input == "y":
        print ("You clash swords!")
        time.sleep(0.5)
        
        # Put the review in a list and convert to a tensor, then use the
        # loaded model to make a classification prediction on the review
        tensor = tf.convert_to_tensor([review])
        predicted_confidence = trained_sa_model.predict(tensor)

        # Check if the output exceeded the classification threshold to determine
        # how it is classified by the model
        if predicted_confidence > threshold:
            predicted_positive = True
            print (f"And you say it was POSITIVE. ({predicted_confidence[0]})")
        else:
            predicted_positive = False
            print (f"And you say it was NEGATIVE. ({predicted_confidence[0]})")

        # If the model's classification matches the true classification,
        # Danbrush wins the fight and gains one point.  If there's a mismatch,
        # Danbrush loses the fight and loses one point.
        if r_class == 1 and predicted_positive == True:
            print ("YOU WIN THE FIGHT!!")
            sa_sword_fighting_score += 1
            print (f"Your score is {sa_sword_fighting_score}")
        elif r_class == 0 and predicted_positive == False:
            print ("YOU WIN THE FIGHT!!")
            sa_sword_fighting_score += 1
            print (f"Your score is {sa_sword_fighting_score}")
        else:
            print ("......you lose the fight and run like a coward.")
            sa_sword_fighting_score -= 1
            print (f"Your score is {sa_sword_fighting_score}")
        
        encounter += 1
    elif fight_input == "r":
        # Try this encounter again (used for cases where display didn't update)
        # Note - a new pirate will be chosen
        print ("Finding another pirate...")
    else:
        # If Danbrush chooses not to fight, no points are gained or lost
        print ("You make your excuses and leave.")
        print (f"You still have {sa_sword_fighting_score}")

        encounter += 1

# Print final message and score
print ("You have finished your training.  It's time to face LeChalk.")
print (f"Your score was {sa_sword_fighting_score}")

