class IndustryReportAgent:
    def __init__(self, industry):
        self.industry = industry
        self.reports = []

    def fetch_reports(self):
        """
        Fetch or scrape industry reports from sources like McKinsey, Deloitte, Nexocode.
        For demonstration, simulate fetching report titles and links.
        """
        print(f"Fetching industry reports for: {self.industry}")
        # Placeholder example reports
        self.reports = [
            {"title": "AI and Digital Transformation in " + self.industry,
             "source": "McKinsey",
             "link": "https://www.mckinsey.com/featured-insights/artificial-intelligence"},
            {"title": "The Future of AI in " + self.industry,
             "source": "Deloitte",
             "link": "https://www2.deloitte.com/global/en/pages/technology/articles/future-of-ai.html"},
            {"title": "AI Use Cases in " + self.industry,
             "source": "Nexocode",
             "link": "https://nexocode.com/blog/ai-use-cases/"},
            {"title": "AI Trends and Insights in " + self.industry,
             "source": "Gartner",
             "link": "https://www.gartner.com/en/information-technology/insights/artificial-intelligence"},
            {"title": "AI and Automation in " + self.industry,
             "source": "Forrester",
             "link": "https://go.forrester.com/research/"},
            {"title": "Digital Transformation and AI in " + self.industry,
             "source": "Accenture",
             "link": "https://www.accenture.com/us-en/insights/artificial-intelligence-index"},
            {"title": "AI Strategy and Use Cases in " + self.industry,
             "source": "PwC",
             "link": "https://www.pwc.com/gx/en/issues/analytics/assets/pwc-ai-analysis-sizing-the-prize-report.pdf"},
            {"title": "AI in Business: Trends and Use Cases in " + self.industry,
             "source": "Boston Consulting Group",
             "link": "https://www.bcg.com/publications/2020/artificial-intelligence-business-transformation"},
        ]
        print(f"Fetched {len(self.reports)} reports.")

    def get_report_links(self):
        """
        Return list of report links with titles and sources.
        """
        return self.reports
