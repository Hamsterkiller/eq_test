import ctypes
import pandas as pd
import cpp_structs as cpps


def create_array_of_structs(t: int, df: pd.DataFrame, df_name: str):

    """
    Create List of cpp_structs.
    :param t: hour (optional)
    :param df: pandas DataFrame with source data
    :param df_name: name of the data table provided with DataFrame
    :return: List of structs specified
    """

    result = []

    # get cpp struct for the dataframe
    struct = cpps.class_dict[df_name]

    # filter only records for t hour (if needed)
    if 't' in df.columns:
        df = df.query(f't == {t}')

    # convert dataframe to list of dict
    df_dict = df.to_dict(orient='records')

    for row in df_dict:
        new_struct = struct(row)
        result.append(new_struct)

    result_p = (struct * len(result))(*result)

    return result_p
