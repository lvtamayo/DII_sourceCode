import requests
import pandas as pd
import numpy as np
import os
import csv
import glob

def getLocName(covidModel,location,fitTo,TIMESERIES_URL):
    # #TIMESERIES_URL = "http://localhost:"+ port
    # TIMESERIES_URL = "http://fassster.ehealth.ph/vaxtsstaging" #if direct to deployed model "http://fassster.ehealth.ph/timeseries"

    if (covidModel == "SVEIR"):
        urlPsgcDetails = "{0}/getPsgcDetails?psgcInput={1}".format(TIMESERIES_URL,int(location[0]))
    else:
        urlPsgcDetails = "{0}/getPsgcDetailsSVEIRS?psgcInput={1}".format(TIMESERIES_URL,int(location[0]))

    getPsgcDetails = requests.get(urlPsgcDetails)
    dataPsgcDetails = getPsgcDetails.json()
    dfPsgcDetails = pd.DataFrame.from_dict(dataPsgcDetails)
    data = dfPsgcDetails.to_dict('records')
    temp = dfPsgcDetails.set_index('FittedTo').to_dict("index")
    data = [temp[fitTo]] if fitTo in temp.keys() else []

    return data[0]['Geographical.Place']


urlPsgcDetails = "{0}/getPsgcDetails?psgcInput={1}".format(TIMESERIES_URL,int(location))
getPsgcDetails = requests.get(urlPsgcDetails)
dataPsgcDetails = getPsgcDetails.json()
dfPsgcDetails = pd.DataFrame.from_dict(dataPsgcDetails)
data = dfPsgcDetails.to_dict('records')

params = {
"psgcInput": location, "projectionDuration": projectionDuration, "lambdaDateInput": lambdaDateInput,
"lambdaValuesInput": lambdaValuesInput, "HcLevel": treatlevel, "startHcDate": startHcDate,
"scaleLevel": scale, "fitParamToUse" : fitTo, "interventionCompliance" : ic, "interventionPercentage": ip,
"interventionEndDate" : interventionEndDate, "interventionStartDate" : interventionStartDate, "dateAdjustment": dateAdjustment,
"v1Value": vax1,"v2Value": vax2, "jValue": jvax, "filterPSGCs": filterPSGC
}

urlProjections = "{0}/getProjections".format(TIMESERIES_URL)
getProjections = requests.get(urlProjections,params=params)
