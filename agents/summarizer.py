from utils.helpers import call_mistral

class SummarizerAgent:
    def summarize(self, chat_history):
        chat_text = "\n".join(chat_history)
        prompt = f"Summarize this conversation in short bullets and extract all code blocks:\n{chat_text}"
        summary = call_mistral(prompt)
        return summary
