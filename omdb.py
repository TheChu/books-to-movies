# Doesn't work
import csv
import urllib2
import json

url = "http://www.omdbapi.com/?t=Harry+Potter&r=json&tomatoes=true&type=movie"
response = urllib2.urlopen(url).read()
data = json.loads(response)

fname = 'data.csv'

with open(fname,'wb') as outf:
    outcsv = csv.writer(outf)
    outcsv.writerows(data)
