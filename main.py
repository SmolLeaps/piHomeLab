from command_parser import parse_command
from github_api import create_github_repo
from run_c_code import run_c_code
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

model_name = "EleutherAI/gpt-neo-125M"
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

token = "your_github_token_here"

while True:
    user_input = input("Enter your command: ")
    response = generate_text(user_input)
    command = parse_command(response)

    if command["action"] == "create_repo":
        create_github_repo(command["repo_name"], token)
    elif command["action"] == "run_c_code":
        run_c_code(command["file_name"])
    else:
        print("Unknown command.")

