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

print("Getting data")
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

liinid = []

def liinide_koostaja(trips, stoptimes, stops):
    liinid = []
    luger=0
    for stop in stoptimes:
        if luger>25600:
            return liinid
        else:
            if len(liinid)==0:
                liin=[]
                liin.append(stop[0])
                for trip in trips:
                    if trip[2]==stop[0]:
                        liin.append(trip[4])
                        break
                
                peatus=[]
                peatus.append(stop[3])
                for stop_name in stops:
                    if stop_name[0]==stop[3]:
                        peatus.append(stop_name[2])
                        break
                peatus.append(stop[2])
                peatused=[]
                peatused.append(peatus)
                liin.append(peatused)
                liinid.append(liin)
                luger+=1
            else:
                i=0
                leidus=0
                while i < len(liinid):
                    if liinid[i][0]==stop[0]:
                        peatus=[]
                        peatus.append(stop[3])
                        for stop_name in stops:
                            if stop_name[0]==stop[3]:
                                peatus.append(stop_name[2])
                                break
                        peatus.append(stop[2])
                        liinid[i][2].append(peatus)
                        luger+=1
                        leidus=1
                        break
                    i+=1
                if leidus==0:
                    liin=[]
                    liin.append(stop[0])
                    for trip in trips:
                        if trip[2]==stop[0]:
                            liin.append(trip[4])
                            break
                    
                    peatus=[]
                    peatus.append(stop[3])
                    for stop_name in stops:
                        if stop_name[0]==stop[3]:
                            peatus.append(stop_name[2])
                            break
                    peatus.append(stop[2])
                    peatused=[]
                    peatused.append(peatus)
                    liin.append(peatused)
                    liinid.append(liin)
                    luger+=1
                else:
                    luger+=1

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
def sama_liin(liinide_list, valjumiskoht, soovitud_koht, time):
    print("Looking in the same line.")
    valjumis_aeg=0
    saabumisaeg=0
    start=False
    end=False
    middle=[]
    middlebool=False
    for liin in liinide_list:
        if end:
            break
        for peatused in liin[2]:
            if valjumiskoht.lower()== peatused[1].lower():
                if time_comp(time, peatused[2])==False:
                    break
                valjumis_aeg=peatused[2]
                start=True
                middlebool=True
                middle=[]
            elif start:
                if soovitud_koht.lower()== peatused[1].lower():
                    saabumisaeg = peatused[2]
                    end=True
                    break      
                middle.append(peatused[1])

    if start and end:
        print("Departure from " +str(valjumiskoht) +" at:  " + str(valjumis_aeg) + " and arrives at " +str(soovitud_koht) + " at: " + str(saabumisaeg))
        print("Stops that will be passed by: ")
        print(middle)
        return True
    else:
        print("Can't find the stops/not in the same line.")
        return False

liinid = liinide_koostaja(trips, stop_times, stops)

#for testing
#for i in liinid:
#    print(i)
#    print()
#print(liinid[-1])
valjumiskoht = input("Insert FROM stop: ")
soovitud_koht = input("Insert TO stop: ")
time=input("Insert time (hh:mm:ss): ")
sama_liin(liinid, valjumiskoht, soovitud_koht,time)
