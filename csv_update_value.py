import csv

# Open the input CSV file
with open('input.csv', 'r') as csvfile:
    # Open the output CSV file
    with open('output.csv', 'w', newline='') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)

        # Loop through each row in the CSV file
        for row in reader:
            # Loop through each cell in the row
            for i, cell in enumerate(row):
                # Check if the cell is equal to the value to be replaced
                if cell == 'old_value':
                    # If the cell is equal to the value to be replaced, replace it with the new value
                    row[i] = 'new_value'

            # Write the updated row to the output CSV file
            writer.writerow(row)
