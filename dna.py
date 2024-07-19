import sys
import math
from csv import reader

csvf = []
list_rows = []
dna_seq = {}
tmp_list = []


def main():

    if len(sys.argv) != 3:
        print("Usage: Incorrect number of arguments\n")
        sys.exit(1)

    with open(sys.argv[1], newline='') as csvf:
        csv_reader = reader(csvf)
        for row in csv_reader:
            list_rows.append(row)

    tmp_list = list_rows[0]
    dna_seq = {field: 0 for field in tmp_list}
    dna_seq.pop('name', None)

    with open(sys.argv[2], newline='') as txtf:
        txtline = txtf.read()

    # get count of sequential dna (substr) for each substr and save in dna_seq
    for key, value in dna_seq.items():
        substr = key
        counts = 0
        counts = dna_seq_ct(substr, txtline)
        dna_seq[key] = counts

    # loop through people in csv file and, when matches dna sequences or "no match", save in wins
    for p in range(1, len(list_rows)):
        person = list_rows[p]
        wins = dna_match(person, dna_seq)
        if wins != "no match":
            break
    # print either name that matches dna sequences or "no match"
    print(wins)


def dna_seq_ct(substr, txtline):
    # loop through text file, counting sequential repeats of dna sequences (substr)
    beg = indx = prev = rep_ct = counts = 0
    while indx != -1:
        indx = txtline.find(substr, beg, len(txtline))

        # check if match immediately follows and increment repeat counter
        if indx == prev:
            rep_ct += 1

            # update counts which keeps track of longest run of dna substr
            if counts < rep_ct:
                counts = rep_ct

        # first time match found, set counters to 1
        elif prev == 0:
            counts = 1
            rep_ct = 1
        else:
            # new run of dna substr, reset repeat counter to 1
            rep_ct = 1

        # remember this position for next loop
        prev = indx + len(substr)
        beg = prev

    return(counts)


def dna_match(person, dna_seq):
    # check each dna_seq with person's record, return name of person if match, or "no match"

    leng = len(dna_seq)
    for i in range(0, (leng)):
        list_dna = list(dna_seq)
        key = list_dna[i]
        value = dna_seq[key]
        if int(person[i + 1]) == value:
            matches = person[0]
        else:
            matches = "no match"
            break

    return (matches)


if __name__ == "__main__":
    main()
