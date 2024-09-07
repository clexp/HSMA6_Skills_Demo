# Decision trees

- Easy to understand
- Decision trees handle categorical data very well
- They can handle nonlinear relationship relationships
- They can handle interactions between features
- Decision trees do not need normalisation of the data
- Decision trees are not strongly affected by outliers
- Decision trees can handle missing values

### downsides

- Decision trees can be presented to overfitting
- Decision trees have high variance.

Decision trees have high variance.

This means small changes in training data can lead to big changes in trees. To manage this week deliberately under Fit to the data. This means we allow some bias to remain in the model. This leads to a bias variance trade-off with too much bias. The model has not captured the true relations. With high variance the model has captured the noise in the train data and has over fi.
To balance bias and variance means capturing patterns while general generalising well they tend to have high variance and are prone to capturing noise and not generalising well

- Decision trees can be slow to build with large data sets
- It is called an NP hard problem
- Decision trees are not so great with linear relationships
- Decision trees can create bias trees when given in balanced data sets

## Building a decision tree

When we build a decision tree, we are making a trade-off between information gain noise and what is called Genie impurity. When building a tree each feature is assessed for how well it would split the data set.

When we build a decision tree, we are making a trade-off between information gain noise and what is called Genie impurity. When building a tree each feature is assessed for how well it would split the data set.

If it if it splits the data set well, it can be a root node. Once we have a first note, we then look at other Features and assess them for value in separating the data set. This cycle repeats using the measure of added data. Currently, we use gini impurity.

## Overcoming overfitting.

The cross validation process for trees requires random sample allocation, so the models that are tested will have different accuracy parameters.

Trees can be deeply branched, overfitting can be avoided by limiting the depth of the tress

## Performance

Recall that all models need performance measurement and that they will deliver true and false, positives and negatives. This means we have the information to determine sensitivity specificity and precision. We also have the information to determine a receiver operator curve and an area under the receiver operator curve. This allows them to be compared directly to other methods such as logistic regression.

Minimum sampling ensure that multiple samples inform every decision in the tree. Too small means over fitting, too large means no learning.

Pruning leaves and nodes also helps to fit the data, this can be pre or post pruning. the above is prepruning. Post pruning uses 'ccp_alpha' or cost complexity alpha.

# Random forest

There are weaknesses to decision trees one of the best ways of managing this is to use a random forest. A random forest is where many hundreds of thousands of trees are made randomly. The DC the trees collectively vote on the outcome and the winning vote goes forwards. This can provide some very high performing models. The random trees are made by bootstrapping. This is where you create a fake data set by randomly selecting data items from your data set. This means you will have multiple data sets most of which will have duplicates and missing entries. This means you end up with new data sets the same size as your original data set. This means any tree built on this data set will be as trained as the first tree on the original data set.

This means any tree built on this data set will be as trained as the first tree on the original data set.
in addition to this not all of the features are included in the new data set only a random subset are included. This means the new random tree will be built on a smaller number of features. This means the number of features will be play a larger role in the tree, built from this new set

Overall, this over fits less than a single decision tree. It performs better on unseen data. Addresses the bias variance trade-off better than decision trees. It is not so vulnerable to noisy data. Overall, this over fits less than a single decision tree. It performs better on unseen data. Addresses the bias variance trade-off better than decision trees. It is not so vulnerable to noisy data.

However, it can be complicated to understand. While it's faster train it's also slow to predict it still does over Fit. It can be memory. Large trees can take up a lot of disk space if you want to save the model for later use

More trees is better for larger data sets, but ultimately performance will plateau and memory use will rise. There will still be some benefit from considering a maximum depth in a random forest. There is no randomness in logistic regression and decision trees but there is randomness in random forests. If you need to work to be reproducer you can set a random seed and record this.. You can also do this when you split the test train.

One of the performance metrics of random forests is called the F1 score. This is known as the harmonic mean to calculate this you calculate all the means to calculate the F1 score you collect a set of observations. Then calculate the reciprocal of each observation. With this set of reciprocals, you calculate the mean and finally with this number you reciprocated again and you arrive at the harmonic mean this is useful when you have an imbalanced data set for example where positive cases are quite rare

## Boosted trees

Random forestry print overfitting modified models for handling this include gradient boost in classifiers such as extreme gradient boost and light grade and boosting machines. They can be used for classification and regression problems, and cope with smaler datasets. Neural networks cope well with large datasets and unstructured data.

Basting works by training a large number of shallow trees but training them in sequence so each subsequent corrects the mistakes with the previous tree. This can lead to powerful models.. XGBoost will make one final good model, Random forest use lots of simple trees and a majority vote. The simple model that is retrained, requires a loss function, which minimises error each time. We can watch the rate of change for a loss function, if it stops improving we can stop early and prevent overtraining.

There are lots of gradient boosting functions. They all have different strengths and weaknesses.

## Other Classification methods

#### kNN k-Nearest-Neighbour

This uses the nearest n neighbours to classify a point. If the number of nearest neighbours are okay is too large you'll fit and have high variance. If the number of nearest neighbours is too small you will overfit and have high bias in a two class classification. Make the number odd in order to avoid tires between different classes.

#### Support vector machines

These are used to find the best boundary to separate data into different classes. It does this by maximising the distance from the nearest point to the boundary of any class. The nearest points are considered to be the support vectors.

#### Naive Bayes

This classifiers built on bass theorem assumes all features in the data are independent. It's like having a big table of probabilities of past data checks against this table and a sign of class.

## Regression Problems

When we are trying to make a machine learning model learn numerical patterns of data we call this a reggression problem. Decision trees can do regression problems but the usual metrics of measuring performance for aggression can't be used in decision trees so we need a different set of metrics. We use the main absolute error. We determine the scaler error and calculate the main and lower is better in addition to this we calculate the absolute percentage error and the main squared error.

The coefficient to the determination is R squared it is the proportion of the variation of the independent variable that is predictable from the independent variables higher is better. It has a maximum of one it's calculated as one minus the sum of the squared residuals over the total sum of squares.

## Data preparation

For some models, we need the data to be binary and not discreet classes. The data can be processed with one hot and coding. This is where the single category is split into multiple columns which are all zero accepting the category column for that row in the table, this used to be a chief encoding mechanism for natural language processing pandas can do this processing with the get dummies function. You may need to generate your own column names. (Can you write a function for this?)
