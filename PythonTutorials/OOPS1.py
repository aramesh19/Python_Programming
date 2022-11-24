class City:
    pass

north_H = City()
south_H = City()

print(north_H, south_H)

north_H.country = 'USA'
north_H.contient = 'NA'
north_H.hemisphere = 'Western'
south_H.country = 'Australia'

print(north_H.hemisphere, south_H.country)

