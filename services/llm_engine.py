from langchain.chat_models import ChatOpenAI
from config_utils import get_config_value

def run_llm():
    return ChatOpenAI(temperature=1, model="o4-mini", openai_api_key=get_config_value("OPENAI_API_KEY"))
