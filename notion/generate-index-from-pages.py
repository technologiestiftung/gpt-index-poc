from gpt_index import GPTListIndex, NotionPageReader

# from IPython.display import display, Markdown
import os

# get the directory of this
# file
dir_path = os.path.dirname(os.path.realpath(__file__))

integration_token = os.getenv("NOTION_INTEGRATION_TOKEN")
page_ids = ["e5436982df224f088de91a9802402872"]
documents = NotionPageReader(integration_token=integration_token).load_data(
    page_ids=page_ids
)

index = GPTListIndex(documents=documents)
index.save_to_disk(f"{dir_path}/index.json")
