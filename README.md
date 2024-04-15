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

## TODO
- [dcp_metadata_import.ipynb](dcp_metadata_import.ipynb)
    - `sample_collection_relative_time_point`: `specimen_from_organism.biomaterial_core.timecourse.value`, add timecourse relevance
    - `organism_ontology_term_id`: `donor_organism.biomaterial_core.ncbi_taxon_id`, keep only the numeric part of NCBI taxon ID
    - `manner_of_death`: `donor_organism.death.hardy_scale`, # add donor_organism.is_living field
    - `sample_source`: `donor_organism.is_living`, # add specimen_from_organism.transplant_organ field
    - `sex_ontology_term_id`: `donor_organism.sex`, # remap from ontology to male/female/other
    - `sample_collection_method`: `collection_protocol.method.ontology_label`, # add collection_id
    - `sampled_site_condition`: `specimen_from_organism.diseases.text`, # if is healthy PATO, if adjacent PATO & adjacent disease_ontology_term_id, else disease_ontology_term_id
    - `cell_enrichment`: `enrichment_protocol.markers`, # if CL ontology add CL label
    - `assay_ontology_term_id`: `library_preparation_protocol.library_construction_method.ontology`, # add_library_id
    - `alignment_software`: `analysis_protocol.alignment_software`, # split to version
    - `development_stage_ontology_term_id`: `donor_organism.organism_age` # remap ontology to age range or specific number