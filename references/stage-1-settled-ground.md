# Stage 1 - Settled ground (the known knowns)

Your first reply shows the map as it stands: what is already settled, so the
rest of the walk only spends the user's attention on what is not.

Express and direct entrances reuse this scan contract without claiming they
walked stage 1.

## Scan first (mostly silent)

Before asking the user for context, inspect every source already available:

- The repository files the task touches and any source files already named.
- Git state, including the current branch, the relevant diff, and changed tests.
- The optional local `territory.md` profile and any territory profile already
  supplied for the task. Use
  [territory.example.md](../territory.example.md) only as the public template,
  never as project evidence.
- Relevant workspace memory or notes that are available.
- Any ticket, Slack thread, recording, document, or other source the user has
  already named and made available.

Then trace the touched behavior through its callers, consumers, dependencies,
state changes, and boundaries for as many hops as needed to explain where it
comes from and what it affects. Stop at a stable explained boundary. Do not
branch into unrelated auditing. Stopping prevents further traversal; it never
removes a finding already encountered. File that finding once with the priority
labels defined in stage 5, then do not trace its own unrelated branches. Keep
every interesting discovery encountered on the trace in the four-quadrant map;
there is no separate parking lot.

Only after this scan, when a relevant fact or decision remains missing, ask for
external context. Name the missing decision and the exact source needed, such as
the ticket that records its acceptance rule or the recording where it was made.
Do not add a generic invitation for more context. Make scan-first visible in the
reply: disclose every finding from the inspected sources before presenting the
external-context request. The missing decision may stay in its natural quadrant,
but the copyable request for the user's answer comes after those findings.

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
- The relevant Git branch, diff against the mainline, and changed verification.
- With a territory profile, any extra ground-state fields it asks for, including
  per-environment flag state when the work touches flagged behavior. Read these
  from the source of truth and never guess.

Ground state is captured before you hypothesize anything. A map built on an
unchecked assumption about the current state is a map of a territory that does
not exist.

## Preload what is already written down

Load the relevant topics from any available workspace memory or notes store,
following the territory profile when it names one, and present them as settled
ground: "your standing rules say X, applying unless you override". This is why
the walk feels like it knows the user: it does not re-ask what they have already
codified. It only surfaces the gap.

## The opening reply

- Declare the selected entrance so the user sees the shape of the conversation.
- Calibrate the explanation depth in one line. Unfamiliarity is the default, but
  how much the user already knows changes how much to explain, so surface it.
  Where memory or the profile shows the user knows this area (they built part of
  it recently), say so and offer to keep the primer light ("you worked here last
  month, so I will keep the primer light"). Where there is no such signal and the
  area is dense, default to explaining from first principles. This is a stated
  calibration, not another question.
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
- Declare the artifact tier (artifact-tier or inline-tier) using the observable
  predicates in stage 5. On an artifact-tier full walk, open the map file
  skeleton now (the four quadrant sections, empty) and append to it as each stage
  closes, so a long walk that gets compacted or interrupted does not lose its
  accumulated state. Express and direct entrances reuse the task's map or start
  the partial map defined in stage 5. Inline-tier work stays in the conversation,
  no file.
- On a full pre-build walk, name the stages ahead, one line each. On an express
  entrance, name only its short route. A direct entrance names its current phase
  and handoff, not the pre-build stages.
- If the scan already surfaced a finding that reframes the task, disclose it now
  in plain words and file it under its quadrant. Do not save it for stage 4.
- On a full walk or interview entrance, the first stage-2 question may ride along
  in this same message. For a taste, design, or brainstorm request, the first
  concrete reaction leads too: open with a few distinct directions or a quick
  mock on plausible data in this same reply, so the user reacts in their first
  message instead of waiting for the taste stage. Nothing else jumps ahead.

**Done when** the user has the settled ground with citations and ground state,
knows which assumptions you treat as settled, and knows the tier and entrance.
On a full pre-build walk they can also see the stages ahead.
