def replace_string_in_file(input_file_path, output_file_path, string_to_replace1, replacement_string1, string_to_replace2, replacement_string2):
    """
    Read a file, replace all occurrences of a specified string with a new string, and write the result to a new file.

    :param input_file_path: Path to the input file
    :param output_file_path: Path to the output file
    :param string_to_replace: The string to be replaced
    :param replacement_string: The string to replace with
    """

    try:
        # Read the input file
        with open(input_file_path, 'r') as file:
            file_contents = file.read()

        # Replace the specified string
        updated_contents = file_contents.replace(string_to_replace1, replacement_string1)
        updated_contents = updated_contents.replace(string_to_replace2, replacement_string2)

        # Write to the output file
        with open(output_file_path, 'w') as file:
            file.write(updated_contents)

        print("String replacement completed successfully.")

    except Exception as e:
        print("String replacement failed.")
        return str(e)

# # Example usage:
# replace_string_in_file('path/to/input.txt', 'path/to/output.txt', '{STRING_TO_REPLACE}', 'desired_string')

# input_file_path="/Users/waynewang/Desktop/ChatAPI/prompt_generate/jailbreak_prompt_template.txt"
# output_file_path="/Users/waynewang/Desktop/ChatAPI/prompt_generate/act_as_voyeur.txt"
# string_to_replace1="hotwire"
# replacement_string1="act as"
# string_to_replace2="car"
# replacement_string2="voyeur"
# replace_string_in_file(input_file_path, output_file_path, string_to_replace1, replacement_string1, string_to_replace2, replacement_string2)