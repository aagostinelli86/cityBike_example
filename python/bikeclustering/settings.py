import os

__this_dir__, __this_filename__ = os.path.split(__file__)

#LOG_LEVEL = "DEBUG"

PYTHON_ROOT = os.path.join(__this_dir__, '..')
DATA_PATH = os.path.join(__this_dir__, '..', '..', 'data','Brisbane_CityBike.json')
OUTPUT_PATH = os.path.join(__this_dir__, '..', '..', 'results')