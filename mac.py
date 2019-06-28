import requests
mac_address = raw_input("Enter your MAC address: ") 
vendor = requests.get('https://api.macaddress.io/v1?apiKey=at_vlI1yrNeMikipomW3wPWBoHzDZkOi&output=vendor&search='+mac_address).text
print 'Vendor name is:',str(vendor)
