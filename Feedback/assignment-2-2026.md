# Assignment 2 formative feedback

This feedback is organised by the relevant computing bootcamp criteria. Use it to decide what is already working, what you need to investigate, and what to revise before the cumulative submission.

The full criteria are in the [Computing Bootcamp assessment rubric](https://github.com/MulQuaBio/MQB/blob/main/content/rubrics/Computing_Bootcamp_Rubric.md).

## 1. Repository organisation and workflow discipline

- Your root README, `.gitignore`, cleaning script, test script and supplied data files are in the expected locations. The supplied CSV and metadata are unchanged, giving you a reproducible starting point.

## 2. Code completeness and functional correctness

- The cleaning workflow ran successfully. Separately, output checks found that all three output tables satisfied the requirements on both test runs. The outputs are correct for the checked input; now make sure you can explain the method and test important edge cases.
- Run the separate tests and cleaning script after any revision, then recheck the three generated tables.

## 3. Code quality and style

- Your `main()` function gives the program a clear overall structure by connecting loading, processing, summarising and writing. Keep these stages distinct as you revise; use descriptive names and add short comments where the reason for a validation check or data-cleaning step is not obvious.

## 4. Documentation

- Your root README is in place. Make it useful to someone opening the repository for the first time: explain what the cleaner does, how to run the script and tests from the repository root, and which three files it creates. Test the instructions in a newly cloned copy of your repository (a separate folder created with `git clone`): enter that folder and run each README command exactly as written. If something fails, correct the command or add the missing step.

## 5. Version-control practice

- Since the previous formative feedback was added, the saved history contains 14 non-merge commits. Messages such as `Implement tree-record validation`, `tests for clean_silwood_trees`, and `update to ignore generated results but keep the directory` make the development sequence easy to follow.
- Keep this pattern for the final revisions. Before each commit, use `git diff --staged` to check that it contains one coherent, working change, then write a concise message that names that change and, where it is not obvious, why it was needed.

## 8. Basic error handling and input validation

- Your separate test file is present and ran successfully. Your test file includes assertion-style checks for record validation, the accepted/rejected partition and the oak summary. The required assessed paths are present, and both supplied data files remain unchanged.
- **Make test coverage easy to inspect.** Your tests currently use top-level assertions rather than named test functions; this is not itself a functional defect. Successful execution also does not show that every important case is covered. Label or group the existing checks by behaviour, then compare them with the released validation rules. Add a focused boundary or invalid-input case wherever a rule is not yet represented, checking the returned result rather than merely that execution finishes.

## 9. Problem-solving approach and method implementation

- Your program follows this route: `main()` loads the unchanged supplied CSV through `load_records()`, then passes the rows to `process_records()`, which calls `validate_record()` and returns `(sorted_records, error_log)`. The cleaned collection feeds `summarise_oaks()`, and three `write_csv()` calls produce the outputs. The route from input to outputs is clear.
- Before final submission, make this check visible in your repository. In `code/test_silwood_trees.py`, add or refine a small assertion-based test with one valid and one invalid record. Check that `process_records()` places them in the cleaned and issues collections respectively. Then pass the returned cleaned collection to `summarise_oaks()` and check that the invalid record does not contribute. Briefly explain this flow in your root README.
