import json
import urllib.request


def fetch_info(title):
    # Parsing url
    API = 'http://www.omdbapi.com/?t=' + title.replace(' ', '+') + '&y=&plot=full&r=json'

    # Graping data from the api
    connection = urllib.request.urlopen(API)
    output = connection.read().decode('utf-8')
    connection.close()

    # Creating dictionary using json object
    apiData = json.loads(output)

    # Gathering data
    box_info = [apiData['Title'], apiData['Runtime'], apiData['Type'], apiData['Year'], apiData['Genre'],
                apiData['imdbRating'], apiData['imdbVotes'], apiData['Plot'], apiData['Director'], apiData['Actors'],
                apiData['Writer'], apiData['imdbID']]

    return box_info