from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run1():
    #part 1: list of rivers with stations
    stations = build_station_list
    ret = rivers_with_station(stations)
    ret = set(ret)#remove duplicates
    ret = list(ret)#back to sliceable list
    ret = sorted(ret)#alphabetical
    ret10 = ret[:10]#first 10 only

    print('{} stations. '.format(len(ret)))
    print("First 10 - {}".format(ret10))

run1()


def run2():
    #part 2: dictionary of rivers: stations
    stations = build_station_list
    RiverDict = stations_by_river(stations)

   # for item in RiverDict:
        #if item in ['River Aire', 'River Cam', 'River Thames'] :
           # print("Key : {} , Value : {}".format(item,RiverDict[item]))


    return RiverDict
    

#print (run2())


    