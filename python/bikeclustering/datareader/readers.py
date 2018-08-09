import json
import pandas as pd
import os
import logging


class Readers(object):
    def __init__(self, logger):
        self.logger = logger

    def fromJSONtoPandas(self, path):
        """
        convert a json file to a pandas df
        :param path: json data path
        :return: a pandas dataframe
        """
        ## check if the file does exist
        if not os.path.isfile(path):
            self.logger.error("input json not found")

        with open(path, 'r') as f:
            datalist = json.load(f)

        return pd.DataFrame(datalist)