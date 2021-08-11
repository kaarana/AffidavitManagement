# Indian Elections Affidavit Archival System

Election Commission of India runs a Candidate & Counting Management System - [*eSuvidha*](https://suvidha.eci.gov.in/) to manage candidate nominations and affidavits
for all legislative assembly and parliamentary elections conducted in India since 2019. As part of it, they publish candidate affidavit details publicly at https://affidavit.eci.gov.in/ linking the nomination / affidavits filed at eSuvidha.


# Notes on data

* elections.json - Contains a list of elections with election codes grouped by election season to fetch candidate profiles from https://affidavit.eci.gov.in/
* affidavits_all/ - Contains nominations data for all elections from https://affidavit.eci.gov.in/
* affidavits_accepted_all.json - Contains detailed candidate profile with link to eSuvidha affidavits for all accepted nominations across all 18 elections from 2019-2021.
* affidavit_urls.txt - List of affidavit URLs to process Archiving Job using [Wayback-GSheets batch tool](https://archive.org/services/wayback-gsheets/)

