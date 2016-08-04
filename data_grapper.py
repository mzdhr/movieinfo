import json
import urllib.request


def fetch_info(title):
    try:
        # Parsing url
        API = 'http://www.omdbapi.com/?t=' + title.replace(' ', '+') + '&y=&plot=full&r=json'

        # Graping data from the api
        connection = urllib.request.urlopen(API)
        output = connection.read().decode('utf-8')
        connection.close()

        # Creating dictionary using json object
        api_data = json.loads(output)

        # Gathering data
        box_info = [api_data['Title'], api_data['Runtime'], api_data['Type'], api_data['Year'], api_data['Genre'],
                    api_data['imdbRating'], api_data['imdbVotes'], api_data['Plot'], api_data['Director'], api_data['Actors'],
                    api_data['Writer'], api_data['imdbID']]

    except KeyError:
        box_info = False
        print('Can\'t recognize movie title!')

    except urllib.request.URLError:
        box_info = False
        print('No Internet connection!')

    return box_info

