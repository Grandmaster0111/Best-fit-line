# Best-Fit Line

Generates a scatter plot of random data points and overlays a **linear regression (best-fit) line** computed from scratch — no sklearn, just pure math.

## How it works

The slope `m` and intercept `b` are computed using the least-squares formula:

```
m = (mean(x)·mean(y) − mean(x·y)) / (mean(x)² − mean(x²))
b = mean(y) − m·mean(x)
```

## Prerequisites

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 best_fit_line.py
```

A matplotlib window opens showing the scatter plot with the regression line overlaid.

## Output

![scatter plot with best-fit line](https://via.placeholder.com/400x300?text=scatter+%2B+regression+line)

## Dependencies

- `numpy` — array operations and random data generation
- `matplotlib` — plotting
