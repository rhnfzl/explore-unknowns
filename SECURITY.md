# Security

This skill ships instructions, not code.

- **No executable code.** The skill is Markdown (`SKILL.md`, `references/*.md`,
  `territory.example.md`) plus one JSON file of evals. There is no Python, no shell
  script, no `bin`, and no `postinstall`. Installing it copies files; it does not run
  anything.
- **No network calls.** Nothing in the skill fetches, uploads, or phones home. Any web
  research the walk suggests uses your agent's own tools, under your control, never a
  bundled endpoint.
- **No telemetry, no analytics.** The skill collects nothing.
- **Local by default.** Maps the walk produces are written to your own workspace as
  self-contained files. Sharing anything is an explicit action you take.

## Reporting

Found something that looks unsafe, or a false positive from an automated scanner? Open
an issue at https://github.com/rhnfzl/explore-unknowns/issues.
