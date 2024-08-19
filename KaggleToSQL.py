import kaggle
import zipfile
import pandas as pd

def extract(file):
    zip_ref = zipfile.ZipFile(file) 
    zip_ref.extractall() # extract file to dir
    zip_ref.close() # close file
    filename = zip_ref.namelist()

    return filename[0]

def transformation(extracted_data):
    pd.set_option("display.max_columns", None)
    orders_df = pd.read_csv(extracted_data)
    null = orders_df.isnull().sum()
    #print(null)
    orders_df.drop('Postal Code',axis = 1, inplace = True)
    orders_df.columns = orders_df.columns.str.lower()
    orders_df.columns = orders_df.columns.str.replace(' ','_')
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'], dayfirst=True)
    orders_df['ship_date'] = pd.to_datetime(orders_df['ship_date'], dayfirst=True)
    print(orders_df.head(2))
    orders_df.to_csv('test.csv',index = False)

    return orders_df
    
extracted_data = extract('train.csv.zip')
sales_data = transformation(extracted_data)