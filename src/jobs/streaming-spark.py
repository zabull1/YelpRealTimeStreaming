from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType, DataType
from pyspark.sql.functions import from_json, col


def start_spark_streaming(spark) -> None:
    try:
        stream_df = (
            spark.readStream.format("socket")
            .option("host", "127.0.0.1")
            .option("port", 9999)
            .load()
        )

        schema = StructType(
            [
                StructField("review_id", StringType()),
                StructField("user_id", StringType()),
                StructField("business_id", StringType()),
                StructField("stars", FloatType()),
                StructField("date", StringType()),
                StructField("text", StringType()),
            ]
        )

        stream_df = stream_df.select(
            from_json(col("value"), schema).alias("data")
        ).select("data.*")

        query = stream_df.writeStream.outputMode("append").format("console").start()

        query.awaitTermination()

    except Exception as e:
        print("Error occured: %s", e)


if __name__ == "__main__":
    spark = SparkSession.builder.appName("SocketStreamConsumer").getOrCreate()

    start_spark_streaming(spark)
