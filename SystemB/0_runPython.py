import pandas as pd
import requests

port = "8567" #change this. it should be same with R server port
API_URL = "http://localhost:"+ port #run via local machine


urlEcho = "{0}/echo?msg={1}".format(API_URL, "Hi")
getEcho = requests.get(urlEcho)
dataEcho = getEcho.json()

print(dataEcho['msg'][0])


urlSum = "{0}/sum?a={1}&b={2}".format(API_URL, int(2), int(3))
getSum = requests.post(urlSum)
dataSum = getSum.json()

print("Sum is" , dataSum[0])


urlPSGC = "{0}/getPsgcDetails?psgcInput={1}".format(API_URL, int(130000000))
getPSGC = requests.get(urlPSGC)
dataPSGC = getPSGC.json()
dfPsgcDetails = pd.DataFrame.from_dict(dataPSGC)
dataPSGC = dfPsgcDetails.to_dict('records')

print(dataPSGC)