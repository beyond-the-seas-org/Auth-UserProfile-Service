from flask_restx import Resource
from flask import request,jsonify
from user import api

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from user.profile.apis.user_profile import profile
from user.profile.models.student import StudentModel


def extract_info(text, link):
    publication_data = {}

    # Split the text into lines
    lines = text.split("\n")

    # Initialize variables to store the extracted information
    title = None
    date_of_conference = None
    doi = None
    citations = None
    ieee_keywords = []
    author_keywords = []

    # Iterate through the lines to find the relevant information
    for i, line in enumerate(lines):
        if i == 1:
            title = line.strip()
        elif "Date of Publication:" in line:
            date_of_conference = line.split(":")[1].strip()
        elif "DOI:" in line:
            doi = line.split(":")[1].strip()
        elif "All Authors" in line:
            if i + 1 < len(lines):
                citations = lines[i + 1].strip()
        elif "Abstract" in line:
                # Collect the lines that follow the "Abstract:" section
            abstract_lines = []
            for j in range(i + 1, len(lines)):
                if "Published in:" in lines[j]:
                    break
                abstract_lines.append(lines[j])
            abstract = " ".join(abstract_lines).strip()

        elif "IEEE Keywords" in line:
            # take the rest of the lines
            rest_of_the_lines = lines[i + 1:]
            # split the lines by Author Keywords
            
            ieee = True
            author = False
            for keyword in rest_of_the_lines:
                if "Author Keywords" in keyword:
                    author = True
                    ieee = False
                    continue
                
                if "INSPEC: Controlled Indexing" in keyword or "INSPEC: Non-Controlled Indexing" in keyword:
                    ieee = False
                    author = False

                if "Metrics" in keyword:
                    break
                
                if ieee and keyword != ",":
                    ieee_keywords.append(keyword)
                elif author and keyword != ",":
                    author_keywords.append(keyword)

            
    # Store the extracted information in a dictionary
    publication_data["title"] = title
    publication_data["link"] = link
    publication_data["date_of_publication"] = date_of_conference
    publication_data["doi"] = doi
    publication_data["citations"] = citations
    publication_data["abstract"] = abstract
    publication_data["ieee_keywords"] = ieee_keywords
    publication_data["author_keywords"] = author_keywords
    publication_data["keywords"] = ieee_keywords + author_keywords

    return publication_data

@profile.route('/get_ieee_publication_info')
class GetIeeePublicationInfo(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def post(self):
        print("get_ieee_publication_info")
        try:
            link = request.json['link']
            driver = webdriver.Chrome()
            driver.get(link)
            time.sleep(5)

            for i in range(1, 5):
                driver.execute_script(f"window.scrollTo(0,{(i+1)*500})")
                time.sleep(3)

            try:
                keyword_id = driver.find_element(By.ID, 'keywords')
                keyword_id.click()
                time.sleep(5)
            except:
                time.sleep(5)

            try:
                all_data = driver.find_element(By.ID, 'xplMainContentLandmark')
                publication_data = extract_info(all_data.text, link)

            except:
                pass
            
            return jsonify(publication_data)
    
        except Exception as e:
            print({"message":"exception occured in get_ieee_publication_info"})
            print(e)
            return jsonify({"message":"exception occured in get_ieee_publication_info"})





       
