# borme
Series of files and scripts to import to ElasticSearch (and visualize in Kibana) using Logstash information about companies and people in company, as in Spanish General Cadaster (Registro General del Catastro) for 09.09.2019.

Folders:
- _CSV_: All csv files, compressed to ZIP
- - _clean_: Final files to directly import to ElasticSearch using Logstash
CSV and logstash files to import to ELK
- - _raw_: Direct dump to csv from libreBorme
- _logstash_: .config files to execute and import into ElasticSearch the csv files.
- _elasticsearch_: .py files to initialize indexes in ElasticSearch using python

