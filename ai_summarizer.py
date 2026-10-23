
import os
import sys
from dotenv import load_dotenv
from google import genai

# Load the API key from the .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: GEMINI_API_KEY was not found.")
    print("Make sure your .env file contains GEMINI_API_KEY=your_key")
    sys.exit(1)

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

# Use the same model that worked in test_gemini.py
MODEL_NAME = "gemini-3.5-flash-lite"


def summarize_repositories(topic, repositories):
    """Generate an AI report about GitHub repositories."""

    if not repositories:
        return "No repositories were found for this topic."

    # Use a maximum of three repositories
    selected = repositories[:3]

    # Prepare repository information
    repository_details = "\n\n".join(
        [
            f"Repository: {repo.get('name', 'Unknown')}\n"
            f"Description: {repo.get('description') or 'No description'}\n"
            f"Language: {repo.get('language') or 'Unknown'}\n"
            f"Stars: {repo.get('stars', 0)}\n"
            f"URL: {repo.get('url', '')}"
            for repo in selected
        ]
    )

    # Keep the prompt short to reduce processing time
    prompt = f"""
You are OpenSource Scout, an assistant that helps beginners
discover open-source software projects.

Topic: {topic}

GitHub repository information:
{repository_details}

For each repository, provide:
1. A short explanation based on its description.
2. Its main programming language.
3. One practical contribution idea for a beginner.
4. Its original GitHub URL.

Do not invent features or claim that issues are open.
Label contribution ideas as suggestions.
Keep the complete report under 200 words.
"""

    print("Sending repository information to Gemini...")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": 0.2,
                "max_output_tokens": 400,
                "http_options": {
                    "timeout": 60000
                },
            },
        )

        report = getattr(response, "text", None)

        if report:
            print("AI report generated successfully!")
            return report

        return (
            "Gemini returned an empty response. "
            "Please try again."
        )

    except Exception as error:
        error_message = str(error)
        error_type = type(error).__name__

        print(f"\nGemini error: {error_type}")
        print(error_message)

        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            return (
                "The Gemini API quota or rate limit may have been "
                "reached. Check your Google AI Studio usage limits "
                "and try again later."
            )

        if (
            "404" in error_message
            or "NOT_FOUND" in error_message
        ):
            return (
                f"The model '{MODEL_NAME}' was not found or is "
                "unavailable to your account. Check the model "
                "available in your Google AI Studio account."
            )

        if (
            "504" in error_message
            or "DEADLINE_EXCEEDED" in error_message
            or "timeout" in error_message.lower()
        ):
            return (
                "Gemini timed out. The request contains only "
                "three repositories. Try again later or check "
                "your internet connection."
            )

        return (
            "Unable to generate the AI report. "
            f"Error type: {error_type}. "
            f"Details: {error_message}"
        )


def main():
    """Run OpenSource Scout."""

    try:
        from search_repositories import search_repositories
    except ImportError:
        print(
            "ERROR: Could not import search_repositories.py.\n"
            "Make sure it is in the same folder as this file."
        )
        sys.exit(1)

    topic = input(
        "Enter a topic to explore (e.g., Python, AI, cybersecurity): "
    ).strip()

    if not topic:
        print("Please enter a topic.")
        return

    try:
        print(f"\nSearching GitHub for '{topic}'...")

        repositories = search_repositories(topic)

        if not repositories:
            print("No repositories found. Try another topic.")
            return

        print(f"Found {len(repositories)} repositories.")
        print("\nGenerating your AI report...")

        report = summarize_repositories(topic, repositories)

        print("\n" + "=" * 55)
        print("              OPENSOURCE SCOUT")
        print("           AI REPOSITORY REPORT")
        print("=" * 55)
        print(report)
        print("=" * 55)

    except Exception as error:
        print("\nAn application error occurred.")
        print(f"Error type: {type(error).__name__}")
        print(f"Details: {error}")


if __name__ == "__main__":
    main()
