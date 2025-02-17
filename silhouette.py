import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

matplotlib.use('agg')

# Load data with clusters
file_path = 'babyNamesUSYOB-mostpopular.csv'
data = pd.read_csv(file_path)

# Keep only numerical columns
numerical_data = data.select_dtypes(include=['float64', 'int64'])

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)

# Silhouette method
silhouette_scores = []
k_range = range(6, 14)

for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(scaled_data)
    score = silhouette_score(scaled_data, kmeans.labels_)
    silhouette_scores.append(score)
    print("iter done)")

# Visualization of the silhouette method
plt.figure(figsize=(10, 8))
plt.plot(k_range, silhouette_scores, 'bx-')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method For Optimal k')
plt.savefig('visual/silhouette_method.png')
