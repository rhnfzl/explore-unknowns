# Territory profile: example template

This is an example profile. Copy it to `territory.md` next to the skill and replace every placeholder with your own project's specifics. If you delete `territory.md` or leave it generic, the walk still works, it just runs as a plain general interview with none of your project's shortcuts.

The skill reads this file at the start of every entrance. It holds every behavior that is specific to your workspace, so the stage files stay portable. Everything below is a slot: a short note on what belongs there, plus a generic example you should overwrite. When you are done, every angle-bracket placeholder should be gone.

## Workspace

State where the walk is running and what it may touch. Example shape:

> Workspace: `<your-workspace-path>`. Owned projects: `<project-a>`, `<project-b>`. Read-only context: `<vendored-or-upstream-checkout>` (inspect, never edit).

Also name the base branch the walk should diff against (for example `main`) and the one command that proves the project is healthy (for example `make verify` or `npm test`). Name anything the walk must treat as read-only. Agents follow these rules more reliably when they are written here than when they live only in your head.

## Writing rules for every artifact and reply

These rules are portable. Keep them, and add any house rules of your own. The overriding one: write so a reader who has never seen this code can follow it.

- Open in plain terms. Start every reply, and every section inside it, with one or two plain sentences: what this is, why it matters for what the user is trying to do, and what you want back from them. Then the technical detail. Product context first, code second.
- Define a coined term the first time you use it, in plain words, with a small concrete example, then use it freely. List your project's coined terms here so the walk knows which ones need a first-use definition (for example, an internal name like "the reconciler" or "shadow mode"). A file path is not a definition. In a committed map, wrap the term in `<dfn>` on that first use.
- No em dashes anywhere. Use commas, parentheses, or separate sentences.
- Keep the prose clean, tuck the evidence. The readable narrative carries no file paths. Put the file and line behind each claim in a separate, collapsed "Evidence" area.
- Show a picture when it helps understanding, and pick the form to fit. A set of labelled options is already a visual. When a flow is the hard part, add a small diagram. Not every reply needs one. Name your preferred diagram tool here: `<your-diagram-tool>`.
- Short sentences. Never put a ticket number in an artifact, a code comment, a docstring, a test name, or an example. No version labels like V1 or V2, use Implemented and Planned markers.

## Stage 1: scan and ground state

Tell the walk how to orient in your codebase before asking you anything.

- Discovery order. If you have a code index or knowledge graph, name it: use `<your-graph-tool>` to discover files and relationships before plain text search. Whatever the source, it can be stale, so nothing enters the map as a citation until the file has actually been read and the line confirmed.
- Extra context sources. List what the workspace can make available beyond the repository and Git state, such as `<your-extra-context-sources>` (design documents, an issue tracker, transcripts, or a durable notes store). Name any access limits and which source wins when they disagree.
- Missing-context gate. Scan the repository, Git state, this profile, memory, extra context sources, and sources the user already named before asking for more. Ask only when context relevant to the current task still remains missing after that scan. State the preferred request route here: `<your-context-request-route>`.
- Ground-state block (required). List what must be captured and shown before the interview starts. A good generic set:
  - current branch and working directory
  - the diff against the base branch
  - when the work touches configurable behavior, the per-environment config state read from `<your-config-source-of-truth>`, never guessed
- Memory preload. If you keep durable project notes in `<your-memory-store>` (a notes directory, a wiki, an agent memory file), name it here. The walk loads the relevant topics as settled ground and presents them as "your standing rules say X, applying unless you override". This is what stops the interview from re-asking questions you settled months ago.

## Mid-build: implementation ledger

Give task-scoped implementation ledgers a predictable home. Set the default directory to `<your-implementation-ledger-directory>` and name any allowed override, such as `<your-ledger-override-rule>`. The default filename is `YYYY-MM-DD-implementation-notes-<task>.md`. A continuing task reuses its ledger; a different task that collides takes the next numeric suffix.

## Stage 3: taste delta and promotion

Taste means your durable preferences about how this project should be built, the calls that are yours to make rather than facts to look up.

- Memory is the baseline, not a blank slate. The walk probes only for taste your `<your-memory-store>` does not already hold.
- When the walk surfaces new durable taste, it closes the stage by proposing it for your memory store. Promote only what passes all three gates:
  1. Hard to reverse. Undoing it later would cost real work.
  2. Surprising without context. A capable newcomer would guess wrong.
  3. A real trade-off. Something was genuinely given up, so the choice needs to stay visible.
- A preference that fails a gate stays in the map for this task and goes no further. Most preferences fail a gate, and that is the point: memory stays small enough to actually get read.

## Stage 4: the fixed landmine checklist

List the 3 to 5 failure families that have actually bitten your project before. The walk sweeps these every time, before the free-form sweep, because known failure shapes recur. Replace the examples below with your own history:

1. A config flag that differs between environments, so behavior verified in one environment silently diverges in another.
2. A boundary two services disagree about, where each side assumes the other validates or owns a field.
3. `<your-third-failure-family>` (for example, a cache or index that goes stale without an error).
4. `<your-fourth-failure-family>`
5. `<your-fifth-failure-family>` (optional; stop at five, a long list stops getting swept)

One sentence per family is enough: what it looks like and where it tends to hide. If you cannot name any yet, leave this section as a stub and add families as they bite you. The checklist earns its place one incident at a time.

## Stage 4 and 5: advisory input from other owners

When a decision touches a surface another person or team owns, the walk offers to pressure-test it. Name your mechanism here: a quick message to `<owner-of-that-surface>`, a review request, or a persona simulation if you use one.

Whatever the source, its output enters the map only as a flagged advisory class, never as file-and-line evidence. Opinions and citations stay in different buckets, so a persuasive opinion cannot masquerade as a verified fact.

## Stage 5: artifact tier and the handoff

- Tier, declared in stage 1. Apply the entrance's objective gate, then use its matching form.
  - Artifact-tier output: build the map as a committed document, with a diagram. State your format and location, for example `<your-docs-path>`.
  - Inline-tier output: a decisions table in the reply, nothing committed.
- Post-build tier gate. Use artifact-tier when merge readiness or stakeholder buy-in is requested, the change crosses an architecture, data, security, cost, or user-visible boundary, or a durable reviewer handoff is needed. Inline applies only to low-risk internal work with none of those conditions.
- Post-build quiz gate. Artifact-tier or merge-readiness work produces an explainer and a quiz on the non-obvious behavior, inherited risks, unverified assumptions, and what to watch after deploy. Record the result in `<your-post-build-gate-location>`. Merge readiness remains blocked while a merge-critical verification gap is open or a merge-critical question is unanswered or incorrect. Inline work has no required quiz.
- Second eye, artifact-tier only. Before hand-over, run an adversarial pass on the map: a fresh agent or a colleague tries to break its claims. Name your preferred reviewer or tool here: `<your-second-eye>`.
- Pipeline handoff. If the map feeds a build process, say what shape the handoff takes. A good generic set:
  - a work entry in whatever queue or tracker your builds start from
  - the scenarios or tests this work must pass to count as done
  - a copyable implementation prompt for whoever (or whatever) builds it

## Persistence of OPEN decisions

An OPEN decision is a question the walk raised that nobody could settle before the interview ended. One that survives unresolved gets proposed to `<your-memory-store>` only when it passes the same three gates: hard to reverse, surprising without context, a real trade-off. Everything else dies with the map, and that is fine.

## Subagent routing

If your agent runtime supports model selection for subagents, state your tiers so the walk spends compute where it matters:

- Read-only gathering (file listing, searching, confirming a line) uses `<your-cheap-model>`.
- Judgment and synthesis (classifying findings, drafting sections) use `<your-mid-model>`.
- Reserve `<your-top-model>` for architecture-level reasoning across many files.

If your runtime has no model routing, delete this section, the walk will run everything on the default model.

## Before you commit your territory.md

A quick self-check once you have filled everything in:

- No angle-bracket placeholders remain.
- The read-only zones and the base branch are stated explicitly.
- The landmine list names your real incidents, not borrowed examples.
- Someone joining your project tomorrow could read this file and know where the walk gets its facts, where it stores its conclusions, and what it must never touch.
