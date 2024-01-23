def extract_and_write_values(input_file_path, output_file_path):
    valid_numbers = ['0.00', '0.33', '0.66', '1.00']
    
    # Read the input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Extract valid numbers and write to the output file
    with open(output_file_path, 'w') as output_file:
        for line in lines:
            # Find the valid number in the line
            for number in valid_numbers:
                if number in line:
                    output_file.write(number + '\n')
                    break  # Move to the next line after finding a valid number

