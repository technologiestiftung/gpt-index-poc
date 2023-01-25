# playing with gpt-index

## General usage [Pattern][pattern] of gpt-index

1. Load in documents (either manually, or through a data loader).
2. Index Construction.
3. \[Optional, Advanced\] Building indices on top of other indices
4. Query the index.

All scripts are split into two steps. One to create the index and another to run a query against it.
The index generation should be run once and the query can be run multiple times. Be aware that the index generation is still dumb and will overwrite the index file every time. A more elaborate system should be in place to only update the index when necessary.

## Setup

1. Install [poetry][poetry]
2. install `direnv` with this command: `brew install direnv` and set it up do work with your shell
3. Copy `.envrc.example` to `.envrc` and set the environment variables
4. Get an openAI API key and set it as an environment variable `OPENAI_API_KEY` in `.envrc`
5. Create new Notion [integration][notion-integrations]
6. Get a Notion API key and set it as an environment variable `NOTION_INTEGRATION_TOKEN` in `.envrc`
7. In the upper right corner of a Notion page click the three dots and add a connection to your integration. Every sub page will also be available to the integration.
8. Get the Notion page ID and set add it to the script `notion/generate-index.py` into the `page_ids` list
9. Make sure to always ignore the generated indices in your git repository e.g. `echo "notion/<YOUR INDEX NAME>.json" >> .gitignore`

## Usage

```bash
cd repo
# install dependencies
poetry install
# activate the virtual environment
poetry shell
# allow direnv to set environment variables in the shell
direnv allow
# write the index to disk
python notion/generate-index.py
# run the query
# The script will prompt you for input
python notion/query-index.py
```

## Utilities

In the folder notion/utils you can find a script to generate a list of all the page or database ids your integration has access to. This is useful if you want to generate an index for all the pages in your Notion workspace.

```bash
poetry shell
direnv allow
python notion/utils/list-ids.py
```

[pattern]: https://gpt-index.readthedocs.io/en/latest/guides/primer.html#general-usage-pattern-of-gpt-index
[notion-integrations]: https://www.notion.so/my-integrations
[poetry]: https://python-poetry.org/
