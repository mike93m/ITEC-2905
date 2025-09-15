city_state = [("New York", "NY"), ("Los Angeles", "CA"), ("Chicago", "IL")]

first_city_state = city_state[0]
print(first_city_state)  

# Unpacking the tuple values
city, state = first_city_state
print(city)
print(state)

# Unpacking directly in the loop
for city, state in city_state:
    print(f"{city} is in {state}")

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km

distances = get_distance()
print(distances)
print(distances[0])
km = distances[1]
print(km)
