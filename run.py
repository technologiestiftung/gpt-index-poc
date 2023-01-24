from gpt_index import GPTSimpleVectorIndex 
# from IPython.display import display
# import os;

# os.environ['OPENAI_API_KEY']

# documents = SimpleDirectoryReader('./gpt_index/examples/paul_graham_essay/data').load_data()
# index = GPTSimpleVectorIndex(documents)
proceed = False
while True:
    res = input("Do you want me to send a request to openAI? Will generate cost (y/N)")
    if res.lower() == 'y':
        proceed = True
        break
    elif res.lower() == 'n':
        proceed = False
        break
    else:
        print("Please enter y or n")

if proceed == True:
    index = GPTSimpleVectorIndex.load_from_disk('./index.json')
    response = index.query("What did the author do growing up?")
    print(response)


