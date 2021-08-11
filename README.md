# Indian Elections Affidavit Archival System

[![Generic badge](https://img.shields.io/badge/View_Data_on-Flat_Github-GREEN.svg)](https://flatgithub.com/kaarana/AffidavitManagement?filename=data%2Faffidavits_accepted_all.json)
[![Generic badge](https://img.shields.io/badge/Archived_Affidavits-Internet_Archive-GREEN.svg)](https://web.archive.org/web/*/suvidha.eci.gov.in/*)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


[![Generic badge](https://img.shields.io/badge/Project-ElectionTech-lightgrey.svg)](https://hasgeek.com/kaarana/electiontech/)
[![Twitter Follow](https://img.shields.io/twitter/follow/kaarana_?style=social)](https://twitter.com/kaarana_)
[![YouTube](https://img.shields.io/badge/ElectionTech-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/playlist?list=PLnKey4ddtgY5X2EZjAH9Law_Pa8s5UEIB)


[Election Commission of India](https://eci.gov.in/) runs a Candidate & Counting Management System - [*Suvidha*](https://suvidha.eci.gov.in/) to manage candidate nominations and affidavits
for all legislative assembly and parliamentary elections conducted in India since 2019. As part of it, they publish candidate affidavit details publicly at https://affidavit.eci.gov.in/ linking the nomination / affidavits filed at Suvidha.

This project has collected metadata of 46850 affidavits of accepted nominations that have been filed for 18 elections since 2019, when Suvidha was put in place and archived them on [Internet Archive](https://web.archive.org) .

# Links
* [Suvidha Manual](https://cdn.s3waas.gov.in/s30ff8033cf9437c213ee13937b1c4c455/uploads/2020/10/2020101935.pdf) - [Archive](https://web.archive.org/web/20210811210321/https://cdn.s3waas.gov.in/s30ff8033cf9437c213ee13937b1c4c455/uploads/2020/10/2020101935.pdf)
* [Affidavit Archive](http://affidavitarchive.nic.in/) - For elections prior to 2019. This is broken, but still contains affidavits from elections dating back to 2004.

## Notes on data

* elections.json - Contains a list of elections with election codes grouped by election season to fetch candidate profiles from https://affidavit.eci.gov.in/
* affidavits_all/ - Contains nominations data for all elections from https://affidavit.eci.gov.in/
* affidavits_accepted_all.json - Contains detailed candidate profile with link to eSuvidha affidavits for all accepted nominations across all 18 elections from 2019-2021.
* affidavit_urls.txt - List of affidavit URLs to process Archiving Job using [Wayback-GSheets batch tool](https://archive.org/services/wayback-gsheets/)

## Disclaimer

Election affidavits are public domain documents. Data archived is based on what is available in Suvidha, source system and we do not offer any guarentees on data quality.
