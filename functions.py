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
        if luger>100:
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
            

def sama_liin(liinide_list, valjumiskoht, soovitud_koht):
    valjumis_aeg=0
    saabumisaeg=0
    samas_liinis=False    
    for liin in liinide_list:
        for peatused in liin[2]:
            if valjumiskoht.lower() == peatused[1].lower():
                valjumis_aeg=peatused[2]
                samas_liinis=True
                print("leidsin")
                break
    if samas_liinis==True:
        print("Väljumiskoht leitud, otsin soovitud kohta samas liinis")
    else:
        print("Ei leidnud peatust")
    for liin in liinide_list:
        for peatused in liin[2]:
            if soovitud_koht.lower()== peatused[1].lower():
                saabumisaeg = peatused[2]
                print("leidsin")
                break
    print("Transport väljub " +str(valjumiskoht) +" peatusest kell " + str(valjumis_aeg) + " ja saabub peatusesse " +str(soovitud_koht) + " kell " + str(saabumisaeg))

                
print("Alustan Liinide tööd")
liinid = liinide_koostaja(trips, stop_times, stops)
#for i in liinid:
    #print(i)
    #print()
valjumiskoht = input("Insert FROM stop: ")
soovitud_koht = input("Insert To stop: ")
sama_liin(liinid, valjumiskoht, soovitud_koht)
