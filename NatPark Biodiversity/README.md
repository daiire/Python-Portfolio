# Nationl Park Biodiversity Analysis

This project analyses biodiversity data from U.S. national parks, with a focus on species conservation status and endangered species observations. It demonstrates an end-to-end workflow in Python: from data cleaning, aggregation, and pivot tables to styled PDF reports and publication-ready plots.

To make the findings accessible to both experts and non-experts, I designed duplicate visualizations using functions that allow easy switching between common and scientific species names. This flexibility ensured the results could be interpreted by diverse audiences while maintaining scientific rigor.

## Project Structure
```
NatPark Biodiversity/
│
├── Data/ # Initial datasets - Explained in the 'Initial Data' section below
│ ├── observations.csv # Species observation records across parks
│ └── species_info.csv # Species metadata including category & conservation status
|
├── Output/ # Generated analysis & visualisations - Explained in the 'Key Outputs' section below
│ ├── Conservation Status by Species Category.csv
│ ├── Endangered_Barplot.png
│ ├── Endangered_Barplot_Common.png
│ ├── Endangered_Obs_Common.pdf
│ ├── Endangered_Obs_Table.pdf
│ └── Protection Count by Species Category.csv
│
├── Initial_Workflow.py # Exploratory / first-pass workflow
└── Portfolio_Workflow.py # Polished, reproducible workflow for portfolio
```

## Features

### Initial Data (Data/)

• [observations.csv](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Data/observations.csv) - This file records sightings of species across different national parks. Each entry usually links a species to a specific park and gives the number of observations. It provides the context for how often and where different species are seen, which is essential for analysing species distribution and tracking populations of endangered species.

• [species_info.csv](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Data/species_info.csv) - This file contains metadata about each species recorded in the parks. It typically includes columns like species name, scientific name, taxonomic category (e.g., Mammal, Bird, Plant), and its conservation status (e.g., Endangered, Threatened, Species of Concern, or None). This dataset establishes the baseline for understanding biodiversity and identifying which species are at risk.



### Data Wrangling

• Cleans and normalises species information.

• Handles missing values and creates new classification columns.

• Builds pivot tables to summarise conservation status and protection counts.

### Visualisation

• Generates bar plots of endangered species observations by park.

• Produces both common name and scientific name views for interpretability.

• Custom label wrapping and grid styling for readability.

### Reporting

• Styled PDF reports with colour-coded species categories.

• Tabular outputs with masked duplicate values for cleaner presentation.

• Exported CSVs with breakdowns of protection status and conservation counts.

### Key Outputs (Output/)

• [Conservation Status by Species Category.csv](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output/Conservation%20Status%20by%20Species%20Category.csv) -- Species distribution by conservation category. Used in initial analysis.

• [Protection Count by Species Category.csv](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output/Protection%20Count%20by%20Species%20Category.csv) -- Protected vs. unprotected species breakdown with percentages. Used in initial analysis.

• [Endangered_Barplot.png](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output/Endangered_Barplot.png) & [Endangered_Barplot_Common.png](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output/Endangered_Barplot_Common.png) -- Endangered species observation counts (scientific & common names).

• [Endangered_Obs_Table.pdf](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output/Endangered_Obs_Table.pdf) & [Output/Endangered_Obs_Common.pdf](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output/Endangered_Obs_Common.pdf) -- Styled tables of endangered species observations by park (scientific & common names).

## Skills Demonstrated

• Data cleaning and transformation with pandas

• Statistical aggregation and pivot table analysis

• Data visualisation with matplotlib & seaborn

• Automated PDF report generation with ReportLab

• Workflow design for reproducibility and portability

## How to Run

Place observations.csv and species_info.csv in the Data/ directory.

Run the main workflow script:

[python Portfolio_Workflow.py](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Portfolio_Workflow.py)

##

Results will be exported to the [Output/](https://github.com/daiire/Python-Portfolio/tree/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Output) directory.






