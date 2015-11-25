import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for word in words:
        mr.emit_intermediate(word, key)

def reducer(key, list_of_values):
    words = {}
    if key not in words:
        words[key] = set()
    for value in list_of_values:
        words[key].add(value)

    mr.emit((key, list(words[key])))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
