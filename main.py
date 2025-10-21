import pandas as pd
from src.data_preprocessing import clean_data
from src.analysis import analyze_signal_quality
from src.visualization import visualize_signal_patterns

def main():
    df = pd.read_csv('data/telecom_signal_data.csv')
    df = clean_data(df)
    
    summary = analyze_signal_quality(df)
    print("\n=== Network Performance Summary ===\n")
    print(summary)
    
    visualize_signal_patterns(df)
    print("\n✅ Analysis complete. Visualizations saved in 'plots/' directory.")

if __name__ == "__main__":
    main()
