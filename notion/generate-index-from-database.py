from gpt_index import GPTListIndex, NotionPageReader

# from IPython.display import display, Markdown
import os

# get the directory of this
# file
dir_path = os.path.dirname(os.path.realpath(__file__))

integration_token = os.getenv("NOTION_INTEGRATION_TOKEN")
database_id = "31bc915a62934189ab2746ff5bd64407"
# database_page_ids = NotionPageReader(
#     integration_token=integration_token
# ).query_database(database_id=database_id)

# print("Page Ids from databse", database_page_ids)

documents = NotionPageReader(integration_token=integration_token).load_data(
    # page_ids=database_page_ids
    database_id=database_id
)

index = GPTListIndex(documents=documents)
index.save_to_disk(f"{dir_path}/index.json")
