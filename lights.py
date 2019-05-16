from api.queries import readLights
import datetime


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def main():
    result = readLights()

    startTime = result[0].split(":")
    stopTime = result[1].split(":")

    start = datetime.time(int(startTime[0]), int(startTime[1]), 0)
    end = datetime.time(int(stopTime[0]), int(stopTime[1]), 0)

    if (time_in_range(start, end, datetime.datetime.now().time())):
        print("Turn on lights")
        pass
    else:
        print("Turn off lights")
        pass

    # print(datetime.datetime.now().time())

    # print(time_in_range(start, end, datetime.time(16, 30, 0)))
    # print(time_in_range(start, end, datetime.time(12, 30, 0)))


if __name__ == "__main__":
    main()
