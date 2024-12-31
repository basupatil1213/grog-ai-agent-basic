# grog-ai-agent-basic

## Overview
The `grog-ai-agent-basic` project is a collection of AI agents designed to perform various tasks such as fetching financial data, summarizing news, and more. The agents leverage models like Groq and OpenAI's GPT-4, and utilize tools such as DuckDuckGo and YFinance.

## Project Structure
- `1_grog_ai_agent.py`: A basic agent that generates text responses using the Groq model.
- `2_finance_agent.py`: An agent focused on financial data, using both Groq and OpenAI models along with YFinance tools.
- `3_agent_teams.py`: A team of agents that work together to fetch and summarize financial data and news.
- `output.example`: Example outputs from running the different agents, showcasing their capabilities and responses.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/basupatil1213/grog-ai-agent-basic.git
    cd grog-ai-agent-basic
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root directory and add your API keys:
    ```env
    GROQ_API_KEY=your_groq_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage
1. Run the basic Groq AI agent:
    ```sh
    python 1_grog_ai_agent.py
    ```
2. Run the finance agent:
    ```sh
    python 2_finance_agent.py
    ```
3. Run the agent teams:
    ```sh
    python 3_agent_teams.py
    ```

## Example Outputs
The [output.example](http://_vscodecontentref_/2) file contains example outputs from running the different agents. It showcases the types of responses you can expect from the agents, including text generation and financial data summaries.

## Phidata
This project utilizes the `phidata` library, which provides tools and models for building AI agents. It includes integrations with various APIs and services, making it easier to develop and deploy AI-driven applications.

## License
This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/3) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Contact
For any questions or inquiries, please contact Basavaraj Patil at patil.basava@outlook.com.