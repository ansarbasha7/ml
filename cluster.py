import logging
from sklearn.externals import joblib
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('clus.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class KMeansClustering:
    def __init__(self, data):
        self.data = data
        logger.info("Inside KMeansClustering class constructor")

    def elbow_plot(self):
        logger.info("Inside the elbow_plot function in KMeansClustering class")
        try:
            data = self.data
            k_range = range(1, 11)
            sse = []
            for k in k_range:
                km = KMeans(n_clusters=k, init="k-means++", random_state=100, max_iter=1000)
                km.fit(data)
                sse.append(km.inertia_)
            plt.title("K vs sse(choose k value)")
            plt.xlabel("Number of clusters")
            plt.ylabel("sse")
            plt.plot(k_range, sse)
            plt.savefig("Elbow_plot.png")
            kn = KneeLocator(k_range, sse, curve="convex", direction="decreasing")
            logger.info("The optimum number of clusters are: {}".format(kn.knee))
            return kn.knee

        except Exception as e:
            logger.warning("Exception has occured in elbow_plot. Exception message: " + str(e))
            logger.warning("Finding the number of clusters failed.")
            raise Exception()

    def create_clusters(self, k_clusters):
        logger.info("Inside the create_clusters function of the KMeanClustering class")
        try:
            data = self.data
            kmeans = KMeans(n_clusters=k_clusters, init="k-means++", random_state=100, max_iter=1000)
            y_predicted = kmeans.fit_predict(data)
            joblib.dump(kmeans, "model_joblib")
            data["Cluster"] = y_predicted
            logger.info("Successfully created {} clusters.".format(k_clusters))
            return data
        except Exception as e:
            logger.warning("Exception has occured in creating_clusters.Exception message: " + str(e))
            logger.warning("Fitting the data to clusters failed.")
            raise Exception()


df = pd.read_csv('data.csv')
df.drop(['Unnamed: 0', 'ID'], axis='columns', inplace=True)
k = KMeansClustering(df)
clus = k.elbow_plot()
data = k.create_clusters(clus)
print(data.head())
