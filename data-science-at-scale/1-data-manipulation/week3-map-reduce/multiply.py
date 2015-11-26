import sys
import MapReduce

mr = MapReduce.MapReduce()

ROWS = 5
COLS = 5

def mapper(record):
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]

    if matrix == 'a':
        for m in range(ROWS):
            mr.emit_intermediate((row, m), record)
    else:
        for n in range(COLS):
            mr.emit_intermediate((n, col), record)

def reducer(key, records):
    a_elements = []
    b_elements_by_row = {}
    for record in records:
        matrix = record[0]
        row = record[1]
        col = record[2]
        value = record[3]
        if matrix == 'a':
            a_elements.append(record)
        else:
            b_elements_by_row[row] = record

    total = 0
    for a in a_elements:
        a_value = a[3]
        a_col = a[2]
        try:
            b = b_elements_by_row[a_col]
            b_value = b[3]
            total += a_value * b_value
        except KeyError:
            continue

    mr.emit((key[0], key[1], total))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
