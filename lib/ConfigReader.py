import configparser
from pyspark import SparkConf

# loading the application configs in python dictionary
def get_app_config(env):        # we pass the environment from which we want to read the configurations - Local | Dev  | Prod
    config = configparser.ConfigParser()
    config.read("configs/application.conf")     # reading the application.conf file
    app_conf = {}       # creating an empty dict
    for (key, val) in config.items(env):        # loop within the items inside that env/section
        app_conf[key] = val     # add them to the dictionary
    return app_conf     # return the dict

# loading the pyspark configs and creating a spark conf object
def get_pyspark_config(env):
    config = configparser.ConfigParser()
    config.read("configs/pyspark.conf")
    pyspark_conf = SparkConf()
    for (key, val) in config.items(env):
        pyspark_conf.set(key, val)
    return pyspark_conf