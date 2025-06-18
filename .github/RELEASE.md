# Release Checklist

Use this checklist before triggering a new release via GitHub.

## Versioning

- [ ] Increment the version number in `pyproject.toml`
  - Follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`

## Code & Tests

- [ ] Run the test suite locally
- [ ] Check linting & formatting
- [ ] Ensure new dependencies (if any) are listed in `pyproject.toml`

## Documentation

- [ ] Update `README.md` with new or changed usage instructions
- [ ] Update `CHANGELOG.md` with:
  - New features
  - Fixes
  - Any breaking changes

## Cleanup

- [ ] Confirm `dist/`, `build/`, and `*.egg-info/` are not checked in or are ignored

## Finalize

Once all checks are complete, trigger the release on GitHub.
