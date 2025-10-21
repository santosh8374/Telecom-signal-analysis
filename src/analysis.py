def analyze_signal_quality(df):
    avg_signal = df['signal_strength'].mean()
    poor_areas = df[df['signal_strength'] < -90]['region'].value_counts().head(5)
    avg_latency = df['latency'].mean()

    summary = {
        "Average Signal Strength (dBm)": round(avg_signal, 2),
        "Average Latency (ms)": round(avg_latency, 2),
        "Top 5 Poor Signal Regions": poor_areas.to_dict()
    }
    return summary
