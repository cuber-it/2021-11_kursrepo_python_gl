#!/usr/bin/env python3
import pandas

def abfrage():
    infile = input("Quelldatei: ")
    outfile = input("Protokolldatei: ")
    return infile, outfile

def read(infile):
    result = []
    with open(infile) as fd:
        for zeile in fd.read().splitlines():
            result.append(zeile.replace(" ", "").split(","))
    return result
    #pandas.read_csv(infile).to_dict('records')

def write(outfile, data):
    with open(outfile, "w") as fd:
        print(",".join(data[0]), file=fd)
        for row in data[1:]:
            output = []
            for field in row:
                if not isinstance(field, str):
                    field = str(field)
                output.append(field)
            print(",".join(output), file=fd)
    #pandas.DataFrame(data).to_csv(outfile)

def calc(weight, size):
    size = float(size) / 100
    weight = float(weight)
    return weight / (size ** 2)

def bewertung(bmi):
    status = ""
    if bmi < 18.5:
        status = "'u'"
    elif bmi >= 18.5 and bmi < 24.9:
        status = "'+'"
    elif bmi >= 24.9 and bmi < 29.9:
        status = "'-'"
    elif bmi >= 30.0 and bmi < 34.9:
        status = "'--'"
    elif bmi >= 35.0 and bmi < 39.9:
        status = "'---'"
    else:
        status = "'----'"
    return status

def process_data(data):
    result = []
    result.append(data[0])
    for row in data[1:]:
        bmi = calc(row[3], row[2])    
        status = bewertung(bmi)
        result.append([row[0], bmi, status])
    return result

if __name__ == "__main__":
    in_file, out_file = abfrage()
    data = read(in_file)
    result = process_data(data)
    write(out_file, result)