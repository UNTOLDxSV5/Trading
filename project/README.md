# Comment Classifier Project

This project provides a pipeline for clustering, labeling, and managing user comments using NLP techniques.

## Scripts
- `dataset_addition.py`:Adds new excel data to trainable file(data).
- `initial_build.py`: Builds the base model and clusters.
- `check_existing_data.py`: Converts comment hierarchy to Excel table.
- `excel_to_csv_converter.py`: Converts `.xlsx` to `.csv`.
- `daily_usage_classifier.py`: Classifies new comments using the existing model.


## For detalied information refer the documentation in the below link:
- https://www.notion.so/Documentation-1f5f1e5e47e9809bb8b0d35e8746db9f?pvs=4

# Downgrade 
- pip install "sentence-transformers==2.2.2" "huggingface-hub==0.16.4"

# This tells Python to treat src as a package relative to the current directory.
- python -m src.run_production_model
