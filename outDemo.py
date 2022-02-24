import json

class Output:
    def __init__(O, results, length):
        O.len = length
        O.results = results

    def outFile(O):
        f = open("output.txt", "w")
        f.write(json.dumps(O.results))
        f.close()

# out = Output(results, length)
# out.outFile()