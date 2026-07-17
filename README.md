# data-science-coursework

This repository contains recovered, publish-eligible coursework notebooks associated with CMSC 320 / data-science coursework. The repository preserves the recovered notebook artifacts and their file-level provenance. It does not claim that every notebook is currently reproducible, executable, or complete without further review.

## Contents

| Project | Location | Description | Validation status |
| --- | --- | --- | --- |
| Regression, gradient descent, and neural networks | `projects/cmsc320-regressiongradientdescentneuralnetworks-119271452-albeladi/` | A notebook project whose recovered filename identifies regression, gradient descent, and neural-network topics. | Notebook presence is known from the recovered file list. Execution and output validity have not been established. |
| CMSC 320 final notebook | `projects/320finalipynb/` | A recovered notebook identified as a CMSC 320 final-project artifact. The available filename does not establish its research question, data source, or results. | Notebook presence is known from the recovered file list. Execution and output validity have not been established. |
| Classifiers notebook | `projects/copy-of-cmsc320-homework04-classifiers/` | A recovered classifier-focused coursework notebook. The `copy-of` filename is retained as provenance and does not establish authorship beyond the recovered artifact. | Notebook presence is known from the recovered file list. Execution and output validity have not been established. |

## Repository layout

```text
.
├── docs/
│   └── notebook-lineage.md
└── projects/
    ├── 320finalipynb/
    │   └── notebooks/
    │       └── 320finalipynb.ipynb
    ├── cmsc320-regressiongradientdescentneuralnetworks-119271452-albeladi/
    │   └── notebooks/
    │       └── cmsc320-regressiongradientdescentneuralnetworks-119271452-albeladi.ipynb
    └── copy-of-cmsc320-homework04-classifiers/
        └── notebooks/
            └── copy-of-cmsc320-homework04-classifiers.ipynb
```

## Setup

The recovered file list contains Jupyter notebooks but does not identify a dependency lockfile, package manifest, or supported Python version. Start with an isolated Python environment and install Jupyter support:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel
jupyter lab
```

Open a notebook from its `notebooks/` directory in JupyterLab. Install additional libraries only after inspecting that notebook's imports. Dependency versions should be recorded in a project-specific environment file if execution work is later performed.

## Validation status

No successful test run, notebook execution, dataset availability check, or result reproduction is established by the supplied repository inventory. The notebooks should therefore be treated as recovered source artifacts rather than verified runnable projects.

Safe structural checks can confirm that the notebook files remain valid JSON. Executing notebooks is a separate step that may require packages, local files, credentials, network access, or environment-specific configuration not represented in the recovered file list.

## Data and private-data requirements

The supplied inventory does not identify the datasets, credentials, local paths, or external services used by any notebook. Before publishing executable examples or running cells:

1. Inspect notebook markdown, code cells, and `docs/notebook-lineage.md` for data references.
2. Do not commit private datasets, access tokens, passwords, or institution-specific paths.
3. Replace hard-coded local paths with configuration, documented environment variables, or repository-relative paths where supported by the original code.
4. If a notebook requires non-public data, document the requirement and provide only a schema, configuration template, or synthetic example when appropriate.
5. Do not represent unavailable data-dependent outputs as reproducible.

## Limitations

- The project descriptions are based on recovered directory and notebook filenames, not a completed notebook-content audit.
- No dependency specification is identified in the supplied file list.
- No dataset inventory, license information, or data-use permissions are established from the supplied file list.
- The final-project notebook's topic and conclusions are not established by its filename.
- The classifier notebook's `copy-of` naming is preserved because it is part of the recovered provenance; it should not be treated as an independent attribution statement.
- Notebook outputs may be stale, absent, dependent on unavailable data, or generated in an environment that cannot yet be reconstructed.

## Provenance

These materials were recovered from university/coursework files and organized as separate subprojects in this portfolio repository. Original recovered names have been retained in paths where practical to preserve traceability:

- `cmsc320-regressiongradientdescentneuralnetworks-119271452-albeladi.ipynb`
- `320finalipynb.ipynb`
- `copy-of-cmsc320-homework04-classifiers.ipynb`

`docs/notebook-lineage.md` is the repository location for notebook-lineage documentation. It should be consulted and updated when notebook origins, transformations, source data, or execution requirements are verified.

## Recommended review workflow

1. Validate notebook JSON without changing files.
2. Review each notebook for imports, data paths, embedded credentials, assignment-specific text, and external dependencies.
3. Record required packages and supported interpreter versions.
4. Identify whether each notebook needs private or licensed data.
5. Execute only after dependencies and data access are documented.
6. Add concise project-level documentation describing confirmed inputs, methods, and limitations without claiming unverified results.

<!-- portfolio-public-release-license:start -->

## License and public-release status

This repository is published under an all-rights-reserved
portfolio license. Viewing the repository does not grant permission to reuse its code,
documentation, datasets, or assets. Third-party and collaborator materials retain
their original rights.

Before changing visibility from private to public, the owner must complete the
ownership checklist in `LICENSE_REVIEW.md`.

<!-- portfolio-public-release-license:end -->

<!-- release-license:start -->

## License and public-release status

This repository uses an all-rights-reserved portfolio license. Review `LICENSE_REVIEW.md` and `THIRD_PARTY_NOTICES.md` before changing visibility to public.

<!-- release-license:end -->
