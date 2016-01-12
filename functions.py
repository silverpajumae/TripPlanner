import codecs

agency = []
calendar = []
calendar_dates = []
routes = []
stop_times = []
stops = []
trips = []


def read_data(file_name):
    f = codecs.open(file_name, 'r', 'UTF-8')
    parts = []
    data = []
    
    for line in f:
        parts.append(line.splitlines())
    
    for i in parts:
        data.append(i[0].split(","))
    parts.clear()
    return data

agency = read_data("Data/agency.txt")
calendar = read_data("Data/calendar.txt")
calendar_dates = read_data("Data/calendar_dates.txt")
routes = read_data("Data/routes.txt")
stop_times = read_data("Data/stop_times.txt")
stops = read_data("Data/stops.txt")
trips = read_data("Data/trips.txt")


