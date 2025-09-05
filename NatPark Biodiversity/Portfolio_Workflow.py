import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors

pd.set_option('display.max_columns', None)

# -------------------- Config --------------------
# Parameterize paths for portability
DATA_DIR = "Data"
OUTPUT_DIR = "Output"

OBSERVATIONS_FILE = os.path.join(DATA_DIR, "observations.csv")
SPECIES_FILE = os.path.join(DATA_DIR, "species_info.csv")


# -------------------- Functions --------------------
def endangered_barplot(data, x_axis_data, x_axis_name, filepath):
    """
    Create a barplot of endangered species observations by park.

    Parameters
    ----------
    data : pd.DataFrame
        Must contain species names, park names, and observation counts.
    x_axis_data : str
        Column to use for the x-axis (e.g. 'common_names' or 'scientific_name').
    x_axis_name : str
        Human-friendly axis label (used in the plot).
    filepath : str
        Output path for the saved PNG chart.
    """
    plt.subplots(figsize=(20, 8))
    endangered_bar = sns.barplot(x=x_axis_data, y="observations",
                                 data=data, hue="park_name")

    # Wrap and capitalize x-axis labels for readability
    x_wrap = [
        textwrap.fill(
            " ".join([label.capitalize() for label in label.get_text().split()]),
            width=13
        )
        for label in endangered_bar.get_xticklabels()
    ]
    plt.xticks(ticks=endangered_bar.get_xticks(), labels=x_wrap)

    # Gridlines and labels
    endangered_bar.yaxis.grid(True, linestyle="--", alpha=0.6)
    plt.xlabel(x_axis_name)
    plt.ylabel("Observations")
    plt.title("Total Observations of Endangered Species")

    # Legend placement
    plt.legend(title="National Park", loc="center left", bbox_to_anchor=(0.725, 1.1))

    # Save figure
    plt.savefig(filepath, bbox_inches="tight")
    plt.clf()


def mask_names(df, col):
    """
    Mask repeated values in a column for table readability.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the column to mask.
    col : str
        Column name where duplicates should be masked.
    """
    df[col] = df[col].mask(df[col].duplicated()).fillna("")


def build_species_pdf(col_name, data, file_path, title_text):
    """
    Build a styled PDF report showing species observations by park.

    Parameters
    ----------
    col_name : str
        Column name to use as species identifier (common or scientific).
    data : pd.DataFrame
        DataFrame containing [species, park_name, observations].
    file_path : str
        Output path for the PDF file.
    title_text : str
        Title to display at the top of the PDF.
    """
    # Prepare table data (add header row)
    table_data = [[col_name, 'Park Name', 'Observations']] + data.values.tolist()

    # Table styling
    style_commands = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("BACKGROUND", (0, 1), (2, 4), colors.lightyellow),
        ("BACKGROUND", (0, 5), (2, 8), colors.lightgreen),
        ("BACKGROUND", (0, 9), (2, 16), colors.lightpink),
        ("BACKGROUND", (0, 17), (2, 24), colors.lightyellow),
        ("BACKGROUND", (0, 25), (2, 28), colors.lightpink),
        ("BACKGROUND", (0, 29), (2, 40), colors.lightblue),
        ("BACKGROUND", (0, 41), (2, 48), colors.lightpink),
        ("BACKGROUND", (0, 49), (2, 52), colors.lightblue),
        ("BACKGROUND", (0, 53), (2, 56), colors.lightseagreen),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]
    line_break_number = list(range(5, 54, 4))
    for line in line_break_number:
        style_commands.append(('LINEABOVE', (0, line), (2, line), 3, colors.black))

    # Styles for title and legend
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Heading1"],
        alignment=1,
        fontSize=16,
        leading=15,
        spaceAfter=0
    )
    legend_style = ParagraphStyle(
        name="LegendStyle",
        parent=styles["Heading2"],
        alignment=1,
        fontSize=9,
        leading=0,
        spaceAfter=0
    )
    legendbody_style = ParagraphStyle(
        name="Legendbody",
        parent=styles["Heading3"],
        alignment=1,
        fontSize=8,
        leading=-1,
        spaceAfter=10
    )

    # Text content for PDF
    title = Paragraph(title_text, title_style)
    legend = Paragraph("Legend", legend_style)
    legend_body = Paragraph(
        "Mammal: Red____Bird: Blue____Fish: Yellow____Vascular Plant: Green____Amphibian: Turquoise",
        legendbody_style
    )

    # Create table and apply style
    table = Table(table_data)
    table.setStyle(TableStyle(style_commands))

    # Build PDF
    doc = SimpleDocTemplate(file_path, topMargin=50, bottomMargin=40)
    doc.build([title, legend, legend_body, table])
    print(f"PDF saved at {file_path}")


# -------------------- Workflow --------------------
def main():
    """Main analysis workflow: load data, process, visualize, and export reports."""

    # Load data
    dfo = pd.read_csv(OBSERVATIONS_FILE)
    dfs = pd.read_csv(SPECIES_FILE)

    # Clean common names
    dfs["common_names"] = dfs["common_names"].apply(lambda x: str(x).split(",")[0])

    # Create a quick pivot table to get a breakdown of conversation status
    con_status_pivot = dfs.pivot_table(index="category",
                                columns="conservation_status",
                                aggfunc="size",
                                fill_value=0)

    con_status_pivot.columns = ["Endangered", "Threatened", "Species of Concern", "In Recovery"]

    con_status_pivot.to_csv("Output/Conservation Status by Species Category.csv")


    # Fill missing conservation_status and add 'is_protected' column for pivot table
    dfs["conservation_status"] = dfs["conservation_status"].fillna("Not of Concern")
    dfs["is_protected"] = dfs["conservation_status"] != "Not of Concern"


    # Create another pivot table to get a breakdown of protection status
    protected_count_pivot = (dfs.groupby(["category", "is_protected"])
                       .scientific_name.nunique()
                       .reset_index()
                       .pivot(index="category",
                              columns="is_protected",
                              values="scientific_name"))

    protected_count_pivot.columns = ["Not Protected", "Protected"]

    # Adding a percentage for ease of analysis.
    protected_count_pivot["Percentage Protected"] = round((protected_count_pivot["Protected"] /
                                                     (protected_count_pivot["Protected"] + protected_count_pivot["Not Protected"]))
                                                    * 100, 2)

    protected_count_pivot.to_csv("Output/Protection Count by Species Category.csv")


    # Filter endangered species only
    dfs_endangered = dfs[dfs["conservation_status"] == "Endangered"]
    dfs_endangered = dfs_endangered.merge(dfo, on="scientific_name")

    # Aggregate observations
    endangered_count = (
        dfs_endangered.groupby(["common_names", "park_name"])
        .agg({"observations": "sum"})
        .reset_index())

    endangered_count_sci = (
        dfs_endangered.groupby(["scientific_name", "park_name"])
        .agg({"observations": "sum"})
        .reset_index())

    # Order species by observations in Great Smoky Mountains NP
    def order_smoky(df, col):
        return (
            df[df["park_name"] == "Great Smoky Mountains National Park"]
            .sort_values("observations", ascending=False)[col]
        )

    order = order_smoky(endangered_count, "common_names")
    order_sci = order_smoky(endangered_count_sci, "scientific_name")

    endangered_count_sorted = endangered_count.set_index("common_names").loc[order].reset_index()
    endangered_count_sci_sorted = endangered_count_sci.set_index("scientific_name").loc[order_sci].reset_index()

    # Generate barplots
    endangered_barplot(
        endangered_count_sorted,
        "common_names",
        "Species (Common Name)",
        os.path.join(OUTPUT_DIR, "Endangered_Barplot_Common.png"),
    )
    endangered_barplot(
        endangered_count_sci_sorted,
        "scientific_name",
        "Species (Scientific Name)",
        os.path.join(OUTPUT_DIR, "Endangered_Barplot.png"),
    )

    # Mask duplicates for table readability
    mask_names(endangered_count_sorted, "common_names")
    mask_names(endangered_count_sci_sorted, "scientific_name")

    # Generate PDF reports
    build_species_pdf(
        "Species (Common Name)",
        endangered_count_sorted,
        os.path.join(OUTPUT_DIR, "Endangered_Obs_Common.pdf"),
        "Count of Endangered Species Observations by National Park",
    )
    build_species_pdf(
        "Species (Scientific Name)",
        endangered_count_sci_sorted,
        os.path.join(OUTPUT_DIR, "Endangered_Obs_Table.pdf"),
        "Count of Endangered Species Observations by National Park",
    )


if __name__ == "__main__":
    main()
