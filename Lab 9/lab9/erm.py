import sys
import numpy as np
from math import sqrt
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans

S3_DATA_SOURCE_PATH="s3://cs1lab2/data/adultdata.txt"
s3_DATA_OUTPUT_PATH="s3://cs1lab2/output/"
if __name__ == "__main__":
    spark = SparkContext(appName="KMeansAssignment")
    data = spark.textFile(S3_DATA_SOURCE_PATH)
    dataset = data.map(lambda line: np.array([x for x in line.split(', ')])[np.array([0,2,11])].astype(float))
    clusters = KMeans.train(dataset, 3, maxIterations=100, initializationMode="random")
    cluster_center=clusters.centers
    print("Centers:",clusters.centers,file=sys.stdout)
    cluster_center.saveAsTextFile(s3_DATA_OUTPUT_PATH)
    def cost(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))
    SSE = dataset.map(lambda point: cost(point)).reduce(lambda x, y: x + y)
    print("Sum of Squared Error = " + str(SSE),file=sys.stdout)
    spark.stop()
