import pandas as pd
from src.data import get_weather_data, get_building_data, get_base_data

df_weather = get_weather_data()
df_building = get_building_data()
df_base = get_base_data()

df_base_building = pd.merge(df_base, df_building, how="left", on=["building_id"])
df = pd.merge(
    df_base_building, df_weather, how="left", on=["site_id", "timestamp"]
)
"""
print(df['year_built'].corr(df['meter_reading']))
0.11183692613860641
"""
print(df['primary_use'].corr(df['meter_reading']))
print(df['floor_count'].corr(df['meter_reading']))
print(df['square_feet'].corr(df['meter_reading']))


#print("base length" + str(len(df_base_building)) + "a total" + str(len(df_full)))


# base = pd.concat([base_train, base_test], sort=False)
# base_weather = pd.concat([weather_train, weather_test], sort=False)

# print(len(pd.merge(base, data, on=['building_id'])))
# print(len(base))

# base_part = pd.merge(base, data, on=['building_id'])
# base_total = pd.merqe(base_part, base_weather, on=['site_id', 'timestamp'])

# print(len(base_total))
# 61913700
# print(data.head(10))
# print(base.head())
# print(pd.merge(base, data, on=['building_id']).head())

# print(len(base))
# print(base.head(10))
# print(type(base))
# print(pd.merge(base, data, on = 'building_id').head())

