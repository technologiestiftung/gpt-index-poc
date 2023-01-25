# docs https://github.com/casey/just
# justfile load .env file
# set dotenv-load
set shell := ["bash", "-uc"]
alias notion:= list-notion-pages


default:
    @just --list


list-notion-pages:
    npx httpyac docs/notion.http

