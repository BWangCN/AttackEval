# README

1. Follow the official document from OPENAI to set up your api key.

   https://platform.openai.com/docs/quickstart?context=python

   Then, you can use your own api key to run the code

2. `jailbreak_prompt_template.txt` contains 70 jailbreak prompt templates from a website, all tailored for `"hotwire a car"`. To generate custom prompts in bulk, modify the template in `method3.py`. For example:

   To generate `"hijack an airplane"`, change `replacement_string1` to `"hijack"` and `string_to_replace2` to `"airplane"`.

   `jailbreak_prompt_template1.txt` is a smaller template with only 1 prompt, used for testing purposes.

3. `method3` is the script for executing the entire method. Its usage is as follows:

   `input_file` is the prompt template you wish to use.

   Users need to create a `jailbreak_prompt` file to store the generated prompts. The example is in the folder `dataset`, named as `example_prompts.txt`.

   Users need to create three `answer` files to store the generated answers of the jailbreak prompts. Users need to create three  `answer_evaluation` files to store the analysis and evaluation for the three `answer` files. Users need to create three `value` files to store the evaluation value for each `answer` file. The examples are in the folder `intermediate_dataset`, named as `answer`, `value` and `answer_evaluation`.

   Users need to create a `prompt_value` file to store the average of the three values, which represents the final prompt evaluation.  The example is in the folder `dataset`, named as `example_prompt_values.txt`.

4. In folder `api`, there are two scripts used for invoking openai api. `process_questions_with_openai.py` is used to generate answers from the jailbreak prompts. `quantify.py` is used to evaluate the answers.

5. In folder `format`, there are two scripts used for the final value. `extract_and_write_values.py` extract values from the evaluation. `calculate_average` calculate the average of three generated values and use it as the final evaluation value of the  corresponding prompt.