""" 
Basic example of scraping pipeline using SmartScraper using Azure OpenAI Key
"""
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

# required environment variable in .env
# AZURE_OPENAI_API_VERSION
# AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME
load_dotenv()

# ************************************************
# Initialize the model instances
# ************************************************

embedder_model_instance = AzureOpenAIEmbeddings(
    azure_deployment=os.environ["AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)

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

prompt_val = '''List me only one event, with the following fields: 
                event_name:
                event_start_date: 
                event_start_time: 
                event_end_date: 
                event_end_time: 
                location: 
                registration_link: 
                event_type: 
                event_category:'''

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