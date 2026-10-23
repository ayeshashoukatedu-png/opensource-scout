# OpenSource Scout 🔎

**Discover open-source projects. Understand their purpose. Find your first contribution.**

OpenSource Scout is an AI-powered tool that helps beginner developers explore GitHub repositories. Users enter a topic, and the tool searches GitHub and uses Gemini to generate a concise report explaining selected repositories and suggesting possible beginner-friendly contributions.

## ✨ Features

* 🔍 Search GitHub repositories by topic.
* 🤖 Generate AI-powered repository summaries using Gemini.
* 💻 Identify repository programming languages.
* ⭐ Display repository star counts.
* 💡 Suggest potential contribution ideas for beginners.
* 🔗 Include links to original GitHub repositories.

## 🎯 Problem

Beginners often struggle to find suitable open-source projects. Repository descriptions and technical terminology can make it difficult to understand where to start or how to contribute.

OpenSource Scout aims to make the discovery process easier by presenting repository information in a concise, beginner-friendly format.

## 💡 Solution

OpenSource Scout combines the GitHub Search API with a generative AI model to help users explore projects.

The current prototype selects up to three repositories and generates a report based on their available metadata.

Contribution ideas are suggestions, not verified open issues.

## 🛠️ Technologies

* Python
* GitHub REST API
* Google Gemini API
* `google-genai`
* `python-dotenv`
* `requests`

## 📋 Requirements

* Python 3.10 or a compatible version
* Internet connection
* GitHub API access
* A Gemini API key

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/opensource-scout.git
cd opensource-scout
```

Replace `YOUR-USERNAME` with your GitHub username after uploading the project.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own key. Never publish your API key.

### 5. Run OpenSource Scout

```bash
python ai_summarizer.py
```

Enter a topic when prompted, such as `python`, `artificial intelligence`, or `cybersecurity`.

## 📁 Project Structure

```text
opensource-scout/
├── ai_summarizer.py
├── search_repositories.py
├── requirements.txt
├── .gitignore
├── .env
├── README.md
└── skills/
    └── opensource-scout/
        └── SKILL.md
```

The `.env` file is local configuration and must not be committed to GitHub.

## 🔐 Responsible Use

* Repository descriptions and metadata may be incomplete.
* AI-generated summaries can contain mistakes.
* Suggested contributions are not confirmed open issues.
* Repository stars alone do not establish quality or security.
* Users should review repositories before installing or running their code.

## 🗺️ Future Improvements

* Filter repositories by programming language and topic.
* Verify open issues labeled `good first issue`.
* Add repository activity and maintenance indicators.
* Improve ranking and relevance of search results.
* Support additional AI model providers.
* Add automated tests and continuous integration.
* Improve compatibility with AI agent skill systems.

## 🤝 Contributing

Contributions are welcome! You can help improve documentation, add tests, improve search relevance, or suggest new features.

Please open an issue to discuss significant changes before submitting a pull request.

## 📄 License

This project is released under the MIT License. See the `LICENSE` file for details.
