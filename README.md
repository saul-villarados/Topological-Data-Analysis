# 📈 TDA Stock Analysis

**Topological Data Analysis for Financial Time Series** 🚀

<img width="1440" height="640" alt="TDA-PLOT" src="https://github.com/user-attachments/assets/d3b6c27d-a814-4de0-b2d3-3712909074ae" />



This project applies Topological Data Analysis (TDA) to analyze stock market data using persistent homology and Wasserstein distances to detect market anomalies and crashes.

## 🎯 What it does

- 📊 Downloads stock data from Yahoo Finance
- 🔄 Transforms time series into topological representations
- 📐 Computes persistence diagrams using Rips complexes
- 📏 Calculates Wasserstein distances between sliding windows
- 📈 Visualizes topological features alongside stock prices
- 🚨 Identifies potential market crashes and anomalies

## 🛠️ Installation

### Prerequisites
- Python 3.10.11
- pip package manager

### Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install ripser
pip install persim
pip install matplotlib
pip install numpy
pip install yfinance
```

## 🚀 Quick Start

### 1. Set up Configuration

Create `Config.py`:
```python
class TDA_CONFIG:
    MAX_DIM = 2
    TIME_SEGMENTS = 1041  # Adjust based on your data length
    WINDOWS = 20
    WASSERSTEIN_D = 1000
    CRASH = 500  # Index of known crash date
    
class Data_Config:
    INDEX_NAMES = '^GSPC'  # S&P 500
    START_DATE_STRING = '2020-01-01'
    END_DATE_STRING = '2023-12-31'
```

### 2. Create Required Directories

```bash
mkdir img
```

### 3. Run the Analysis

```python
from DataLoader import DataLoader
from TDA import TDA

# Initialize components
data_loader = DataLoader()
tda_analyzer = TDA()

# Load and transform data
print("📥 Loading stock data...")
data_loader.Extract()
data_loader.Transform()
print(f"✅ Loaded {len(data_loader.transform)} data points")

# Generate persistence diagram
print("🔍 Computing persistence diagrams...")
tda_analyzer.Persistance(data_loader)
tda_analyzer.save_plot()
print("✅ Persistence diagram saved to img/Persistance_Diagram.png")

# Compute and plot Wasserstein distances
print("📏 Computing Wasserstein distances...")
tda_analyzer.plot_wasserstein(data_loader)
print("✅ TDA analysis plot saved to img/TDA-PLOT.png")

print("🎉 Analysis complete! Check the img/ folder for results.")
```

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/8da8c6d0-5921-457a-8c88-2f6e24b8748b" />




## 📁 Project Structure

```
TDA-Stock-Analysis/
│
├── 📄 Config.py          # Configuration parameters
├── 📄 DataLoader.py      # Data loading and preprocessing
├── 📄 TDA.py             # Main TDA analysis class
├── 📄 main.py            # Example usage script
├── 📁 img/               # Generated plots and diagrams
│   ├── 🖼️ Persistance_Diagram.png
│   └── 🖼️ TDA-PLOT.png
└── 📄 README.md          # This file
```

## ⚙️ Configuration Options

### TDA_CONFIG Parameters:
- `MAX_DIM`: Maximum homology dimension (default: 2)
- `TIME_SEGMENTS`: Number of time windows to analyze
- `WINDOWS`: Size of each sliding window
- `WASSERSTEIN_D`: Number of distances to plot
- `CRASH`: Index of known market crash for visualization

### Data_Config Parameters:
- `INDEX_NAMES`: Stock symbol (e.g., '^GSPC' for S&P 500)
- `START_DATE_STRING`: Data start date
- `END_DATE_STRING`: Data end date

## 🔧 Troubleshooting

### Common Issues:

**❌ "Found array with 0 sample(s)"**
- Solution: Reduce `TIME_SEGMENTS` value in config
- Formula: `TIME_SEGMENTS ≤ data_length - (2 × WINDOWS) - 1`

**❌ "'NoneType' object is not subscriptable"**
- Solution: Call `Extract()` before `Transform()`

**❌ "No diagrams to plot"**
- Solution: Run `Persistance()` method first

## 📊 Output Interpretation

### Persistence Diagram
- Shows birth-death pairs of topological features
- Longer bars indicate more persistent features
- Can reveal underlying structure in time series

### Wasserstein Distance Plot
- Red line: Normalized stock prices
- Blue line: Wasserstein distances between consecutive windows
- Red dashed line: Known crash date
- High Wasserstein distances may indicate market instability

## 🔬 Research Applications

- **Market Crash Detection**: Sudden spikes in Wasserstein distances
- **Volatility Analysis**: Persistent homology features correlate with market volatility
- **Regime Change Detection**: Topological features change during market transitions
- **Risk Assessment**: Early warning signals from topological analysis

## 📚 References

- [Ripser Documentation](https://ripser.scikit-tda.org/)
- [Persim Documentation](https://persim.scikit-tda.org/)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📜 License

This project is open source. Feel free to use and modify for research purposes.

---

**Happy Analyzing! 📈✨**
