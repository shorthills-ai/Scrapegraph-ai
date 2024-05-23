""" 
Basic example of scraping pipeline using SmartScraper using Azure OpenAI Key
"""

from langchain_community.embeddings import OllamaEmbeddings
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

# ************************************************
# Initialize the model instances
# ************************************************

embedder_model_instance = OllamaEmbeddings()

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

from langchain_community.llms import Ollama

llm_model_instance = Ollama(model="llama2:latest")

graph_config = {
     "llm": {"model_instance": llm_model_instance},
    "embeddings": {"model_instance": embedder_model_instance},
    "verbose": True,
}

prompt_val = '''List me all events that are in April.'''

smart_scraper_graph = SmartScraperGraph(
    prompt=prompt_val,
    # also accepts a string with the already downloaded HTML code
    source="https://www.gsa.gov/about-us/events-and-training/gsa-events",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))