from pprint import pprint

# def sort_people(people_list, field, direction):
#     people_list.sort(key=lambda p: p[field], reverse= (direction == 'desc'))

def filter_males(people_list):
    return  list(filter(lambda p:p["sex"]=='male',people_list))

