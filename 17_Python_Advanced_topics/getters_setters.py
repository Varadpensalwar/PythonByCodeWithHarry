class VaradPensalwar:
    def __init__(self):
        self.name = "Varad Pensalwar"
        self.role = "AI/ML & Generative AI Engineer"
        self.education = "B.Tech in AIML @ Sanjay Ghodawat University"
        self.location = "Pune, Maharashtra, India 🇮🇳"
        self.passion = "Building Intelligent Systems that Transform Reality"

        # Core AI/ML Expertise
        self.ai_domain = {
            "Generative AI": ["LLMs", "LangChain", "Prompt Engineering"],
            # "Machine Learning": ["Numpy", "Pandas",],
            "Deployment": ["APIs", "Model Serving"]
        }

        self.current_focus = [
            "🔥 Large Language Models",
            "🔥 LangChain",
            "🔥 Generative AI Applications"
        ]

    def get_mission(self):
        return "Pushing the boundaries of AI to create systems that augment human intelligence."

    def introduce(self):
        return (
            f"👋 Hi, I'm {self.name}!\n"
            f"🎯 Role: {self.role}\n"
            f"🎓 Education: {self.education}\n"
            f"📍 Location: {self.location}\n"
            f"💡 Passion: {self.passion}\n"
            f"🚀 Mission: {self.get_mission()}\n"
            f"🔍 Current Focus: {', '.join(self.current_focus)}\n"
        )

# Initialize the AI Engineer
ai_engineer = VaradPensalwar()
print(ai_engineer.introduce())
