city_names = ["Oakland", "San Francisco", "Dalas", "Los Angeles", "Boston","New York"]
soccer_team_names = ["Chealsea", "Man United", "Man City", "Arsenal", "Everton"]
print(soccer_team_names[2])
print(city_names[1])
three_cities = city_names[0:3]
print(three_cities)
three_teams = soccer_team_names[0:3]
print(three_teams)
city_names[0]= "San Francisco"
city_names[5]= "Brooklyn"
city_names.append("New Jersey")
city_names.extend(["Chicago", "Santa Cruiz", "Washingtron"])
print(city_names)