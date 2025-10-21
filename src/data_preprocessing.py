import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    df['signal_strength'] = df['signal_strength'].clip(-120, -40)
    df['latency'] = df['latency'].clip(0, 500)
    return df
