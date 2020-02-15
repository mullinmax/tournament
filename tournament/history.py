import os

class history():
    path = None
    records = []

    def __intit__(self, path):
        if path is not None:
            if os.path.exists(path):
                self.load_history(path)
        
    def load_history(self, path):
        self.path = path
        f = open(path, 'r')
        self.records = []
        for line in f.read():
            self.records += record(line) 

    def save_history(self, path=None):
        if path is not None:
            p = path
        elif self.path is not None:
            p = self.path
        else:
            raise Exception('Path not specified to save history to and default not saved')
        f = open(self.path, 'w')
        f.write(self.__str__())

    def add_record(self, data):
        self.records.append(record(data))

    def __str__(self):
        return '\n'.join([str(r) for r in self.records])


class record():

    data = {}

    def __intit__(self, d=None):
        self.data = d

    # "player_path":score,"player_path":score,"player_path":score
    def parse_line(self, line):
        self.data = {}
        lines = line.strip().split(',')
        for line in lines:
            vals = line.strip().split(':')
            vals[0] = vals[0].strip()[1:-1]
            vals[1] = vals[1].strip()
            self.data[str(vals[0])] = str(vals[1])

    def __str__(self):
        return ','.join(['"{path}:",{score}'.format(path=k, score=self.data[k]) for k in self.data])
