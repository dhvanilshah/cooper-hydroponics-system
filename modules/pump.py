import requests

headers = {"system": "5bec7b2b008be98c392c517a"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('http://localhost:8000/api', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run.")

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
mutation {
  recordTemp(value: """+str(19.1)+""") 
  }
"""

result = run_query(query) # Execute the query
remaining_rate_limit = result["data"]["recordTemp"] # Drill down the dictionary
print("Remaining rate limit - {}".format(remaining_rate_limit))
