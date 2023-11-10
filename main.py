from data_loader import load_input_data
from start_calculation import start_calculation
from start_calculation_with_struct import start_calculation_with_struct
from datetime import date, timedelta
from sqlalchemy import create_engine
import os
import logging
import pickle
from generate_states import generate_states

if __name__ == '__main__':

    start_date = date(2023, 9, 1)
    end_date = date(2023, 9, 2)
    num_days = (end_date - start_date).days
    date_range = [start_date + timedelta(days=d) for d in range(num_days)]
    connection_string = "mssql+pyodbc://calculator:calculator@195.133.69.14/SKMRUSMSSQL?driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(connection_string, fast_executemany=True)
    logger = logging.getLogger('equillibrium_logger')
    logger.setLevel('DEBUG')
    filehandler_dbg = logging.FileHandler(filename=logger.name+'-debug.log', mode='w')
    logger.addHandler(filehandler_dbg)
    logger.debug(f"Running equillibrium for dates from '{start_date.isoformat()}' to {end_date.isoformat()}...")
    pwd = os.getcwd()

    dict = {}
    for dt in date_range:
        dict[dt] = load_input_data(dt, engine, logger)
        # with open('data.pickle', 'wb') as f:
        #     pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        # with open('data.pickle', 'rb') as f:
        #     data = pickle.load(f)
        # states = generate_states(data)
        # start_calculation_with_struct(dt, states, range(0, 24), 24, 20)
                # dir = f'/{dt.year}_{dt.month}_{dt.day}'
                # folder_path = pwd + dir
                # os.makedirs(folder_path, exist_ok=True)
                # j.to_csv(folder_path + '/' + i + '.csv', sep=',', index=False)

    # for dt, d in dict.items():
    #     for k, v in d.items():
    #         for i, j in v.items():
    #             dir = f'/{dt.year}_{dt.month}_{dt.day}'
    #             folder_path = pwd + dir
    #             os.makedirs(folder_path, exist_ok=True)
    #             j.to_csv(folder_path + '/' + i + '.csv', sep=',', index=False)

    # # start test calculation
    hours = list(range(0, 24))
    for dt in date_range:
        dt_dict = dict[dt]
        in_folder = pwd + f'/{dt.year}_{dt.month}_{dt.day}'
        out_folder = pwd + f'/{dt.year}_{dt.month}_{dt.day}_out'
        start_calculation(dt, in_folder=in_folder,
                                out_folder=out_folder,
                                hours=range(0, 24),
                                hours_num=24,
                                max_iter=20)
        # start_calculation_with_struct(dt, in_folder, out_folder, hours, 24, 20)