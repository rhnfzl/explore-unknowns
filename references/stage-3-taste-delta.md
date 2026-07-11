# Stage 3 - Taste delta (the unknown knowns)

The user (or the codebase) holds answers nobody has put into words: taste,
vocabulary, tacit conventions, the context that otherwise surfaces as "oh, one
thing I forgot to mention" after it is too late. You cannot ask for these
directly. Asking "what do you want?" gets a shrug.

## Probe only the delta

This is the stage where a personalized walk earns its keep. If the territory
profile points at a memory store, the user has already written down a lot of
their taste. Do not re-elicit it.

- Load the relevant standing rules from memory in stage 1 and treat them as
  settled. In stage 3, probe only for taste that memory does not already hold.
- When the walk surfaces new durable taste, close the stage by proposing it to
  the configured memory store or optional local `territory.md`. If no local
  profile exists, copy [territory.example.md](../territory.example.md) to
  `territory.md` before adding project-specific durable taste; never write those
  rules into the public template. Stage 3 is not just an interview, it is a
  memory-write loop that compounds across walks: each walk makes the next one
  ask fewer questions.
- With no profile, there is no memory to lean on, so probe taste from scratch.

## Do not defer the concrete reaction

When the request is a taste or design problem from the start (the user asks for
options, directions, mockups, or a layout, or says they will know it when they
see it), the design-directions or mock move belongs in the **opening reply**,
not three stages later. Settled ground and open decisions can be filled in
around a set of rendered directions. Making the user answer scoping questions
before they have seen anything is the most common way this stage fails: a person
cannot react to a question as well as they can react to a rendered option, so a
scoping question that a mock would have answered is a wasted turn. Lead with the
option, then let their reaction sharpen the scope.

## Procedure

1. Frame the reader first, in one line. Before the directions, say who will use
   this thing and what they need from it. That one sentence is what makes the
   options mean something, a person judges a dashboard differently once they know
   it is for a standup glance versus a solo debugging session.
2. Hand over something concrete to react to (see techniques). Ground it in the
   user's real data so the thing being judged is the only variable. If this is a
   taste-first request, this is your first move, right after the one-line frame,
   not a later one. A set of clearly labelled options (A, B, C, D) written out is
   already a visual and is often enough; reach for a Mermaid or Excalidraw diagram
   only when the shape itself is the thing being judged. When you name the parts
   of an option (the axes a scorecard grades, the columns a table shows), gloss
   each one in brackets right there so the reader never has to leave the sentence.
3. Probe for unstated context the user would not think to volunteer: **who
   consumes this, where does it run, what does done look like to whoever inherits
   it.** Ask these deliberately. The decisive constraint usually arrives as a
   throwaway remark, and this probe is how you stop depending on luck. When the
   consumer is another team, offer the persona chip the profile describes, and
   keep any persona answer as advisory only.
4. When an extracted fact reshapes earlier decisions, say so and update the map.
   Quadrants are a living record, not a script.

**Done when** the user has reacted to something concrete, the context probes are
answered (or explicitly shrugged off), the extracted answers are on the map, and
any new durable taste has been proposed to memory.

## Techniques

- **Design directions.** Render the same real data four incompatible ways so the
  only variable is the design. Steal/skip chips under each assemble the reply.
  For users who will know it when they see it.
- **Mock before you wire.** A throwaway clickable mock with fake data, toggleable
  placements, A/B questions, before touching the real app. The user finds out
  what they want the moment they can click it.
- **Teach the vocabulary.** When the request is vague because the user lacks the
  domain's words, ladder from their words to the professional terms, each rung
  paired with the precise prompt it unlocks. Watch for a vocabulary collision:
  one word the user and the code use for different things (the user says
  "account", the code means `Customer`, `User`, or `Workspace`). When one
  surfaces, record it as the preferred term, the conflicting term, and an
  "avoid: X, Y" note, so the map's glossary can carry it and the next prompt does
  not reintroduce the confusion.
- **The concrete sample.** For non-visual outputs (a file format, an API
  response, a report), show the actual artifact with labeled fake data and
  per-line steal/skip choices, instead of asking the user to imagine columns.
