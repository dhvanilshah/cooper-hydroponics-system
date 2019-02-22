from run_query import run_query


def recordTemp(temp):
    query = """
            mutation {
            recordTemp(value: """+str(temp)+""") 
            }
            """
    result = run_query(query)
    status = result["data"]["recordTemp"]
    return status
