# n11.com Search Load Test (Locust)

This repository contains a Locust-based load test implementation for analyzing the behavior and performance of the search module of **https://www.n11.com/**.

## Scope
The test covers:
- Homepage load (`/`)
- Search requests (`/arama?q=...`)
- Search result listing pages (pagination)

## Tech Stack
- Python 3.x
- Locust

## Installation

### 1) Clone repository
```bash
git clone <repo-url>
cd n11-load-test