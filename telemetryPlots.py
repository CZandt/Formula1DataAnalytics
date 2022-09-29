import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.collections import LineCollection


def telemetryComparison(year,raceSession,location,in_driver_1,in_driver_2):

#Enables the cache so that you do not have to download the
    ff1.Cache.enable_cache('cache')

    #sets up plot
    ff1.plotting.setup_mpl()
    #Specify the session (NO DATA IS DOWNLOADED HERE)
    session = ff1.get_session(year,location, raceSession)


    session.load()

    #picks the drivers to compare

    driver_1, driver_2 = in_driver_1, in_driver_2

    laps_driver_1 = session.laps.pick_driver(driver_1)
    laps_driver_2 = session.laps.pick_driver(driver_2)

    #gets the fastest lap for each driver in the session provided
    fastest_driver_1 = laps_driver_1.pick_fastest()
    fastest_driver_2 = laps_driver_2.pick_fastest()

    #gets the telemetry for each driver on the fastest lap
    telemetry_driver_1 = fastest_driver_1.get_telemetry()
    telemetry_driver_2 = fastest_driver_2.get_telemetry()

    #calculates the delta time between the drivers
    delta_time, ref_tel, compare_tel = ff1.utils.delta_time(fastest_driver_1, fastest_driver_2)

    # Identify team color
    team_driver_1 = laps_driver_1['Team'].iloc[0]
    team_driver_2 = laps_driver_2['Team'].iloc[0]

    color_1 = ff1.plotting.team_color(team_driver_1)
    color_2 = ff1.plotting.team_color(team_driver_2)
    #color_2 = '#e3ff87'

    # HAMILTON HEX #e3ff87
    # RUSSEL HEX

    #PLOTTING
    #Set the size of the plot
    plt.rcParams['figure.figsize'] = [20,15]

        #7 Sub plots
            #Delta
            #Speed 
            #Throttle
            #Braking
            #Gear
            #RPM
            #DRS

    #Creates the seven different plots
    fig, ax = plt.subplots(7, gridspec_kw = {'height_ratios' : [1, 3, 2, 1, 1, 2, 1]})

    # Set the title of the plot

    ax[0].title.set_text(f'Telemetry Comparison {driver_1} vs. {driver_2}')

    #subplot 1 Delta
    ax[0].plot(ref_tel['Distance'], delta_time, color=color_1)
    ax[0].axhline(0)
    ax[0].set(ylabel= f'Gap to {driver_2} (s)')

    #Subplot 2: Speed
    ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1, color=color_1)
    ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2, color=color_2)
    ax[1].set(ylabel= f'Speed')
    ax[1].legend(loc="lower right")

    #Subplot 3: Throttle
    ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1, color=color_1)
    ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2, color=color_2)
    ax[2].set(ylabel= f'Throttle')
    ax[2].legend(loc="lower right")

    #Subplot 4: Braking
    ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1, color=color_1)
    ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2, color=color_2)
    ax[3].set(ylabel= f'Brake')
    ax[3].legend(loc="lower right")

    #Subplot 5: Gear
    ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1, color=color_1)
    ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2, color=color_2)
    ax[4].set(ylabel= f'Gear')
    ax[4].legend(loc="lower right")

    #Subplot 6: RPM
    ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1, color=color_1)
    ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2, color=color_2)
    ax[5].set(ylabel= f'RPM')
    ax[5].legend(loc="lower right")

    #Subplot 7: DRS
    ax[6].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=driver_1, color=color_1)
    ax[6].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=driver_2, color=color_2)
    ax[6].set(ylabel= f'DRS')
    ax[6].legend(loc="lower right")

    fig.tight_layout()

    plt.savefig(f"Telemetry_Comparisons/{driver_1}_VS_{driver_2}_{location}_{year}_{raceSession}.pdf", format="pdf", bbox_inches="tight")