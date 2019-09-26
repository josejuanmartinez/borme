# borme
Series of files and scripts to import to ElasticSearch (and visualize in Kibana) using Logstash information about companies and people in company, as in Spanish General Cadaster (Registro General del Catastro) for 09.09.2019.

Kibana PRO (paid version) is highly recommended to use the GRAPH functionality, that looks as nice as this:

![borme example](https://drive.google.com/uc?export=view&id=1JKWH4XQSsrnv6u_lYpJ53im0GsZesfY0 "borme example")



Folders:
- _CSV_: All csv files, compressed to ZIP
- - _clean_: Final files to directly import to ElasticSearch using Logstash
CSV and logstash files to import to ELK
- - _raw_: Direct dump to csv from libreBorme
- _logstash_: .config files to execute and import into ElasticSearch the csv files.
- _elasticsearch_: .py files to initialize indexes in ElasticSearch using python

