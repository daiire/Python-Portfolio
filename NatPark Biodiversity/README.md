# NatPark Biodiversity Analysis

This project analyzes biodiversity data from U.S. national parks, with a focus on species conservation status and endangered species observations. It demonstrates an end-to-end workflow in Python: from data cleaning, aggregation, and pivot tables to styled PDF reports and publication-ready plots.

## Project Structure

```
NatPark Biodiversity/
│
├── Data/
│ ├── observations.csv # Species observation records across parks
│ └── species_info.csv # Species metadata including category & conservation status
|
├── Output/ # Generated analysis & visualizations
│ ├── Conservation Status by Species Category.csv # Used in intial analysis
│ ├── Endangered_Barplot.png
│ ├── Endangered_Barplot_Common.png
│ ├── Endangered_Obs_Common.pdf
│ ├── Endangered_Obs_Table.pdf # Table of endangered species observations by nat. park
│ └── Protection Count by Species Category.csv # Used in intial analysis
│
├── Initial_Workflow.py # Exploratory / first-pass workflow
└── Portfolio_Workflow.py # Polished, reproducible workflow for portfolio

```

## Features

### Data Wrangling

Cleans and normalizes species information.

Handles missing values and creates new classification columns.

Builds pivot tables to summarize conservation status and protection counts.

### Visualization

Generates bar plots of endangered species observations by park.

Produces both common name and scientific name views for interpretability.

Custom label wrapping and grid styling for readability.

### Reporting

Styled PDF reports with color-coded species categories.

Tabular outputs with masked duplicate values for cleaner presentation.

Exported CSVs with breakdowns of protection status and conservation counts.

## Key Outputs

Output/Conservation Status by Species Category.csv → Species distribution by conservation category.

Output/Protection Count by Species Category.csv → Protected vs. unprotected species breakdown with percentages.

Output/Endangered_Barplot.png & Output/Endangered_Barplot_Common.png → Endangered species observation counts (scientific & common names).

Output/Endangered_Obs_Table.pdf & Output/Endangered_Obs_Common.pdf → Styled tables of endangered species observations by park.

## Skills Demonstrated

Data cleaning and transformation with pandas

Statistical aggregation and pivot table analysis

Data visualization with matplotlib & seaborn

Automated PDF report generation with ReportLab

Workflow design for reproducibility and portability

## How to Run

Place observations.csv and species_info.csv in the Data/ directory.

Run the main workflow script:

python Portfolio_Workflow.py


Results will be exported to the Output/ directory.







