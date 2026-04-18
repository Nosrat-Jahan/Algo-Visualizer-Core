# Security Policy | Algo-Visualizer Core

This document outlines the security procedures and reporting protocols for the **Algo-Visualizer Core** engine. As a project focused on algorithmic integrity, ensuring a secure environment for users and developers is a top priority.

## Supported Versions
Only the latest stable release is currently supported for security updates.

| Version | Supported          |
| ------- | ------------------ |
| v6.6.6  | :white_check_mark: |
| < v6.0  | :x:                |

## Reporting a Vulnerability
If you discover a security vulnerability or a logic flaw that could be exploited, please follow these steps:

1. **Do Not Open a Public Issue**: To prevent exploitation, please do not report security bugs through the public issue tracker.
2. **Contact the Developer**: Directly reach out via GitHub or professional contact channels.
3. **Disclosure**: Once the vulnerability is reported, I will investigate and implement a patch. A public disclosure will be made once the fix is deployed.

## Security Standards
This project adheres to the following practices:
- **Zero-Dependency Core**: Minimizing external libraries to reduce the attack surface.
- **Input Sanitization**: Ensuring all dynamic array inputs are validated.
- **Async Safety**: Preventing race conditions during algorithmic execution.

---
**Build:** v6.6.6 | **Academic:** BSc in CSE | **Status:** Active Security Monitoring
