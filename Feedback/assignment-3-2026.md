# Assignment 3 formative feedback

This feedback is organised using the [Computing Bootcamp rubric](https://mulquabio.github.io/MQB/rubrics/Computing_Bootcamp_Rubric.html). It does not award a mark; use it to decide what to revise and check before final submission.

## Criterion 1: Repository organisation & workflow discipline

- All required paths are present, and the supplied inputs match the supplied-file references. Your `.gitignore` excludes generated results, with none tracked beyond `.gitkeep`. The history includes descriptive commits for code, validation and documentation changes.

## Criterion 2: Code completeness & functional correctness

- The fixed and generalised tree-height programs each ran successfully. Separately, their generated CSVs satisfied the checked tree-height required output format and values. Your code shows the degree-to-radian conversion, angle-first function interface and checks before writing results.

## Criterion 3: Code quality & style

As you revise, keep names descriptive, use comments to explain decisions rather than restating code, and avoid repeating the same calculation in several places.

## Criterion 4: Documentation

- Before final submission, **Repair the README formatting.** In the supplied excerpt, the R code block beginning before `install.packages(...)` is not closed before the Data section. This can obscure headings and instructions in the rendered document. Add the closing fence immediately after the installation command, then preview the README to check that headings and command blocks render correctly.

## Criterion 5: Version-control practice

Commit each functional revision with a short message that says what changed; this makes your development easier to follow than one large final commit.

## Criterion 8: Basic error-handling & input validation

- Both invalid-input runs stopped without producing an output. Their error messages identify a distance-range problem in the fixed route and a non-finite distance in the generalised route. This supports those particular checks, rather than establishing all validation behaviour.

## Criterion 9: Problem-solving approach & method implementation

- Your Pound Hill table had the expected rows, plot identifiers and richness values. The code makes the route from counts to quadrat richness and then plot-level means clear. When I opened the figure, I found readable axes, all plot-level points and a compact block-colour legend. Your interpretation comments distinguish richness from abundance and appropriately caution against inferring causation from the figure alone.
- Before final submission, **Make your independent height check visible.** The output matches support the checked output requirements, but do not demonstrate your own checking process. An independent height calculation is not visible in the files reviewed; if you already have one elsewhere, link to it; otherwise add one. Locate or add a short worked check using one tree: compare a direct calculation from its angle and horizontal distance with the corresponding row in each program’s output, explaining the units and degree conversion.
- Before final submission, **Finish the table-to-figure check.** Automated evidence confirms that `results/pound_hill_plot_richness.pdf` exists; it does not verify its plotted values or biological interpretation. I found the figure readable. Trace one plot’s quadrat richness values through their mean in `results/pound_hill_plot_richness.csv` to its point on the PDF. Check that your written interpretation describes the plotted measure and acknowledges the overlap you discuss.

## Criterion 10: Learning progression demonstration

Use this feedback as a revision checklist. Make the changes in small, descriptive commits, then add a short README note explaining what you changed and how you checked it. This will make your development from this formative checkpoint visible in the final portfolio.

## Priorities before final submission

- Work from the directory containing `code/`, `data/` and the root `README.md`.
- Rerun an ordinary and an invalid case for each tree-height route separately. Check the error message, exit status and absence of a newly written result for invalid input; test the two routes separately.
- Preview the repaired README, complete the independent calculation and table-to-figure checks, then commit the revisions with a descriptive message while keeping generated results untracked.
