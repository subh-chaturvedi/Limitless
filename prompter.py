def starter():
    import openai
    openai.api_key = get_api_key_from_yaml("./key.yaml")
    

def get_api_key_from_yaml(file_path):
    import yaml

    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        api_key = yaml_data.get('api_key', None)
    
    
    return api_key


def prompt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # This is the model ID for GPT-4, change if needed
        messages=[{"role": "user", "content": prompt}],
        max_tokens=70
    )

    return response.choices[0].message.content