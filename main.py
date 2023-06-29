
# Update with the exercise you are trying to test
from src import solutions


def main():

    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]

    # people_list = [
    #     {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    #     {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    # ]
    # -----------------------------Ex1-----------------------------------
    # solutions.sort_people()
    # solutions.sort_people(people_list, 'name', 'desc')
    # print(people_list)
    # -----------------------------Ex2-----------------------------------
    #
    # filtered_list = solutions.filter_males(people_list)
    # print(filtered_list)

    # -----------------------------Ex3-----------------------------------

    # new_people_list = solutions.calc_bmi(people_list)
    # print(new_people_list)

    # -----------------------------Ex4-----------------------------------
    # print(solutions.get_people(people_list))

    # -----------------------------Ex5-----------------------------------
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.














if __name__ == '__main__':
    main()
