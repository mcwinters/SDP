import csv
from collections import defaultdict


class Database:
    def __init__(self):
        self.species = defaultdict(Bird)

    def __str__(self):
        return str(self.species)

    def add(self, species, timestamp, confidence):
        self.species[species].timestamps.append(timestamp)
        self.species[species].confidences.append(confidence)
        self.species[species].occurrances += 1


class Bird:
    def __init__(self):
        self.occurrances = 0
        self.timestamps = []
        self.confidences = []

    def average_confidence(self):
        return sum(self.confidences) / self.occurrances


def main():
    database = Database()
    with open("BirdNET_Output.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            database.add(row[8], (row[3], row[4]), row[9])
    print(database)


if __name__ == "__main__":
    main()
