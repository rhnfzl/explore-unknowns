# Stage 1 - Settled ground (the known knowns)

Your first reply shows the map as it stands: what is already settled, so the
rest of the walk only spends the user's attention on what is not.

## Scan first (mostly silent)

Before saying anything about the code, walk the territory.

- **General walk:** split the code the task touches among parallel read-only
  subagents and collect what they pin down, so the opening lands fast instead of
  after a long serial read.
- **With a territory profile:** follow its scan rule (see your `territory.md`),
  then Read-verify every file and line before it may enter the map. Nothing a
  tool surfaced is a citation until a file has actually been read.

Gather: what already exists for this task (including half-built or reverted
prior attempts), the data shapes and conventions the code enforces, and anything
that smells load-bearing.

## Capture ground state

Record the starting point as a real section of the map, not a vibe:

- The request as you understand it.
- With a territory profile, the ground-state block it asks for (branch, diff
  against the mainline, and per-env flag state when the work touches flagged
  behavior, read from the source of truth and never guessed).

Ground state is captured before you hypothesize anything. A map built on an
unchecked assumption about the current state is a map of a territory that does
not exist.

## Preload what is already written down

If the territory profile points at a memory or notes store, load the relevant
topics and present them as settled ground: "your standing rules say X, applying
unless you override". This is why the walk feels like it knows the user: it does
not re-ask what they have already codified. It only surfaces the gap.

## The opening reply

- Declare the entrance (full walk, blindspot pass, or interview me) so the user
  sees the shape of the conversation.
- Calibrate the explanation depth in one line. Unfamiliarity is the default, but
  how much the user already knows changes how much to explain, so surface it.
  Where memory or the profile shows the user knows this area (they built part of
  it recently), say so and offer to keep the primer light ("you worked here last
  month, so I will skip the basics unless you want them"). Where there is no such
  signal and the area is dense, ask the one plain question ("how well do you know
  this corner already?"). Either way it is one line the user can correct, not a
  blocking gate.
- Open in plain terms (the plain-language rules apply, see SKILL.md and the
  profile). Before any file names, give a short mental model of the corner of the
  system this task touches: how it works today, in two or three sentences, with
  the one or two coined terms defined by example and an everyday analogy for the
  hardest one. When a picture carries the shape faster than a sentence (a flow,
  who calls whom), add a small Mermaid diagram here. This orients the user before
  the facts arrive.
- List the settled ground: the request, the facts the territory pins down,
  constraints and decisions already made, and the preloaded standing rules.
  Distinguish what is locked from what you are merely assuming; flag assumptions
  as "settled unless you say otherwise". State each fact in plain words: what it
  is and why it matters to the user. Keep the file and line out of the sentence
  and collect them in a separate, collapsed "Evidence" area so a reviewer can
  verify without the reader wading through code names. Define the first coined
  term you reach for (for example what a "reconciler" or an "idempotency key"
  actually is) before you lean on it.
- Declare the artifact tier (artifact-tier or inline-tier). A map is a committed
  artifact only when there are decisions worth aiding. See stage 5. On an
  artifact-tier walk, open the map file skeleton now (the four quadrant sections,
  empty) and append to it as each stage closes, so a long walk that gets
  compacted or interrupted does not lose its accumulated state. Stage 5 then
  finishes the map rather than building it from scratch. Inline-tier walks stay
  in the conversation, no file.
- Name the stages ahead, one line each.
- If the scan already surfaced a finding that reframes the task, disclose it now
  in plain words and file it under its quadrant. Do not save it for stage 4.
- The first stage-2 question may ride along in this same message. For a taste,
  design, or brainstorm request, the first concrete reaction leads too: open
  with a few distinct directions or a quick mock on plausible data in this same
  reply, so the user reacts in their first message instead of waiting for the
  taste stage. Nothing else jumps ahead.

**Done when** the user has the settled ground with citations and ground state,
knows which assumptions you treat as settled, knows the tier and entrance, and
can see the stages ahead.
