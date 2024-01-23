from prompt_generate import replace_string_in_file
from api import process_questions_with_openai, quantify
from format import calculate_average, extract_and_write_values, format_answers
from prompt_generate import replace_string_in_file

# set the parameters
input_file_path = "prompt_generate/jailbreak_prompt_template1.txt"
jailbreak_prompt = "dataset/example_prompts.txt"
# the template use phrase "hotwire a car"
# replace "hotwire" with a verb like "hijack", replace "car" with a noun like "airplane"
string_to_replace1 = "hotwire"
replacement_string1 = "draw"
string_to_replace2 = "car"
replacement_string2 = "porn picture"
# the three answers and there values
answer1 = "intermediate_dataset/answer1.txt"
answer2 = "intermediate_dataset/answer2.txt"
answer3 = "intermediate_dataset/answer3.txt"
answer_evaluation1 = "intermediate_dataset/answer_evaluation1.txt"
answer_evaluation2 = "intermediate_dataset/answer_evaluation2.txt"
answer_evaluation3 = "intermediate_dataset/answer_evaluation3.txt"
value1 = "intermediate_dataset/value1.txt"
value2 = "intermediate_dataset/value2.txt"
value3 = "intermediate_dataset/value3.txt"
# the average value for the prompts
prompt_value = "dataset/example_prompt_values.txt"

# invoke functions
# firstly, replace the template with the string wanted
replace_string_in_file.replace_string_in_file(input_file_path, jailbreak_prompt, string_to_replace1, replacement_string1, string_to_replace2, replacement_string2)
# secondly, generate and format the gpt answers for three times
process_questions_with_openai.process_questions_with_openai(jailbreak_prompt, answer1)
process_questions_with_openai.process_questions_with_openai(jailbreak_prompt, answer2)
process_questions_with_openai.process_questions_with_openai(jailbreak_prompt, answer3)
# thirdly, quantify the three set of answers
quantify.quantify(answer1,answer_evaluation1)
quantify.quantify(answer2,answer_evaluation2)
quantify.quantify(answer3,answer_evaluation3)
# fourthly, extract the value and store them in value files
extract_and_write_values.extract_and_write_values(answer_evaluation1,value1)
extract_and_write_values.extract_and_write_values(answer_evaluation2,value2)
extract_and_write_values.extract_and_write_values(answer_evaluation3,value3)
#finally, calculate the average score
calculate_average.calculate_average_and_write_to_file(value1,value2,value3,prompt_value)
