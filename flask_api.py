import os
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext
from flask import Flask, request

# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ['OPENAI_API_KEY'] = "your-key-here"

app = Flask(__name__)
index = None

def initialize_index():
    global index
    storage_context = StorageContext.from_defaults()
    index_dir = "./index"
    if os.path.exists(index_dir):
        index = load_index_from_storage(storage_context)
    else:
        documents = SimpleDirectoryReader("./documents").load_data()
        index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context)
        storage_context.persist(index_dir)

@app.route("/query", methods=["GET"])
def query_index():
  global index
  query_text = request.args.get("text", None)
  if query_text is None:
    return "No text found, please include a ?text=blah parameter in the URL", 400
  query_engine = index.as_query_engine()
  response = query_engine.query(query_text)
  return str(response), 200

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    initialize_index()
    app.run(host="0.0.0.0", port=5601)