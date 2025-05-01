class ResourceAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases
        self.resource_links = []

    def search_datasets(self):
        """
        Search for relevant datasets on platforms like Kaggle, HuggingFace, and GitHub.
        Scrape Kaggle search results and GitHub repositories for each use case keyword.
        """
        import requests
        from bs4 import BeautifulSoup
        import urllib.parse

        print("Searching for datasets related to use cases...")
        self.resource_links = []

        if not self.use_cases:
            print("No use cases provided.")
            return

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        for use_case in self.use_cases:
            # Kaggle scraping
            query = urllib.parse.quote_plus(use_case)
            kaggle_search_url = f"https://www.kaggle.com/datasets?search={query}"
            try:
                response = requests.get(kaggle_search_url, headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # Updated selector for Kaggle dataset links
                    dataset_links = soup.select('a.sc-fzqBZW.hXqzZP, a.sc-fzqBZW')
                    count = 0
                    for ds in dataset_links:
                        href = ds.get('href', '')
                        title = ds.get_text(strip=True)
                        if href.startswith('/datasets/') and title:
                            link = "https://www.kaggle.com" + href
                            link_md = f"[Kaggle: {title}]({link})"
                            if link_md not in self.resource_links:
                                self.resource_links.append(link_md)
                                count += 1
                        if count >= 3:
                            break
                    if count == 0:
                        print(f"No Kaggle datasets found for use case: {use_case}")
                        # Add fallback static Kaggle link
                        fallback_link = "[Kaggle: General Datasets](https://www.kaggle.com/datasets)"
                        if fallback_link not in self.resource_links:
                            self.resource_links.append(fallback_link)
                else:
                    print(f"Failed to fetch Kaggle search results for use case: {use_case}, status code: {response.status_code}")
                    # Add fallback static Kaggle link
                    fallback_link = "[Kaggle: General Datasets](https://www.kaggle.com/datasets)"
                    if fallback_link not in self.resource_links:
                        self.resource_links.append(fallback_link)
            except Exception as e:
                print(f"Error searching Kaggle datasets for use case: {use_case}: {e}")
                # Add fallback static Kaggle link
                fallback_link = "[Kaggle: General Datasets](https://www.kaggle.com/datasets)"
                if fallback_link not in self.resource_links:
                    self.resource_links.append(fallback_link)

            # GitHub search for dataset repos with retry and delay to handle rate limits
            import time
            github_search_url = f"https://github.com/search?q={query}+dataset&type=repositories"
            max_retries = 1  # Reduce retries to speed up
            for attempt in range(max_retries):
                try:
                    response = requests.get(github_search_url, headers=headers, timeout=5)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        repo_links = soup.select('a.v-align-middle')
                        count = 0
                        for repo in repo_links:
                            href = repo.get('href', '')
                            title = repo.get_text(strip=True)
                            if href and title:
                                link = "https://github.com" + href
                                link_md = f"[GitHub: {title}]({link})"
                                if link_md not in self.resource_links:
                                    self.resource_links.append(link_md)
                                    count += 1
                            if count >= 3:
                                break
                        if count == 0:
                            print(f"No GitHub dataset repositories found for use case: {use_case}")
                        break
                    elif response.status_code == 429:
                        print(f"Rate limited by GitHub API, skipping further retries.")
                        break
                    else:
                        print(f"Failed to fetch GitHub search results for use case: {use_case}, status code: {response.status_code}")
                        break
                except Exception as e:
                    print(f"Error searching GitHub repositories for use case: {use_case}: {e}")
                    break

        # Add static link for HuggingFace models
        self.resource_links.append("[HuggingFace: Pretrained Language Models](https://huggingface.co/models)")

        print(f"Found resource links: {self.resource_links}")

    def save_resource_links(self, filepath):
        """
        Save the collected resource links in a text or markdown file.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("# Resource Links for Use Cases\n\n")
                for link in self.resource_links:
                    f.write(f"- {link}\n")
            print(f"Resource links saved to {filepath}")
        except Exception as e:
            print(f"Error saving resource links: {e}")
