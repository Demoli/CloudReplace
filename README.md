# Welcome to Cloud Replace

## What is it?
Cloud Replace utilises the power of the cloud to do string replacements.

Why use old, outdated methods for string replacement when you can utilise a modern, trendy RESTful service?

## What's in this repo

This repo contains both the server and python client so you can either use [URL TBC] or host your own instance.

## How do I use it

Simply POST a JSON string to `/replace` containing your subject string, search string and replacement string.

### Request

    {
      "subject":"Hello World!",
      "search":"Hello",
      "replace":"Goodbye"
    }

### Response
    {
      "subject": "Hello World!",
      "search": "Hello",
      "replace": "Goodbye",
      "result": "Goodbye World!"
    }

## Python client
    from cloud_replace.client import Client
    replace = Client()
    replace.replace('Hello World!', 'Hello', 'Goodbye')