import pandas as pd
import time
from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

#To load the final evaluation dataset and main 
final_df = pd.read_csv('evaluation_100dataset.csv')
total_df = pd.read_csv('tripadvisor_hotel_reviews.csv')

#To exclude the evaluation dataset from the main dataset to avoid data leakage
train_df = total_df[~total_df['Review'].isin(final_df['Review'])].copy()

def assign_sentiment(rating):
    return 'positive' if rating >= 4 else ('neutral' if rating == 3 else 'negative')

train_df['sentiment_label'] = train_df['Rating'].apply(assign_sentiment)

#To train a Logistic Regression model using TF-IDF features

start_time = time.time()
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2), stop_words='english')
X_train = vectorizer.fit_transform(train_df['Review'].astype(str))
y_train = train_df['sentiment_label']

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

#To predict sentiment for the evaluation dataset using the trained model

X_eval = vectorizer.transform(final_df['Review'].astype(str))
final_preds = model.predict(X_eval)
final_time = (time.time() - start_time) * 1000  # Convert to milliseconds

#To calculate the accuracy of the Logistic Regression model on the evaluation dataset
final_accuracy = accuracy_score(final_df['sentiment_label'], final_preds) *100

#To print the results of the Logistic Regression model evaluation
print("\n--- MODEL COMPARISION RESULTS---")
print(f"{'Model':<30} {'Accuracy (%)':<10}")
print("" + "-" * 60)
print(f"{'TF-IDF + Logistic Regression':<30} {final_accuracy:.2f}%  {'PASS' if final_accuracy >= 75 else 'FAIL':<20}")