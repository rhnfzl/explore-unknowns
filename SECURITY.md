# Security

This repository ships declarative skill instructions and evaluation material, not a
runtime integration.

- **No automatic execution.** The installed skill is Markdown and JSON. The repository
  also includes an inert Python source fixture for evaluation and static HTML review
  documents with local display scripts. There is no `bin`, shell script, install hook,
  or `postinstall`; installing the skill does not execute those files.
- **No bundled network client.** The skill does not fetch, upload, or phone home, and the
  static review documents make no external requests. Any web research the walk suggests
  uses your agent's own tools under your control, never a bundled endpoint.
- **No telemetry, no analytics.** The skill collects nothing.
- **Local by default.** Maps the walk produces are written to your own workspace as
  self-contained files. Sharing anything is an explicit action you take.

## Reporting

Found something that looks unsafe, or a false positive from an automated scanner? Open
an issue at https://github.com/rhnfzl/explore-unknowns/issues.
