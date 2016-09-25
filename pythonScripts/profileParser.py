import json
import urllib
import urllib2
from re import sub
from decimal import Decimal

responseCall 	= urllib2.urlopen('http://steamcommunity.com/id/sinbra/inventory/json/753/6')
jsonResponse 	= responseCall.read()
jsonData 		= json.loads(jsonResponse);
totalPrice		= 0.0

if ( jsonData is None ):

	print "Json Structure is not correct"

elif ( jsonData["success"] == False ):

	print "Json Response is not valid"

else:

	for itemID in jsonData["rgDescriptions"]:

		try:

			itemObj		= jsonData["rgDescriptions"][itemID];

			appid		= itemObj["appid"];
			iconURL		= itemObj["icon_url"];
			name		= itemObj["name"];
			marketName  = itemObj["market_name"];
			marketHash	= itemObj["market_hash_name"];
			typeItem	= itemObj["type"];

			itemCall 	= urllib2.urlopen('http://steamcommunity.com/market/priceoverview/?currency=3&appid=' + str(appid) + '&market_hash_name=' + urllib.quote(str(marketHash)));
			itemResp 	= itemCall.read();
			itemData 	= json.loads(itemResp);

			if ( itemData["success"] == True ):

				itemPrice		= itemData["median_price"];
				itemPriceDec	= float(Decimal(sub(r'[^\d.]', '', itemPrice.replace(",","."))))

				print "Name Item: " + marketName
				print "Price:     " + itemPrice

				totalPrice = totalPrice + itemPriceDec

		except:

			print("Oops! Error in the current Item.")

print "#######################################"
print "TotalPrice: " + str(totalPrice);


