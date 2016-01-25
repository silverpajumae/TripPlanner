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

print("Getting data, may take a minute")
agency = read_data("Data/agency.txt")
calendar = read_data("Data/calendar.txt")
calendar_dates = read_data("Data/calendar_dates.txt")
routes = read_data("Data/routes.txt")
stop_times = read_data("Data/stop_times.txt")
stops = read_data("Data/stops.txt")
trips = read_data("Data/trips.txt")

agency.pop(0)
calendar.pop(0)
calendar_dates.pop(0)
routes.pop(0)
stop_times.pop(0)
stops.pop(0)
trips.pop(0)

line_list = []

def line_list_maker(trips, stoptimes, stops):
    line_list = []
    counter=0
    for stop in stoptimes:
        if counter>25600:
            return line_list
        else:
            if len(line_list)==0:
                one_line=[]
                one_line.append(stop[0])
                for trip in trips:
                    if trip[2]==stop[0]:
                        one_line.append(trip[4])
                        break
                
                one_stop=[]
                one_stop.append(stop[3])
                for stop_name in stops:
                    if stop_name[0]==stop[3]:
                        one_stop.append(stop_name[2])
                        break
                one_stop.append(stop[2])
                stops_list=[]
                stops_list.append(one_stop)
                one_line.append(stops_list)
                line_list.append(one_line)
                counter+=1
            else:
                i=0
                found=0
                while i < len(line_list):
                    if line_list[i][0]==stop[0]:
                        one_stop=[]
                        one_stop.append(stop[3])
                        for stop_name in stops:
                            if stop_name[0]==stop[3]:
                                one_stop.append(stop_name[2])
                                break
                        one_stop.append(stop[2])
                        line_list[i][2].append(one_stop)
                        counter+=1
                        found=1
                        break
                    i+=1
                if found==0:
                    one_line=[]
                    one_line.append(stop[0])
                    for trip in trips:
                        if trip[2]==stop[0]:
                            one_line.append(trip[4])
                            break
                    
                    one_stop=[]
                    one_stop.append(stop[3])
                    for stop_name in stops:
                        if stop_name[0]==stop[3]:
                            one_stop.append(stop_name[2])
                            break
                    one_stop.append(stop[2])
                    stops_list=[]
                    stops_list.append(one_stop)
                    one_line.append(stops_list)
                    line_list.append(one_line)
                    counter+=1
                else:
                    counter+=1

#to compare times saved as strings
def time_comp(user, current):
    time1=user.split(":")
    time2=current.split(":")
    if int(time1[0])<int(time2[0]):
        return True
    elif int(time1[0])==int(time2[0]):
        if int(time1[1])<int(time2[1]):
            return True
        elif int(time1[1])<int(time2[1]):
            if int(time1[2])==int(time2[2]):
                return True
    
    return False
    
#same lines
def same_line(line_list, starting_point, destination, time):
    print("Looking in the same line.")
    departure_time=0
    arriving_time=0
    start=False
    end=False
    middle=[]
    middlebool=False
    for one_line in line_list:
        if end:
            break
        for stops_list in one_line[2]:
            if starting_point.lower()== stops_list[1].lower():
                if time_comp(time, stops_list[2])==False:
                    break
                departure_time=stops_list[2]
                start=True
                middlebool=True
                middle=[]
            elif start:
                if destination.lower()== stops_list[1].lower():
                    arriving_time = stops_list[2]
                    end=True
                    break      
                middle.append(stops_list[1])

    if start and end:
        if len(middle)>40:
            return False
        print("Departure from " +str(starting_point) +" at:  " + str(departure_time) + " and arrives at " +str(destination) + " at: " + str(arriving_time))
        print("Stops that will be passed by: ")
        print(middle)
        return True
    else:
        print("Can't find the stops/not in the same line.")
        return False


def lines_check(line_list,start, end, i,j):

    line_start=line_list[i][2]
    line_end=line_list[j][2]

    for stop1 in line_start:

        for stop2 in line_end:

            if stop1[1]==stop2[1]:
                return [True, stop1]
    return [False, stop1] 
            
         

    
#one change in lines
def one_change(line_list, starting_point, destination, time, i, j):

    print("Looking lines with one change.")
    departure_time=0
    arriving_time=0
    start=False
    end=False
    middle=[]
    middlebool=False
    for line in line_list:

        if start:
            break
        i+=1
        for stops_list in line[2]:
            if starting_point.lower()== stops_list[1].lower():
                if time_comp(time, stops_list[2])==False:
                    break
                departure_time=stops_list[2]
                start=True
                middlebool=True
                middle=[]
    if start:
        for line in line_list:
            j+=1
            for stops_list in line[2]:
                if destination.lower()== stops_list[1].lower():
                    if time_comp(time, stops_list[2])==True and time_comp(departure_time,stops_list[2])==True:
                        
                        middle.append(stops_list[1])
                        arriving_time=stops_list[2]
                        check=lines_check(line_list, starting_point, destination, i, j)
                        if check[0]:
                            print("Departure from " +str(starting_point) +" at:  " + str(departure_time) + " and arrives at " +str(destination) + " at: " + str(arriving_time))
                            print("Change lines at :" +check[1][1])
                            
                            return True
                        else:
                            print("Error, something went wrong")
                            return False
                    else:
                        break
    else:
        print("Cant find the stops")

def check_stop_exists(stop_name, stops_list):
    for i in stops_list:
        if i[2].lower()==stop_name.lower():
            return True
    return False
     
        
line_list = line_list_maker(trips, stop_times, stops)

#for testing
#for i in liinid:
#    print(i)
#    print()
#print(liinid[-1])


testing=input("Testing mode? y/n: ")

if testing=="y":
    print()
    print("Testing the functions with input: ")
    print("From: kosmos")
    print("To: jaanika")
    print("Time: 15:55:00")
    print()
    print("-----Expected-----")
    print("Departure from kosmos at:  15:57:00 and arrives at jaanika at: 16:34:00")
    print("Middle stops to pass by:")
    print("['Vineeri', 'Tallinn-Väike', 'Kalev', 'Virve', 'Risti', 'Valdeku', 'Hiiu', 'Hõimu', 'Vana-Pääsküla', 'Viljaku', 'Laagri', 'Urda', 'Peoleo', 'Kanama', 'Laiavainu', 'Uku', 'Jõgisoo', 'Harutee', 'Allikamäe', 'Ruila tee', 'Laitse tee']")
    print()
    print("-----Results-----")
    same_line(line_list,"kosmos", "jaanika","15:55:00")
else:
    closing=0
    while closing==0: 
        check_names=0
        while check_names==0:
            starting_point = input("Insert starting stop: ")
            destination = input("Insert destination stop: ")
            time=input("Insert expected departure time (hh:mm:ss): ")
            if check_stop_exists(starting_point,stops):
                if check_stop_exists(destination,stops):
                    check_names=1
                    print()
                    if same_line(line_list, starting_point, destination,time)== False:
                        print()
                        one_change(line_list, starting_point, destination,time, -1, -1)
                else:
                    print("Given destination stop does not exist. Try again.")
            else:
                print("Given starting stop does not exist. Try again.")
        answer=input("Do you with to search more? y/n: ")
        if answer=="n":
            closing=1
            print("Closing program.")
    
            
