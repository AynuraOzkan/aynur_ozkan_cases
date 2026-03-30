# Load Test Scenarios - n11.com Search Module

## 1. Purpose
The purpose of this load test is to analyze the behavior, stability, and performance of the **search module** on https://www.n11.com/.

This includes measuring:
- Response times for homepage and search requests
- Stability of search result listing pages under repeated requests
- Failure rates (HTTP errors, forbidden responses, timeouts)
- Pagination performance after a search operation

---

## 2. Scope
This test covers the following functional flow:

1. Open the homepage (`/`)
2. Perform product searches using the search endpoint (`/arama?q=<keyword>`)
3. Load search results listing pages
4. Navigate through pagination pages after searching

This test is executed with **1 virtual user**, as required in the case.

---

## 3. Scenarios

### Scenario 1: Homepage Load
**Objective:** Validate that the homepage loads successfully and measure response time.

**Request:**
- `GET /`

**Expected Result:**
- HTTP 200 response
- Homepage loads without errors

---

### Scenario 2: Product Search
**Objective:** Simulate the usage of the search bar by searching different product keywords and measuring response time.

**Requests (examples):**
- `GET /arama?q=telefon`
- `GET /arama?q=laptop`
- `GET /arama?q=ayakkabı`
- `GET /arama?q=kamera`
- `GET /arama?q=tablet`
- `GET /arama?q=çanta`

**Expected Result:**
- HTTP 200 response for each search query
- Search results listing page loads correctly

---

### Scenario 3: Search Results Pagination
**Objective:** Validate performance of listing pages after a search by navigating result pages.

**Requests:**
- `GET /arama?q=telefon&pg=1`
- `GET /arama?q=telefon&pg=2`

**Expected Result:**
- HTTP 200 response for each pagination request
- Pages load consistently without significant delay

---

## 4. Success Criteria
The test is considered successful if:

- Homepage requests return HTTP 200
- Search requests return HTTP 200
- Pagination requests return HTTP 200
- No unexpected crashes or timeouts occur
- Response times remain stable during the 5-minute run

If the system responds with **HTTP 403 Forbidden**, it indicates bot/WAF protection on production environment.
In that case, the test outcome should be documented as an environment limitation rather than a script failure.

---

## 5. Run Command

The load test is executed using Locust with 1 user and a total runtime of 5 minutes:

```bash
locust -f locustfile.py --host https://www.n11.com --run-time 5m --csv=n11_test