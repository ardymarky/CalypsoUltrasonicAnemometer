import asyncio
import numpy as np
import matplotlib.pyplot as plt
from calypso_anemometer.core import CalypsoDeviceApi
from calypso_anemometer.model import Settings
from calypso_anemometer.model import CalypsoReading, CalypsoDeviceDataRate
from calypso_anemometer.util import wait_forever
import matplotlib as mlb
from windrose import WindroseAxes
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

async def calypso_subscribe():

    async with CalypsoDeviceApi(ble_address = "E3:E0:AA:0D:09:6D", settings = Settings(ble_discovery_timeout=60, ble_connect_timeout=60)) as calypso:    
        
        await calypso.set_datarate(CalypsoDeviceDataRate.HZ_4)
        
        def process_reading(reading: CalypsoReading):
        
            data = reading.asdict()
            wind_direction = data['wind_direction']
            wind_speed = data['wind_speed']
            ax.clear()
            color = cmap(norm(wind_speed))	
            ax.set_title("Windspeed is: %.1f m/s" % wind_speed)
            ax.bar([wind_direction], [wind_speed], normed=True, opening=0.8, color = color)
            print(data['wind_speed'], data['wind_direction'])
            plt.pause(0.001)
         
        norm = Normalize(vmin = 0, vmax = 10)
        cmap = plt.get_cmap('hot')
        sm = ScalarMappable(norm=norm, cmap=cmap)
        
        fig = plt.figure(figsize=(5,5)) 
        ax = fig.add_subplot(111, projection = "windrose")
        ax.set_ylim(0,10)
        
        cbar = plt.colorbar(sm, ax=ax, orientation='vertical', pad= 0.1)
  
        await calypso.subscribe_reading(process_reading)
            
        await wait_forever()

if __name__ == "__main__":
    
    mlb.rcParams['toolbar'] = 'None'
    asyncio.run(calypso_subscribe())
    
    
