import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Replace sensitive info with placeholders
subsDf = glueContext.create_dynamic_frame.from_catalog(
    database="your_transaction_database",
    table_name="your_transaction_data_input_table",
    transformation_ctx="s3_input_new"
    )

sparkSubsDf = subsDf.toDF()

# removing null transaction id
filter_df = sparkSubsDf.na.drop(subset=['transaction_id'])

# droping duplicate transaction id
result_df = filter_df.dropDuplicates(subset=['transaction_id'])

result_df.write.mode('append').parquet('s3://your_processed_transaction_data_output_bucket/output/')
job.commit()
