# After the walk

The map lives on past planning. Three moves for the phases that follow. Each one
prefers an existing skill over a reimplementation.

- **Implementation notes** (during the build). Keep a running log in the skeleton
  the handoff prompt carried: Deviations as planned / actual / why / risk, New
  unknowns, Verification. Follow the handoff prompt's stop-and-ask rule: when the
  deviation touches architecture, data migration, security, cost, or user-visible
  behavior, stop and ask; otherwise record it, take the conservative call, and
  keep going. Tag entries that need the user's judgment. Each deviation is an
  unknown unknown that escaped the walk, so fold it back into the map for the next
  attempt. This is the same skeleton the builder was handed, so notes started
  during the build already have their home.

- **The buy-in doc** (before shipping). Other people inherit your unknowns.
  Package the prototype, the spec, and the notes into one skimmable pitch that
  leads with a demo, pre-answers each reviewer's objections with evidence, states
  the assumptions that were never verified (reviewers inherit exactly those), and
  names who signs off on what. With a territory profile that already owns a
  human-facing artifact lane, build this with that lane's skill rather than a
  boutique page.

- **Quiz before merge** (before merging a long diff or someone else's change). A
  merge-readiness report: the mental model, the non-obvious behaviors introduced,
  the assumptions still unverified, and what to watch after deploy, ending in a
  quiz the user must pass. Wrong answers point back to the section they skimmed.
  Only merge after passing.

A note on scope. This skill maps unknowns and hands over a map. It does not run
the build, the review, or the merge. Those are separate tasks, and in a workspace
with its own review and test pipeline they have their own skills. Point at them;
do not absorb them.
