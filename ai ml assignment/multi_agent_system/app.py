import streamlit as st
from research_agent import ResearchAgent
from industry_report_agent import IndustryReportAgent
from use_case_agent import UseCaseAgent
from resource_agent import ResourceAgent
from proposal_agent import ProposalAgent
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

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

import streamlit as st
from research_agent import ResearchAgent
from industry_report_agent import IndustryReportAgent
from use_case_agent import UseCaseAgent
from resource_agent import ResourceAgent
from proposal_agent import ProposalAgent
import networkx as nx
import matplotlib.pyplot as plt

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

def main():
    st.title("Market Research & Use Case Generation Agent")

    company_name = st.text_input("Enter the company name for research:")

    if st.button("Run Multi-Agent System"):
        if not company_name:
            st.warning("Please enter a company name.")
            return

        st.info("Generating architecture flowchart...")
        create_architecture_flowchart_nx()
        st.image("multi_agent_architecture_nx.png", caption="Architecture Flowchart")

        st.info(f"Researching company: {company_name}")

        # Removed browser_action due to import issues; removed info message as per user request

        research_agent = ResearchAgent(company_name)
        research_agent.research_industry()
        research_agent.identify_key_offerings()

        if research_agent.industry:
            st.markdown("### Company Overview")
            st.write(research_agent.industry)

        if research_agent.key_offerings:
            st.markdown("### Key Offerings")
            for offering in research_agent.key_offerings:
                st.write(f"- {offering}")

        st.info("Fetching detailed company information...")
        company_details = research_agent.get_company_details()
        if company_details:
            st.markdown("### Detailed Company Information")
            st.write(company_details)

        st.info("Fetching industry reports...")
        industry_report_agent = IndustryReportAgent(company_name)
        industry_report_agent.fetch_reports()
        reports = industry_report_agent.get_report_links()
        if reports:
            st.markdown("### Industry Reports")
            for report in reports:
                st.markdown(f"- [{report['title']}]({report['link']}) (Source: {report['source']})")

        # Combine company industry info and report titles for use case analysis
        company_industry_info = research_agent.industry if research_agent.industry else ""
        report_titles = " ".join([report["title"] for report in reports])
        industry_info = company_industry_info + " " + report_titles
        use_case_agent = UseCaseAgent(industry_info.strip())
        use_case_agent.analyze_industry_trends()
        use_cases = use_case_agent.generate_use_cases()

        resource_agent = ResourceAgent(use_cases)
        resource_agent.search_datasets()
        resource_agent.save_resource_links("resource_links.md")

        st.info("Resource Assets for Use Cases")

        kaggle_links = [link for link in resource_agent.resource_links if link.lower().startswith("[kaggle:")]
        other_links = [link for link in resource_agent.resource_links if not link.lower().startswith("[kaggle:")]

        if kaggle_links:
            st.markdown("#### Kaggle Dataset Links")
            for link in kaggle_links:
                import re
                match = re.match(r'\[(.*?)\]\((.*?)\)', link)
                if match:
                    text, url = match.groups()
                    st.markdown(f"- [{text}]({url})")
                else:
                    st.markdown(f"- {link}")

        if other_links:
            st.markdown("#### Other Resource Links")
            for link in other_links:
                import re
                match = re.match(r'\[(.*?)\]\((.*?)\)', link)
                if match:
                    text, url = match.groups()
                    st.markdown(f"- [{text}]({url})")
                else:
                    st.markdown(f"- {link}")

        proposal_agent = ProposalAgent(use_cases, "resource_links.md")
        proposal_agent.generate_final_proposal()

        st.success("Multi-agent workflow completed.")
        st.markdown("### Final Proposal")
        with open("final_proposal.md", "r", encoding="utf-8") as f:
            proposal_text = f.read()
        st.markdown(proposal_text)

if __name__ == "__main__":
    main()
