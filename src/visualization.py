import matplotlib.pyplot as plt
import os

def visualize_signal_patterns(df):
    os.makedirs('plots', exist_ok=True)
    
    plt.figure(figsize=(8,5))
    df.groupby('region')['signal_strength'].mean().plot(kind='bar')
    plt.title('Average Signal Strength by Region')
    plt.ylabel('Signal Strength (dBm)')
    plt.tight_layout()
    plt.savefig('plots/signal_by_region.png')
    
    plt.figure(figsize=(8,5))
    df.groupby('network_type')['latency'].mean().plot(kind='bar', color='orange')
    plt.title('Average Latency by Network Type')
    plt.ylabel('Latency (ms)')
    plt.tight_layout()
    plt.savefig('plots/latency_by_network.png')
