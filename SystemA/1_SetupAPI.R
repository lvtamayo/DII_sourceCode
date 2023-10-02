source("2_LoadLibraries.R")

#* @apiTitle Plumber Example API
#* @apiDescription Plumber example description.

#* Echo back the input
#* @param msg The message to echo
#* @get /echo
function(msg = "") {
  list(msg = paste0("The message is: '", msg, "'"))
}

#* Return the sum of two numbers
#* @param a The first number to add
#* @param b The second number to add
#* @post /sum
function(a, b) {
  as.numeric(a) + as.numeric(b)
}

#* Get Location Details
#* @param psgcInput No leading zero (ie. Region 1 is only 10000000)
#* @get /getPsgcDetails
function(psgcInput) {
  return(getPsgcDetails(psgcInput))
}

