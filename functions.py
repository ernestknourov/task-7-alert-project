import pandas as pd
import config


def read_logs(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    data.columns = config.columns
    # data['date'] = pd.to_datetime(data['date'], unit='s')
    data.sort_values(by=['date'], inplace=True)
    return data[['error_message', 'severity', 'bundle_id', 'date']]


def rule1(df: pd.DataFrame, time: float) -> int:
    return len(df.loc[(time - 60 <= df['date']) & (df['date'] <= time) & (df['severity'] == "Error")])


def rule2(df: pd.DataFrame, time: float):
    return max(df.loc[(time - 3600 <= df['date']) & (df['date'] <= time)
                      & (df['severity'] == "Error")].groupby(['bundle_id'])['bundle_id'].count())
