class ProposalAgent:
    def __init__(self, use_cases, resource_links_file):
        self.use_cases = use_cases
        self.resource_links_file = resource_links_file

    def generate_final_proposal(self):
        """
        Compile top use cases and resource assets into a final actionable report.
        """
        try:
            with open("final_proposal.md", "w", encoding="utf-8") as f:
                f.write("# Final Proposal: AI & GenAI Use Cases\n\n")
                f.write("## Top Use Cases\n")
                for i, use_case in enumerate(self.use_cases, 1):
                    f.write(f"{i}. {use_case}\n")
                f.write("\n## References\n")
                f.write("- [McKinsey Industry Reports](https://www.mckinsey.com/industries)\n")
                f.write("- [Deloitte Insights](https://www2.deloitte.com/us/en/insights.html)\n")
                f.write("- [Nexocode AI Reports](https://nexocode.com/ai-reports/)\n")
                f.write("- Market research and competitor analysis\n")
                # Read resource links and separate Kaggle links
                with open(self.resource_links_file, "r", encoding="utf-8") as rf:
                    lines = rf.readlines()
                kaggle_links = [line for line in lines if line.lower().startswith("- [kaggle:")]
                other_links = [line for line in lines if not line.lower().startswith("- [kaggle:")]
                f.write("\n## Kaggle Dataset Links\n")
                if kaggle_links:
                    for link in kaggle_links:
                        f.write(link)
                else:
                    f.write("No Kaggle dataset links found.\n")
                f.write("\n## Other Resource Links\n")
                for link in other_links:
                    f.write(link)
                # Optional GenAI solutions section
                f.write("\n## Optional GenAI Solutions\n")
                f.write("- Document search system for internal knowledge bases\n")
                f.write("- Automated report generation using Generative AI\n")
                f.write("- AI-powered chat systems for customer support and internal use\n")
            print("Final proposal generated as 'final_proposal.md'")
        except Exception as e:
            print(f"Error generating final proposal: {e}")
