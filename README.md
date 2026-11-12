# offsec-notebook

Public log of my move from senior software engineering (payments, OAuth/SSO, Electron, CI/CD) into offensive security.

Every lab note records three things: the root cause, the payload, and how I would have prevented it as the engineer who wrote the code.

## Layout

| Path | What lives there |
|---|---|
| `labs/portswigger/` | PortSwigger Web Security Academy notes, one file per topic |
| `writeups/` | Long-form posts and disclosure write-ups (published after fixes ship) |
| `tools/` | Small Python/Go tools written while solving labs |
| `templates/` | Note templates |

## Rules of engagement

- Testing happens only in official labs, on my own machines and cloud accounts, or inside a program's published scope.
- Open-source vulnerabilities are reported privately to maintainers first and written up only after a fix is released.
- Nothing from any employer's code or systems appears here.
