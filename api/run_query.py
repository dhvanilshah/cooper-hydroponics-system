import os, sys, inspect
import requests
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import settings

headers = {"system": settings.SYSID}

# A simple function to use requests.post to make the API call. Note the json= section.
def run(query):
    request = requests.post(settings.API,
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run.")

    return
