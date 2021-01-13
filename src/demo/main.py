import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as psf


def main(filepath, value):
    """Read in data, add a column `added_column`."""
    spark = SparkSession.builder.getOrCreate()

    databricks_check = os.environ.get('DATABRICKS_HOST', None)
    if databricks_check is not None:
        cwd = "/"
    else:
        cwd = ""

    print(cwd, databricks_check)

    return (
        spark.read
        .option('inferSchema', True)
        .csv(cwd+filepath, header=True)
        .withColumn('added_column', psf.lit(value))
    )


if __name__ == "__main__":
    value = sys.argv[1]
    main('mnt/demo/*.csv', value).show()
