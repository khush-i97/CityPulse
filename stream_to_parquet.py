import os
os.environ['HADOOP_HOME']     = r'C:\hadoop'
os.environ['hadoop_home_dir'] = r'C:\hadoop'
os.environ['PATH'] = r'C:\hadoop\bin;' + os.environ.get('PATH','')


from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

# 1️⃣ Build the Spark session
spark = (
    SparkSession.builder
        .appName("CityPulseBronze")
        .config(
          "spark.jars.packages",
          "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1"
        )
        .getOrCreate()
)
# 2️⃣ Define the JSON schema matching your producer
schema = StructType() \
    .add("sensor", StringType()) \
    .add("speed", IntegerType()) \
    .add("timestamp", IntegerType())

# 3️⃣ Read the stream from Kafka topic "traffic"
raw_df = (
    spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "127.0.0.1:9092")
        .option("subscribe", "traffic")
        .load()
        .select(from_json(col("value").cast("string"), schema).alias("data"))
        .select("data.*")
)

# 4️⃣ Write that raw stream out to Parquet files
query = (
    raw_df.writeStream
        .format("parquet")
        .option("path", "data/bronze")
        .option("checkpointLocation", "checkpoint/bronze")
        .outputMode("append")
        .start()
)

# 5️⃣ Let it run until you stop it
query.awaitTermination()
