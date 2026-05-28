2024-11-08 00:49

Status: #baby 

Tags: [[guide]]



How to set up a local RAG pipeline

For this, we'll use the repo located in the references below.

You'll need Python, Pip, and Poetry.

Clone the repo locally into wherever you want.  Then, you'll need to make a directory called .streamlit. In this directory, you must construct a secrets.toml file.  This is where your OpenAI API key will go.  Simple create a field called "openai_key", assign it the value of your API key, enclosed within quotes to make it a string, and save the file.

It should look like

`openai_key = "fake_key_here"`

After that, set up your environment.

run `python -m venv .venv`

and activate it with

`.venv\Scripts\activate`. You can exit the environment be using the `deactivate` command.

Then, run `poetry install --with dev`.  

Then, you can run the app with


```
streamlit run 1_🏠_Home.py
```


Once the app is loaded, you can create an agent by entering into the chatbot field at the home page.  Just tell it the file path of what you want to analyze, and it will load it and create the agent.  

It can only load one file at a time, or one directory.  PDFs, .txt, markdown, or JSON is the best for analysis.

You can go to the RAG config page to rename the agent and adjust the parameters.  6-8 Documents is where I personally prefer to keep it at.  Increasing the chunk size usually goes over the rate limit for OpenAI, so I just keep it at 1024.  You can adjust the model it uses, but I've messed around with them and gpt-4-1106-preview seems to be overall the best.  gpt-3.5-turbo allows a lot of tokens, but even maxing out the documents and chunk size, the analysis is very surface level.

## References:
https://github.com/run-llama/rags