from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from datetime import datetime
import os

@tool("save_text_to_file")
def save_tool(
    topic: str,
    summary: str,
    sources: str,
    filename: str = "research_output.txt"
) -> str:

    """Save research topic, summary, and sources to a text file."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    content = f"""--- Research Output ---\nTimestamp: {timestamp}\n\nTopic: {topic}\n\nSummary:\n{summary}\n\nSources:\n{sources}"""
    
    os.makedirs("research", exist_ok=True)
    with open(f"research/{filename}", "a", encoding="utf-8") as f:
        f.write(content)

    return f"Data successfully saved to research/{filename}"


search = DuckDuckGoSearchRun()
@tool
def search_tool(query: str) -> str:
    """Search the web for information."""
    return search.run(query)
