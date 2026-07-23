# Business Profit Analysis

## Project Overview

This project examines whether geographic location is associated with small-business profitability in Canada. Using aggregated Statistics Canada data, the analysis compares businesses located in functional urban areas with those in rural and small-town areas.

Because the dataset does not contain reported profit, average revenue per business was calculated and profit was estimated using an assumed 15% profit margin. Statistical testing, regression analysis, and visualization were then used to evaluate whether the difference between urban and rural businesses was statistically meaningful.

---

## Features and Workflow

1. **Data Loading and Cleaning**
   - Loads a CSV dataset containing business revenue and business count data.
   - Cleans and renames columns for clarity.
   - Filters relevant variables for analysis.

2. **Data Transformation and Calculation**
   - Reshapes the dataset into a wide format for analysis.
   - Calculates average revenue per business.
   - Estimates profit using an assumed 15% profit margin.
   - Filters observations outside the 5th and 95th percentile thresholds.
   - Applies a `log(1 + estimated profit)` transformation to reduce skew.

3. **Statistical Analysis**
   - Calculates descriptive statistics by location type.
   - Estimates 95% confidence intervals.
   - Performs an independent t-test comparing urban and rural log-estimated profit.
   - Builds an OLS regression model using location type as the explanatory variable.

4. **Statistical Testing**
   - Performs independent t-tests comparing estimated profits between urban and rural areas.

5. **Regression Analysis**
   - Builds an Ordinary Least Squares (OLS) regression model to evaluate the relationship between location type and estimated profit.

6. **Visualization**
   - Creates histograms showing the distribution of log-estimated profits.
   - Generates connected scatter plots illustrating yearly profit trends across locations.

---

## Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels

---

## Data Source

This project uses data from **Statistics Canada**:

**Rural Canada Business Profile, total revenue and other revenue variables of small businesses by industry, location indicator and incorporation status (Table 33-10-0584-01).**

The original dataset is approximately **400 MB** and is **not included in this repository**.

To run this project:

1. Download the dataset from the Statistics Canada website.
2. Place the downloaded file (`33100584.csv`) in the project root directory.
3. Run `main.py`.

---

## Usage

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Place `33100584.csv` in the project directory.

3. Run:

```bash
python main.py
```

4. Generated statistics, regression results, and visualizations will be saved in the prroject directory.

---

## Output Files

- `Log_Profit_Stats.csv` / `.txt` – Summary statistics
- `Log_Profit_CI.csv` / `.txt` – 95% confidence intervals
- `T_test_log_profit.txt` – Independent t-test results
- `Regression_Log_Profit.txt` – OLS regression summary
- `Log_Estimated_Profit_Distribution.png` – Profit distribution visualization
- `Connected_Scatter_Log_Profit.png` – Yearly profit trend visualization

---

## Results and Insights

- Rural and small-town businesses had higher mean and median estimated profits than businesses in functional urban areas.
- The independent t-test produced a t-statistic of approximately `-1.237` and a p-value of `0.218`.
- Because the p-value was greater than `0.05`, the observed difference was not statistically significant.
- The 95% confidence intervals for urban and rural log-estimated profit also overlapped.
- The yearly comparison showed that rural estimated profit remained higher, although the gap narrowed over time.
- Overall, the results suggest that location alone was not a strong predictor of small-business profitability in this dataset.

## Limitations

- Profit was not directly reported in the source dataset and was estimated using an assumed 15% profit margin.
- The dataset contains aggregated observations rather than individual business records.
- The analysis does not control for industry, business size, business age, policy conditions, or regional economic differences.
- The results therefore describe patterns in estimated profitability rather than establishing that geographic location causes differences in profit.

---

## License

This project is licensed under the MIT License.