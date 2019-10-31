import pandas as pd
import os

# to know the lenght
# print("train is: " , len(base_train), "test is: ", len(base_test))


def get_weather_data():
    weather_train = pd.read_csv(os.path.join("data", "weather_train.csv"))
    weather_test = pd.read_csv(os.path.join("data", "weather_test.csv"))
    df = pd.concat([weather_train, weather_test], sort=False)
    return df


def get_base_data():
    train = pd.read_csv(os.path.join("data", "train.csv"))
    test = pd.read_csv(os.path.join("data", "test.csv"))
    df = pd.concat([train, test], sort=False)
    return df


def get_building_data():
    building_data = pd.read_csv(os.path.join("data", "building_metadata.csv"))
    return building_data
