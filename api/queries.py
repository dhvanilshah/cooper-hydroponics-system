from api.run_query import run


def recordTemp(temp):
    query = """
            mutation {
            recordTemp(value: """+str(temp)+""") 
            }
            """
    result = run(query)
    status = result["data"]["recordTemp"]
    return status
