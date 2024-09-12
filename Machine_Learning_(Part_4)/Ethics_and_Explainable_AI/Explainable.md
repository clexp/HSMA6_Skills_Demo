# Explainable AI

**This was a slide pack of 173 slides. Even 80 is waay too many. The material here was likely lost lots of people.**

Ultimately, your customer will want to have faith in what you have done. They will want to know how you have come to the conclusions you have come to. You need to be explained to them what you have done. There are a number of tools for this.
You can use some sort of indicative of the importance of each feature. This will be suggestive of the mechanism of action you can also graph the decision trees however this is not clear.

explainability falls into four territories. These are globally explainability techniques, local explainability techniques, model specific techniques, and model agnostic techniques.

### Feature importance

The package will give you a feature importance, 0 is not important, 1 is strong positive correlation and -1 is strong negative correlation. These coefficient represent the change in the log odds of the outcome occurring for a one unit increase in the corresponding feature stop this is a long way of saying one-to-one, and assumes no other features have changed. You take the absolutes of these if you're interested in how much of an impact but not the direction.

The description and pictures here are getting a bit heavy

### Odds

1 is certainty, 0 is impossible and 0.5 is equally likely to happen or not happen. p/(1-p)

#### log odds

this lets yoe see if we are four or five nines. useful for comparing 2 things that are both very likely.

**I had to abandon this for timeliness, and just listed the headings for future reference**

###### Permutation Feature Importance

###### Mean Decrease impurity

###### Model Agnostic xAI

###### Partial Dependence Plots and ICE PLOTs

###### SHAP values "Lloyd Shapley" Game theory and economic theory

These are Shapley Additive Explanations, there is a shap library for this.
Has weaknesses, influenced by feature dependencies, causeal inference and human biases.

###### Local importance : Waterfall

###### Plots

- Violin plots
- cohort bar plots
- decision plots
- Global force plots

#### Prediction uncertainty

bagging, or bootstrap aggregation in random forest plots
We can use this to give us an indication of prediction uncertainty. Higher error suggest sensitivity to the training data, Lower error suggests patterns captured, and there has been sufficient training data

###### xAI for Deep learning

The shap values for images can be done with slicing the image into pieces. Each slice has a chap value,

###### Accumulated for local effect

###### Two Way Partial dependance plots

###### LIME Local interpretable model-agnostic plots

** this was too much information even when racing through at my own pace**
