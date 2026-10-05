# Pizza Order Analytics — Quality Engineering Portfolio Project

A Quality Engineering portfolio project demonstrating an end-to-end software quality lifecycle using **Python, pytest, GitHub Actions CI/CD, requirements-based test design, and requirements traceability**.

The application analyzes pizza order data to identify and rank the **20 most frequently ordered topping combinations** while handling normalization, invalid input, deterministic ranking, boundary conditions, and human-readable output.

## Project Highlights

- **6 functional requirements**
- **33 acceptance criteria**
- **42 formal test cases**
- **45 automated pytest tests**
- **100% passing automated regression suite**
- Requirements Traceability Matrix (RTM)
- Positive, negative, alternate, boundary, and edge-case testing
- Automated CI execution through GitHub Actions
- Deterministic ranking and tie-handling validation
- Requirements-to-test-to-automation traceability

## Quality Engineering Workflow

**Requirements → Acceptance Criteria → Test Design → RTM → Python/pytest Automation → GitHub Actions CI → Test Results**

The project demonstrates how requirements are translated into testable acceptance criteria, formal test cases, automated regression tests, and continuous integration validation.

## Functional Scope

| Requirement | Capability |
|---|---|
| REQ-001 | Process Pizza Order Data |
| REQ-002 | Normalize Topping Combinations |
| REQ-003 | Calculate Topping Combination Frequency |
| REQ-004 | Rank Topping Combinations |
| REQ-005 | Return Top 20 Topping Combinations |
| REQ-006 | Produce Ranked Results |

Detailed requirements and acceptance criteria are maintained in [`docs/requirements.md`](docs/requirements.md).

## Test Strategy and Coverage

The test suite validates:

- Valid and invalid pizza-order data
- Single- and multi-topping combinations
- Topping-order normalization
- Case and whitespace normalization
- Duplicate topping quantities
- Frequency calculation
- Descending frequency ranking
- Deterministic alphabetical tie handling
- Top-20 selection
- 19 / 20 / 21 combination boundary conditions
- Empty-result behavior
- Ranked human-readable output

Formal QA artifacts are maintained in the [`qa`](qa) directory.

## Test Automation

Automated regression testing is implemented using **Python and pytest**.

Current CI baseline:

| Metric | Result |
|---|---:|
| Automated Tests | 45 |
| Passed | 45 |
| Failed | 0 |
| Pass Rate | 100% |

Automated tests are maintained in [`tests/test_pizza_analyzer.py`](tests/test_pizza_analyzer.py).

## Continuous Integration

GitHub Actions automatically executes the pytest regression suite when changes are pushed to the repository.

The CI pipeline validates that application and test changes do not introduce regression failures before integration into the primary branch.

## Requirements Traceability

The project includes a Requirements Traceability Matrix connecting:

**Requirement → Acceptance Criterion → Formal Test Case → Automated Test → CI Execution → Result**

The finalized QA workbook contains **42 formal test cases (TC-001 through TC-042)** covering all **33 acceptance criteria**.

See [`qa/Pizza_Order_Analytics_QE_Test_Management.xlsx`](qa/Pizza_Order_Analytics_QE_Test_Management.xlsx) for the complete test-management workbook and RTM.

## Repository Structure

```text
pizza-order-analytics-qe/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── docs/
│   └── requirements.md
├── qa/
│   ├── Pizza_Order_Analytics_QE_Test_Management.xlsx
│   └── README.md
├── src/
│   └── pizza_analyzer.py
├── tests/
│   └── test_pizza_analyzer.py
├── README.md
└── requirements.txt

Tools and Technologies
- Python
- pytest
- GitHub
- GitHub Actions
- Microsoft Excel
- Requirements Traceability Matrix (RTM)
- Risk- and requirements-based test design

Quality Engineering Objectives
This project demonstrates practical Quality Engineering capabilities, including requirements analysis, testability assessment, functional test design, boundary and negative testing, automation development, regression testing, CI/CD integration, defect prevention, and end-to-end requirements traceability.
