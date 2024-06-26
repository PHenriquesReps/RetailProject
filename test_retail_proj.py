import pytest
from lib.DataReader import read_customers, read_orders
from lib.DataManipulation import filter_closed_orders, count_orders_state, filter_orders_generic
from lib.ConfigReader import get_app_config

@pytest.mark.read()
def test_read_customers_df(spark):
    customers_count = read_customers(spark, "LOCAL").count()
    assert customers_count == 12435

@pytest.mark.read()
def test_read_orders_df(spark):
    orders_count = read_orders(spark, "LOCAL").count()
    assert orders_count == 68884

@pytest.mark.transformation()
def test_filter_closed_orders(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_orders_count = filter_closed_orders(orders_df).count()
    assert filtered_orders_count == 7556

@pytest.mark.skip("Example: Work in Progress")
def test_read_app_config():
    conf = len(get_app_config("LOCAL"))
    assert conf == 2

@pytest.mark.transformation()
def test_count_orders_state(spark, expected_results):
    customers_df = read_customers(spark, "LOCAL")
    filtered_orders_count = count_orders_state(customers_df)
    assert filtered_orders_count.collect() == expected_results.collect()      # expected results will be a data frame, we need to get the local python list so we need to say collect


# Generic Test Values
    
@pytest.mark.transformation()
def test_check_closed_count(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_closed_count = filter_orders_generic(orders_df, "CLOSED").count()
    assert filtered_closed_count == 7556

@pytest.mark.transformation()
def test_check_pendingpayment_count(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_pendingpaymen_count = filter_orders_generic(orders_df, "PENDING_PAYMENT").count()
    assert filtered_pendingpaymen_count == 15030

@pytest.mark.transformation()
def test_check_complete_count(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_complete_count = filter_orders_generic(orders_df, "COMPLETE").count()
    assert filtered_complete_count == 22900

# Parameterize the Generic Tests
    
@pytest.mark.parametrize(       # used to pass parameters
        "status, count",
        [
            ("CLOSED", 7556),
            ("PENDING_PAYMENT", 15030),
            ("COMPLETE", 22900)
        ]
)
def test_check_count(spark, status, count):
    orders_df = read_orders(spark, "LOCAL")
    filtered_count = filter_orders_generic(orders_df, status).count()
    assert filtered_count == count
