from floodsystem.stationdata import build_station_list, update_water_levels
from Task2G import flood_factor_classification, mostRiskList


def test_taskG():
    out = flood_factor_classification()
    
    #assert that a list of high stations is returned
    assert type(out) == list
    #assert that it's a list of tuples
    assert type(out[0]) == tuple
    
    #check that the list is correctly ordered from high to low flood factor
    for item in range(len(out) - 1):
        assert out[item][1] > out[item + 1][1]
    

