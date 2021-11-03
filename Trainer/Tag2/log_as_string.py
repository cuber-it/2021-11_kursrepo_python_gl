#!/usr/bin/env python3
pfad = "/home/coder/Workspace/kurse_python_gl/"

with open(pfad + "/Materialien/Sample.log") as fd:
    data = fd.read()

with open(pfad + "/Trainer/Tag2/outfile.txt", "w") as outfile:
    zeilen = data.split("\n") # oder splitlines()

    trace_counter = 0
    event_counter = 0
    for zeile in zeilen:
        if "EVENT" in zeile:
            event_counter += 1 # <=> event_counter = event_counter + 1
            start = zeile.find(":.") # wo die Message beginnt
            text = zeile[start:].replace(".", "") # Punkt durhc nichts ersetzen <=> Punkt löschen
            ausgabe = text[1:]
            outfile.write(ausgabe + "\n")
            print(ausgabe)# Ausgabe (NUR!) der dazugehörigen Message
        elif "TRACE" in zeile:
            trace_counter += 1
    print("Events: ", event_counter)
    print("Traces: ", trace_counter)

    outfile.write(f"Events: {event_counter}\n")
    outfile.write(f"Traces: {trace_counter}\n")
