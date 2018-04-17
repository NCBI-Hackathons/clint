# CLINT (CLInical Neurosynth Translator)
Linking clinical questions with fMRI research literature

[Neurosynth](http://neurosynth.org/) is a database of functional neuroimaging results linking function with brain locations from over 11,000 published fMRI studies. 

# Aim 1
Clinical radiology reports indicate the structures involved in any clinical finding, but might not make it clear what those structures do. We'll parse those reports and grab related regions from neurosynth and return a report in an EHR ingestible format. 

# Aim 2
Similarly, sometime it takes a long time to get a patient into the scanner, if you know what symptoms a patient has, we can try to guess which region of the brain is involved, and return those results in an EHR ingestible format.

# Aim 3
Go directly from an image to other image databases and find the most similar scans (definition TBD) and their metadata.

In a perfect world here's hour CLINT might work:

![CLINT Workflow](docs/clint_workflow.png)


TODO:  
~~1. Get a better name~~ (Unless someones thinks of something better still)  
~~2. Find Data~~  
  * [Synthetic Public Use File from OHDSI parsed with their ETL-CMS tool](https://github.com/OHDSI/ETL-CMS)  
3. Parse reports  
  * In progress. We've got [Snowmed](http://bioportal.bioontology.org/ontologies/SNOMEDCT) condition codes that we'll link with neurosynth keywords.  
4. Query Neurosynth  
  * In progress. We understand the detailed workflows for our interactions with neurosynth, implementing these workflows now.  
5. Aggregate Neurosynth reports  
6. Create FHIR JSON
7. Containerize endpoint and drop it on an AWS box
