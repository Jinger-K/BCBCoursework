# Assignment 1 feedback - Ke JIANG

**Formative feedback | Rubric 2026.2**

The README gives a useful account of purposes, dependencies, tests, limitations and help used. Your own TSV contains an empty field, the converters have consistent validation and error checking, and all five FASTA answers matched the independent checks. Joining the supplied sequence lines with xargs printf is a valid alternative here; it does not need replacing simply because another answer uses tr.

The main correction is the converter invocation. Both scripts write through ../results and assume a code/ starting directory, whereas the released interface starts at the repository root. Keep the existing checks, correct the path convention and update the README examples at the same time.

Then repeat the clean-checkout tests you describe, inspecting the actual files and exit statuses. Include a missing results directory, an empty field, a spaced filename and a repeated run. These checks should describe the corrected scripts, not only a previous local version.

There is also a small but important mismatch between the documentation and .gitignore: the README says generated results are ignored, but the rule is not present. Add it before new outputs are accidentally committed. The tracked .gitkeep is only a placeholder and can remain. Keep the task-specific history and the explanations of the methods' assumptions.

---

## Project structure

Relevant tracked layout (simplified; missing required paths are marked):

```text
README.md
.gitignore
code/  unixPrac1.txt, tabtocsv.sh, csvtospace.sh
data/fasta/  3 required files present
data/temperatures/  4 required files present
data/tab-example.tsv
results/  placeholder only
sandbox/  no files tracked; optional
```

All required root files, assessed scripts and inputs are present. results/ contains only a .gitkeep placeholder; no generated conversions are tracked. Sandbox and local environments are ignored, but results is not, despite the README saying generated outputs are excluded.

Add the missing results rule and keep the placeholder if useful. Align the converter commands with the root structure and retain the clear README map. The existing organisation does not need a new hierarchy; it needs the documentation, ignore rules and script paths to agree.

**Assessed snapshot:** `8c6c7217c290c83491b2bf7cc851b414b7b7af0d`
