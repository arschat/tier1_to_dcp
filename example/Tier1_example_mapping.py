rename_cols = {
    "library": "library_id",
    "experiment": "library_id_repository",
    "specimen": "sample_id",
    "donor_id": "donor_id",
    "region.l1": "tissue_free_text",
    "sample_tissue_type": "sample_collection_method",
    "disease_ontology_term_id": "disease_ontology_term_id",
    "sex_ontology_term_id": "sex_ontology_term_id",
    "development_stage_ontology_term_id": "development_stage_ontology_term_id",
    "self_reported_ethnicity_ontology_term_id": "self_reported_ethnicity_ontology_term_id",
    "BMI": "BMI",
    "diabetes_history": "diabetes_history",
    "hypertension": "hypertension",
    "tissue_ontology_term_id": "tissue_ontology_term_id",
    "organism_ontology_term_id": "organism_ontology_term_id",
    "assay_ontology_term_id": "assay_ontology_term_id",
    "assay": "assay",
    "cell_type_ontology_term_id": "cell_type_ontology_term_id",
    "is_primary_data": "is_primary_data",
    "suspension_type": "suspension_type",
    "tissue_type": "tissue_type"
}
replace_values = {
    "sample_source":
    {
        "Biopsy": "surgical donor",
        "Deceased Donor": "postmortem donor",
        "Nephrectomy": "surgical donor"
    },
    "sample_collection_method":
    {
    	"Biopsy": "biopsy",
    	"Deceased Donor": "surgical recesion",
    	"Nephrectomy": "surgical recesion"
    },
    "sampled_site_condition":{
    	"MONDO:0005300": "diseased",
    	"MONDO:0002492": "diseased",
    	"PATO:0000461": "healthy"
    },
    "sample_preservation_method": {
    	"Biopsy": "fresh",
    	"Deceased Donor": "frozen at -70C",
    	"Nephrectomy": "frozen in liquid nitrogen"
    }
}
uniform_values = {
    "title": "An atlas of healthy and injured cell states and niches in the human kidney",
    "study_pi": "Sanjay,,Jain",
    "default_embedding": "umap",
    "protocol_url": "10.17504/protocols.io.b3gxqjxn",
    "institute": "University of California",
    "sample_collection_site": "Kidney Translational Research Center",
    "cell_viability_percentage": "20",
    "cell_number_loaded": "5000",
    "sample_collection_year": "2017",
    "sequenced_fragment": "3 prime",
    "sequencing_platform": "OBI:0002630",
    "reference_genome": "GRCh38",
    "gene_annotation_version": "v110",
    "alignment_software": "Cellranger v3.0.0",
    "intron_inclusion": "no"
}