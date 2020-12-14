import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as sf

def main(filepath, value):
    """Read in data, add a column `added_column`."""
    spark = SparkSession.builder.getOrCreate()

    return (
        spark.read
        .option('inferSchema', True)
        .csv(filepath, header=True)
        .withColumn('added_column', sf.lit(value))
    )

if __name__ == "__main__":
    value = sys.argv[1]
    main('mnt/demo/*.csv', value).show()