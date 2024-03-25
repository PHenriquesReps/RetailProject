from lib import ConfigReader

#defining customers schema
def get_customers_schema():
    schema = "customer_id int, customer_fname string, customer_lname string, username string, password string, address string, city string, state string, pincode string"
    return schema

# creating customers dataframe
def read_customers(spark,env):      # We need to pass the spark session. And the environment because based on the env it will define the path to the data.
    conf = ConfigReader.get_app_config(env)     # get the function from the ConfiReader file
    customers_file_path = conf["customers.file.path"]       # get the customers file path from the dictionary
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_customers_schema()) \
        .load(customers_file_path)

#defining orders schema
def get_orders_schema():
    schema = "order_id int, order_date string, customer_id int, order_status string"
    return schema

#creating orders dataframe
def read_orders(spark,env):
    conf = ConfigReader.get_app_config(env)
    orders_file_path = conf["orders.file.path"]
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_orders_schema()) \
        .load(orders_file_path)