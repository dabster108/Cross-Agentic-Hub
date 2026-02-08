class PlannerAgent:
    """Splits a high-level goal into actionable steps"""
    def plan(self, goal: str):
        steps = [
            "Understand the requirement",
            "Define project structure",
            "Setup FastAPI app",
            "Generate APIs and endpoints",
            "Validate and test code"
        ]
        return steps
