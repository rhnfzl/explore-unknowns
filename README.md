<p align="center">
  <img src="assets/banner.webp" alt="explore-unknowns: map the unknowns of a task before you build it" width="100%">
</p>

# explore-unknowns

[![skills.sh](https://skills.sh/b/rhnfzl/explore-unknowns)](https://skills.sh/rhnfzl/explore-unknowns)
[![Release](https://img.shields.io/github/v/release/rhnfzl/explore-unknowns)](https://github.com/rhnfzl/explore-unknowns/releases)
[![License](https://img.shields.io/github/license/rhnfzl/explore-unknowns)](LICENSE)

**Find the unknowns before they find you.**

## Quickstart (30 seconds)

One command, and it auto-detects your installed agents; that is the whole setup:

```bash
npx skills add rhnfzl/explore-unknowns
```

Then, before you build something you do not fully understand yet, ask your agent to
"explore the unknowns", "do a blindspot pass", or "interview me about this change". It
walks you through a map of the task and hands the finished map back to you.

<details>
<summary>Other install routes and manual use</summary>

- `npx openskills install rhnfzl/explore-unknowns` (AGENTS.md ecosystems)
- Claude Code natively: `/plugin marketplace add rhnfzl/explore-unknowns`, then `/plugin install explore-unknowns@rhnfzl`
- Manual: clone this repo and symlink it into your agent's skills directory (`~/.claude/skills/`, `~/.codex/skills/`, or `~/.agents/skills/`)

</details>

## Why this exists

The map is not the territory. Your prompt, your plan, and the context window are the map.
The codebase, the domain, and what you actually want are the territory. The gap between
them is the unknowns.

- **Unknowns are cheapest before code.** An assumption caught in a two-minute conversation
  costs two minutes. The same assumption caught three pull requests later costs the three
  pull requests.
- **You know more than you can say up front.** Reacting to a concrete option pulls out
  taste you cannot produce from a blank prompt. So the walk hands you things to react to,
  it does not quiz you.
- **A plan you cannot read is not a plan.** The walk explains before it cites, defines its
  terms, and keeps file paths out of the prose. You finish holding a map you actually
  understand.

## The four quadrants

The walk fills in one map with four regions, one per kind of unknown:

| Quadrant | Plain name | What it holds |
|---|---|---|
| Known knowns | **Settled ground** | What the code and your notes already pin down. |
| Known unknowns | **Open decisions** | The questions you can name, resolved highest-stakes first. |
| Unknown knowns | **Taste** | The preferences you have but never wrote down. |
| Unknown unknowns | **Landmines** | The traps you would only find by stepping on them. |

## The five stages

Walked in order, one at a time, so you always know where you stand.

1. **Settled ground.** Scan the territory, capture the starting state, surface what is
   already decided.
2. **Open decisions.** One question at a time, highest-stakes first, each with a
   recommended answer you can override.
3. **Taste.** Probe only the preferences nobody has written down yet.
4. **Landmine sweep.** A fixed checklist of trap families, then a free sweep.
5. **The map.** Hand it over. The walk is done only when the map is in your hands.

Implementation is a separate task that starts after the map is delivered. The map is the
deliverable, not the code.

## What is in the box

| Path | What it is |
|---|---|
| `SKILL.md` | The portable spine: the walk, its three moves, its rules. |
| `references/` | One file per stage, plus an after-the-walk guide, read as each stage opens. |
| `territory.example.md` | Fill-in-the-blanks template for your own project profile. |
| `evals/evals.json` | Example prompts and the behavior each should produce. |

## Writing your own territory profile

The walk is domain-agnostic on its own. Everything specific to a project (which graph to
query, where maps get committed, which trap families to sweep, what the map feeds into)
lives in one optional file: `territory.md`.

Copy `territory.example.md` to `territory.md` next to the skill and fill in your project.
With a profile present, the walk uses it. With none, it runs as a plain general interview.
That is the whole extension mechanism: one swappable file, no config schema.

Your filled-in `territory.md` is gitignored by default, because it describes your own
workspace. Ship only the example.

## Trust

- No telemetry, no analytics, no phone-home.
- No executable code. The skill is Markdown plus one JSON file of evals; installing copies
  files, it does not run anything.
- No network calls. Any research the walk suggests uses your own agent's tools, under your
  control.
- Local by default. Maps are self-contained files in your workspace; sharing is an explicit
  act. See [SECURITY.md](SECURITY.md).

## Agent support

Any agent that loads a `SKILL.md` works: Claude Code, Codex, Cursor, and the rest of the
`npx skills` / `openskills` ecosystem. The walk delegates to sibling skills (grilling for
the interview, an HTML-artifact skill for committed maps, a research skill for deep dives)
when they are installed, and falls back to doing that work inline when they are not. It
degrades, it never stalls.

## Credits

Built on the framing in Thariq's [A Field Guide to Fable: Finding Your Unknowns](https://x.com/trq212/article/2073100352921215386). The map-and-territory idea, and the four kinds of unknown, come from there.

## License

MIT. See [LICENSE](LICENSE).
