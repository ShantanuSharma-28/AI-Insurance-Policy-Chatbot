# AI-Powered Insurance Policy Chatbot

## Overview

This project is an AI-powered chatbot that helps users understand different types of insurance policies. It uses natural language processing (NLP) techniques to answer queries related to health, auto, home, and life insurance. The chatbot can retrieve relevant information from a knowledge base built from insurance PDF documents.

## Hackathon Project

This chatbot was developed as part of a hackathon aimed at creating an AI-driven solution for the insurance industry. The chatbot is designed to help users quickly understand complex insurance policies, making it easier for them to make informed decisions.

## Features

- **Natural Language Understanding:** The chatbot can process user queries and provide accurate, detailed answers about insurance policies.
- **Knowledge Base Integration:** The chatbot retrieves information from a collection of insurance PDFs that contain details about various types of insurance, coverage options, premiums, and claim processes.
- **Conversation History:** The chatbot maintains a history of user queries and responses, allowing for a continuous conversation.
- **Fallback Mechanism:** In case the chatbot cannot answer a query, it escalates to human agents for complex issues.

## How to Run the Project

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.8 or above
- Streamlit for the UI
- Necessary libraries for running the AI models and processing PDFs

### Setup Instructions

1. **Clone the Repository:**

   Clone the repository to your local machine:
   
   `git clone https://github.com/your-username/insurance-chatbot.git`

   Navigate into the project directory:
   
   `cd insurance-chatbot`

2. **Create a Virtual Environment:**

   It is recommended to use a virtual environment to manage dependencies:
   
   `python -m venv venv`

   Activate the virtual environment:
   
   On Windows: `venv\Scripts\activate`

   On MacOS/Linux: `source venv/bin/activate`

3. **Install Dependencies:**

   Install the required libraries:
   
   `pip install -r requirements.txt`

4. **Prepare the Knowledge Base:**

   - Ensure that the folder containing the insurance PDF documents (`insurance_pdfs`) is in the project directory.
   - The knowledge base will be automatically created when you run the project, and the PDF documents will be indexed.

5. **Run the Streamlit App:**

   Start the Streamlit app to interact with the chatbot:
   
   `streamlit run main.py`

6. **Chat with the Bot:**

   Open your browser and navigate to `http://localhost:8501`. You can now ask the chatbot questions related to insurance policies, and it will provide responses based on the information from the knowledge base.

## Files in the Repository

- **main.py:** Streamlit interface that allows users to interact with the chatbot.
- **chatbot_backend.py:** Contains the AI model and logic for retrieving answers from the knowledge base.
- **knowledge_base.py:** Handles the loading of PDF documents, splitting them, and creating the FAISS index for efficient retrieval.
- **insurance_pdfs:** Folder containing PDF documents with insurance policy details.

## Contributions

If you'd like to contribute to this project, please fork the repository, make changes, and create a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The AI model used in this project is based on `Google's FLAN-T5`, a state-of-the-art NLP model.
- Special thanks to the LangChain library for simplifying the integration of various AI components like embeddings and retrievers.
