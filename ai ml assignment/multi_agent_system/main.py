import networkx as nx
import matplotlib.pyplot as plt
from research_agent import ResearchAgent
from industry_report_agent import IndustryReportAgent
from use_case_agent import UseCaseAgent
from resource_agent import ResourceAgent
from proposal_agent import ProposalAgent

def create_architecture_flowchart_nx():
    G = nx.DiGraph()

    # Add nodes
    G.add_node('Industry/Company Research Agent')
    G.add_node('Market Standards & Use Case Generation Agent')
    G.add_node('Resource Asset Collection Agent')
    G.add_node('Final Proposal Generator')

    # Add edges with labels
    edges = [
        ('Industry/Company Research Agent', 'Market Standards & Use Case Generation Agent', 'Industry & Company Insights'),
        ('Market Standards & Use Case Generation Agent', 'Resource Asset Collection Agent', 'Use Cases'),
        ('Resource Asset Collection Agent', 'Final Proposal Generator', 'Resource Assets & Links'),
        ('Industry/Company Research Agent', 'Final Proposal Generator', 'Company Goals & Focus Areas')
    ]
    for u, v, label in edges:
        G.add_edge(u, v, label=label)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10,6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', arrowsize=20, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)
    plt.title("Multi-Agent Architecture Flowchart")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("multi_agent_architecture_nx.png")
    plt.close()
    print("Architecture flowchart generated as 'multi_agent_architecture_nx.png'")

def main():
    create_architecture_flowchart_nx()

    # Example workflow with placeholder data
    company_name = input("Enter the company name for research: ")
    research_agent = ResearchAgent(company_name)
    research_agent.research_industry()
    research_agent.identify_key_offerings()

    # Fetch industry reports
    industry_report_agent = IndustryReportAgent(company_name)
    industry_report_agent.fetch_reports()
    reports = industry_report_agent.get_report_links()

    # Use the titles of reports as industry info for use case analysis
    industry_info = " ".join([report["title"] for report in reports])
    use_case_agent = UseCaseAgent(industry_info)
    use_case_agent.analyze_industry_trends()
    use_cases = use_case_agent.generate_use_cases()

    resource_agent = ResourceAgent(use_cases)
    resource_agent.search_datasets()
    resource_agent.save_resource_links("resource_links.md")

    proposal_agent = ProposalAgent(use_cases, "resource_links.md")
    proposal_agent.generate_final_proposal()

    print("Multi-agent workflow executed with real data.")

if __name__ == "__main__":
    main()
