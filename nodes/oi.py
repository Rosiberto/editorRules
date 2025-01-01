
TYPE = "email"
TEMPLATE = "foi enviado para vc" 
TO = "to@to.com"
FROM = "from@from.com.br"
SUBJECT = "enviando email"

#data = "\"action\":{"+ "\"X\":\"{}".format( TYPE )+"\"}"
data = "\"action\": {"+"\"type\":"+ "\"{}".format(TYPE)+"\",\"template\": \"{}".format(TEMPLATE)+ "\",\"parameters\": {\"to\": \"{}".format(TO)+"\",\"from\": \"{}".format(FROM)+"\",\"subject\": \"{}".format(SUBJECT)+"\"}}"

print( data )