import sys
import numpy as np
from math import sqrt
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans

if __name__ == "__main__":
    spark = SparkContext(appName="KMeansExample")
    data = spark.textFile("file:///home/amitesh/Downloads/lab9-Assignment/adultdata.txt")
    dataset = data.map(lambda line: np.array([x for x in line.split(', ')])[np.array([0,2,11])].astype(float))
    clusters = KMeans.train(dataset, 3, maxIterations=50, initializationMode="random")
    def cost(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))
    SSE = dataset.map(lambda point: cost(point)).reduce(lambda x, y: x + y)
    print("Centers:",clusters.centers,"SSE=",SSE,file=sys.stdout)
    spark.stop()
