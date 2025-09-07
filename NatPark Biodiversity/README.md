# Python-Portfolio

Welcome to my Python repository portfolio! This repository features a collection of projects and code that demonstrates my skills in data cleaning, analysis and report creation.

While I do not have a lot of experience with Pyhton, I wanted to document my progress and showcase my abilities and work. 



# 📊 Report Generation

## 🐾 [Endangered Species Observations Analysis](https://github.com/daiire/Python-Portfolio/tree/888047d67a9635422d620b6cb16d4f5ba17e4abd/NatPark%20Biodiversity)

This project analyzes endangered species observation data across multiple national parks and generates visual and PDF reports for conservation insights.

<details> <summary>The workflow includes:</summary>

• Data import: loading species information and park observation data from CSV files.

• Data cleaning: standardizing species common names, filling missing conservation statuses, and creating protected/not protected flags.

• Aggregation & analysis: summarizing species counts by category, protection status, and park, with a focus on endangered species.

• Visualization: generating barplots of endangered species observations by park, formatted for readability with wrapped labels, grids, and legends.

• Automated reporting: creating styled PDF tables of observations, including color-coded species categories and legends for easy interpretation.

This workflow demonstrates practical skills in data wrangling, analysis, visualization, and automated reporting, suitable for conservation research or environmental reporting workflows.

</details>

## 📈 [Sales Report](https://github.com/daiire/Python-Portfolio/tree/ee380342b649dc42ae54685f4442b8a49c5f25d3/Fictional%20Sales%20Report%20(Class%20%2B%20Report%20Creation))

This project implements a Python class to streamline the preparation of sales reports for management.

<details>
  <summary>The workflow includes:</summary>

• Data import: loading raw period sales reports into a structured format.

• Data cleaning: trimming unnecessary fields and standardizing the dataset for analysis.

• Summary generation: producing key metrics and aggregated tables that highlight performance trends.

• Visualization: creating simple charts to support management’s review and decision-making.

This workflow shows practical skills in data wrangling, reporting automation, and visualization to improve the efficiency of business reporting workflows.

</details>


# ✅ Data Cleaning

## 🌦️ [Indonesian Climate Data](https://github.com/daiire/Python-Portfolio/tree/0c4b6affd8b799f9970cd70318492e4fa0e49138/Indonesian%20Climate%20Data)

This project preprocesses raw climate station data to prepare it for analysis and modeling. 
<details>
  <summary>The workflow includes:</summary>

• Data cleaning: renaming columns for clarity, removing stations with insufficient records, stripping whitespace, and handling outliers by replacing invalid values with NaN.

• Outlier detection: applying custom rules for temperature, humidity, sunshine hours, and wind speed and direction to ensure data falls within realistic ranges.

• Missing data handling: using IterativeImputer (a multivariate imputation method) to estimate missing values based on relationships between variables.

• Station-level processing: splitting the dataset by station ID to ensure imputations are tailored to each station’s conditions.

Output: Saving cleaned and completed datasets per station for downstream use (A Power BI dashboard on this dataset is being worked on).

</details>


## 👤 [US Census Data](https://github.com/daiire/Python-Portfolio/tree/ee380342b649dc42ae54685f4442b8a49c5f25d3/US%20Census%20(Data%20Cleaning))

This project implements a Python workflow to preprocess and consolidate US Census data. 

<details>
  <summary>The workflow includes:</summary>

• Data import and consolidation: using glob to load multiple CSV files and combine them into a single, unified DataFrame.

• Data cleaning: removing duplicate entries to maintain accuracy and replacing missing values (NaN) with zeros where appicable.

• Column management: splitting and renaming columns where necessary for clarity and consistency.

This script demonstrates practical skills in data wrangling, cleaning, and consolidation, essential for preparing large datasets for analysis.

</details>







