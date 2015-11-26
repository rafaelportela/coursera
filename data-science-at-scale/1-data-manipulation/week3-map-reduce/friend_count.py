import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    person_a = record[0]
    mr.emit_intermediate(person_a, 1)

def reducer(person, friends_count_list):
    number_of_friends = 0
    for friendcount in friends_count_list:
        number_of_friends += friendcount

    mr.emit((person, number_of_friends))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
