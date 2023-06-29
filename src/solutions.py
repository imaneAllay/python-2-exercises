from pprint import pprint

# def sort_people(people_list, field, direction):
#     people_list.sort(key=lambda p: p[field], reverse= (direction == 'desc'))

# def filter_males(people_list):
#     return  list(filter(lambda p:p["sex"]=='male',people_list))

def transform_person(person):
    weight = person['weight_kg']
    height = person['height_meters']
    bmi = round(weight / (height ** 2), 1)

    p = {
        'id': person['id'],
        'name': person['name'],
        'weight_kg': weight,
        'height_meters': height,
        'bmi': bmi
    }
    return p

def calc_bmi(people_list):
    return list(map( transform_person,people_list))