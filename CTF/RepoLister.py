import requests
def get_github_repos(username, access_token):
    url = f"https://api.github.com/user/repos?visibility=all"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    repos = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos.extend(response.json())
            # Check if there is a next page
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f"Failed to retrieve repositories: {response.status_code}")
            return []

    return repos


username = 'CandleOil-Karthik'
access_token = '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'

repositories = get_github_repos(username, access_token)
for repo in repositories:
    print(f"Repo Name: {repo['name']}, URL: {repo['html_url']}")
