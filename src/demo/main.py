import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as psf


def main(filepath, value):
    """Read in data, add a column `added_column`."""
    spark = SparkSession.builder.getOrCreate()

    spark_home = os.environ.get('SPARK_HOME', None)
    if 'databricks' in spark_home:
        cwd = "/"
    else:
        cwd = ""

    print(spark_home)

    return (
        spark.read
        .option('inferSchema', True)
        .csv(cwd+filepath, header=True)
        .withColumn('added_column', psf.lit(value))
    )


if __name__ == "__main__":
    value = sys.argv[1]
    main('mnt/demo/*.csv', value).show()
