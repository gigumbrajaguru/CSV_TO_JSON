import urllib.request
from urllib.request import urlopen
import zipfile
import os.path
import os
from os.path import basename
import csv
import json


ziplocation="./"
urls="https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip"
request=urllib.request

def getUrl():
    url=input("Enter Input")
    ziplocation=input("Enter save location")
    fileRetriever(url,ziplocation)

def fileRetriever(url,ziplocation=ziplocation):
    filename = downloadFromUrl(url, ziplocation)
    unzipFile(filename,ziplocation)

def downloadFromUrl(url=urls,ziplocation=ziplocation):
    filename=basename(urlopen(url).url)
    request.urlretrieve(url,ziplocation+filename)
    return filename

def unzipFile(filename,ziplocation):
    if os.path.isfile(ziplocation+filename):
        with zipfile.ZipFile(ziplocation+filename,'r') as zip:
            zip.extractall(ziplocation+"/csv")
        readFile(ziplocation+"/csv")
    else:
        print("Unable to find file")


def readFile(file_path):
    path= "./csv/"
    if os.path.isfile(path):
        with open(path) as csvf:
            csvReader=csv.DictReader(csvf)
            for rows in csvReader:
                print(rows)
    else:
        print("unable to find .csv file")

fileRetriever("https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip")