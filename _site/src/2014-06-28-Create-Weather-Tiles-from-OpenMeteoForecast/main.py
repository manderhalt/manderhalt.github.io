# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 20:30:53 2014

@author: Mathieu Anderhalt
@mail: mathieu.anderhalt@gmail.com
"""

#import sys, os
from pydap.client import open_url
import numpy as np
#from pymongo import MongoClient
import datetime
import re
from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
#import time
import gdal
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm, interp
import os
import sys

def LoadData():
    response = urlopen('http://dap.ometfn.net/')
    # Regular expressions to identify files metedata
    reg_grid = re.compile('eu12-pp')
    reg_ext = re.compile('$nc')
    reg_date = re.compile('[20]\d\d\d\d\d\d\d\d\d')
    html = response.read()
    # Parse the html page of the server to find available files
    soup = BeautifulSoup(html)
    # List refs to files on the server
    files = [l.get('href') for l in soup.find_all('a') if                 l.get('href')]
    files2 = [l for l in files if reg_grid.search(l) and l.endswith('.nc')]
    print files2[0]
    file = files2[0]
    dataset = open_url(file)
    data = {
            "projection": dataset['Lambert_Conformal'].attributes,
            "longitudes":  np.array(dataset['lon'].array[:,:],dtype=float).tolist(),
            "latitudes": np.array(dataset['lat'].array[:,:],dtype=float).tolist(),
            "temperature":  np.around(np.array(dataset['temp2m'].array[:,:],dtype=float),decimals=1).tolist()
    }
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def CreateWeatherTile(weather_var,weather):
    with open("data.json", "r") as fichier:
        data = json.load(fichier)
    GDAL_DATA = os.path.join('/opt','local','share','gdal')
    temp = os.path.join('/Volumes','DATA','temp')
    TilesServer = os.path.join('/Volumes','DATA','TilesServer')

    fig = plt.imshow(data['temperature'],cm.GMT_haxby,alpha=0.5)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(os.path.join('temperature.png'),bbox_inches='tight',pad_inches=0)

    command_translate = "gdal_translate -a_srs '+proj=lcc +lon_0=4 +lat_0=47.5 +lat_1=47.5 +lat_2=47.5 +a=6370000. +b=6370000. +no_defs' -a_ullr -2963997.87057 -1848004.2008 2964000.82884 1848004.09676 " + os.path.join('temperature.png') + " " + os.path.join('temperature.tif')

    command_tile = "/Users/Mathieu/anaconda/bin/gdal2tiles.py --config GDAL_DATA " + GDAL_DATA + " --profile=mercator -z 1-8 " + os.path.join('temperature.tif') +  " " + os.path.join('./tile')

    os.system(command_translate)
    os.system(command_tile)










if __name__ == '__main__':
    main()
