import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    id = record[0]
    nucleiod = record[1]
    mr.emit_intermediate(nucleiod[:-10], id)

def reducer(unique_nucleiod, ignore):
    mr.emit(unique_nucleiod)

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
