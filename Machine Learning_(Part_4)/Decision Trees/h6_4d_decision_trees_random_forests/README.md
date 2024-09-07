# HSMA Session 4D: Decision Trees & Random Forests

## Slides

<a href="https://docs.google.com/presentation/d/1LgVvgLzm4dxCdDCusjWWC_SBrtXhhCPchHXK4oI0kWU/edit?usp=sharing"><img src="https://img.shields.io/static/v1?label=Google+Slides&message=Click+here+to+view+the+slides+for+this+session&color=%23FBBC04&style=for-the-badge&logo=googleslides&logoColor=%23FBBC04" alt="Google Slides - Click here to view slides for this session"></a>

## Lecture Recording

Decision Trees: <a href="https://youtu.be/p3Bc2kDtPPs"><img src="https://img.shields.io/static/v1?label=Youtube&message=Click+here+to+watch+the+lecture&color=%23282828&style=for-the-badge&logo=youtube&logoColor=%23FF0000" alt="Youtube - Click here to watch the lecture"></a>

Random Forests: <a href="https://www.youtube.com/watch?v=jqvn_OXbIfg"><img src="https://img.shields.io/static/v1?label=Youtube&message=Click+here+to+watch+the+lecture&color=%23282828&style=for-the-badge&logo=youtube&logoColor=%23FF0000" alt="Youtube - Click here to watch the lecture"></a>

## Exercises

The notebooks in the `exercises` folder can be downloaded and run locally if you have Python installed.

Alternatively, you can run each exercise on **Google Colab**, a free online platform for coding exercises. You will need to be logged in to a google account in your browser. 

Using the links below will open a fresh copy of the notebook to work on - your changes will not be visible to anyone else. However, if you want to be able to refer back to your version of the notebook in future, make sure you click **'File --> Save to Drive'**. 
Your changes will then be saved to your own account, and you can access your edited copy of the notebook from https://colab.research.google.com/.

Open Exercise 1 in Google Colab: <a target="_blank" href="https://colab.research.google.com/github/hsma-programme/h6_4d_decision_trees_random_forests/blob/main/exercises_colab/decision_tree_stroke_exercise.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Open Exercise 2 in Google Colab: <a target="_blank" href="https://colab.research.google.com/github/hsma-programme/h6_4d_decision_trees_random_forests/blob/main/exercises_colab/random_forest_stroke_exercise.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### Exercise Structure

Notebooks are split into **core**, **extension** and **challenge** sections. 

All students should aim to complete the exercises within the **core** section. Completing these exercises will give you practice of all of the key concepts discussed in the lectures and you can stop after this section if you wish. 

Students looking to push themselves and their understanding can go on to attempt the **extension** exercises if they would like to.

The **challenge** section contains exercises that may go beyond what is covered in the lectures; there will be an expectation of looking things up in documentation or on sites such as StackOverflow, or using tools such as perplexity.ai to obtain boilerplate code. These exercises may take significantly longer than is allocated during the lectures and are designed to be an enjoyable challenge for those who want to push their coding skills.

## Solutions

Coming Soon. 

## Learning Objectives

Students should be able to:

- Explain the main points of how a decision tree works
- List the methods that may be used to determine splits (Gini Impurity, entropy, information gain)
- Explain why feature scaling is not required in decision trees
- Explain some benefits and downsides of decision trees
- Write code to classify a dataset using a decision tree using the sklearn library
- Write code to plot the resulting decision tree
- Explain some of the hyperparameters that may be set when using decision trees
    - Pruning
    - Minimum samples (leaf and split)
    - Maximum depth
- Explain the main points of how random forests work
- List the two ways in which randomness is introduced into the tree building process
- Explain the concept of bootstrapping
- Explain the difference between sampling with and without replacement
- Explain some benefits and downsides of random forests
- Write code to classify a dataset using a random forest using the sklearn library
- Explain what f1 score is
- Explain the different kinds of averages that can be calculated for metrics like precision and recall
- Write code to create a confusion matrix using the sklearn library
- Explain the benefits of normalising a confusion matrix
- Write code to create a normalised confusion matrix using the sklearn library
