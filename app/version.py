"""Single source of truth for the service version.

Rules (Semantic Versioning, https://semver.org):
  MAJOR.MINOR.PATCH  ->  breaking . new feature . bug fix
  "-dev" suffix      ->  work in progress, not released yet

Only the Release team (Team 6 - Launch Crew) changes this line,
in the same Pull Request that updates CHANGELOG.md.
"""

__version__ = "0.1.0-dev"
