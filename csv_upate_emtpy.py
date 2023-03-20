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
                # Check if the cell is blank
                if cell.strip() == '':
                    # If the cell is blank, add a value
                    row[i] = 'attala123'

            # Write the updated row to the output CSV file
            writer.writerow(row)
