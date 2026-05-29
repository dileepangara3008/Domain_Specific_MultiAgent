from tavily import TavilyClient

TAVILY_API_KEY = "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"

tavily = TavilyClient(api_key=TAVILY_API_KEY)

def tavily_search(query: str):
    response = tavily.search(query=query, max_results=3)

    results = []
    for r in response["results"]:
        results.append({
            "title": r["title"],
            "content": r["content"],
            "url": r["url"]
        })

    return results