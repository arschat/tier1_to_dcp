"""
Dictionary with keys Tier 1 fields, and values, the corresponding DCP fields
"""

tier1_to_dcp = {
    'title': 'project.project_core.project_title',
    'study_pi': 'project.contributors.name',
    # batch_condition
    # default_embedding
    # comments
    'sample_id': 'specimen_from_organism.biomaterial_core.biomaterial_id',
    'donor_id': 'donor_organism.biomaterial_core.biomaterial_id',
    'protocol_url': 'library_preparation_protocol.protocol_core.protocols_io_doi',
    # 'institute': 'project.contributors.institute',
    # 'sample_collection_site': 'sample_collection_site',
    # 'sample_collection_relative_time_point': 'specimen_from_organism.biomaterial_core.timecourse.value', 
    'library_id': 'cell_suspension.biomaterial_core.biomaterial_id',
    'library_id_repository': 'cell_suspension.biomaterial_core.biomaterial_name',
    # 'author_batch_notes': 'cell_suspension.biomaterial_core.biomaterial_description',
    'organism_ontology_term_id': 'donor_organism.biomaterial_core.ncbi_taxon_id', 
    'manner_of_death': 'donor_organism.death.hardy_scale', 
    # 'sample_source': 'donor_organism.is_living', 
    'sex_ontology_term_id': 'donor_organism.sex', 
    'sample_collection_method': 'collection_protocol.method.text', 
    # tissue_type
    # 'sampled_site_condition': 'specimen_from_organism.diseases.text', # if is healthy PATO, if adjacent PATO & adjacent disease_ontology_term_id, else disease_ontology_term_id
    'tissue_ontology_term_id': 'specimen_from_organism.organ.ontology',
    'tissue_free_text': 'specimen_from_organism.organ_parts.text',
    'sample_preservation_method': 'specimen_from_organism.preservation_storage.storage_method',
    'suspension_type': 'library_preparation_protocol.nucleic_acid_source',
    'cell_enrichment': 'enrichment_protocol.markers', # if CL ontology add CL label
    'cell_viability_percentage': 'cell_suspension.cell_morphology.percent_cell_viability',
    'cell_number_loaded': 'cell_suspension.estimated_cell_count',
    'sample_collection_year': 'specimen_from_organism.collection_time',
    'assay_ontology_term_id': 'library_preparation_protocol.library_construction_method.ontology', 
    'library_preparation_batch': 'sequence_file.library_prep_id',
    # 'library_sequencing_run': 'library_sequencing_run',
    'library_sequencing_run': 'sequence_file.insdc_run_accessions',
    'sequenced_fragment': 'library_preparation_protocol.end_bias',
    'sequencing_platform': 'sequencing_protocol.instrument_manufacturer_model.ontology',
    # is_primary_data
    'reference_genome': 'analysis_file.genome_assembly_version',
    'gene_annotation_version': 'analysis_protocol.gene_annotation_version',
    # 'alignment_software': 'analysis_protocol.alignment_software', 
    'intron_inclusion': 'analysis_protocol.intron_inclusion',
    # author_cell_type
    # cell_type_ontology_term_id
    'disease_ontology_term_id': 'donor_organism.diseases.ontology',
    'self_reported_ethnicity_ontology_term_id': 'donor_organism.human_specific.ethnicity.ontology',
    'development_stage_ontology_term_id': 'donor_organism.organism_age'
    # # More from author metadata of the example
    # 'library': "cell_suspension.biomaterial_core.biomaterial_id",
    # 'organism': "donor_organism.genus_species.text",
    # 'development_stage': "donor_organism.development_stage.text",
    # 'self_reported_ethnicity': "donor_organism.human_specific.ethnicity.text",
    # 'disease': "donor_organism.diseases.text",
    # 'tissue': "specimen_from_organism.organ.text",
    # # 'assay': "library_preparation_protocol.library_construction_method.text",
    # 'BMI': "donor_organism.human_specific.body_mass_index",
    # 'condition.l1': 'condition.l1',
    # 'condition.l2': 'condition.l2',
    # 'condition.long': 'condition.long',
    # 'diabetes_history': "donor_organism.diseases.text",
    # 'eGFR': "donor_organism.medical_history.test_results",
    # 'experiment': "experiment",
    # 'hypertension': "donor_organism.diseases.text",
    # 'id': "id",
    # 'region.l1': 'region.l1',
    # 'region.l2': 'region.l2',
    # 'specimen': "specimen_from_organism.biomaterial_core.biomaterial_id",
    # 'percent.cortex': 'percent.cortex',
    # 'percent.medulla': 'percent.medulla'
}
"""
Dictionary with fields that could potentially generate a meaninigful protocol name like i.e. 10x_3_v2_protocol, biopsy_protocol etc.
"""
protocol_ids = {
    "sample_collection_method": "collection_protocol.protocol_core.protocol_id",
    "assay": "library_preparation_protocol.protocol_core.protocol_id",
    "sequencing_platform": "sequencing_protocol.protocol_core.protocol_id",
    "alignment_software": "analysis_protocol.protocol_core.protocol_id"
}