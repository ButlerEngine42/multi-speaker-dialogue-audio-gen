# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.6.x   | yes       |
| 0.5.x   | critical fixes only |
| < 0.5   | no        |

## Threat model

Plugins execute in-process. A malicious plugin can do anything the host
process can do. **Only load plugins you trust.** The loader refuses to
import from world-writable paths and logs every module it loads, but it is
not a sandbox.

If you want isolation, run the host with `--plugin-isolation subprocess`
(experimental, 0.6+), which forks each backend into its own process and
talks to it over a pipe.

## Reporting a vulnerability

Email `security@msdag.dev` with a repro. Do not open a public issue for
anything that lets a plugin escape the declared contract, overwrite
`renders/` outside its own job dir, or exfiltrate the config (which may
contain cloud TTS API keys).

We aim to acknowledge within 72h and patch within 14 days for high severity.

## Supply chain

- `pip-audit` runs in CI on every push to `main`.
- Plugin registry entries are pinned by sha256 in `config/plugins.lock`
  once they're promoted to the "verified" list.