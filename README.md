# Business Profit Analysis

## Project Overview

This project analyzes business profitability across different geographic locations and over time using business revenue and business count data from Statistics Canada. The analysis focuses on estimating profit metrics, performing statistical testing, regression analysis, and creating informative visualizations to compare profitability across regions.

---

## Features and Workflow

1. **Data Loading and Cleaning**
   - Loads a CSV dataset containing business revenue and business count data.
   - Cleans and renames columns for clarity.
   - Filters relevant variables for analysis.

2. **Data Transformation and Calculation**
   - Reshapes the dataset into a wide format for analysis.
   - Calculates average revenue per business.
   - Estimates business profit assuming a fixed profit margin (15%).
   - Applies winsorization to reduce the influence of extreme outliers.
   - Performs log transformation on estimated profit to normalize the distribution.

3. **Descriptive Statistics and Confidence Intervals**
   - Computes summary statistics by location type.
   - Calculates 95% confidence intervals for log-estimated profit.

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

## Project Insights

This analysis demonstrates how statistical techniques and data visualization can be used to compare business profitability across different geographic regions. The combination of descriptive statistics, hypothesis testing, regression modeling, and visualization provides insights into spatial and temporal patterns in estimated business profit.

---

## License

This project is licensed under the MIT License.