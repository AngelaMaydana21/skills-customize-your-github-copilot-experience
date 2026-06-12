import argparse
from pathlib import Path
import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(p)


def descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


def custom_stats(df: pd.DataFrame, col: str) -> dict:
    series = df[col].dropna()
    return {
        'mean': series.mean(),
        'median': series.median(),
        'std': series.std(),
        'min': series.min(),
        'max': series.max(),
        '25%': series.quantile(0.25),
        '50%': series.quantile(0.50),
        '75%': series.quantile(0.75),
    }


def group_aggregations(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    g = df.groupby(group_col)[value_col].agg(['mean', 'count', 'sum']).reset_index()
    return g.sort_values('mean', ascending=False)


def correlation_pairs(df: pd.DataFrame, threshold: float = 0.5):
    corr = df.corr()
    pairs = []
    for i in range(len(corr.columns)):
        for j in range(i+1, len(corr.columns)):
            a = corr.columns[i]
            b = corr.columns[j]
            val = corr.iloc[i, j]
            if abs(val) >= threshold:
                pairs.append((a, b, val))
    return corr, pairs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Basic statistics analysis with pandas and numpy')
    parser.add_argument('--path', required=True, help='Path to CSV file')
    parser.add_argument('--group-by', help='Column name to group by')
    parser.add_argument('--value-col', default='value', help='Numeric column to aggregate')
    parser.add_argument('--fill-na', choices=['drop', 'mean'], default='drop', help='How to handle NA values')
    parser.add_argument('--corr-threshold', type=float, default=0.5, help='Threshold for strong correlations')

    args = parser.parse_args()

    df = load_data(args.path)

    if args.fill_na == 'mean':
        df = df.fillna(df.mean(numeric_only=True))
    else:
        df = df.dropna()

    print('\n=== Descriptive statistics ===')
    print(descriptive_stats(df.select_dtypes(include=[np.number])))

    if args.group_by:
        print(f"\n=== Aggregations by {args.group_by} ===")
        print(group_aggregations(df, args.group_by, args.value_col))

    corr_matrix, strong_pairs = correlation_pairs(df.select_dtypes(include=[np.number]), threshold=args.corr_threshold)
    print('\n=== Correlation matrix ===')
    print(corr_matrix)
    if strong_pairs:
        print('\n=== Strong correlation pairs ===')
        for a, b, v in strong_pairs:
            print(f"{a} - {b}: {v:.3f}")
