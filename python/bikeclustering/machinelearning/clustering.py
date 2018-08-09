import hdbscan
from gmplot import gmplot
from bikeclustering.settings import OUTPUT_PATH

class HDBscanCity(object):
    def __init__(self, logger, min_cluster_size = 4,metric= "haversine"):
        """
        This class is a wrapper to hdbscan. It scans points in rads
        and maps them into a Google Map.
        :param min_cluster_size: min number of components per cluster, to be optimized
        with a silouhette analysis
        :param metric: for lat & long data best metrics is haversine, once radians are considered,
        according to
        http://hdbscan.readthedocs.io/en/latest/faq.html?highlight=lat%20lon%27#q-haversine-metric-is-not-clustering-my-lat-lon-data-correctly
        :param city: the name of the city to download with Google API
        :param logger: logging object
        """
        self.min_cluster_size = min_cluster_size
        self.logger = logger
        self.metric = metric
        self.hb = hdbscan.HDBSCAN(min_cluster_size = self.min_cluster_size,
                                  metric= self.metric)

    def runClustering(self, rads):
        """
        this method runs the HDBSCAN without splitting data into train / test
        this was chosen due to the small amount of data, but it is a good
        :param rads: point radians
        :return: a list of labels with the cluster. According to HDBSCAN, -1 means noise
        """
        self.logger.warning("Overfitting Scenario due to the small dataset")
        cls = hdbscan.HDBSCAN(min_cluster_size=4, metric='haversine')
        cluster_labels = cls.fit_predict(rads)
        self.logger.info("Extracted Clusters: %s", len(set(cluster_labels)))
        return cluster_labels

    def visualizeClusters(self, cls, df):
        """
        visualize results over a Map
        :param cls: list of clusters as from runClustering()
        :param df: pandas dataframe with latitude and longitude data
        :return: a html file with the clusters overlapped to a map
        """
        ouputFile = OUTPUT_PATH+"/min_cluster_size_"+str(self.min_cluster_size)+".html"
        c_lat = df["latitude"].mean()
        c_lon = df["longitude"].mean()

        palette = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6',
                   '#6a3d9a', '#ffff99']
        classes = range(-1, len(palette) - 1)
        colors = dict(zip(classes, palette))
        c_array = [colors[x] for x in cls]

        gmap = gmplot.GoogleMapPlotter(center_lat=c_lat,
                                       center_lng=c_lon,
                                       zoom=14)
        for c in classes:
            index = [i for i, v in enumerate(cls) if cls[i] == c]
            subset = df.iloc[index]
            color = "#000000" if (c == -1) else colors[c]
            gmap.scatter(subset["latitude"], subset["longitude"], c=color, size=60, marker=False, face_color="#FF0000",
                         face_alpha=1)
            gmap.heatmap(df["latitude"], df["longitude"], radius=25)

            gmap.draw(ouputFile)

        self.logger.info('You can now visualize the clustering stored in the results folder')

