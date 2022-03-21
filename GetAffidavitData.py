import base64
import json
import logging
import os
import time

import requests
from bs4 import BeautifulSoup
from lxml import html

BASE_URL = 'https://affidavit.eci.gov.in/CandidateCustomFilter?electionType={{season_code}}&election={{election_code}}&page={{page_num}}'
MIN_SEASON = 11

def write_json(new_data, filename):
    with open(filename, 'w') as file:
        json.dump(new_data, file, indent=4)


def getCandidatesInElection(season_code, election_code):
    logging.info("====getCandidatesInElection===" +
                 season_code + "====" + election_code)
    election_url = BASE_URL.replace('{{season_code}}', season_code).replace(
        '{{election_code}}', election_code)

    page = 1
    pages = 2
    affidavits = {}
    affidavits['list'] = []
    while (page < pages):
        url = election_url.replace('{{page_num}}', str(page))
        s = BeautifulSoup(requests.get(url).text, 'lxml')

        if page == 1:
            pagination = s.find('ul', attrs={'class': 'pagination'})
            if (pagination is not None):
                pages = int(pagination.find_all('li')[-2].text) + 1
                logging.info("===Total Pages====    " + str(pages))
            else:
                pages = 2
        logging.info("Page Number " + str(page))
        candidate_profiles = s.find(
            'table', attrs={'id': 'data-tab'}).find_all('tr')
        candidate_profiles.pop(0)

        for profile in candidate_profiles:
            affidavit = {}
            affidavit['name'] = profile.find('h4').text
            affidavit['link'] = profile.find(
                'div', attrs={'class': 'img-bx'}).find('a')['href']
            affidavit['photo'] = profile.find(
                'div', attrs={'class': 'img-bx'}).find('img')['src']
            affidavit_details = profile.find(
                'div', attrs={'class': 'details-name'}).find_all('p')
            affidavit['party'] = affidavit_details[0].text.split('Party :')[
                1].rstrip().lstrip()
            affidavit['status'] = affidavit_details[1].find('font').text
            affidavit['election_state'] = affidavit_details[2].text.split('State :')[
                1].rstrip().lstrip()
            affidavit['election_constituency'] = affidavit_details[3].text.split(
                'Constituency :')[1].rstrip().lstrip()
            affidavits['list'].append(affidavit)
        page = page + 1
    write_json(affidavits['list'], 'affidavits_all_' +
               season_code + '__' + election_code + '.json')


def getAffidavitLink(candidate):
    logging.debug("====getAffidavitLink===" + candidate['link'])
    s = BeautifulSoup(requests.get(candidate['link']).text, 'lxml')
    candidate['affidavit_upload_date'] = s.find(
        'div', attrs={'class': 'aside-af'}).find_all('span')[-1].text.strip()
    candidate['affidavit_download_count'] = s.find(
        'span', attrs={'id': 'updateCount'}).text
    candidate['nomination_file_date'] = s.find('div', attrs={'class': 'col-md-5 col-sm-6 mt-5 party'}).find_all(
        'div', attrs={'class': 'row'})[6].find_all('div', attrs={'class': 'col-sm-6'})[1].text.strip()
    candidate_bio = s.find('form', attrs={
                           'class': 'form-horizontal'}).find_all('div', attrs={'class': 'form-group'})
    candidate['father_husband_name'] = candidate_bio[0].find_all(
        'div', attrs={'class': 'col-sm-6'})[0].text.strip()
    candidate['address'] = candidate_bio[4].find_all(
        'div', attrs={'class': 'col-sm-6'})[0].text.strip()
    candidate['gender'] = candidate_bio[5].find_all(
        'div', attrs={'class': 'col-sm-6'})[0].text.strip()
    candidate['age'] = candidate_bio[6].find_all(
        'div', attrs={'class': 'col-sm-6'})[0].text.strip()
    try:
        candidate['affidavit_link'] = base64.b64decode(s.find(
            'div', attrs={'class': 'aside-af'}).find('input', attrs={'id': 'pdfUrl'})['value']).decode('utf-8')
    except:
        candidate['affidavit_link'] = 'NOT AVAILABLE'
        return candidate
    return candidate


def getCandidateProfiles():
    logging.debug("====getCandidateProfiles===")
    with open("elections.json") as json_file:
        data = json.load(json_file)
    for season in data:
        if int(season['season']) >= MIN_SEASON:
            for election in season['elections']:
                getCandidatesInElection(season['code'], election)
        else:
            logging.info("Skipping season " + season['season'] + " as it is below " + str(MIN_SEASON))


def getAffidavitDetails():
    logging.debug("====getAffidavitDetails===")
    json_folder_path = os.path.abspath(os.getcwd()) + '/data'
    json_files = [x for x in os.listdir(
        json_folder_path) if x.endswith("json")]

    affidavit_accepted_all = []
    for json_file in json_files:
        logging.info("Processing --- " + json_file)
        json_file_path = os.path.join(json_folder_path, json_file)
        with open(json_file_path, "r") as f:
            data = json.load(f)

        for candidate in data:
            if candidate['status'] != 'Accepted':
                continue
            try:
                candidate['election_code'] = json_files[1].split('__')[1][:-5]
                affidavit_accepted_all.append(getAffidavitLink(candidate))
            except:
                logging.info("Other Exception getting AffidavitLink for candidate " +
                             candidate['name'] + " using link " + candidate['link'])
                pass
    write_json(affidavit_accepted_all, 'affidavits_accepted_all.json')


def main():
    logging.basicConfig(filename='AffadavitExtractor' + time.strftime("%Y%m%d-%H%M%S") +
                        '.log', format='%(asctime)s %(message)s', level=logging.INFO)
    getCandidateProfiles()
    getAffidavitDetails()


if __name__ == "__main__":
    main()
