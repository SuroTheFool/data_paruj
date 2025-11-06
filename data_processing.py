import csv, os

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps
# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    pass

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
my_list = filter(lambda x: x['country'] == 'Germany', cities)
# All cities germany
fil_list = filter(lambda x: x['country'] == 'Germany', cities)
print(fil_list)


