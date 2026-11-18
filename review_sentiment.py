import pandas as pd

#Loading the dataset collected from Kaggle
df=pd.read_csv('tripadvisor_hotel_reviews.csv')

#Assigning sentiment_labels to the rating colum of te dataset

def assign_sentiment(rating):
    if rating >= 4:
        return 'positive'
    elif rating == 3:
        return 'neutral'
    else:
        return 'negative'

df['sentiment_label'] = df['Rating'].apply(assign_sentiment)

#To manually extract the 100 evaluation dataset sample from the original dataset
positive_data = df[df['sentiment_label'] == 'positive'].sample(n=34, random_state=42)
neutral_data = df[df['sentiment_label'] == 'neutral'].sample(n=33, random_state=42)
negative_data = df[df['sentiment_label'] == 'negative'].sample(n=33, random_state=42)

#Combination into a single evaluation dataset of 100 samples
final_df = pd.concat([positive_data, neutral_data, negative_data]).sample(frac=1, random_state=42).reset_index(drop=True)

#Add auditing column for peer check

final_df['peer_checked'] = False
final_df['peer_notes']=""

#Saving the final dataset to a new CSV file

final_df = final_df[['Review', 'Rating', 'sentiment_label', 'peer_checked', 'peer_notes']]
final_df.to_csv('evaluation_100dataset.csv', index=False)

print("Evaluation dataset of 100 samples has been created and saved as 'evaluation_100dataset.csv'.")