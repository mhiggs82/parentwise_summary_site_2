---
description: Deploy new book summaries and verify site quality
---

Follow these steps to deploy new books to the ParentWise site and ensure they meet quality standards.

1.  **Batching Rule**: Always process books in batches of **maximum 5**. Do not exceed this limit to ensure high extraction quality and prevent context rot.

2.  **Standardize JSON Data** (Optional but recommended if formatting changed)
    // turbo
    `python3 execution/standardize_json.py`

3.  **Generate MDX and Sync Data**
    // turbo
    `python3 execution/json_to_mdx.py`

4.  **Run Quality Control**
    // turbo
    `python3 execution/qc_output.py`

5.  **Confirm Results**
    If the QC script returns "✅ All checks passed!", proceed to the next step.
    If issues are found, fix them in the source JSON files and repeat steps 2-4.

6.  **Update Progress**
    Update `execution/PROGRESS.md` with the new completion counts.

7.  **Reset Context**
    Notify the user that the batch is complete and request to **clear the context window/start a new turn** before beginning the next batch of 5.
