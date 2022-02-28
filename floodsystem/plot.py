import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
import numpy as np

def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level /m')
    plt.xticks(rotation=45);
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    stations = build_station_list()
    poly, shift = polyfit(dates, levels, p)
    typical_min=[]
    typical_max=[]
    numbered_dates = matplotlib.dates.date2num(dates)
    for station in stations:
        typical_min.append(station.typical_range[0])
        typical_max.append(station.typical_range[1])
    np.plot(numbered_dates, levels, label = 'Actual data')
    np.plot(numbered_dates, typical_min, label = 'Typical Minimum')
    np.plot(numbered_dates, typical_max, label = 'Typical Maximum')
    np.plot(numbered_dates, poly, label = 'Polynomial model')


