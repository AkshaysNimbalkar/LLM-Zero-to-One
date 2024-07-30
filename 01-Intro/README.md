

01 - Introduction:

LLM: Large langua Model:
    (Large: trained on tons of data and tons of parameters) unlike traditional lanuguage models)
    Input (prompt) --> LLM --> ANswer

RAG: Retrieval Augumented Generation:
    Retrieval: (Search)
    Generation (LLM)


Set open_api_key as a enviournment vaiable:
 use below command for windows:
    setx OPEN_API_KEY "your_open_api_key"

So in Summary we build the knowledge database, from knowledge database we build the propmt, and this prompt is passed to the OpenAI chatgpt.

Run Elastic Search with the Docker:
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3

command to check elasticsearch running on the localhost:
    curl localhost:9200

-Elastic Search:
    Elastic Search is more persistent than toy search as it keeps data on the disk after the execution

The OpenAI python package uses tiktoken for tokenization:

pip install tiktoken
Let's calculate the number of tokens in our query:

encoding = tiktoken.encoding_for_model("gpt-4o")