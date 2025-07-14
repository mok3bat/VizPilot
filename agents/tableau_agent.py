from services.embeddings import semantic_search_with_justification
from services.llm_engine import run_llm
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

llm = run_llm()

def search_metadata_with_vectors(query: str) -> str:
    results = semantic_search_with_justification(query)

    if not results:
        return "❌ No dashboards found matching your query."

    justification_texts = []
    raw_context = []
    for doc, score in results:
        justification_texts.append(
            f"✅ **{doc.metadata['source']}**\n- Relevance score: `{score:.4f}`\n- Matched content: *{doc.page_content}*"
        )
        raw_context.append(doc.page_content)

    summary_prompt = f"""
The user asked: "{query}"

Below are the dashboards retrieved via semantic search, along with their metadata content. Please summarize why these dashboards are relevant to the query and highlight their purpose.

Dashboards:
{chr(10).join(raw_context)}

Answer in a helpful, concise, user-facing tone.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("human", "{input}")
    ])
    chain = prompt | llm

    summary_response = llm([HumanMessage(content=summary_prompt)])
    summary = summary_response.content

    return "### 🔍 Why These Dashboards Were Selected:\n" + "\n\n".join(justification_texts) + "\n\n---\n" + "### 🤖 AI Summary:\n" + summary
