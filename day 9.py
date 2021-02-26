#Nesting
capitals = {'France': 'Paris', 'Germany': 'Berlin'}

#Nesting a List in a Dic

travel_log = [
{
    'Country': 'France',
    'cities_visited': ['Paris', 'Lille', 'Dijon'],
    'total_visits': 12
},
{
    'Country': 'Germany',
    'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
    'total_visits': 5
}
]



travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
  third_data = {}
  third_data['country'] = country_visited
  third_data['visits'] = times_visited
  third_data['cities'] = cities_visited
  travel_log.append(third_data)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)











