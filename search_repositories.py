import requests


def search_repositories(topic, limit=5):
    url = "https://api.github.com/search/repositories"

    params = {
        "q": topic,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    response = requests.get(
        url,
        params=params,
        timeout=20,
        headers={"Accept": "application/vnd.github+json"}
    )

    print("GitHub status code:", response.status_code)

    response.raise_for_status()
    data = response.json()

    print("Repositories found:", data.get("total_count", 0))

    repositories = []

    for repo in data.get("items", []):
        repositories.append({
            "name": repo["full_name"],
            "description": repo.get("description") or "No description",
            "language": repo.get("language") or "Not specified",
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "updated_at": repo["updated_at"]
        })

    return repositories


if __name__ == "__main__":
    topic = input("Enter a topic, e.g. Python: ")

    try:
        results = search_repositories(topic)

        for index, repo in enumerate(results, start=1):
            print(f"\n{index}. {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Language: {repo['language']}")
            print(f"Stars: {repo['stars']}")
            print(f"Last updated: {repo['updated_at']}")
            print(f"URL: {repo['url']}")

    except requests.RequestException as error:
        print(f"GitHub request failed: {error}")
