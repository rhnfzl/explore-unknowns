---
name: explore-unknowns
description: >-
  Walk the user through mapping the unknowns of a task before, during, and after
  they build it, and hand them a four-quadrant map (settled ground, open
  decisions, taste, and landmines) they keep. Reach for this eagerly whenever a
  request is ambiguous or underspecified, the codebase or domain is unfamiliar,
  the user will "know it when they see it", a reference implementation must be
  understood before porting, a build-queue or architecture-changing task is
  about to start, a mid-build deviation needs capturing, or a finished change
  needs buy-in or verified understanding before merge. Trigger even when the
  skill is not named: "do a blindspot pass", "find my unknown unknowns",
  "interview me about this change", "brainstorm the approach for a task I am about
  to build", "help me scope this", "what am I missing here", "plan this before I
  build", "I know nothing about X in this codebase". When a territory profile is
  present it reads memory and the graph first and feeds the map into the build
  pipeline; without one it degrades to a plain general map. Not for trivial or
  mechanical tasks with clear acceptance criteria, single-fact lookups, pure
  debugging of a known symptom, or pure code review, those have their own tools.
  Do not use it to run the build itself; the map is the deliverable and
  implementation is a separate task that starts after hand-over.
license: MIT
metadata:
  version: "1.0.0"
  author: "rhnfzl"
---

# Explore Unknowns

The map is not the territory. The prompt, the plan, and the context window are
the map. The codebase, the domain, and the user's real intent are the territory.
The gap between them is the unknowns. An unknown found before code is written
costs minutes. The same unknown found three PRs later costs the three PRs.

This skill is a guided conversation: the **quadrant walk**. You and the user
fill in a four-quadrant map of the task, one quadrant across each of the first
four stages, then a fifth stage hands it over and the user walks away holding the
completed map. The map is the deliverable. Implementation is a different task
that starts only after the map is handed over.

**Do not walk when the walk would just be ceremony.** Skip it, and say why in one
line, when the task is trivial, mechanical, or already has unambiguous acceptance
criteria; when the user clearly wants immediate execution and the risk of a wrong
assumption is low; or when a single tool call would settle the question and no
interview is needed. The walk earns its five stages only when the unknowns are
real.

## The portable spine and the territory profile

The walk itself is domain-agnostic. Every project-specific behavior (which graph
to query, where committed maps live, which landmines to sweep for, what the map
feeds into) lives in one file: your `territory.md`. Copy
[territory.example.md](territory.example.md) to `territory.md` and fill in your
project to switch it on. Read it at the start of a walk. If it is present, the
walk uses it. If it is absent or generic, the walk degrades to a plain general
map with self-contained HTML and no harness coupling. This keeps the skill
portable without a config schema: the territory is swappable by editing one
file, not by threading options through the walk.

## Three moves at every stage

- **Explain before you cite.** This skill fires when the user does not know the
  territory yet, and the code was often written by someone, or something, other
  than them. So assume they cannot read the domain's jargon. Lead every fact and
  every finding with plain words: what it is, and why it matters for what they
  are trying to do. Keep the file and line out of the sentence; the evidence
  belongs in a separate, tucked-away place a reviewer can open (see the map and
  the stage files). The reader should be able to follow the whole reply without
  ever opening a file. Four habits make prose readable, and the eval feedback
  showed each one matters:
  - **Define on first use, with a real-world analogy.** The first time you use a
    coined or domain word, define it in one plain sentence, and for anything
    abstract add a concrete example and, for the hardest idea, an everyday analogy.
  - **Gloss a named set inline.** When you list named things (axes, modes,
    states), put a short plain gloss in brackets right after each one, so the
    reader never has to leave the sentence to know what a name means.
  - **Do not make the reader open files.** A wall of paths and type names is not
    an explanation. Name at most what is load-bearing, in prose, and tuck the
    rest into the evidence area.
  - **Do not use the walk's own vocabulary at the reader.** Words like "blast
    radius", "load-bearing finding", and "landmine" are how this skill thinks,
    not how you talk to the user. Say the plain thing instead: "the decision that
    changes the most", "the finding that reframes your task", "a trap that bites
    silently". A map the user cannot read is not a map.
- **Reacting beats imagining.** Never ask the user to describe what they want
  when you can hand them something concrete to react to: a rendered option, a
  clickable mock, a decisions table, a landmine card. Reacting extracts
  knowledge the user has but cannot articulate unprompted. When the request is
  itself a taste, design, or brainstorm problem (the user will know it when they
  see it, or asks for options, directions, mockups, or a layout), this move
  leads the opening. Show the concrete directions first and fill the settled
  ground and decisions in around them. Do not make the user wait for the taste
  stage's scheduled turn to see anything. That wait is the single most common
  way this walk fails: it stalls on scoping questions when a rendered option
  would have answered them faster and better.
- **Every artifact assembles the reply.** End each artifact with the user's next
  message pre-drafted: steal/skip chips, resonate checkboxes, a decisions table,
  a copyable sharpened prompt. Their reaction becomes their next message with
  near-zero typing.

## The walk

Five stages, walked in order, one at a time. **When you enter a stage, read its
reference file and follow it.** Name the current stage as you go so the user
always knows where they stand, and finish the stage in front of you before
opening the next. Each stage carries a plain name, and the map defines the
underlying quadrant term once, in plain words, the first time it appears.

1. **Settled ground** (the known knowns) ->
   [stage-1-settled-ground.md](references/stage-1-settled-ground.md). Scan the
   territory, capture ground state, preload what memory already knows, then open
   with what is already settled.
2. **Open decisions** (the known unknowns) ->
   [stage-2-open-decisions.md](references/stage-2-open-decisions.md). The
   questions you can name. Resolve them one at a time, highest blast radius
   first, by delegating the interview to grilling.
3. **Taste delta** (the unknown knowns) ->
   [stage-3-taste-delta.md](references/stage-3-taste-delta.md). The taste and
   tacit context nobody has written down. Skip what memory already holds, probe
   only the delta, and promote new taste back to memory.
4. **Landmine sweep** (the unknown unknowns) ->
   [stage-4-landmine-sweep.md](references/stage-4-landmine-sweep.md). Sweep the
   fixed checklist first, then the free sweep, and turn silent traps into map
   entries.
5. **The map** (hand over) ->
   [stage-5-the-map.md](references/stage-5-the-map.md). The completed
   four-quadrant map, plus the handoff the map feeds into. The walk's only
   done-condition.

When the user moves on to build, review, or merge what the walk mapped, read
[after-the-walk.md](references/after-the-walk.md). The map lives on past
planning.

## Entrances

Declare the entrance in your first reply so the user knows the shape ahead.

- **Full walk** (default for build-queue and architecture-changing work). All
  five stages in order.
- **Blindspot pass** ("do a blindspot pass", "what am I missing"). Stage 1 lite
  plus stage 4. Stamp the map fragment with what was skipped so a partial map
  never reads as complete.
- **Interview me** ("interview me", "grill me on this"). Stage 1 lite plus stage
  2. Same stamping rule.
- **Too big for one session.** When the full walk finds the effort will not fit
  in one agent session, stop and hand the settled ground plus open decisions to
  the **wayfinder** skill, which charts the work as tickets on the issue tracker.
  Wayfinder sits above this walk, it is not a stage inside it.

## What the walk owns and what it delegates

The walk owns the conversation moves that have no drift risk: the quadrant
framing, blast-radius ordering, memory-seeding, the landmine sweep, and the map.
It delegates work that other skills already own, so their conventions stay
enforced by their own tooling:

- **The interview** (stage 2) -> the **grilling** skill. Inline-tier walks use
  `grill-me` (plain grilling). Artifact-tier walks use `grill-with-docs`, whose
  ADRs and glossary feed the map's `<dfn>` glossary.
- **The map artifact** (artifact-tier, opened in stage 1 and finished in stage 5)
  -> the **human-html** skill for the committed page and **excalidraw-mcp** for
  the map diagram.
- **Graph queries** (stage 1) -> the graph tools the profile names.
- **Profile landmine checks** (stage 4) -> the skills the profile names for them.
- **Deep external research** inside a stage -> **recursive-research**.

Delegation is the primary path, not a hard dependency. If a delegated skill is
not installed on this machine, do the work inline rather than break: run the
question loop yourself (one material question at a time, highest blast radius
first, recommended answer as lettered options, close on the map), write the map
as a self-contained HTML file or a plain table, and skip the diagram or draw it
as a text sketch. The walk degrades, it never stalls.

## Rules

- Walk the quadrants in order, one stage at a time, naming the current stage.
  The walk ends with the map in the user's hands. No map, not done.
- Stages order the walk, they never embargo information. A finding that
  materially bears on a decision in flight is disclosed the moment you have it,
  then filed on the map under its quadrant. Never hold it back for its stage.
  The same rule governs the concrete-reaction move: when something the user can
  react to (design directions, a mock) is the highest-value next step, it leads,
  it does not wait for the taste stage's scheduled turn.
- Nothing closes off-screen. Any question or judgment call the map records as
  closed must have been shown to the user first, including ones the territory
  answered.
- Claims about the territory cite real files actually read. A settled fact needs
  a Read-verified file and line. Any claim about flow, boundary, or architecture
  needs a leaf trace, one file and line per hop, never a claim from a name or
  from graph output alone. A fabricated specific destroys the map's authority;
  label anything invented as invented.
- Decisions are the user's. Facts you can find in the territory, you find; you do
  not ask the user for them.
- HTML artifacts are self-contained single files: inline CSS and JS, no external
  requests, plausible fake data over lorem ipsum, and the writing rules in
  your `territory.md` when a profile is present.
- When a territory profile defines writing rules, they bind every reply and
  artifact, not just committed docs. Re-read them before you send.
- Stop at every stage boundary that needs the user's reaction. Never barrel into
  implementation on unconfirmed guesses. Implementing is a separate task that
  begins after the map is delivered.
