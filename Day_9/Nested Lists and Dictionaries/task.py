
# Nested dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print out the Lille from the dictionary
print(travel_log["France"][1])

nested_list = ["A", "B", ["C","D"]] # List inside list
# Print list item inside list
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },}
print(travel_log["Germany"]["cities_visited"][2])
