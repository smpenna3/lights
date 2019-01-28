from phue import Bridge
import time
import numpy as np

def fire(lights, average_brightess=80):
    for light in lights:
        bri = np.random.normal(loc=average_brightess, scale=10)
        if(bri < 10):
            bri = 10
        light.brightness = 50
        hue = np.random.normal(loc=2000, scale=2000)
        if(hue < 0):
            hue = 65535 + hue
        light.hue = hue
        print('Light '+str(light)+' to '+str(light.hue)+' brightness: '+str(bri))

if __name__ == '__main__':
    bridge = Bridge('10.0.0.28')
    lights = bridge.get_light_objects()
    print(lights)

    while(1):
        fire(lights)
        time.sleep(0.1)