import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from dictionarywtime import months
from aqipm import pm25_dict
from aqipm import pm10_dict
import math
def calc_aqi(ih,il,ch,cl,c):
    aqi_math = ((ih-il)/(ch-cl))*(c-cl)+il
    return aqi_math

def read_dict(reading):
    new_dict = {}
    if reading <= 12:
        for key, value in pm25_dict["lev1"].items():
            new_dict[key] = value
    if reading > 12 and reading <= 35.4:
        for key, value in pm25_dict["lev2"].items():
            new_dict[key] = value
    if reading >= 35.5  and reading <= 55.4:
        for key, value in pm25_dict["lev3"].items():
            new_dict[key] = value
    if reading >= 55.5  and reading <= 150.4:
        for key, value in pm25_dict["lev4"].items():
            new_dict[key] = value
    if reading >= 150.5  and reading <= 250.4:
        for key, value in pm25_dict["lev5"].items():
            new_dict[key] = value
    if reading >= 250.5  and reading <= 350.4:
        for key, value in pm25_dict["lev6"].items():
            new_dict[key] = value
    if reading >= 350.5  and reading <= 500.4:
        for key, value in pm25_dict["lev7"].items():
            new_dict[key] = value
    if reading >= 500.5  and reading <= 1001:
        for key, value in pm25_dict["lev8"].items():
            new_dict[key] = value
    aqi_air = new_dict["air"]
    aqi_v = math.floor(calc_aqi(new_dict["ihigh"],new_dict["ilow"],new_dict["chigh"],new_dict["clow"], reading))
    return aqi_v, aqi_air

def read10_dict(reading):
    new_dict = {}
    if reading > 1001:
        reading = 999
        print(reading)
    if reading <= 54:
        for key, value in pm10_dict["lev1"].items():
            new_dict[key] = value
    if reading > 54 and reading <= 154:
        for key, value in pm10_dict["lev2"].items():
            new_dict[key] = value
    if reading > 154  and reading <= 254:
        for key, value in pm10_dict["lev3"].items():
            new_dict[key] = value
    if reading > 254  and reading <= 354:
        for key, value in pm10_dict["lev4"].items():
            new_dict[key] = value
    if reading > 354  and reading <= 424:
        for key, value in pm10_dict["lev5"].items():
            new_dict[key] = value
    if reading > 424  and reading <= 504:
        for key, value in pm10_dict["lev6"].items():
            new_dict[key] = value
    if reading > 504  and reading <= 604:
        for key, value in pm10_dict["lev7"].items():
            new_dict[key] = value
    if reading > 604  and reading <= 1001:
        for key, value in pm10_dict["lev8"].items():
            new_dict[key] = value
    if reading < 1 and reading > 1001:
        print("Out of range")
        
    if not new_dict:
        print("Dict is Empty")
        print(new_dict)
        print(reading)
    aqi_air = new_dict["air"]
    aqi_v = math.floor(calc_aqi(new_dict["ihigh"],new_dict["ilow"],new_dict["chigh"],new_dict["clow"], reading))
    return aqi_v, aqi_air