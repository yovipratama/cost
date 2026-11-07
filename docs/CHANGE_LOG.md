# Packaging changes (no scientific algorithm changes)

Original source notebooks were stripped of outputs and execution counts. Four **read-only, historical notebook source-inspection** cells pointing to unavailable notebook filenames were removed. No model, training, preprocessing, evaluation, or statistics cells were edited. Changes to Markdown headings remove editorial review wording only.

- `02_architecture_matched_gating_training.ipynb`: removed original cell index 8: Read-only audit of a historical, unavailable notebook.
- `02_architecture_matched_gating_training.ipynb`: removed original cell index 11: Read-only audit of a historical, unavailable notebook.
- `04_external_validation_eicu.ipynb`: removed original cell index 29: Read-only audit of a historical, unavailable notebook.
- `04_external_validation_eicu.ipynb`: removed original cell index 33: Read-only audit of a historical, unavailable notebook.

## Public-release cleanup (v2)

- Removed Colab cell metadata (`colab.base_uri`, `executionInfo` with account display name, account userId and execution timestamps) from notebooks 01, 02, 03, 04 and 06. Code-cell source is byte-identical to v1.
- Rewrote the title/description Markdown cells of notebooks 01 (cells 0, 52), 02 (cell 0), 03 (cells 0, 2, 10), 05 (cell 0) and 07 (cells 0, 21) to neutral, experiment-oriented wording in English. Development-stage names ("Revision I/II") and output folder names (`revision2_outputs`, `final_round_reviewer`, `reviewer2_targeted_completion`) remain inside code cells so saved artifacts stay traceable.
- Documentation now references manuscript `IEEE_ACCESS_FINAL_1043.docx` (previously `..._1018.docx`).
- `requirements.txt` completed from notebook imports and in-notebook installs (added imbalanced-learn, torchmetrics, joblib, requests, thop, fvcore; removed unused torchvision and statsmodels).
- `docs/SOURCE_CHECKSUMS.tsv` regenerated for the cleaned notebooks.
