import csv
from collections import defaultdict
import matplotlib.pyplot as plt


class Database:
    def __init__(self):
        self.dictionary = defaultdict(Bird)

    def __str__(self):
        return str(self.dictionary)

    def add(self, species, timestamp, confidence):
        self.dictionary[species].timestamps.append(timestamp)
        self.dictionary[species].confidences.append(confidence)
        self.dictionary[species].occurrances += 1


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
            database.add(row[8], (float(row[3]), float(row[4])), float(row[9]))
    for species, bird in database.dictionary.items():
        print(species, bird.average_confidence())
    plot_occurrances(database)
    plot_average_confidences(database)


def plot_occurrances(database):
    figure = plt.figure(figsize=(10, 5))
    species = database.dictionary.keys()
    confidences = [bird.occurrances for bird in database.dictionary.values()]
    plt.bar(species, confidences)
    plt.xlabel("Species")
    plt.ylabel("Occurrances")
    plt.title("Occurrances of Each Species")
    plt.locator_params(axis="y", nbins=4)
    plt.show()


def plot_average_confidences(database):
    figure = plt.figure(figsize=(10, 5))
    species = database.dictionary.keys()
    confidences = [bird.average_confidence() for bird in database.dictionary.values()]
    plt.bar(species, confidences)
    plt.xlabel("Species")
    plt.ylabel("Average Confidence")
    plt.title("Average Confidence of Each Species")
    plt.show()


if __name__ == "__main__":
    main()
