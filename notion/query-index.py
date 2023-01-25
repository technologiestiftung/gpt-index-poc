from gpt_index import GPTListIndex
from IPython.display import Markdown, display
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

index = GPTListIndex.load_from_disk(f"{dir_path}/index.json")
proceed = False
while True:
    prompt = input("Enter a query: ")
    if len(prompt) == 0:
        proceed = False
        break
    else:
        proceed = True
        break

try:
    if proceed == True:
        result = index.query(prompt, verbose=True)
        print(result.response)
    else:
        print("Query entered")
except Exception as e:
    print(e)


# response = index.query("How should branches be named?", verbose=True)


