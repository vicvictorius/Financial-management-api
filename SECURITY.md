# Security

## Dependency Vulnerability Exception

### PYSEC-2026-1325

The dependency `ecdsa` is currently installed transitively through
`python-jose`.

The application uses JWT with the `HS256` algorithm. The application
does not use ECDSA-based JWT algorithms such as `ES256`, `ES384`, or
`ES512`.

Therefore, the vulnerable ECDSA functionality is not used by the
current authentication implementation.

The vulnerability is explicitly ignored by `pip-audit` until an
upstream dependency provides a suitable fix or the JWT dependency is
replaced.

The exception is defined in `.pip-audit-ignore.txt`.

