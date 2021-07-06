# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damage(lst):
    new_damages = []
    b = 10**9
    m = 10**6
    for i in lst:
        # retaining the value when record is "Damages not recorded"
        if i == "Damages not recorded":
            new_damages.append(i)
            continue

        # converting the records in million
        elif i[len(i)-1] == "M":
            convert_to_million = float(i[:len(i)-1]) * m
            new_damages.append(convert_to_million)

        # cinverting the values in billion 
        else:
            convert_to_billion = float(i[:len(i)-1]) * b
            new_damages.append(convert_to_billion)
    return new_damages

#checkimg the function damage  
# print(damage(damages))
new_damage = damage(damages)

# write your construct hurricane dictionary function here:
def hurrican_dict(name, month, year, max_sustained_wind, affected_area, damage, death):
    hurricane = {}
    for i in range(34):
        hurricane[name[i]] = {'Name': name[i], 'Month': month[i], 'Year': year[i], 'Max Sustained Wind': max_sustained_wind[i], 'Areas Affected': affected_area[i], 'Damage': damage[i], 'Deaths': death[i]}
    return hurricane

# testing the hurricane_dict function 
# print(hurrican_dict(name= names, month = months, year = years, max_sustained_wind = max_sustained_winds, affected_area = areas_affected, damage = damages, death = deaths))

hurricane  = hurrican_dict(name= names, month = months, year = years, max_sustained_wind = max_sustained_winds, affected_area = areas_affected, damage = damages, death = deaths)

# write your construct hurricane by year dictionary function here:
def dict_by_year(dict, name, year):
    hurricane_by_year = {}
    y = []
    index = {}
    for i in range(34):
        if year[i] in y:
            continue
        else:
            y.append(year[i])
    # print(y)
    # print("\n")  
    for j in y:
        index[j] = []
        for k in range(34):
            if year[k] == j:
              index[j].append(k)
    #print(index)
    for l in y:
        lst1= []
        for m in index[l]:
            x = name[m]
            lst1.append(dict[x])
        hurricane_by_year[l] = lst1   
    return hurricane_by_year

# tseting dict_by_year function
# print(dict_by_year(dict= hurricane, name= names, year= years))

# write your count affected areas function here:
def count_affected_areas(areas):
    a = []
    unique_a = []
    count = {}
    for i in areas:
        for j in i:
            a.append(j)
    for k in a:
        if k in unique_a:
            continue
        else:
            unique_a.append(k)
    for l in unique_a:
        count[l] = a.count(l)
    return count

# testing count_affected_areas
# print(count_affected_areas(areas_affected))
count = count_affected_areas(areas_affected)
# write your find most affected area function here:
def most_affected(count):
    lst = list(count.values())
    area = list(count.keys())
    max_value = max(lst)
    max_value_index = lst.index(max_value)
    area_affected_most = area[max_value_index]
    return "The area most affected by the hurricanes is {area} and it has been hit {number} times.".format(area = area_affected_most, number = max_value)

#testing most_affected function 
# print(most_affected(count))


# write your greatest number of deaths function here:
def max_death(list, name):
    max_no_of_death = max(list)
    name_of_hurricane = names[deaths.index(max_no_of_death)]
    return "the maximum number of deaths caused by a hurricane is {number} and this was caused by {name}.".format(number = max_no_of_death, name = name_of_hurricane)

# testing max_death function
# print(max_death(deaths, names))
    

# write your catgeorize by mortality function here:
'''mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000} 
'''
def mortality(name, death, dict):
    mortality_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []} 
    
    for i in range(34):
        death_no = death[i]
        name1 = name[i]
        if death_no == 0:
            mortality_scale[0].append(dict[name1])
        elif death_no <= 100 and death_no > 0:
            mortality_scale[1].append(dict[name1])
        elif death_no > 100 and death_no <= 500:
            mortality_scale[2].append(dict[name1])
        elif death_no > 500 and death_no <= 1000:
            mortality_scale[3].append(dict[name1])
        elif death_no > 1000 and death_no <= 10000:
            mortality_scale[4].append(dict[name1])
        else:
            mortality_scale[5].append(dict[name1])
    return mortality_scale

# testing mortality function
# print(mortality(names, deaths, hurricane))

# write your greatest damage function here:
def damage(name, damage):
    lst = []
    for i in damage:
        if i == "Damages not recorded":
            continue
        else:
            lst.append(i)
    max_damage = max(lst)
    most_affected_hurricane = name[damage.index(max_damage)]
    return "The hurricane that cuased the maximum damage was {name} and it costed a damage of {cost}.".format(name = most_affected_hurricane, cost = max_damage)

# testing teh damage function
# print(damage(names, new_damage))


# write your catgeorize by damage function here:
''' damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}'''

def categorize(damage, name, dict):
    categorized_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []} 
    lst = []
    for i in range(34):
        damage_done = damage[i]
        name_hurricane = name[i]
        if damage_done == "Damages not recorded":
            continue
        else:
            if damage_done == 0:
              categorized_dict[0].append(dict[name_hurricane])
            elif damage_done > 0 and damage_done <= 100000000:
              categorized_dict[1].append(dict[name_hurricane])
            elif damage_done > 100000000 and damage_done <= 1000000000:
              categorized_dict[2].append(dict[name_hurricane])
            elif damage_done > 1000000000 and damage_done <= 10000000000:
              categorized_dict[3].append(dict[name_hurricane])
            elif damage_done > 10000000000 and damage_done <= 50000000000:
              categorized_dict[4].append(dict[name_hurricane])
            else:
              categorized_dict[5].append(dict[name_hurricane])
    return categorized_dict

# testing categorize function
print(categorize(new_damage, names, hurricane))
