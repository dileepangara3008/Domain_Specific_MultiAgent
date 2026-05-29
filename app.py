from graph import build_graph
import time
import logging
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# 🔧 Logging Setup
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_initial_state(query: str):
    return {
        "query": query,
        "research_data": [],
        "analysis": "",
        "report": "",
        "sources": [],
        "messages": [],
        "steps_log": []
    }


def main():
    graph = build_graph()

    # Save graph visualization once
    graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
    logging.info("✅ Graph saved as graph.png")

    print("\n💻 Tech Research Assistant (type 'exit' to quit)\n")

    while True:
        try:
            # -----------------------------
            # 🧑 User Input
            # -----------------------------
            query = input("👉 Enter your question: ").strip()

            if query.lower() in ["exit", "quit"]:
                print("\n👋 Exiting... Goodbye!")
                break

            if not query:
                print("⚠️ Please enter a valid query.\n")
                continue

            # -----------------------------
            # ⏱️ Execution
            # -----------------------------
            start = time.time()

            result = graph.invoke(get_initial_state(query))

            end = time.time()

            # -----------------------------
            # 📊 Metrics
            # -----------------------------
            latency = round(end - start, 2)
            steps = len(result.get("steps_log", []))

            logging.info(f"⏱️ Latency: {latency}s")
            logging.info(f"🔁 Steps: {steps}")

            # -----------------------------
            # 📄 Output
            # -----------------------------
            print("\n✅ FINAL REPORT:\n")
            print(result.get("report", "No report generated."))
            print("\n" + "="*60 + "\n")

        except Exception as e:
            logging.error(f"❌ Error: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()