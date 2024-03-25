import pytest
from lib.Utils import  get_spark_session

@pytest.fixture
def spark():
    "Create spark session"
    spark_session = get_spark_session("LOCAL")       # create the spark session
    yield spark_session     # this will await until the unit test cases are done
    spark_session.stop()    # stop the spark session    

@pytest.fixture
def expected_results(spark):
    "Expected results for the aggregation order count per state"
    results_schema = "state string, count int"
    return spark.read \
        .format("csv") \
        .schema(results_schema) \
        .load("data/test_results/test_aggregate.csv")