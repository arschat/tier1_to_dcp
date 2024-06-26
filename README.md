# CxG / Tier 1 to DCP spreadsheet

This is a project to convert the Human Cell Atlas Tier 1 metadata fields from a published CELLxGENE dataset, to the 'HCA DCP metadata schema' based, ingestible [spreadsheet](https://github.com/ebi-ait/geo_to_hca/tree/master/template).

## Usage 
To convert there are two notebooks
* [cellxgene_metadata_export.ipynb](cellxgene_metadata_export.ipynb) to download using the CELLxGENE API and export to a csv file
* [dcp_metadata_import.ipynb](dcp_metadata_import.ipynb) to create a list of dataframes (based on the mapping of fields specified on [tier1_to_dcp_dict.py](tier1_to_dcp_dict.py)) and export as an excel spreadsheet with the HCA style.

Please specify the `collection_id` and the `dataset_id` in the corresponding fields both notebooks. Everything else should be automated.

## Requirements

The packages needed for these notebooks are listed in the [requirements.txt](requirements.txt) file. To install via pip use:
```bash
pip install -r requirements.txt
```

## Known limitations
Sequence file tab is filled only with run ID & library ID (since we don't have file_names of fastq files)

## TODO
