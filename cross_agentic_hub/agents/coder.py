from utils.helpers import call_mistral

class CoderAgent:
    def generate_code(self, plan):
        prompt = f"Generate Python code for the following steps:\n{plan}"
        code = call_mistral(prompt)
        return code
