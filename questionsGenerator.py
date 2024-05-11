import prompts
import prompter

def generate(pros,cons):
    questions=[]

    prompter.starter()
    prompt = prompts.questionsPrompt(pros,cons)

    response = prompter.prompt(prompt)
    questions=response.split("\n")
    return questions
