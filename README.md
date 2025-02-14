# Topsis-Vivek-102203871

This Python package implements the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) decision-making method. It helps evaluate and rank alternatives based on multiple criteria, supporting both **CSV** and **Excel** file formats.

## Features

- Simple command-line interface.
- Supports both `.csv` and `.xlsx` input formats.
- Allows specifying weights and impacts for decision criteria.
- Outputs the Topsis score and rank for each alternative.

# Reference Link
You can find the package on PyPI: [Topsis-Vivek-102203871 on PyPI](https://pypi.org/project/Topsis-Vivek-102203871/)

## Installation

To install the package, use `pip` (Python package manager). Run the following command in your terminal:

```bash
pip install Topsis-Vivek-102203871
```

## STEPS
Step 1: Prepare Your Input Data
The input file should have at least 3 columns:

The first column should represent the alternatives/objects (e.g., M1, M2, M3, etc.).
The second column and beyond should contain numeric values representing the criteria for each alternative.
Example Input Data (CSV format)
Fund Name, P1, P2, P3, P4, P5
M1, 0.84, 0.71, 6.7, 42.1, 12.59
M2, 0.91, 0.83, 7.0, 31.7, 10.11
M3, 0.79, 0.62, 4.8, 46.7, 13.23
M4, 0.78, 0.61, 6.4, 42.4, 12.55
M5, 0.94, 0.88, 3.6, 62.2, 16.91
Example Input Data (Excel format)
Alternatively, you can provide the data in Excel (.xlsx) format.

Step 2: Define Weights and Impacts
Weights: The relative importance of each criterion (must be comma-separated).
Impacts: The direction of preference for each criterion (+ for benefit, - for cost).
Example Weights and Impacts
Weights: "0.25, 0.25, 0.25, 0.25"
Impacts: "+,+,-,+"
Step 3: Running the Command
Once your input data is ready, you can run the package using the command line. The format is:

```bash
python -m Topsis_Vivek_102203871 <input_file> <weights> <impacts> <result_file>
```
Example Command
```bash
python -m Topsis_Vivek_102203871 102203871-data.xlsx "0.25, 0.25, 0.25, 0.25" "+,+,-,+" 102203871-result.csv
```
Where:

102203871-data.xlsx is the input file (can be .csv or .xlsx).
"0.25, 0.25, 0.25, 0.25" represents the weights of each criterion.
"+,+,-,+" represents the impacts of each criterion.
102203871-result.csv is the output file where results will be saved.
Step 4: Understanding the Output
The output file will contain:

The original data.
Two additional columns:
Topsis Score: The computed score for each alternative.
Rank: The rank based on the Topsis score (lower score = better rank).
Example Output (CSV):

Fund Name, P1, P2, P3, P4, P5, Topsis Score, Rank
M1, 0.84, 0.71, 6.7, 42.1, 12.59, 0.865, 2
M2, 0.91, 0.83, 7.0, 31.7, 10.11, 0.799, 3
M3, 0.79, 0.62, 4.8, 46.7, 13.23, 0.935, 1
M4, 0.78, 0.61, 6.4, 42.4, 12.55, 0.876, 4
M5, 0.94, 0.88, 3.6, 62.2, 16.91, 0.980, 5
The Topsis Score column represents how close each alternative is to the ideal solution, and the Rank column indicates the rank based on the Topsis score.

## How it works
How the Package Works
Normalization: The decision matrix is normalized using vector normalization.
Weighted Matrix: The normalized matrix is weighted according to the user-defined weights.
Ideal Solutions: The positive and negative ideal solutions are determined based on the direction of the impacts.
Topsis Score: The Topsis score is calculated using the distance between the alternatives and the ideal solutions.
Rank: The alternatives are ranked based on the calculated Topsis score.
Error Handling
The package performs the following validations:

File Not Found: Checks if the input file exists.
Correct Number of Parameters: Ensures that the number of command-line arguments is correct.
Valid Weights: Ensures that the weights are numeric and properly formatted.
Valid Impacts: Ensures that the impacts contain only + or -.
Valid Input Data: Ensures that the data columns contain only numeric values (except the first column).
## License
This package is distributed under the MIT License. See LICENSE.txt for more details.

## Contact
For any questions or issues, feel free to contact me at atrivivek001@gmail.com.



### Summary

- This `README.md` provides a full guide on how to install, use, and understand the **Topsis-Vivek-102203871** package.
- It includes clear instructions, example inputs/outputs, and error handling.






