# Changelog

All notable changes to this skill are documented here. The version in this file,
in `.claude-plugin/plugin.json`, and in `SKILL.md`'s frontmatter must always match
the release tag; the release workflow fails loudly if they drift.

## Unreleased

- Corrected the lifecycle so pre-build work uses the five-stage walk while direct
  mid-build and post-build work starts from the phase already in progress.
- Kept every discovery in one broad four-quadrant map, prioritized as Changes this
  task, Nearby finding, or Urgent outside scope.
- Made maps, implementation ledgers, and post-build explainers task-scoped, with
  deliberate same-task reuse and safe suffixes for different-task collisions.
- Expanded eval coverage for direct lifecycle entrances, scan-first context, adaptive
  tracing, discovery priorities, and artifact collisions.

## 1.0.0 - 2026-07-10

Initial release.

- The quadrant walk: a five-stage interview that maps a task's unknowns and hands
  over a four-quadrant map (settled ground, open decisions, taste, and landmines).
- Portable spine plus a swappable `territory.md` profile. The walk runs as a plain
  general interview with no profile, and picks up project-specific behavior when one
  is present. `territory.example.md` is the fill-in-the-blanks template.
- Plain-language mandate throughout: explain before you cite, define coined terms on
  first use, keep file paths out of the prose and tucked into a separate evidence area.
- Graceful delegation to grilling, artifact, and research skills when installed, with
  a self-contained inline fallback when they are not.
