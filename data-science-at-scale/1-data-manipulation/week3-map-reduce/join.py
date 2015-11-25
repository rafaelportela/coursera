import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(order_id, list_of_records):
    line_items = []
    order = []
    for record in list_of_records:
        if record[0] == "order":
            order = record
        else:
            line_items.append(record)

    for line_item in line_items:
        mr.emit(order + line_item)

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
