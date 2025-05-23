# preprocess_and_model.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from textblob import TextBlob
import plotly.express as px


# Load Data
attendance_data = pd.read_csv("attendance_data.csv")
merchandise_sales = pd.read_csv("merchandise_sales.csv")
fan_data = pd.read_csv("fan_data.csv")
social_data = pd.read_csv("social_media_comments.csv")

# ----- FAN SEGMENTATION -----
features = fan_data[['AttendanceFreq', 'MerchSpend', 'DigitalEngagement']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
fan_data['Segment'] = kmeans.fit_predict(scaled_features)

# Save the updated data
fan_data.to_csv("fan_data_segmented.csv", index=False)

# ----- SENTIMENT ANALYSIS -----
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

social_data["Sentiment"] = social_data["Comment"].apply(get_sentiment)
social_data.to_csv("social_media_comments_scored.csv", index=False)
