import re
import ply.yacc as yac
import ply.lex as lex

alphaNum = "[0-9a-zA-Z_-]"
numeric = "[0-9]"
date = numeric + numeric + numeric + numeric + '/' + numeric + numeric + '/' + numeric + numeric
datePrefix = date + "[\s]*"
dateQuery = datePrefix + "[\s]*" + date
price = numeric + "+"
pricePrefix = price + "[\s]*" + "(=|>|<|<=|>=)"
priceQuery = pricePrefix + price
location = alphaNum + "+"
locPrefix = location + "[\s]*="
locQuery = locPrefix + "[\s]*" + location
cat = alphaNum + "+"
catPrefix = cat + "[\s]*"
catQuery = catPrefix + "[\s]+"
term = alphaNum + "+"
termSuffix = "%"
termQuery = "(" + term + "|" + term + termSuffix + ")"
expression = dateQuery + "|" + priceQuery + "|" + locQuery + "|" + catQuery + "|" + termQuery
query = expression + "([\s]*" + expression + ")*"

def clean(queries):
	
	match = re.findall("\s*[=><]\s*", queries)
	for thing in match:
		print(thing.strip())
		queries = re.sub(thing, thing.strip(), queries)
	return queries
		


def classify(query):
	alphaNum = "[0-9a-zA-Z_-]"
	numeric = "[0-9]"
	date = numeric + numeric + numeric + numeric + '/' + numeric + numeric + '/' + numeric + numeric
	datePrefix = date + "[\s]*"
	dateQuery = datePrefix + "[\s]*" + date
	price = numeric + "+"
	pricePrefix = price + "[\s]*" + "(=|>|<|<=|>=)"
	priceQuery = pricePrefix + price
	location = alphaNum + "+"
	locPrefix = location + "[\s]*="
	locQuery = locPrefix + "[\s]*" + location
	cat = alphaNum + "+"
	catPrefix = cat + "[\s]*"
	catQuery = catPrefix + "[\s]+"
	term = alphaNum + "+"
	termSuffix = "%"
	termQuery = "(" + term + "|" + term + termSuffix + ")"
	expression = dateQuery + "|" + priceQuery + "|" + locQuery + "|" + catQuery + "|" + termQuery
	
	if re.search('date[<>=]' + date, query) is not None:
		return "date"
		
		
	elif re.search('location=' + location, query) is not None:
		return "location"
		
	elif re.search(term, query) is not None:
		return "term"
		
	else:
		return "invalid input"
		
	
	
	

	
if __name__ == "__main__":

	print("Please Enter Queries:")
	while True:
		queries = input(">>> ")
		
		for query in clean(queries).split():
			print(classify(query))
		
		
		
		
	
			
		
		
