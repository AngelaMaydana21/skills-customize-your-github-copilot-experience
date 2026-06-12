import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(p)


def plot_line(df, x_col, y_col, out_path: Path):
    plt.figure(figsize=(8, 4))
    plt.plot(df[x_col], df[y_col], marker='o', linestyle='-')
    plt.title(f"{y_col} over {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path)
    plt.close()


def plot_bar(df, x_col, y_col, out_path: Path):
    plt.figure(figsize=(8, 4))
    plt.bar(df[x_col], df[y_col], color='C1')
    plt.title(f"{y_col} by {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path)
    plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple data visualization utilities')
    parser.add_argument('path', help='Path to CSV file')
    parser.add_argument('--line', nargs=2, metavar=('X', 'Y'), help='Create a line chart using columns X and Y')
    parser.add_argument('--bar', nargs=2, metavar=('X', 'Y'), help='Create a bar chart using columns X and Y')
    parser.add_argument('--out-dir', default='output', help='Output directory for figures')
    args = parser.parse_args()

    df = load_data(args.path)

    out_dir = Path(args.out_dir)

    if args.line:
        x, y = args.line
        plot_line(df, x, y, out_dir / f'line_{y}_over_{x}.png')
        print(f'Wrote line chart to {out_dir / f"line_{y}_over_{x}.png"}')

    if args.bar:
        x, y = args.bar
        plot_bar(df, x, y, out_dir / f'bar_{y}_by_{x}.png')
        print(f'Wrote bar chart to {out_dir / f"bar_{y}_by_{x}.png"}')

    if not args.line and not args.bar:
        print('No chart requested. Use --line X Y or --bar X Y')
