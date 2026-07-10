# Stage 5 - The map (hand over)

The walk's deliverable. Close by finishing the four-quadrant map into one thing
the user keeps. On an artifact-tier walk the map file was opened in stage 1 and
filled as each stage closed, so this stage finishes and polishes it rather than
building it from scratch. On an inline-tier walk the map is assembled here.

## Tier decides the form

The tier was declared back in stage 1.

- **Artifact-tier** (architecture-changing or build-queue work): finish the
  committed page opened in stage 1 with the **human-html** skill, and draw the
  four-quadrant map diagram with **excalidraw-mcp**. Follow the profile for where
  it lands and how it is indexed. Before hand-over, run the second-eye pass the
  profile describes (an adversarial read asking what the map missed and which
  claim lacks evidence); if the reviewer is unavailable, note that on the map and
  proceed.
- **Inline-tier** (small walk): a decisions table in the reply, no committed file.
  The "every artifact assembles the reply" move still applies, it is just the
  reply itself.

## The map contents

One place holding all four quadrants:

- **Settled ground** (known knowns): the settled facts in plain words with the
  ground-state block. File and line citations sit in a collapsed "Evidence" area
  beside or below each fact, not inside the readable sentence.
- **Open decisions** (known unknowns): the decision ledger. Every named question
  with its answer and how it closed (answered by user, answered by territory,
  OPEN, user-owned, or DEFAULTED). OPEN items state what unblocks them; DEFAULTED
  items state the default taken and why it is safe, so the user can veto.
- **Taste** (unknown knowns): what got extracted. Taste, consumers, environment,
  tacit conventions, what each reshaped, and any advisory persona input flagged
  as advisory.
- **Landmines** (unknown unknowns): the landmine cards with evidence, each marked
  decided, OPEN, or sharp-edge.

Anything still open lives on the map, not in scrollback. Each quadrant section
opens with one plain sentence before its entries. In a committed map, define each
quadrant term once with `<dfn>` so a colleague who opens it is not reading jargon.
When the walk surfaced a vocabulary collision (one word the user and the code use
for different things), the glossary entry gains an "avoid: X, Y" tail naming the
dangerous synonyms, so the next prompt does not reintroduce the confusion.
In an inline map, close with a short "terms used" list, three to five lines
defining the coined words in plain language, so the definitions do not die in
scrollback.

## What rides along

- **A build plan may accompany the map, never replace it.** Sort it as a
  tweakable plan: by likelihood-of-tweaking, not execution order. Judgment calls
  first with their alternatives toggleable, mechanical work collapsed at the
  bottom ("I trust you on that part").
- **The handoff the map feeds.** Always emit a portable handoff block: scope,
  locked decisions, open decisions, the evidence behind each, known risks, the
  assumptions still unverified (reviewers and the builder inherit exactly those),
  the first check the built work must pass, the files the implementer should read
  before editing, and the taste criteria stage 3 extracted stated verbatim (the
  freshest, least-written-down knowledge, and so the likeliest to be dropped at
  hand-over if it is not carried in the prompt). With a profile, also emit the
  extra shape it asks for (see [territory.md](../territory.md)).
- **The copyable implementation prompt carries the rules the build must obey,**
  because implementation is a separate task that may never load this skill, so
  the prompt is the only instruction bundle guaranteed to cross the boundary
  (the map and handoff cross too, but the prompt is what the builder acts from).
  Give it a standard tail: the remaining unverified assumptions, the stop-and-ask
  conditions (stop and ask if the change touches architecture, data migration,
  security, cost, or user-visible behavior; otherwise take the conservative option
  and log it and keep going), a short notes skeleton for the build to keep
  (Deviations as planned / actual / why / risk, New unknowns, Verification), and
  one line granting the implementer judgment inside those rails. This is what
  makes the deviation policy and the notes survive the session boundary instead of
  dying in a reference file the next session never opens.
- **Persistence.** The decisions table always lands here. An OPEN that survives
  the walk gets proposed to memory when it passes the profile's memory-promotion
  gates, so it does not die with the session.
- **An optional understanding-check, offered not forced.** A map is only useful
  if the user actually holds it, and a long walk can leave them nodding along
  without the model really landing. So offer a short check: three or four plain
  questions on the decisions that carry the most weight, the kind where a wrong
  answer would send the build the wrong way. If they want it and miss one, point
  back at the part of the map that answers it rather than just giving the answer.
  This is the merge quiz used early, to confirm the map is understood before the
  build starts, not only at merge. Skip it on a quick inline walk.

**Done when** the user holds the map. Implementation is a separate task that
starts from it. Offer to begin, and point at
[after-the-walk.md](after-the-walk.md) for how the map lives on during the build.
