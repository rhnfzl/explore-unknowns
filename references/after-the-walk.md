# After the walk

Use this reference when work is already Mid-build or Post-build, whether a
pre-build map exists or the user enters directly. Do not replay the five-stage
pre-build walk. Run stage 1's scan contract, then reuse the task's existing map
or apply stage 5's phase-stamped partial-map contract.

## Artifact identity

Derive one short task slug from the task's stable subject and reuse it across
the default artifact names:

- `YYYY-MM-DD-unknowns-map-<task>.html`
- `YYYY-MM-DD-implementation-notes-<task>.md`
- `YYYY-MM-DD-post-build-explainer-<task>.html`

Continuing the same task deliberately updates its artifacts. If a path already
belongs to a different task, choose the next numeric suffix for the new task and
reuse that suffixed slug across its artifacts. Never overwrite or repurpose a
different task's file.

## Mid-build

When implementation is already underway:

Use artifact-tier when the deviation touches architecture, data, security, cost,
or user-visible behavior, or when a durable reviewer handoff is needed. A small,
low-risk deviation may stay inline.

1. Declare the Mid-build entrance and artifact tier. Reuse the task's map when
   present. Otherwise create the phase-stamped partial map from stage 5 using
   the repository, Git, profile, memory, and named sources that were actually
   inspected.
2. For artifact-tier work, create the dedicated task-scoped implementation
   ledger. When a map existed at entry, link the ledger to it. When none existed,
   begin the ledger with the new phase-stamped partial map itself before the log.
3. Record each deviation under six fields: **Planned**, **Actual**, **Why**,
   **Risk**, **New unknowns**, and **Verification**. Fold every new discovery
   back into its quadrant and discovery priority on the map.
4. When a deviation changes architecture, data migration, security, cost, or
   user-visible behavior, mark the decision OPEN and hand it to the user. For a
   lower-risk deviation, record the conservative choice and hand the updated
   ledger back to the builder. This skill records and routes the unknown; it
   does not make the implementation change.

Inline-tier Mid-build work keeps the same fields in the reply and finishes with
the inline partial map fragment. Artifact-tier work finishes with the updated
map, ledger, and the next missing decision or verification named explicitly.

## Post-build

Choose the recipe from the size and requested outcome.

- **Artifact-tier or merge-readiness work:** reconstruct what matters from the
  diff, tests, implementation ledger, map, and named sources actually available.
  Reuse the task's map or create a Post-build partial map that states those
  sources and the stages not walked. Produce the task-scoped post-build
  explainer and a quiz on the non-obvious behavior, inherited risks, unverified
  assumptions, and what to watch after deploy. When a verification gap leaves a
  safety-sensitive path unproven, mark the gap merge-critical. Mark questions
  whose wrong answer could make the change unsafe as merge-critical too. Merge
  readiness remains blocked while a merge-critical verification gap is open or
  a merge-critical question is unanswered or incorrect; a wrong answer points
  back to the relevant explanation. The explainer can also serve as the buy-in
  document: lead with the demonstrated behavior, pre-answer reviewer objections
  with evidence, and name who signs off on each remaining decision.
- **Small inline work:** give a concise inline explanation of what changed, its
  callers or consumers, whether behavior changed, and the supplied verification.
  Do not require a formal artifact or quiz. Offer a lightweight understanding
  check only when meaningful uncertainty remains.

This is an understanding and unknowns gate, not a code review or merge action.
Follow [the skill's scope boundary](../SKILL.md#rules), and point to the
workspace's own build, review, and merge skills for those actions.
