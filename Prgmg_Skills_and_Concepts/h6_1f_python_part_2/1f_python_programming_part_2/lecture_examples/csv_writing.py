import csv # import the csv library

# Here's a list of column titles
list_of_column_titles = ["Name", "ID"]

# Here's a few lists containing data we want to write out to file
data_row_1 = ["Dan", 43102]
data_row_2 = ["Sammi", 31023]
data_row_3 = ["Amy", 54098]

# Let's combine the data rows into a single list of lists
combined_data = [data_row_1, data_row_2, data_row_3]

# Do the following block of code with output.csv opened in write mode ("w"),
# and setting the newline parameter to null (this is a necessary inclusion on
# Windows, otherwise it'll add an extra line between lines), and refer to it as
# f
with open("output.csv", "w", newline='') as f:
    # Create a csv writer object, which uses f (the file opened in write mode
    # etc) with a comma delimiter
    writer = csv.writer(f, delimiter=",")

    # Write the first row (the column titles)
    writer.writerow(list_of_column_titles)

    # Loop through the other data rows and write them (one on each line)
    for data_row in combined_data:
        writer.writerow(data_row)

