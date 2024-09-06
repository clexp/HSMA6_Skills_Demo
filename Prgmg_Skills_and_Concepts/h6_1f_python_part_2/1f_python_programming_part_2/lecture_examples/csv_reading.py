import csv # import the csv library

# Set up two empty lists - one to store names, one to store ages
list_of_names = []
list_of_ages = []

# do the following block of code holding the csv file open in "read only" mode
# ("r"), and henceforth we'll refer to this file opened in read only mode as f
# (alias)
with open("filename.csv", "r") as f:
    # Create a csv reader object (we'll come back to that in Object Oriented
    # Programming), which uses the file opened in read-only mode (f), and where
    # the delimiter is a comma
    reader = csv.reader(f, delimiter=",")

    # For each row it reads in, take the first value before a comma and add it
    # to the list of names, and take the second value, and add it to the list
    # of ages.
    for row in reader:
        list_of_names.append(row[0])
        list_of_ages.append(row[1])

