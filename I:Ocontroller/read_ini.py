import configparser
from os.path import dirname, join, abspath

ini_file_name =("qajarvix.ini")
configuration = configparser.ConfigParser()
configuration.optionxform = str
configuration.read(ini_file_name)

print(configuration['mysql 56']['type'])