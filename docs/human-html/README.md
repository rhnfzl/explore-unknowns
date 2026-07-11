# Human HTML Artifacts

## What lives here

This directory holds the HTML pages your team actually opens to review work.
Plans before they get built. Code reviews before they get merged. Architecture
explainers when someone new is trying to understand a system. Status snapshots
when a stakeholder asks "where are we." Decision aids when there is a real
choice to make.

If the artifact is meant for a human to read and act on, it lives here as
a single self-contained `.html` file. Open one in a browser, share the path,
print to PDF, archive it; it is portable and it is legible.

Agent scratch notes, ticket drafts, durable references, and meeting transcripts
stay as Markdown elsewhere in the repo. Those are the agent's memory layer.
This directory is the human's review layer.

## Naming pattern

```text
YYYY-MM-DD-kind-slug.html
```

Nested portable collections under `docs/human-html/<collection>/` may use short
filenames such as `index.html` or `flow-overview.html`. They are still checked
recursively for required metadata, the human body marker, and local links.

Allowed kinds:

```text
plan review architecture understanding research decision prototype status incident
```

## Commands

The script resolves the workspace root automatically by walking up from your
current directory. `<skill-dir>` is wherever your agent installed this skill
(e.g. `~/.claude/skills/human-html` for Claude Code, `~/.agents/skills/human-html`
for Codex):

```bash
python3 <skill-dir>/human_html_artifacts.py new plan "Title to review"
python3 <skill-dir>/human_html_artifacts.py check
python3 <skill-dir>/human_html_artifacts.py index
```

The `new` command refreshes `index.html` after creating an artifact. The
autoindex hook also regenerates `index.html` after direct edits to HTML files in
this directory.

## Canonical source

Skill: this skill's `SKILL.md`. Updates to the script, hooks,
or contract land there and propagate to every workspace that has wired the
hooks.
