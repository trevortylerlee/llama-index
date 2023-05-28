# llama-index

1. Clone the repository:
```shell
git clone https://github.com/trevortylerlee/llama-index
```

2. Change into the repository directory:
```shell
cd llama-index
```

3. Create the virtual environment inside the repository directory:
```shell
python -m venv llamaindexenv
```

4. Activate the virtual environment:
```shell
source llamaindexenv/bin/activate
```

5. Install the required dependencies:

```shell
pip install flask llama-index
```

6. Add your OpenAI API key in flask_api.py

7. Start the server:

```shell
python flask_api.py
```

8. Navigate to localhost:5601/query?text=what is wrong with Professor Quirrells head

9. Replace harry-potter.txt in the documents folder to whatever you want
