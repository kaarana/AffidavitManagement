# Indian Elections Affidavit Archival System

[![Generic badge](https://img.shields.io/badge/View_Data_on-Flat_Github-GREEN.svg)](https://flatgithub.com/kaarana/AffidavitManagement?filename=data%2Faffidavits_accepted_all.json)
[![Generic badge](https://img.shields.io/badge/Archived_Affidavits-Internet_Archive-GREEN.svg)](https://web.archive.org/web/*/suvidha.eci.gov.in/*)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Project ElectionTech - Kaarana
[![Generic badge](https://img.shields.io/badge/Project-ElectionTech-lightgrey.svg)](https://hasgeek.com/kaarana/electiontech/)
[![YouTube](https://img.shields.io/badge/ElectionTech-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/playlist?list=PLnKey4ddtgY5X2EZjAH9Law_Pa8s5UEIB)
[![Medium](https://img.shields.io/badge/Medium-Kaarana-black)](https://medium.com/karana)
[![Telegram](https://img.shields.io/badge/Telegram-Kaarana-blue)](https://t.me/Kaarana)
[![Twitter Follow](https://img.shields.io/twitter/follow/kaarana_?style=social)](https://twitter.com/kaarana_)


[Election Commission of India](https://eci.gov.in/) runs a Candidate & Counting Management System - [*Suvidha*](https://suvidha.eci.gov.in/) to manage candidate nominations and affidavits
for all legislative assembly and parliamentary elections conducted in India since 2019. As part of it, they publish candidate affidavit details publicly at https://affidavit.eci.gov.in/ linking the nomination / affidavits filed at Suvidha.

This project has collected metadata of 46850 affidavits of accepted nominations that have been filed for 18 elections since 2019, when Suvidha was put in place and archived them on [Internet Archive](https://web.archive.org) .

## Links

### Suvidha
* [ECI Guideline](https://cdn.s3waas.gov.in/s302e74f10e0327ad868d138f2b4fdd6f0/uploads/2020/10/2020100216.pdf) - [Archive](https://web.archive.org/web/20210812090602/https://cdn.s3waas.gov.in/s302e74f10e0327ad868d138f2b4fdd6f0/uploads/2020/10/2020100216.pdf)
* [Suvidha Manual](https://cdn.s3waas.gov.in/s30ff8033cf9437c213ee13937b1c4c455/uploads/2020/10/2020101935.pdf) - [Archive](https://web.archive.org/web/20210811210321/https://cdn.s3waas.gov.in/s30ff8033cf9437c213ee13937b1c4c455/uploads/2020/10/2020101935.pdf) 
* [Suvidha Candidate Android App](https://play.google.com/store/apps/details?id=suvidha.eci.gov.in.candidateapp)

### ENCORE Permissions Platform
* [ENCORE](https://encore.eci.gov.in) 
* [Overview](https://eci.gov.in/img/2020/Election%20Permission%20Application.pdf) - [Archive](https://web.archive.org/web/20210812091919/https://eci.gov.in/img/2020/Election%20Permission%20Application.pdf) - [Presentation](https://charaideo.gov.in/sites/default/files/swf_utility_folder/departments/charaideo_epr_amtron_in_oid_2/portlet/level_2/encore_permission.pdf) - [Archive](https://web.archive.org/web/20210812091349/https://charaideo.gov.in/sites/default/files/swf_utility_folder/departments/charaideo_epr_amtron_in_oid_2/portlet/level_2/encore_permission.pdf)
* [ENCORE Manual](https://cdn.s3waas.gov.in/s3e2ef524fbf3d9fe611d5a8e90fefdc9c/uploads/2021/02/2021022651.pdf) - [Archive](https://web.archive.org/web/20210812091423/https://cdn.s3waas.gov.in/s3e2ef524fbf3d9fe611d5a8e90fefdc9c/uploads/2021/02/2021022651.pdf)

* [Affidavit Archive](http://affidavitarchive.nic.in/) - For elections prior to 2019. This is broken, but still contains affidavits from elections dating back to 2004.

## Notes on data

* elections.json - Contains a list of elections with election codes grouped by election season to fetch candidate profiles from https://affidavit.eci.gov.in/
* affidavits_all/ - Contains nominations data for all elections from https://affidavit.eci.gov.in/
* affidavits_accepted_all.json - Contains detailed candidate profile with link to eSuvidha affidavits for all accepted nominations across all 18 elections from 2019-2021.
* affidavit_urls.txt - List of affidavit URLs to process Archiving Job using [Wayback-GSheets batch tool](https://archive.org/services/wayback-gsheets/)

## Disclaimer

Election affidavits are public domain documents. Data archived is based on what is available in Suvidha, source system and we do not offer any guarentees on data quality.
