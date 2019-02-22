import settings
import requests
headers = {"system": settings.SYSID}


# A simple function to use requests.post to make the API call. Note the json= section.
def run_query(query):
    request = requests.post(settings.API,
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run.")
