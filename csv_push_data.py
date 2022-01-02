import pandas as pd
import utils
import constants as const


def insert_csv_to_db(data_frame:pd.DataFrame, index):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[index]
    for row in data_array:
        query = utils.generate_insert_query_with_array(params, row, const.csv_tables[index])
        utils.insert(query)


