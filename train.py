from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
# from IPython.display import display
# import os;

# os.environ['OPENAI_API_KEY']
proceed = False
documents = SimpleDirectoryReader('./data').load_data()
while True:
    res = input("Should we send the data to openAI? It will generate costs (y/N)")
    if res.lower() == 'y':
        proceed = True
        break
    elif res.lower() == 'n':
        proceed = False
        break
    else:
        print("Please enter y or n")

if proceed == True:
    index = GPTSimpleVectorIndex(documents)
    index.save_to_disk("./index.json")

# response = index.query("What did the author do growing up?")
# print(response)


