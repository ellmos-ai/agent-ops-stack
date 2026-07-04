# Security Policy

`agent-ops-stack` itself is a manifest + a thin installer. `install.sh` only performs
public, read-only `git clone` operations over HTTPS into a gitignored `./modules/`
directory — it does not read or write credentials, does not call any network endpoint
other than GitHub, and does not register anything with an MCP host or agent
configuration.

## Scope

Security issues in the composed modules should be reported to those repositories
directly:

- [dev-bricks/ticket-master](https://github.com/dev-bricks/ticket-master)
- [dev-bricks/lock-master](https://github.com/dev-bricks/lock-master)
- [ellmos-ai/build-your-users-mind](https://github.com/ellmos-ai/build-your-users-mind)
- [ellmos-ai/skills](https://github.com/ellmos-ai/skills)
- [ellmos-ai/ellmos-controlcenter-mcp](https://github.com/ellmos-ai/ellmos-controlcenter-mcp)
- [ellmos-ai/ellmos-homebase-mcp](https://github.com/ellmos-ai/ellmos-homebase-mcp)

## Reporting a Vulnerability

If you find an issue specific to this repository (the manifest, the installer script,
or the documentation), please open a GitHub issue or contact the maintainers listed on
the [ellmos-ai](https://github.com/ellmos-ai) organization profile.
