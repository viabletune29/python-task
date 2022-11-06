# Print result after every function to check
# Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value
filepaths = 'C:/Users/tariv/desktop/data.json'


def read_data(filepaths):
    with open(filepaths) as json_file:
        dat = json.load(json_file)
        return dat
    # Read data from filepaths


data = read_data(filepaths)


def get_oldest(data):
      oldest = {}
      max = 0
      c = 0

      for i in data["AVENGERS"]:
         if data["AVENGERS"][i]["age"] >max:
             max = data["AVENGERS"][i]["age"]
             oldest[c] = data["AVENGERS"][i]


      for i in data["DC"]:
         if data["DC"][i]['age'] >max:
             max = data["DC"][i]['age']
             oldest[c] = data["DC"][i]

         if data["DC"][i]['age'] == max:
             c = c+1
             oldest[c] = data["DC"][i]
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes

      l = 0
      for i in oldest:
          p = oldest[l]["name"]
          oldest[l] = p
          l = l+1

      return oldest
# returns info: Thor and Wonder Woman


light = get_oldest(data)


print(light)

'''
def get_oldest(data):
     oldest = {}
     max = 0
     c = 0

     for i in data["AVENGERS"]:
         if (data["AVENGERS"][i]["age"] > max):
             max = data["AVENGERS"][i]["age"]
             oldest[c] = i

     for i in data["DC"]:
         if (data["DC"][i]['age'] > max):
             max = data["DC"][i]['age']
             oldest[c] = i

         if data["DC"][i]['age'] == max:
             c = c + 1
             oldest[c] = i
     # Return all info of the oldest superheroes
     # Return all info of the oldest superheroes

     return oldest


 # returns info: Thor and Wonder Woman


light = get_oldest(data)

print(light)

'''

print("\n")


def get_oldest_avenger(data):
   max = 0
   for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']
            oldest_avenger=data["AVENGERS"][i]
    # Return all info of the oldest avenger
   return oldest_avenger["name"]

# returns info: Thor


old = get_oldest_avenger(data)
print(old)
print("\n")


def get_total_points(data):
    total_points = {}
    for i in data["AVENGERS"]:
        key=data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
          total_points[key]+=data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key=data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
          total_points[key]+=data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points

# returns info: Dict of superhero name and total points


total_point = get_total_points(data)

print(total_point)
print("\n")


def get_more_than_average(data):
    more_than_average = []
    avg_mcu=0
    avg_dc=0
    for i in data["AVENGERS"]:
        avg_mcu+=data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu = avg_mcu/len(data["AVENGERS"])

    c=0

    for i in data["AVENGERS"]:
        if data["AVENGERS"][i]['points']['stealth'] > avg_mcu:
            more_than_average.insert(c,data["AVENGERS"][i])
            c += 1

    for i in data["DC"]:
        avg_dc += data["DC"][i]['points']['strength']
    avg_dc = avg_dc/len(data["DC"])

    for i in data["DC"]:
        if data["DC"][i]['points']['strength'] > avg_dc:
            more_than_average.insert(c, data["DC"][i])
            c += 1
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    l = 0
    for i in more_than_average:
        p = more_than_average[l]["name"]
        more_than_average[l] = p
        l = l + 1

    return more_than_average

# returns info: Steve Rogers and Superman


above_average = get_more_than_average(data)

for i in above_average:
    print(i)

print("\n")


def get_names(data):
    names = []
    k = 0
    for i in data["AVENGERS"]:
        names.insert(k, data["AVENGERS"][i]["name"])
        k = k+1
    for j in data["DC"]:
        names.insert(k, data["DC"][j]["name"])
        k = k+1
    # Return a list of superhero names
    return names

# returns a list


superhero_name = get_names(data)

for i in superhero_name:
    print(i)