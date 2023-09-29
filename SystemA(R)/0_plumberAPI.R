setwd("~/DII_sourceCode/SystemA(R)/")
r = plumber::plumb("1_SetupAPI.R") 
r$run(port=8567,swagger = TRUE)
getwd()