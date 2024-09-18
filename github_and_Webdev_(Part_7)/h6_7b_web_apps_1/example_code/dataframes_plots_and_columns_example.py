import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit to use the whole width of the page instead of the
# roughly middle 2/3 of the page that it uses by default
# The page will still try to intelligently respond to being provided
# on different sizes of browsers
st.set_page_config(layout="wide")

# Add a title
st.title('IMDB Dataset Explorer')

# Import data
# This time we try to look locally, but fall back to reading from
# a URL where the dataset is stored if needed
try:
    data = pd.read_csv("../data/imdb_top_1000.csv")
except FileNotFoundError:
    data = pd.read_csv("https://github.com/hsma-programme/h6_7b_web_apps_1/raw/main/data/imdb_top_1000.csv")


##########################
# Data Cleaning          #
##########################

# Filter out row with an error in
# We could correct this in our source dataset instead as this
# gets done every time
data = data[data["Series_Title"] != "Apollo 13"]

# Turn runtime into a numeric column
# By default, this column is in the form '123 minutes'
# This just uses a useful little pattern that extracts the first
# group of digits that appear in a column
# We tell it to overwrite the 'runtime' column with just the
# digits
# Finally, we tell it to convert from a string to an integer
# This is just done so we can do calculations on the runtime column
# but it's something you may find yourself wanting to do yourself
# if the datasets you work with aren't already nicely cleaned up
data["Runtime"] = data["Runtime"].str.extract(r"(\d+)").astype('int')

# Turn Released_Year into an integer instead of a string
# We could do this as part of reading in the csv with pandas
# but doing it here works fine too!
# Again, converting it from a string to an integer just gives us more
# opportunities to do calculations with the value or to display
# it differently in graphs as something with an actual scale rather than
# treating it as a series of categorical labels
data["Released_Year"] = data["Released_Year"].astype('int')

################################
# App Code                     #
################################

# We use this code to set up two equal-width columns
# Just setting them up does nothing - we then need to tell
# Streamlit what to put in each of them
# We could call these whatever we want - e.g. col_a, col_b or apples, bananas
col1, col2 = st.columns(2)
# If we have more columns, we just unpack into more variables
# e.g. col1, col2, col3, col4 = st.columns(4)
# That would give us 4 columns that each take up 25% of the screen

# We use the 'with' notation and refer to one of our columns
with col1:
    year_range = st.slider(
        "Select a range of years", # label displayed to the user
        # Minimum possible value
        # We look at the dataset to find what the minimum value
        # actually is
        min_value=data['Released_Year'].min(),
        # We repeat with the maximum (the upper limit of the slider)
        max_value=data['Released_Year'].max(),
        # Here we want users to be able to select a *range*
        # By providing a *tuple* of values here (two values
        # presented inside brackets) then we get a double-ended
        # slider to select the upper and lower range in a single
        # input widget
        value=(1980, 1990)
        )

    # Now we need to filter our dataframe
    # Here we opt to overwrite our dataframe
    # The year_range slider returns two values as it has
    # an upper and lower selected limit
    # This code says to filter to include rows where
    # the value in 'released_year' is higher than
    # the lower selected range in the slider, and
    # rows with a released year lower than the higher
    # selected value in the slider
    # The [0] and [1] just refer to the first and
    # second values returned from the year_range
    # slider respectively
    #
    # Notice that when filtering by multiple conditions we
    # need to wrap each separate condition with brackets
    # and put a '&' symbol (with no quotes) between each
    data = data[
        (data["Released_Year"]>=year_range[0]) &
        (data["Released_Year"]<=year_range[1])
        ]

    # Let's now display this
    st.dataframe(
        # We pass in the dataframe but limit it to these 5 columns
        data[['Series_Title', 'Released_Year', 'Certificate', 'Runtime', 'IMDB_Rating']],
        # This means it will take up the maximum possible width
        # (here, the full width of the column)
        use_container_width=True,
        # This hides the index column, which isn't really necessary in this dataframe
        hide_index=True,
        # We can then specify configurations for some or all of the columns
        # to refine how they get displayed
        # This is a dictionary with the original column name on the left
        # and each column separated by commas
        # If we just provide a string on the right of the :, then this will just change the
        # name that is displayed in the column header
        # If we provide a st.column_config then we can select from a range
        # of column types detailed in the Streamlit documentation
        column_config={
            "Series_Title": "Title",
            "IMDB_Rating": "Rating",
            "Released_Year":st.column_config.NumberColumn(
                "Released In", # Change the title displayed
                format="%d" # Format it as digits with no comma in
                ),
            "Runtime":"Runtime (Minutes)"
        }
        )

# Now we can start defining the contents of our second column
# Notice the unindent before we say 'with col2'
with col2:
    # Manually count how many values fall into each category
    # in our dataframe and save this as a new df
    cert_df = data["Certificate"].value_counts()

    # Create a bar chart
    st.plotly_chart(
        px.bar(cert_df, # pass in the dataframe
               x="count", # display the values from the 'count' column horizontally
               # Use the 'index' of our count df as the labels for the vertical axis
               # This will be 'U', 'PG', '12', etc.
               y=cert_df.index
               )
    )

# Add in an extra chart outside of the columns
# This will display in its own row below the two columns
# This is because we have unindented - notice that this
# isn't indented within the 'with col2' level.
# Here, we just plot each individual movie's runtime against its average
# rating on IMDB
st.plotly_chart(
    px.scatter(data, x="Runtime", y="IMDB_Rating")
)
