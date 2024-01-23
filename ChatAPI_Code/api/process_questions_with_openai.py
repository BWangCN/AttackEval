from openai import OpenAI

def process_questions_with_openai(input_file, output_file):
    API_KEY = 'YOUR_API_KEY'
    client = OpenAI(api_key=API_KEY)

    # open file and read the prompts
    with open(input_file, "r", encoding="utf-8") as file:
        questions = file.readlines()

    # set the model
    model = "gpt-3.5-turbo"

    # initialize the answer
    answers = []

    # iterate through the prompts and generate answers
    for question in questions:
        question = question.strip()
        if question:
            completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": question}],
            )
            answer = completion.choices[0].message.content.strip()
            answer = answer.replace('\n',' ')
            answers.append(answer)

    # write the answers to the file
    with open(output_file, "w", encoding="utf-8") as file:
        for answer in answers:
            answer_str = str(answer)
            file.write(answer_str + "\n")

    print(f"already save the answers to file: {output_file}")

