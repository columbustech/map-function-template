import pandas as pd
import package1, package2
from .modules.local_module import *

# download_url : Url path to a file. The file is a CSV table in our example but could
# also be a zipped folder, which can be extracted inside the process function.

def process(download_url):
    # Test local package, package1
    package1.test_package1()

    # Test local package, package2
    package2.test_package2()

    # Test local module
    test_local_module()

    # Read the csv table into a pandas dataframe
    df = None
    try:
        df = pd.read_csv(download_url)
    except:
        df = pd.read_csv(download_url, encoding = "ISO-8859-1")

    # Get tablename from the filename by removing .csv extension
    url_wo_sig = download_url[:download_url.find('?')]
    table_name = url_wo_sig[url_wo_sig.rfind('/') + 1 : url_wo_sig.rfind('.')]

    # Create output dataframe with columns table_name, column_name
    of = pd.DataFrame([table_name, i] for i in df.columns)
    of.columns = ['table_name', 'column_name']

    # Return dataframe
    return of
