import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

dfo = pd.read_csv("Data/observations.csv")
dfs = pd.read_csv("Data/species_info.csv")



                                  ########### Initial analysis ###########

# The "common_names" column contains a list of common names assigned to each species. As the most commonly used
# name is the first in the list, that is the one we will assign to visualisations going forward.
# Additionally, in case of inconsistencies within the "common_names" column.
dfs["common_names"] = dfs["common_names"].apply(lambda x: x.split(",")[0])


# Creating a simple pivot table to see the category of species and their protection level.
dfs_pivot = dfs.pivot_table(index="category",
                           columns="conservation_status",
                           aggfunc="size",
                           fill_value=0)

dfs_pivot.columns = ["Endangered", "Threatened", "Species of Concern", "In Recovery"]

dfs_pivot.to_csv("Output/Conservation Status by Species Category.csv")

# If a species is not under protection, the DF assigns a null value. Instead, I will assign the value "Not of
# Concern" for future analysis.
dfs["conservation_status"] = dfs["conservation_status"].fillna("Not of Concern")
dfs["is_protected"] = dfs["conservation_status"] != "Not of Concern"


# Splitting the DF into protected and not protected
dfs_protected = dfs[dfs["conservation_status"] != "Not of Concern"]
dfs_not_protected = dfs[dfs["conservation_status"] == "Not of Concern"]

print("Not of Concern: ", len(dfs_not_protected))
print("Of Concern: ", len(dfs_protected))


# Creating another pivot table to examine the count of protected and not protected species by category.
protected_count = (dfs.groupby(["category", "is_protected"])
                        .scientific_name.nunique()
                        .reset_index()
                        .pivot(index = "category",
                           columns = "is_protected",
                           values = "scientific_name")
                        .reset_index())

protected_count.columns = ["Category", "Not Protected", "Protected"]

# Adding a percentage for ease of reading/analysis.
protected_count["Percentage Protected"] = round((protected_count["Protected"] /
                                    (protected_count["Protected"] + protected_count["Not Protected"]))
                                    * 100,2)

protected_count.to_csv("Output/Protection Count and Percentage by Species Category.csv")




                        ########### Investigating the 14 endangered species ###########

# Creating a DataFrame for to show only the endangered species
dfs_endangered = dfs[dfs["conservation_status"] == "Endangered"]

# Merging the endangered species DF with the observation DF
dfs_endangered = dfs_endangered.merge(dfo, on = "scientific_name")


endangered_count = (dfs_endangered
                    .groupby(["common_names", "park_name"])
                    .agg({"observations": "sum"}))

endangered_count_sci = (dfs_endangered
                    .groupby(["scientific_name", "park_name"])
                    .agg({"observations": "sum"}))


endangered_count = endangered_count.reset_index()
endangered_count_sci = endangered_count_sci.reset_index()
#
# Ordering x-axis by the value of the observations from one national park, to ensure the two barplots will be identical
# Ordering by Big Smoky Nat. Park to ensure both tables are in the same order
def order_smoky(df, col):
    df = (df[df["park_name"] == "Great Smoky Mountains National Park"]
        .sort_values("observations", ascending=False)[col])
    return df

order = order_smoky(endangered_count, "common_names")
order_sci = order_smoky(endangered_count_sci, "scientific_name")

endangered_count_sorted = endangered_count.set_index("common_names").loc[order].reset_index()
endangered_count_sci_sorted = endangered_count_sci.set_index("scientific_name").loc[order_sci].reset_index()



# Barplot function
def endangered_barplot(data, x_axis_data, x_axis_name, filepath):
    plt.subplots(figsize=(20, 8))
    endangered_bar = sns.barplot(x=x_axis_data, y="observations",
                                 data=data,
                                 hue="park_name")

    # Wrapping and capitalizing the x-axis labels
    x_wrap = [
        textwrap.fill(
            " ".join([label.capitalize() for label in label.get_text().split()]), width=13)
        for label in endangered_bar.get_xticklabels()]

    # Applying to the barplot
    plt.xticks(ticks=endangered_bar.get_xticks(),
               labels=x_wrap)

    # Adding guidelines for ease of reading
    endangered_bar.yaxis.grid(True, linestyle="--", alpha=0.6)

    # Adding labels, and title. Also fixing legend positioning
    plt.xlabel(x_axis_name)
    plt.ylabel("Observations")
    plt.title("Total Observations of Endangered Species")
    plt.legend(
        title="National Park",
        loc="center left",
        bbox_to_anchor=(0.725, 1.1))

    plt.savefig(filepath, bbox_inches="tight")
    plt.clf()

# Calling barplot function for both the common and scientific name. Depending on target audience
endangered_barplot(endangered_count_sorted, "common_names",
                   "Species (Common Name)", "Output/Endangered Species Observations - Common.png")
endangered_barplot(endangered_count_sci_sorted, "scientific_name",
                   "Species (Scientific Name)", "Output/Endangered Species Observations - Sci.png")



# Masking repeated species/common names for table readability
def mask_names(df, col):
    df[col] = (df[col]
               .mask(df[col]
               .duplicated()).fillna(""))
    return df

mask_names(endangered_count_sorted, "common_names")
mask_names(endangered_count_sci_sorted, "scientific_name")

def build_species_pdf(col_name, data, file_path, title_text):
    # Prepare table data (prepend header row)
    table_data = [[col_name, 'Park Name', 'Observations']] + data.values.tolist()

    # Table style (shared)
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

    # Add line breaks dynamically
    line_break_number = list(range(5, 54, 4))
    for line in line_break_number:
        style_commands.append(('LINEABOVE', (0, line), (2, line), 3, colors.black))

    # Styles
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

    # Text content
    title = Paragraph(title_text, title_style)
    legend = Paragraph("Legend", legend_style)
    legend_body = Paragraph(
        "Mammal: Red____Bird: Blue____Fish: Yellow____Vascular Plant: Green____Amphibian: Turquoise",
        legendbody_style
    )

    # Create table
    table = Table(table_data)
    table.setStyle(TableStyle(style_commands))

    # Build PDF
    doc = SimpleDocTemplate(file_path, topMargin=50, bottomMargin=40)
    doc.build([title, legend, legend_body, table])
    print(f"PDF saved at {file_path}")



# Common names table
build_species_pdf("Species (Common Name)", endangered_count_sorted,
    "Output/Endangered Observations - Common.pdf",
    "Count of Endangered Species Observations by National Park")

# Species table
build_species_pdf("Species",
    endangered_count_sci_sorted,
    "Output/Endangered Observations - Scientific.pdf",
    "Count of Endangered Species Observations by National Park")



# Look into the bird and mammal populations, higher protected percentage over the other categories























# def strip_punctuation(text):
#     for punctuation in string.punctuation:
#         text = text.replace(punctuation, "")
#     return text
#
#
# concern_common_names = list(dfs_concern.common_names.apply(strip_punctuation).str.split())
#
# concern_common_names = list(chain.from_iterable(
#                  dict.fromkeys(item)
#                  for item in concern_common_names))
#
# concern_words_counted = []
#
# for word in concern_common_names:
#     count = concern_common_names.count(word)
#     concern_words_counted.append((word, count))
#
# concern_name_count = pd.DataFrame(set(concern_words_counted), columns=["Word", "Count"])
#
# print(concern_name_count.sort_values("Count", ascending = False).head(10), "\n\n")











