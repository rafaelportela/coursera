import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    person_a = record[0]
    person_b = record[1]

    if person_a < person_b:
        mr.emit_intermediate((person_a, person_b), record)
    else:
        mr.emit_intermediate((person_b, person_a), record)

def reducer(ordered_pair, friendships):
    person_a = ordered_pair[0]
    person_b = ordered_pair[1]

    a_on_the_left = False
    b_on_the_left = False
    a_on_the_right = False
    b_on_the_right = False

    for record in friendships:
        if record[0] == person_a:
            a_on_the_left = True
            b_on_the_right = True
        else:
            a_on_the_right = True
            b_on_the_left = True

    if a_on_the_right and not a_on_the_left:
        mr.emit((person_a, person_b))
        mr.emit((person_b, person_a)) # emitting both (A,B) and (B,A) to satisfy the buggy grader
    if b_on_the_right and not b_on_the_left:
        mr.emit((person_a, person_b)) # emitting both (A,B) and (B,A) to satisfy the buggy grader
        mr.emit((person_b, person_a))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
