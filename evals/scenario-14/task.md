# Compliance Right-Click Menu for Data Entry

## Problem Description

A data-entry compliance team wants to speed up their review workflow by adding
shortcuts to Excel's cell right-click menu via their PyXLL add-in. When a user
right-clicks on a cell, they want three things available:

1. A **toggle** that marks the cell as reviewed (and shows whether it is currently
   marked — so users can see the state at a glance and toggle it off again)
2. A **"Flag for Follow-up"** action button
3. An **inline text field** where a reviewer can type a short annotation note
   directly from the context menu without opening a separate dialog

All callbacks live in the `compliance_tools` Python module.

## Output Specification

Produce `compliance_ribbon.xml` — a complete customUI XML file that adds these
controls to the Excel cell right-click context menu.

If any of the requested controls cannot be placed in a context menu, omit them
(do not add them to the ribbon instead) and leave a short XML comment explaining
the limitation.
