import locale
import pandas as pd
import requests
import json
import constants as const
import  csv_pull_data
import  api_pull_data
import init_db
import sql_connector

connector = sql_connector.SQLConnector()


def run():
    init_db.create_tables()
    api_pull_data.pull()
    csv_pull_data.pull_csv_data()
    connector.close()
    print('Finished creating DB')


if __name__ == "__main__":
    run()
