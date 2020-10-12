# Genomic Data Visualization Tool

## The study

This website is intended to allow for easy and interactive visualization of the proteomics and phosphoproteomics data analyzed by Brubaker *et al.* in ["Proteogenomic Network Analysis of Context-Specific KRAS Signaling in Mouse-to-Human Cross-Species Translation."](https://www.sciencedirect.com/science/article/pii/S2405471219302388?via%3Dihub)
The study measured the effects of mutant *KRAS* G12D on the colon and pancreas in a preneoplastic and neoplastic state.

## The data

The data presented on this website is the original proteomics and phosphoproteomics collected from mouse colon and pancreas.
Both organs were collected in a preneoplastic state and a neoplastic state with either a *KRAS* G12D mutation or wild-type *KRAS*.
The neoplastic state for colon was replicated by inducing a loss-of-function mutation to *APC*.
In pancreas, this state was modeled by inducing a loss-of-function mutation to *TP53*.
These two genes were chosen as they best represent the mutations found in the cancer of each organ.

The proteomics was conducted quantitatively using TMT-labeled mass spectrometry (MS).
The *KRAS* mutant and wild-type samples for each organ  and state (preneoplastic and neoplastic) were run together.

### Searching the data

To search for a gene or protein, enter its full or partial name into the search bar at the top of the page and hit "Enter."
This will bring you to a table of the entries that statisfy your search term in any of the table's categories: "Gene Symbol," "Protein ID," and "Description."
The results can be further filtered using the "Filter" box in the top-right.
The data for the desired protein in the table can be viewed by clicking on the entry number in the left-most column.

Selecting an entry will bring up its proteomics data - the phosphoproteomics will be included, soon.
Along the top are cards with various pieces of information on the protein.

### Understanding the plots

Up to four box-plots will be shown for a protein.
The box-plots are "Colon Empithelium" (*APC* WT), "Apc-mutant Colon" (*APC* mutant), "Whole Pancreas" (*TP53* WT), and "Tp53-mutant Pancreas" (*TP53* mutant).
Each box-plot shows the data for mice with either *KRAS* WT or *KRAS* G12D.
If a plot is empty, that means the protein was not identified in that MS analysis.

The y-axis for the proteomics indicates the normalized level of protein.
Each mouse organ run through the MS contained 1000 mg of protein.
Thus, within a single run of the MS, the total protein for each mouse should be equivalent.
The amount of each peptide measured was normalized such that the total amount summed to 1000 for each mouse.

Each organ and state (preneoplastic and neoplastic) is displayed separately because they were run through the MS, separately.
Thus, their values cannot be directly compared.
Instead, the plot below the box-plots allows one to easily compare the ratio of protein in the *KRAS* G12D to *KRAS* WT in each organ.
Each point indicates the lagarithm of this ratio and the horizontal line indicates the 95% confidence interval (bootstrapped).
Because the ratios are log-scaled, if the protein was present in equal amounts in the *KRAS* mutant and wild-type organs, the point will lie at 0.
Further, if the protein was more abundant in the *KRAS* WT organ, the log-transformed ratio will be negative.
The oppositite is true if the protein was more abundant in the *KRAS* G12D organ.

### Data availability

The entire dataset can be downloaded at the "Data" page.
The spreadsheets include the original and normalized peptide levels for each sample.
The phosphoproteomics data will be made available, soon.
