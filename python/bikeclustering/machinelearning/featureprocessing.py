import numpy as np


class DataHandler(object):
    def __init__(self, df, logger):
        """
        class for data manipulation and feature engineering
        :param df: raw input pandas dataframe from json file
        :param logger: logging object
        """
        self.df = df
        self.logger = logger
    def fromGeoToRadiants(self):
        """
        Transform Latitude and Longitude into radiants
        :param df: a pandas dataframe with latitude and longitude info
        :return: data in radiants
        """
        points = list(zip(self.df.latitude, self.df.longitude))
        rads = np.radians(points)
        self.logger.debug(rads)
        return rads

    def splitStreets(self):
        def transform(s):
            tokens = s.split('-',1)
            if(len(tokens) > 1):
                return tokens[1].strip()
            return None

        self.df["corner_1"], self.df["corner_2"] = self.df["name"].str.split('/', 1).str
        self.df["corner_1"] = self.df["corner_1"].apply(lambda x: transform(x))
        self.df["corner_2"] = self.df["corner_2"].str.strip()