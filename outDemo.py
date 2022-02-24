import json

class Output:
    def __init__(self, results, length):
        self.len = length
        self.results = results

    def outFile(self):
        f = open("output.txt", "w")
        f.write(json.dumps(self.results))
        f.close()

# out = Output(results, length)
# out.outFile()