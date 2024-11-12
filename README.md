
# Chronic Disease Analysis in Colombia

This project aims to analyze the prevalence and patterns of chronic diseases in Colombia using data from public health datasets. By examining data on various chronic conditions, the project seeks to provide insights into the distribution and factors associated with these diseases in different populations within the country.

## Project Overview

Chronic diseases represent a significant burden in Colombia, affecting quality of life and health care systems. This analysis focuses on identifying key trends and visualizing the impact of these conditions through statistical and data visualization techniques.

### Objectives
- To understand the prevalence of chronic diseases in Colombia.
- To identify patterns based on demographic information.
- To create visualizations that highlight major findings and trends.

## Data

The dataset used in this project is publicly available through the [Datos Abiertos Colombia](https://www.datos.gov.co) portal and can be accessed [here](https://dev.socrata.com/foundry/www.datos.gov.co/2uxx-gxp3). It contains records on various chronic diseases across the Colombian population.

### Data Cleaning and Preprocessing
1. Load the dataset and inspect it for missing values and inconsistencies.
2. Filter relevant columns for the analyss.
3. Handle missing data and ensure uniform data types.

## Analysis Workflow

### 1. Exploratory Data Analysis (EDA)
- Summary statistics to understand the data distribution.
- Visualizations such as histograms and bar charts to observe age groups, disease counts, and demographic distributions.

### 2. Data Visualization
- Heatmaps to identify correlations among numerical features.

### 3. Insights and Findings
Key observations will be documented to provide insights on chronic disease prevalence across demographics, age groups, and regions.

## Setup and Installation

### Requirements
- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/chronic-disease-analysis.git
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   cd chronic-disease-analysis
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scriptsctivate`
   pip install -r requirements.txt
   ```

## Usage

Run the analysis by executing:
```bash
python src/data_cleaning.py
python src/analysis.py
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request to suggest improvements.

## License

This project is licensed under the MIT License.
