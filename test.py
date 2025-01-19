import os
import pandas as pd
import numpy as np

def test_topsis(input_file, output_file):
    try:
        print("Starting test script for Topsis...")
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            print("Error: Input file not found. Ensure the file path is correct.")
            return

        print("Input file found. Loading data...")
        file_extension = os.path.splitext(input_file)[-1].lower()

        # Load the file
        if file_extension == ".csv":
            data = pd.read_csv(input_file)
        elif file_extension == ".xlsx":
            data = pd.read_excel(input_file, engine="openpyxl")
        else:
            print("Error: Unsupported file format. Use .csv or .xlsx.")
            return

        print("File loaded successfully. Displaying the first few rows:")
        print(data.head())

        # Validate number of columns
        if data.shape[1] < 3:
            print("Error: Input file must have at least three columns.")
            return

        # Validate numeric data in criteria columns
        print("Checking data types of columns:")
        print(data.dtypes)

        matrix = data.iloc[:, 1:]  # Exclude the first column (object names)
        print("Validating numeric data in matrix columns...")
        matrix = matrix.apply(pd.to_numeric, errors='coerce')  # Convert non-numeric to NaN
        if matrix.isnull().values.any():
            print("Error: Non-numeric or invalid values found in the matrix:")
            print(matrix)
            return

        print("Data validation passed.")

        # Save a simple test output
        print("Testing file saving...")
        test_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        test_df.to_csv(output_file, index=False)
        print(f"Test file saved successfully to: {output_file}")

        # Run a simple Topsis test
        print("Running a simple Topsis test...")
        weights = [0.25, 0.25, 0.25, 0.25, 0.25]
        impacts = ['+', '+', '-', '+', '+']

        # Normalize the matrix
        norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

        # Apply weights
        weighted_matrix = norm_matrix * weights

        # Calculate ideal and negative-ideal solutions
        ideal_solution = np.where(np.array(impacts) == '+', weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
        negative_ideal_solution = np.where(np.array(impacts) == '+', weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

        # Calculate distances
        pos_distance = np.sqrt(((weighted_matrix - ideal_solution)**2).sum(axis=1))
        neg_distance = np.sqrt(((weighted_matrix - negative_ideal_solution)**2).sum(axis=1))

        # Calculate scores and ranks
        scores = neg_distance / (pos_distance + neg_distance)
        ranks = scores.argsort()[::-1] + 1

        # Print results
        print("Scores and ranks calculated:")
        print("Scores:", scores)
        print("Ranks:", ranks)

        # Save results
        result = data.copy()
        result['Topsis Score'] = scores
        result['Rank'] = ranks
        result.to_csv(output_file, index=False)
        print(f"Topsis results saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the test
if __name__ == "__main__":
    input_file = "/Users/vivekattri/topsis_vk/102203871-data.xlsx"  # Update the path if needed
    output_file = "/Users/vivekattri/topsis_vk/102203871-test-result.csv"
    test_topsis(input_file, output_file)
