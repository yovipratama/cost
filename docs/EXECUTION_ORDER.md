# Execution order and artifact dependencies

1. Run `01_cohort_baselines_and_initial_cost.ipynb` after obtaining authorized MIMIC-IV access and configuring the private input and cache paths. Baselines, Initial COST, feature analysis, and threshold sweep are separate subsections; the threshold sweep is **not** the five-run primary performance table.
2. Run `02_cost_improved_training_and_ablation.ipynb` after the data cache from step 1 is available. It reuses the original Improved preprocessing and runs 3 seeds. Review local paths and checkpoint naming.
3. Run `03_gating_on_off_control.ipynb` for the matched control. **The source contains safety flags** that may default to only seed 42; running only the default cell does not reproduce all three seeds. Activate the prespecified 42–44 protocol when intended.
4. Run `04_trained_random_mask_control.ipynb` to train the random sparse comparator under the matched protocol. It requires the authorized test cache and previously stored learned-gating predictions for comparison.
5. Run `05_temporal_calibration_and_interventions.ipynb` on the required saved checkpoints, test predictions and cohort metadata. Sections requiring patient identifiers must be run in an authorized environment.
6. Run `06_external_eicu_validation.ipynb` using authorized eICU access, harmonization, and a frozen fitted MIMIC checkpoint. **Do not fine-tune on eICU**.
7. Run `07_paired_statistical_tests.ipynb` with the matching paired patient-level predictions of learned gating and trained random mask. The mean bootstrap CI/p-value is conditional on the three fitted seed models.
8. Optional **post-training** inference helper: `08_saved_checkpoint_prediction_reconstruction.ipynb` regenerates main single-model and snapshot ensemble predictions; it does not create or train a checkpoint.

### Missing files / paths

Some notebook cells use original Colab or Google Drive paths for private `.npz` caches, checkpoints, or saved predictions. Those are deliberate local dependencies, not public assets. Update the path setup to your own authorized environment; do not push data or credentials to GitHub.

No end-to-end numerical equivalence is claimed until the notebooks are tested against the original authorized data and checkpoints.
