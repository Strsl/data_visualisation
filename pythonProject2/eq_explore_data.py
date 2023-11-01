import json

filename = 'eq_data_1_day_m1.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

#print(json.dumps(all_eq_data, indent=4))

all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10])
print(lons[:5])
print(lats[:5])