def calculate_average_and_write_to_file(file1, file2, file3, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3, open(output_file, 'w') as out:
        for line1, line2, line3 in zip(f1, f2, f3):
            try:
                # Convert the lines to floats and calculate the average
                average = (float(line1) + float(line2) + float(line3)) / 3
            except ValueError:
                # Handle the case where the line can't be converted to a float
                out.write('Invalid data\n')
                continue

            # Write the average evaluation of the prompt to the output file
            out.write(f'{average}\n')

