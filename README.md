# COST — Controlled Sparsity for Reliable Clinical Time-Series Modeling

**Research code corresponding to:** *COST: Controlled Sparsity for Reliable Clinical Time-Series Modeling: A Trade-off Analysis in ICU Mortality Prediction* (IEEE Access, accepted manuscript).

This repository is organized according to the **paper's Methods and experimental Results**, not the journal revision history. Its scope is restricted to the reported experiments. **Initial COST**, although it performs poorly, is intentionally included because its failure and sparsity diagnosis are central reported findings. Earlier unused trials are excluded.

## Notebook order and reported experiment coverage

| Notebook | Manuscript experiment |
|---|---|
| `01_cohort_baselines_and_initial_cost.ipynb` | Cohort, LR/RF/LSTM/Attention LSTM/TCN baselines, Initial COST, initial ablation, efficiency, gradient attribution, feature retention and Table XX threshold sweep |
| `02_cost_improved_training_and_ablation.ipynb` | Improved COST, training, multi-seed snapshot ensemble, model and optimization ablations |
| `03_gating_on_off_control.ipynb` | Architecture-matched gating ON/OFF and binary-mask sparsity |
| `04_trained_random_mask_control.ipynb` | Independently trained random-mask comparator |
| `05_temporal_calibration_and_interventions.ipynb` | 48-hour mortality sensitivity, calibration, frozen checkpoint gate interventions, ON/OFF statistics |
| `06_external_eicu_validation.ipynb` | Frozen MIMIC-trained model evaluated on eICU, descriptive external calibration |
| `07_paired_statistical_tests.ipynb` | Paired DeLong and patient-level stratified bootstrap for learned vs trained random-mask |
| `08_saved_checkpoint_prediction_reconstruction.ipynb` | Recover single-model and five-snapshot test predictions from saved original checkpoints |

Notebooks 03–07 may depend on **outputs from preceding experiments** and/or original saved checkpoints. The presence of code does not imply automatic reproduction of numerical results from a clean environment. See `docs/EXECUTION_ORDER.md` and `docs/PAPER_CODE_AUDIT.md`.

## Data access and privacy

MIMIC-IV v2.1 and eICU-CRD are controlled-access clinical databases. They are **not redistributed** here. Users must independently obtain appropriate access and comply with PhysioNet credentialing, training and data-use requirements:

- MIMIC-IV v2.1: https://physionet.org/content/mimiciv/2.1/
- eICU-CRD v2.0: https://physionet.org/content/eicu-crd/2.0/

No individual patient records, cached arrays, passwords, saved test predictions or model checkpoints are included in this release. Users must configure their authorized storage locations in the notebook setup cells.

## Environment

The experiments were developed in Python/PyTorch on Google Colab with NVIDIA A100 GPU, as described in the paper. Install the Python packages from `requirements.txt`; for Colab, follow each notebook's setup cell. Checkpoint and full-dataset validation are not possible without authorized data and the original saved weights.

## Methodology and reproducibility notes

- The source is derived from supplied research notebooks. It includes notebook-based implementations rather than a newly written and untested library.
- `config/paper_protocol.yaml` records the manuscript's parameters **for reference**; it does not override notebook variables.
- `docs/SOURCE_PROVENANCE.tsv` records which historical code was selected and the research reason.
- `docs/PAPER_CODE_AUDIT.md` flags implementation–description differences that must not be misrepresented as verified equality.
- Static code compilation is not the same as successful data-dependent end-to-end execution. No output numbers are fabricated.

## Citation

Please cite the COST paper when using this code (final IEEE Xplore bibliographic information to be added once available), together with the MIMIC-IV and eICU-CRD dataset citations listed in `docs/DATA_ACCESS.md`. Repository: https://github.com/yovipratama/cost — see `docs/CODE_AVAILABILITY.md`.

## License

The source notebooks and documentation are released under the MIT License (see `LICENSE`). The license covers this repository only; MIMIC-IV and eICU-CRD remain governed by their PhysioNet credentialed data use agreements and are not redistributed. Dependencies retain their own terms.
