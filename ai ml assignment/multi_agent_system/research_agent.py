from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class ResearchAgent:
    def __init__(self, company_name):
        self.company_name = company_name
        self.industry = None
        self.key_offerings = None
        self.driver = None

    def _init_driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def research_industry(self):
        """
        Use Selenium to research the industry and segment the company is working in.
        For demonstration, search Google and extract snippet from first result.
        """
        try:
            self._init_driver()
            query = f"{self.company_name} industry overview"
            self.driver.get(f"https://www.google.com/search?q={query}")
            time.sleep(3)  # wait for page to load

            # Try to extract the knowledge panel or snippet
            snippet = ""
            try:
                snippet_elem = self.driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="wa:/description"] span')
                snippet = snippet_elem.text
            except:
                try:
                    snippet_elem = self.driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/organization/organization:description"] span')
                    snippet = snippet_elem.text
                except:
                    try:
                        snippet_elem = self.driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/business/business_operation:operation"] span')
                        snippet = snippet_elem.text
                    except:
                        snippet = ""

            if snippet:
                self.industry = snippet
                print(f"Industry/Company info: {self.industry}")
            else:
                print("No industry overview snippet found on Google search.")
        except Exception as e:
            print(f"Error during research_industry: {e}")
        finally:
            if self.driver:
                self.driver.quit()

    def identify_key_offerings(self):
        """
        Use Selenium to identify the company’s key offerings and strategic focus areas.
        For demonstration, search Google and extract offerings from knowledge panel or website.
        """
        try:
            self._init_driver()
            query = f"{self.company_name} products services"
            self.driver.get(f"https://www.google.com/search?q={query}")
            time.sleep(3)  # wait for page to load

            offerings = []
            try:
                elems = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-attrid="kc:/organization/organization:products"] span')
                offerings = [elem.text for elem in elems if elem.text]
            except:
                offerings = []

            if offerings:
                self.key_offerings = offerings
                print(f"Key offerings: {self.key_offerings}")
            else:
                print("No key offerings found on Google search.")
        except Exception as e:
            print(f"Error during identify_key_offerings: {e}")
        finally:
            if self.driver:
                self.driver.quit()

    def get_company_details(self):
        """
        Fetch detailed company information from Wikipedia.
        """
        import requests
        from bs4 import BeautifulSoup

        try:
            url = f"https://en.wikipedia.org/wiki/{self.company_name.replace(' ', '_')}"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')
                details = ''
                for p in paragraphs[:5]:  # get first 5 paragraphs
                    text = p.get_text().strip()
                    if text:
                        details += text + '\n\n'
                if details:
                    print(f"Company details fetched from Wikipedia.")
                    return details
                else:
                    print("No detailed paragraphs found on Wikipedia page.")
                    return None
            else:
                print(f"Failed to fetch Wikipedia page for {self.company_name}")
                return None
        except Exception as e:
            print(f"Error fetching company details: {e}")
            return None
