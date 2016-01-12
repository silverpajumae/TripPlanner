import codecs


def read_agency(file_name):
    f = codecs.open(file_name, 'r', 'UTF-8')
    
    parts = []
    agencies = []
    for line in f:
        parts.append(line.splitlines())
    
    for i in parts:
        agencies.append(i[0].split(","))
    agencies.remove(agencies[0])
    parts.clear()
    return agencies
        
        
test = read_agency("Data/agency.txt")

for i in test:
    print(i)