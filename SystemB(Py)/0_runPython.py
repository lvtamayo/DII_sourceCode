from runCode import *
import pandas as pd
import os
import math
# unused package/module
# import xlsxwriter
# import glob

port = "8567" #change this. it should be same with R server port
TIMESERIES_URL = "http://localhost:"+ port #run via local machine
#TIMESERIES_URL = "http://fassster.ehealth.ph/vaxtsstaging" #run via deployed server
  
BASE_DIR = os.getcwd()
df = pd.read_csv(BASE_DIR + "/SVEIRS-Projection/scenario-files/May10.csv") #Scenario File
