import csv

class Dataset:
    inputs = []
    labels = []

    def __init__(self, filename):
        filename = 'data.csv' #django doesn't detect the filename when passed
        with open(filename, newline='') as dataset:
            data_reader = csv.reader(dataset)
            for index, row in enumerate(data_reader):
                Dataset.inputs.append([])
                for x in row[:5]:
                    Dataset.inputs[index].append(x)
                Dataset.labels.append(row[5])
        #print(Dataset.labels)
        #inputs = self.input.copy()
        #labels = self.labels.copy()

#    def getInput():
#        global inputs
#        return inputs

#    def getLabels():
#        global labels
#        return labels
#Dataset('data.csv')
