# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # task 1Fa
    def typical_range_consistent(self):
        '''Trying to see when this function gets added to the class'''
        if self.typical_range == None:
            return False
        elif self.typical_range[1] < self.typical_range[0]:
            return False
        else:
            return True

    #task 2B
    def relative_water_level(self):
        #if not self.typical_range_consistent() or not(self.latest_level()==None):
            #return None
        #are the water levels consistent?
        if self.typical_range_consistent():
            #is there a value for the latest level (which would be a float)?
            if type(self.latest_level) == float:
                #let's get the fraction (split into top & bottom to make it easier to see)
                top_frac = self.latest_level-self.typical_range[0]
                bottom_frac = (self.typical_range[1]-self.typical_range[0])
                fraction = top_frac / bottom_frac
                return fraction
             #if the levels aren't consistent or there is no latest level...
        else: 
            return None

            

# task1Fb
def inconsistent_typical_range_stations(stations):
#    global typical_range_consistent()
    ret = []
    for station in stations:
        if not station.typical_range_consistent():
            ret.append(station.name)
    return sorted(ret)