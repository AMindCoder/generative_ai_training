## Evaluation Metrics for Classification Tasks

True Positive (TP): Correctly predicted positive cases.
True Negative (TN): Correctly predicted negative cases.
False Positive (FP): Incorrectly predicted positive cases (Type I error).
False Negative (FN): Incorrectly predicted negative cases (Type II error).

### Accuracy

Accuracy is the proportion of correct predictions out of all predictions. It is a balanced measure since it takes into account both true positives and true negatives. It is calculated as (TP + TN) / (TP + TN + FP + FN).

### Precision

Precision is the proportion of true positives out of all predictions. It is also known as the positive predictive value. It is calculated as TP / (TP + FP).

### Recall (or Sensitivity)

Recall is the proportion of true positives out of all actual positive cases. It is also known as the true positive rate. It is calculated as TP / (TP + FN).

### F1 Score

The F1 score is the harmonic mean of precision and recall. It is a balanced measure since it takes into account both precision and recall. It is calculated as 2 * (Precision * Recall) / (Precision + Recall).




E.g Consider a spam email classifier evaluated on 1,000 emails:

Actual Spam: 100 emails
Actual Not Spam: 900 email

Model predictions:

Correctly identified 80 spam emails (TP = 80)
Incorrectly marked 50 non-spam emails as spam (FP = 50)
Missed 20 spam emails, marking them as not spam (FN = 20)
Correctly identified 850 non-spam emails (TN = 850)


Lets Calculate :

Accuracy  = (TP + TN)/ (TP + FP + FN + TN)


Recall (Sensitivity) = TP/(TP + FN)

FN is more dangerous for the use case e.g Detecting Cancer, Security Threat Detection.
​

Precision = TP/(TP + FP)

FP is more dangerous for the use case e.g Bank Loan app (Misclassifying a high-risk applicant as low-risk) 



Consider a model designed to classify images into three categories: Dogs, Cats, and Rabbits. Suppose we evaluate this model on a test set of 30 images, with 10 images per category.


| Actual \ Predicted | Dog | Cat | Rabbit |
|--------------------|-----|-----|--------|
| **Dog**            |  8  |  1  |   1    |
| **Cat**            |  2  |  7  |   1    |
| **Rabbit**         |  0  |  2  |   8    |


Interpreting the Matrix:

Diagonal Elements: These represent correctly classified instances.

8 Dogs correctly identified as Dogs.
7 Cats correctly identified as Cats.
8 Rabbits correctly identified as Rabbits.
Off-Diagonal Elements: These indicate misclassifications.

1 Dog misclassified as a Cat; 1 Dog misclassified as a Rabbit.
2 Cats misclassified as Dogs; 1 Cat misclassified as a Rabbit.
2 Rabbits misclassified as Cats.
Calculating Metrics for Multiclass Classification:

In multiclass settings, metrics like Precision and Recall can be computed for each class individually, and then averaged to obtain overall performance measures.

Precision for Each Class:

Precision (Dog): Proportion of images predicted as Dogs that are actually Dogs. 
Precision (Dog)=True Positives (Dog)/Predicted as Dog =8/8+2 = 8/10 =0.80(80%)

Precision (Cat): Proportion of images predicted as Cats that are actually Cats. 

Precision (Cat)=7/7+3=7/10=0.70(70%)

Precision (Rabbit): Proportion of images predicted as Rabbits that are actually Rabbits. 
Precision (Rabbit)=8/8+2 =8/10=0.80 (80%)

Recall for Each Class:

Recall (Dog): Proportion of actual Dog images correctly identified. 
Recall (Dog) =True Positives (Dog)/Actual Dog Images =8/8+1+1=8/10=0.80(80%)

Recall (Cat): Proportion of actual Cat images correctly identified. 
Recall (Cat)=7/7+2+1=7/10=0.70(70%)

Recall (Rabbit): Proportion of actual Rabbit images correctly identified. 
Recall (Rabbit)=8/8+2=8/10=0.80(80%)


Introducing the Harmonic Mean:

The harmonic mean is a way to calculate an average that emphasizes the smaller values. It's particularly useful when averaging rates or ratios, such as precision and recall, because it penalizes extreme differences between them.

The harmonic mean of two numbers, 
𝑎 b, is calculated as:

Harmonic Mean=2×𝑎×𝑏/𝑎+𝑏
​ 

F1 Score:

The F1 score is the harmonic mean of precision and recall. It provides a single metric that balances both concerns, especially useful when you need to balance the trade-off between precision and recall.

The formula for the F1 score is:
𝐹1=2×Precision×Recall/Precision+Recall

We previously calculated precision and recall for each class:

Precision:

Dog: 80%
Cat: 70%
Rabbit: 80%
Recall:

Dog: 80%
Cat: 70%
Rabbit: 80%
Calculating F1 Scores:

F1 Score for Dog: 
𝐹1 Dog = 2×0.80×0.80/0.80+0.80 =2×0.64/1.60=0.80(80%)

F1 Score for Cat: 
𝐹1 Cat =2×0.70×0.70/0.70+0.70 = 2×0.491/.40=0.70(70%)

F1 Score for Rabbit: 
𝐹1 Rabbit=2×0.80×0.80/0.80+0.80=2×0.64/1.60=0.80(80%)

Why Use the Harmonic Mean?

The harmonic mean is particularly sensitive to low values. In the context of the F1 score, this means that if either precision or recall is low, the F1 score will also be low. This property ensures that a high F1 score is achieved only when both precision and recall are high and balanced.

For example, if a model has a precision of 100% but a recall of 0%, the arithmetic mean would suggest a performance of 50%, which is misleading. The harmonic mean, however, would correctly reflect the poor performance with an F1 score of 0%.

Understanding the F1 score and its reliance on the harmonic mean is crucial for evaluating models, especially in scenarios where there's an imbalance between classes or when both false positives and false negatives carry significant consequences.
