# End Semester Examination, Set 3, Question 2
# Preserve Original Records in a Priority View

**Total: 30 marks | Submit one PDF**

## Problem

A task organiser displays high-priority tasks correctly, but viewing them changes the original task list. Repair this side effect without changing which tasks are selected.

Starter: https://github.com/kalviumcommunity/endsem-priority-preservation

Use your assigned repository. Run supplied Python files from project root with available Python 3 launcher. Standard library only. Editable files: priority_view.py, regression_check.py and RUNBOOK.md. Keep README.md, app.py, sample_data.py and checks.py unchanged. Preserve non-placeholder assertions.

## Requirements

high_priority(tasks) must return a new list of all records whose priority is "high", in original order, whether completed or unfinished. Do not alter source list order, remove source records or change their values. Empty input and no matches return an empty list. A deep copy of returned records is not required: the function must not mutate input during selection; later caller edits to returned records are outside scope. Supplied flat record structure is the assessed domain.

## Task 1: Reproduce and locate the side effect

Show initial Git status and files. Run app.py, showing input before selection, selected output and input afterward. Compare observed values with requirements. Locate caller and selection helper using code search or editor navigation. Explain which source operation changes original input and how the run supports that diagnosis.

Evidence: initial status/files, actual before/selected/after output, comparison, located caller/helper and supported cause explanation.

## Task 2: Demonstrate missing protection

Create repair branch. Run checks.py unchanged. Complete only the marked snapshot placeholder in regression_check.py so it independently preserves the original flat records before execution. Run regression against unchanged priority_view.py and capture the preservation assertion failing before repair. Show unchanged implementation and explain why selected-output checks can pass despite input mutation.

Evidence: branch, original checks, completed independent snapshot/assertions, actual pre-fix failure, unchanged implementation and coverage-gap explanation.

## Task 3: Repair and verify

Make focused correction in priority_view.py. Keep output semantics and all supplied assertions. Rerun app.py, old checks and complete regression. Verify mixed, no-match, all-match and empty cases, including record values and source/selected order, completed high-priority inclusion and new result list. Remove temporary diagnostics. Explain how correction avoids mutating original records without deleting valid input.

Evidence: focused diff, corrected before/after output, complete passing checks and short correction explanation. No hard-coded sample outputs or weakened expectations.

## Task 4: Link and propose

Create one GitHub issue recording steps, expected behaviour and original observed behaviour. Complete RUNBOOK.md with reproduction, cause, correction, actual run/check commands and results, plus one testing limit. Review staged changes, commit meaningfully and push. Open PR into main in the same repository, referencing actual issue number and describing cause, change and validation. Capture issue, runbook, staged review, commit/push, open PR/title/direction/description and clean local state. Leave issue and PR open for review; do not claim a merge or independent approval.

Evidence: actual issue and PR link, documentation, staged diff, commit/push, open PR and clean status.

## Submission

Submit one PDF containing solutions for all four tasks. Organise it into Task 1 to Task 4. Include screenshots requested in each task, with a one- or two-sentence label explaining the result and answering any requested short question. Multiple readable screenshots per task are allowed. Do not include credentials.

