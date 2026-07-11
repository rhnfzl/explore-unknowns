# Stage 4 - Landmine sweep (the unknown unknowns)

What neither of you knows to ask, the territory often does. This stage sweeps the
code the task will touch and turns silent traps into map entries.

## Sweep the checklist first, then sweep free

- **With a territory profile:** run its fixed landmine checklist first, and use
  the skills the optional local `territory.md` profile names for any check it
  delegates. Start from
  [territory.example.md](../territory.example.md) when a public template is
  useful. These are the families that have bitten before, so they deserve
  deterministic detection rather than luck.
- **Then the free sweep, always.** The checklist finds the known families; the
  free sweep is where the genuinely novel unknown-unknowns live, which is the
  whole point of the quadrant. Do not let the checklist crowd out the open sweep.

## What to hunt in the free sweep

- **Landmines.** Things that bite silently: wrong-by-default data, stale
  denormalizations, filters that pass bad rows, escaping that corrupts output.
- **Unwritten conventions.** Rules the code enforces that no doc states.
- **Half-built or reverted prior attempts** at the same job, and why they died.
- **Findings adjacent to the feature.** Latent bugs encountered on the causal
  trace that the task's code path inherits or exposes. Keep them on the map
  without launching an unrelated audit.

## Report

1. State the coverage plainly: "the sweep covered the N files this task touches,
   plus the M checklist families". Silent truncation reads as full coverage when
   it is not.
2. Report each finding as a card, plain words first: **what it is** (one plain
   sentence a non-expert can follow), **why it bites**, **what it changes** about
   the task, then the **evidence** (file and line, leaf-traced for any flow or
   boundary claim). Print a visible `Priority: <label>` field using exactly one
   stage 5 label: `Changes this task`, `Nearby finding`, or
   `Urgent outside scope`. Show `Changes this task` cards first without hiding
   adjacent cards. Confirmation is a separate field; a finding without a trace
   is PLAUSIBLE, not CONFIRMED, and that status never substitutes for priority.
3. A finding that needs a user decision is put to the user with lettered options
   and your recommendation, and closes as decided or OPEN. A finding that only
   needs awareness goes straight on the map as a sharp edge. A landmine is never
   Defaulted or User-owned; a silent trap is exactly the thing that must be seen,
   so it is always decided, OPEN, or a sharp edge.

Remember the global rule: findings that bear on decisions already in flight
should have been disclosed when found. This stage is where the systematic sweep
happens, not where disclosures wait.

Every card stays in its natural quadrant on the same map. Do not create a
parking lot for nearby or out-of-scope discoveries.

**Done when** the sweep has covered the code the task will touch and the
checklist families, and every finding is on the map, decided, OPEN, or noted as
a sharp edge.

## Technique

- **Blindspot pass.** The sweep packaged for reaction: landmine cards, each with
  the evidence, why it bites, and a copyable prompt fix, assembled into one
  better implementation prompt at the end. This is also the express entrance
  "do a blindspot pass" (stage 1 lite plus this stage). Finish with stage 5's
  stamped partial map showing all four quadrant headings: `Settled ground`,
  `Open decisions`, `Taste`, and `Landmines`. Keep a heading visible when its
  quadrant is empty. Every finding card retains its `Priority: <label>` field;
  confirmation status does not replace it. Before the handoff, include every
  already encountered discovery outside the task boundary once as `Nearby
  finding` or `Urgent outside scope` under stage 5's precedence. Do not trace it
  further or add it to the implementation handoff unless the user expands scope.
