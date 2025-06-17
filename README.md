
---

# Conversational AI Agent with LangChain, Wikipedia Tools & Streamlit UI

A modular, memory-aware AI chat assistant that combines the power of **LangChain**, **OpenAI GPT**, **tool calling (Wikipedia search)**, and **Streamlit**. Designed for real-world use across customer support, enterprise helpdesks, and knowledge management.

---
## 💼 Business Scope

This project delivers a lightweight yet powerful **AI Chat Assistant** leveraging OpenAI’s `gpt-3.5-turbo` model via a Streamlit front-end and LangChain backend. It supports context-aware interactions and tool-based augmentations, making it suitable for domain-specific AI agents across industries.

### Key Objectives:

* Enable seamless human-AI interaction via chat.
* Provide contextual responses using memory.
* Serve as a base for autonomous agents with tools.
* Automate knowledge delivery and enterprise assistance.

---

## 🚀 Real-World Use Cases

| Sector               | Use Case Description                                       |
| -------------------- | ---------------------------------------------------------- |
| Customer Support     | Answer FAQs, resolve issues, and escalate tickets.         |
| Enterprise Helpdesk  | Automate internal queries (HR, IT, policy, onboarding).    |
| Education & Training | 24/7 tutoring support or personalized learning assistants. |
| Healthcare           | Answer health-related questions and triage direction.      |
| E-commerce           | Product discovery, recommendations, and order tracking.    |
| Knowledge Management | Fast retrieval of company SOPs, documents, and procedures. |
| HR & Recruitment     | Handle candidate queries and job-fit explanations.         |
| Legal & Compliance   | Summarize regulations or explain legal procedures.         |
| Real Estate          | Respond to queries about listings, prices, or loans.       |

---

## 🌍 Why This Matters

1. **Reduces Manual Workload** with automation.
2. **Scalable** to thousands of users concurrently.
3. **24/7 Availability** with no downtime.
4. **Boosts Productivity** via faster answers.
5. **Enhances Experience** through personalized chats.
6. **Cost-Effective** by reducing support staff load.
7. **Modular & Extendable** for tools, APIs, or vector search.

---

## 🧠 LangChain Integration

This assistant uses **LangChain's ConversationChain** and **ConversationBufferMemory**, allowing it to remember prior context and respond naturally over multi-turn conversations.

### Benefits:

* Maintains session memory
* Future-proof for multi-agent or RAG integrations
* Easy to plug in other tools or retrievers

---

## 🧰 Tool Calling with Wikipedia Search

This agent includes a tool for **Wikipedia-powered Q\&A** using LangChain's agent-based tool system. It enhances factual answers when the assistant lacks direct knowledge.

> **Example**:
> *"Who was Nikola Tesla?"* → The assistant searches and returns a reliable summary.

---

## 📂 Project Structure

```
conversational-ai-agent/
├── streamlit_app/
│   ├── app.py                  # Streamlit interface
│   ├── langchain_agent.py      # LangChain agent + memory + tool logic
│   └── tools.py                # Wikipedia tool integration
├── .env                        # API key (optional, recommended for local dev)
├── requirements.txt            # Project dependencies
├── architecture_diagram.png    # System architecture
└── README.md                   # Project documentation
```

---
## 🔧 Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/conversational-ai-agent.git
   cd conversational-ai-agent
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\\Scripts\\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key**

   * Method 1: `.env` file (recommended for local dev)

     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   * Method 2: **Enter via Streamlit UI** (if `.env` is not found)

5. **Run the app**

   ```bash
   streamlit run streamlit_app/app.py
   ```
---

## 🔐 OpenAI API Key Configuration

You can configure your OpenAI key in two ways:

1. **`.env` File Method**

   * Create a `.env` file in the root folder:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

2. **Streamlit Prompt Method**

   * If `.env` is missing, the app will ask for the key via secure UI input on startup.

> ✅ This dual-mode setup makes it easy to use locally or deploy to cloud services.

---

## 🖼 Architecture Diagram

![Architecture Diagram](architecture_diagram.png)

---

## 📬 Contact

* [GitHub](https://github.com/amitkharche)
* [LinkedIn](https://www.linkedin.com/in/amit-kharche)

---
