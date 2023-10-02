#
# This is a Plumber API. You can run the API by clicking
# the 'Run API' button above.
#
# Find out more about building APIs with Plumber here:
#
#    https://www.rplumber.io/
#
library(plumber) 


summaries = read.csv("./CSV/psgcDetails.csv")

#SVEIR Code ------------------
getPsgcDetails = function(psgcInput) {
  dfToReturn = summaries[which(as.numeric(summaries$area) == as.numeric(psgcInput)),]
  return(dfToReturn)
}
