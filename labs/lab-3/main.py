import sys
import requests

URI = "https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress?address=845%20Market%20St.%2C%20San%20Francisco%2C%20CA&benchmark=Public_AR_Current&vintage=Current_Current&layers=14&format=json"

def save(response):
  """
  Fill in this method.

  Save the text response to the file /tmp/endpoint.json.

  See https://realpython.com/read-write-files-python/#opening-and-closing-a-file-in-python
  """

  with open('/tmp/endpoint.json', 'w') as f:
    f.write(response)

def query(uri):
  """
  Fill in this method.

  Query the passed URI and return the text response.

  See https://2.python-requests.org/en/master/
  """

  response = requests.get(uri)
  return response.text

def main():
  """
  Fill in this 
  """
  save(query(URI))
  

main()