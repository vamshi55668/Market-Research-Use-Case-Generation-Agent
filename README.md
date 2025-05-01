# Multi-Agent Market Research & Use Case Generation System

## Overview
This project implements a multi-agent architecture system designed to generate relevant AI and Generative AI use cases for a given company or industry. The system performs market research, analyzes industry trends, generates use cases, collects resource assets, and produces a final proposal.

## Agents
- **Industry/Company Research Agent**: Uses web browsing tools to understand the industry and company focus areas.
- **Market Standards & Use Case Generation Agent**: Analyzes industry trends and proposes relevant AI/ML use cases.
- **Resource Asset Collection Agent**: Collects datasets and resource links related to the generated use cases.
- **Final Proposal Generator**: Compiles top use cases and resources into a final actionable report.

## Architecture Flowchart
The architecture flowchart is generated programmatically using Graphviz and saved as `multi_agent_architecture.png`.

## How to Run
1. Install dependencies:
   ```
   pip install graphviz
   ```
2. Run the main script to generate the architecture flowchart:
   ```
   python main.py
   ```

## Next Steps
- Implement each agent as a separate module.
- Integrate web browsing and data collection tools.
- Develop use case generation logic.
- Create report generation and optional deployment on Streamlit or Gradio.
