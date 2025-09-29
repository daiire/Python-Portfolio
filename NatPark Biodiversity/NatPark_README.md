# National Park Biodiversity Analysis

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
│ ├── Protection Status by Category.csv
│ ├── Endangered Observations Barplot - Scientific Name.png
│ ├── Endangered Observations Barplot - Common Name.png
│ ├── Endangered Species Observation Count - Common Name.PDF
│ ├── Endangered Species Observation Count - Scientific Name.PDF
│ └── Protected Count by Species Category.csv
│
├── NatPark Analysis - JNB.ipynb # Jupyter Notebook of analysis
└── NatPark Analysis - JNB (HTML).html # HTML version of the above file.
```

## Features

### Initial Data (Data/)

• [observations.csv](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Data/observations.csv) - This file records sightings of species across different national parks. Each entry links a species to a specific park and provides the number of observations. It provides the context for how often and where different species are seen, which is essential for analysing species distribution and tracking populations of endangered species.

• [species_info.csv](https://github.com/daiire/Python-Portfolio/blob/b2315b222d99f7285fd755cadec593b95bd70812/NatPark%20Biodiversity/Data/species_info.csv) - This file contains metadata about each species recorded in the parks. It typically includes columns like species name, scientific name, taxonomic category (e.g., Mammal, Bird, Plant), and its conservation status (e.g., Endangered, Threatened, Species of Concern, or None). This dataset establishes the baseline for understanding biodiversity and identifying which species are at risk.



### Data Wrangling

• Cleans and normalises species information.

• Handles missing values and creates new classification columns.

• Builds pivot tables to summarise conservation status and protection counts.

### Visualisations

• Generates bar plots of endangered species observations by park.

• Produces both common name and scientific name visualasations to reach a wider audience.

• Custom label wrapping and grid styling for readability.

### Reporting

• Styled PDF reports with colour-coded species categories.

• Tabular outputs with masked duplicate values for cleaner presentation.

• Exported CSVs with breakdowns of protection status and conservation counts.

### Key Outputs (Output/)

• [Protection Status by Category](https://github.com/daiire/Python-Portfolio/blob/92c81b1e655ee7f8c18a40b2300d16133bd31ff8/NatPark%20Biodiversity/Output/Protection%20Status%20by%20Category.csv) -- Species distribution by conservation category. Used in initial analysis.

• [Protected Count by Species Category](https://github.com/daiire/Python-Portfolio/blob/92c81b1e655ee7f8c18a40b2300d16133bd31ff8/NatPark%20Biodiversity/Output/Protected%20Count%20by%20Species%20Category.csv) -- Breakdown of protected versus unprotected species with percentages. Used in initial analysis.

• [Endangered Observations Barplot - Scientific Name](https://github.com/daiire/Python-Portfolio/blob/main/NatPark%20Biodiversity/Output/Endangered%20Observations%20Barplot%20-%20Scientific%20Name.png) & [Endangered Observations Barplot - Common Name](https://github.com/daiire/Python-Portfolio/blob/92c81b1e655ee7f8c18a40b2300d16133bd31ff8/NatPark%20Biodiversity/Output/Endangered%20Observations%20Barplot%20-%20Common%20Name.png) -- Endangered species observation counts (scientific & common names).

• [Endangered Species Observation Count - Scientific Name](https://github.com/daiire/Python-Portfolio/blob/92c81b1e655ee7f8c18a40b2300d16133bd31ff8/NatPark%20Biodiversity/Output/Endangered%20Species%20Observation%20Count%20-%20Scientific%20Name.PDF) & [Endangered Species Observation Count - Common Name](https://github.com/daiire/Python-Portfolio/blob/92c81b1e655ee7f8c18a40b2300d16133bd31ff8/NatPark%20Biodiversity/Output/Endangered%20Species%20Observation%20Count%20-%20Common%20Name.PDF) -- Styled tables of endangered species observations by park (scientific & common names).

## Skills Demonstrated

• Data cleaning and transformation with pandas

• Statistical aggregation and pivot table analysis

• Data visualisation with matplotlib & seaborn

• Automated PDF report generation with ReportLab

• Workflow design for reproducibility and portability
