# Sample draft storage decision

## Settled

- Draft storage must use atomic replacement.
- Recovery may read the last backup when current JSON is invalid.

## Missing external decision

The product owner has not decided whether failed autosave blocks navigation or warns and continues.
