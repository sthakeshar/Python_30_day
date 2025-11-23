import requests
#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
url='https://api.thecatapi.com/v1/breeds'

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
#print(response.text) # gives all the text from the page
countries = response.json()
print(countries[:1])