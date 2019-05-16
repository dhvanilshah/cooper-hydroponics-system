from api.run_query import run


def recordReadings(temp, tds, wl):
    query = """
            query($temp: Float, $tds: Float, $wl: Int) {
            recordReadings(temp: $temp, tds: $tds, wl: $wl)
            }
            """
    variables = {
        "temp": temp,
        "tds": tds,
        "wl": wl
    }
    print(query)
    result = run(query, variables)
    status = result["data"]["recordReadings"]
    return status


def readLights():
    query = """
            query {
            readLights
            }
            """
    variables = {}
    print(query)
    result = run(query, variables)
    times = result["data"]["readLights"]
    return times
