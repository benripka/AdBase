import re

class Parser:
	#TODO: Make sure that we don't create empty lines in the files (incase of nulls in say date or price)'
	# Parser constructor for a given file
	def __init__(self, myFile):
		self.myFile = myFile
		self.ads = []
	
	# Returns a lise of the important lines of the file (the ones describing ads)	
	def getLines(self):
		openFile = open(self.myFile, "r")
		print("Opened")
		print(openFile)
		
		ads = openFile.readlines();
		firsLine = ads.pop(0)
		secondLine = ads.pop(0)
		lastLine = ads.pop(-1)
		
		return ads
		
	# Returns list of results after searching a line for a given regex pattern
	def parseLine(self, regex, line):
		found = re.findall(regex, line)
		if len(found) == 1:
			return found
		else: return None
		
	# Parses raw text lines and returns a list of ad object for each 
	def parseForAds(self):
		
		lines = self.getLines()
		
		reDates = "<date>(.*)</date>"
		reIds = "<aid>(.*)</aid>"
		reCat = "<cat>(.*)</cat>"
		reLoc = "<loc>(.*)</loc>"
		reDesc = "<desc>(.*)</desc>"
		reTi = "<ti>(.*)</ti>"
		rePrice = "<price>(.*)</price>"
		
		global ads
		
		for line in lines:
			adXML = line
			date = self.parseLine(reDates, line)[0]
			adId = self.parseLine(reIds, line)[0]
			cat = self.parseLine(reCat, line)[0]
			loc = self.parseLine(reLoc, line)[0]
			desc = self.parseLine(reDesc, line)[0]
			title = self.parseLine(reTi, line)[0]
			price = self.parseLine(rePrice, line)[0]
			
			self.ads.append(Ad(adXML, date, adId, loc, cat, title, desc, price))
		
		return	
		
	def displayAds(self):
		for ad in self.ads:
			ad.display()
		
	def renderTermsFile(self):
		termsFile = open("terms.txt", "w+")
		for ad in self.ads:
			for term in ad.findTerms():
				termsFile.write(term.lower() + ":" + ad.adId +"\n")
	
	def renderDatesFile(self):
		datesFile = open("pdates.txt", "w+")
		for ad in self.ads:
			datesFile.write(ad.date + ":" + ad.adId + "," + ad.title + "," + ad.loc + "\n")

		
	def renderPriceFile(self):
		priceFile = open("prices.txt", "w+")
		for ad in self.ads:	
			priceFile.write(ad.price + ":" + ad.adId + "," + ad.cat + "," + ad.loc + "\n")
		
	def renderAdsFile(self):
		adFile = open("ads.txt", "w+")
		for ad in self.ads:
			adFile.write(ad.adId + ":" + ad.adXML)
		
	
class Ad:
	
	# Ad object constructor
	def __init__(self, adXML, date, adId, loc, cat, title, desc, price):
		self.adXML = adXML
		self.date = date
		self.adId = adId
		self.loc = loc
		self.cat = cat
		self.title = title
		self.desc = desc
		self.price = price
		self.terms = None
		
	# Utility funciton to display the contents of an ad
	def display(self):
		print("These are the ad parameters:")
		print("\tadXML: " + self.adXML)
		print("\tDate: " + self.date)
		print("\tId: " + self.adId)
		print("\tLocation: " + self.loc)
		print("\tCatagory: " + self.cat)
		print("\tTitle: " + self.title)
		print("\tDescription: " + self.desc)
		print("\tPrice: " + self.price)
		print("\n---------------------------------------------------\n")
		
		
	# Return a list of all terms in the title and description of the ad
	def findTerms(self):
		
		reTerms = "[a-zA-Z0-9_-]{3,}"
		
		terms = re.findall(reTerms, self.title) + re.findall(reTerms, self.desc)
		
		return terms
				
		
	

if __name__ == "__main__":
	print("Hello World")
	parser = Parser("1000.txt")

	parser.parseForAds()
	parser.renderDatesFile()
	parser.renderTermsFile()
	parser.renderPriceFile()
	parser.renderAdsFile()


	
	
	
	
	
