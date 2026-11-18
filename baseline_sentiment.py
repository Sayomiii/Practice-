import pandas as pd 
import nltk
nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import classification_report, accuracy_score

#Load the final evaluation dataset
final_df = pd.read_csv('evaluation_100dataset.csv')

#To perform sentiment analysis using VADER on the 'Review' column
sia = SentimentIntensityAnalyzer()

#To predict sentiment for each review and assign sentiment labels

def predict_vadar_sentiment(review):
    score = sia.polarity_scores(review)
    compound_score = score['compound']
    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'
    
#To generate predicted sentiment labels for the reviews in the dataset

final_df['predicted_vader'] = final_df['Review'].apply(predict_vadar_sentiment)

#To calculate the baseline accuracy

baseline_accuracy = accuracy_score(final_df['sentiment_label'], final_df['predicted_vader']) *100

print("=" * 30)
print(f"BASELINE MODEL ACCURACY: {baseline_accuracy:.2f}")
print("=" * 30)
print("\nClassification Report:\n")
print(classification_report(final_df['sentiment_label'], final_df['predicted_vader'], zero_division=0))