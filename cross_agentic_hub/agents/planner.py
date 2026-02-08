from utils.helpers import call_mistral

class PlannerAgent:
    def plan(self, goal: str):
        prompt = f"Break down the following goal into clear actionable steps:\nGoal: {goal}"
        plan_text = call_mistral(prompt)
        steps = plan_text.split("\n")
        return steps
