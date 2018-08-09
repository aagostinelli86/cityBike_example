import sys
import os
import logging
sys.path.append(os.getcwd() + "/../")

from bikeclustering.datareader.readers import Readers
from bikeclustering.settings import DATA_PATH
from bikeclustering.machinelearning.featureprocessing import DataHandler
from bikeclustering.machinelearning.clustering import HDBscanCity

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main(argv):
    """
    Run th whole analysis
    :param argv: command line parameter representing the minimum number
    of desired components in the HDBscan clustering
    :return: 1
    """

    nMinClsSize = int(sys.argv[1:][0])

    logger.info('Start reading database')
    rd = Readers(logger)
    data = rd.fromJSONtoPandas(DATA_PATH)

    logger.info('Feature Engineering and Data Manipulation ...')
    handler  = DataHandler(data, logger)
    handler.splitStreets()
    logger.debug(data["corner_1"])

    points = handler.fromGeoToRadiants()
    logger.debug(points)

    logger.info('Running the Clustering with HDBSCAN')

    ##these should be aprameters from args
    scanHDB = HDBscanCity(logger = logger,
                          min_cluster_size = nMinClsSize,
                          metric= "haversine")
    cls  = scanHDB.runClustering(points)
    scanHDB.visualizeClusters(cls = cls, df=data)

    return 1


if __name__ == "__main__":
    main(sys.argv[1:])