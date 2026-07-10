# Stage 2 - Open decisions (the known unknowns)

The questions that must be answered but are not yet. You know the question; the
answer lives with the user or in the territory.

## Delegate the interview

The interview loop is a solved problem: the **grilling** skill already runs a
relentless, one-at-a-time, blast-radius-ordered interview that recommends an
answer per question and looks up facts instead of asking. Use grilling for the
question loop when it is available; if it is not installed, run the fallback loop
from SKILL.md inline rather than breaking. Do not invent a second interview
mechanic beyond that fallback:

- **Inline-tier walks:** `grill-me` (plain grilling).
- **Artifact-tier walks:** `grill-with-docs`, so its ADRs and glossary feed the
  map's decisions ledger and `<dfn>` glossary.

What this stage adds on top of grilling is the quadrant framing: you are filling
the known-unknowns quadrant of a specific map, the questions are scoped to that
task, and every answer lands on the map, not just in the conversation. It also
passes grilling the plain-language contract: each question defines the terms it
uses and leads with why the answer matters, so the user is never asked to decide
about code they have not first seen explained in plain words.

## Procedure

1. Inventory the questions the task cannot proceed without. Disclose the queue
   ("still queued after this: ...") so the user sees how much walk remains.
2. Hand the queue to grilling, resolved one at a time, highest architectural
   blast radius first, each with your recommended answer as lettered options the
   user can pick in a few characters. When the user prefers a structured choice,
   present it as a single question with a marked recommended default.
3. Close every question one of five ways, always in front of the user:
   - **Answered by the user.**
   - **Answered by the territory.** Go read it instead of asking, then show the
     user the question and the found answer. A question closed off-screen is not
     closed.
   - **Recorded OPEN on the map,** explicitly deferred, with what unblocks it.
   - **User-owned.** The user is the expert on this slice and takes it off the
     table. Record the scope they own and stop probing inside it, so their
     expertise is not re-interrogated.
   - **Defaulted.** Low blast radius, and asking would cost a round-trip the
     answer does not deserve. State the default you are taking and why it is safe
     in the same message, then move on. The map marks it DEFAULTED so the user can
     veto any time before the build. This is not a silent choice: it is shown, it
     just does not wait for a reply. Reserve it for genuinely low-stakes
     questions; anything that changes architecture, data, security, cost, or
     user-visible behavior is never defaulted.

**Done when** every named question is closed one of those ways, in front of the
user. Announce the stage closed (a small decisions table recaps it well) before
crossing into stage 3.

## When the effort is bigger than one session

If the queue of decisions is clearly too large for one agent session, stop the
walk and hand the settled ground plus the decision queue to the **wayfinder**
skill, which charts them as tickets on the issue tracker and resolves them one
at a time. Do not try to force a multi-session effort through a single walk.

## Techniques (beyond the plain interview)

- **Brainstorm the intervention** (when the question is "which solution?"):
  search the codebase first, then plot roughly ten interventions from
  ship-this-afternoon to quarter-long bet, each grounded in what actually exists.
  Half-built features behind flags and disconnected wiring are the cheapest wins.
  Resonate checkboxes assemble the reply.
- **Point at a reference** (when an existing implementation encodes the wanted
  behavior): produce a semantics map proving you understood it. What it does with
  excerpts, how each behavior maps to the target stack, and every place the port
  cannot be literal. Nothing gets ported until sign-off. Source code is the best
  reference; a diagram or screenshot is a weaker one.
