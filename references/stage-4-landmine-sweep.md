# Stage 4 - Landmine sweep (the unknown unknowns)

What neither of you knows to ask, the territory often does. This stage sweeps the
code the task will touch and turns silent traps into map entries.

## Sweep the checklist first, then sweep free

- **With a territory profile:** run its fixed landmine checklist first, and use
  the skills the profile names for any check it delegates (see
  [territory.md](../territory.md)). These are the families that have bitten
  before, so they deserve deterministic detection rather than luck.
- **Then the free sweep, always.** The checklist finds the known families; the
  free sweep is where the genuinely novel unknown-unknowns live, which is the
  whole point of the quadrant. Do not let the checklist crowd out the open sweep.

## What to hunt in the free sweep

- **Landmines.** Things that bite silently: wrong-by-default data, stale
  denormalizations, filters that pass bad rows, escaping that corrupts output.
- **Unwritten conventions.** Rules the code enforces that no doc states.
- **Half-built or reverted prior attempts** at the same job, and why they died.
- **Findings beyond the feature.** Latent bugs the task's code path inherits.
  Escalate them to the map rather than silently absorbing them.

## Report

1. State the coverage plainly: "the sweep covered the N files this task touches,
   plus the M checklist families". Silent truncation reads as full coverage when
   it is not.
2. Report each finding as a card, plain words first: **what it is** (one plain
   sentence a non-expert can follow), **why it bites**, **what it changes** about
   the task, then the **evidence** (file and line, leaf-traced for any flow or
   boundary claim). Worst first. A finding without a trace is a PLAUSIBLE, not a
   CONFIRMED; label it so.
3. A finding that needs a user decision is put to the user with lettered options
   and your recommendation, and closes as decided or OPEN. A finding that only
   needs awareness goes straight on the map as a sharp edge. A landmine is never
   Defaulted or User-owned; a silent trap is exactly the thing that must be seen,
   so it is always decided, OPEN, or a sharp edge.

Remember the global rule: findings that bear on decisions already in flight
should have been disclosed when found. This stage is where the systematic sweep
happens, not where disclosures wait.

**Done when** the sweep has covered the code the task will touch and the
checklist families, and every finding is on the map, decided, OPEN, or noted as
a sharp edge.

## Technique

- **Blindspot pass.** The sweep packaged for reaction: landmine cards, each with
  the evidence, why it bites, and a copyable prompt fix, assembled into one
  better implementation prompt at the end. This is also the express entrance
  "do a blindspot pass" (stage 1 lite plus this stage).
