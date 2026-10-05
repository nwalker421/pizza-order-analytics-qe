# Quality Engineering Artifacts

This folder contains the Quality Engineering test management artifacts for the Pizza Order Analytics project.

The project demonstrates an end-to-end Quality Engineering workflow from requirements and acceptance criteria through test design, automation, traceability, and continuous integration.

## QA Test Management Workbook

**Pizza_Order_Analytics_QE_Test_Management.xlsx**

The finalized QA workbook provides traceability across **6 functional requirements, 33 acceptance criteria, and 42 formal test cases (TC-001 through TC-042).**

The workbook contains:

- **Test Cases** — 42 detailed functional test cases derived from the project requirements and acceptance criteria, including positive, negative, alternate, boundary, and edge-case coverage.
- **Requirements Traceability Matrix (RTM)** — provides many-to-many traceability between requirements, acceptance criteria, formal test cases, implementation/test components, automation, CI execution, and results.
- **Test Execution Results** — supports recording execution evidence, expected and actual results, execution status, defects, and applicable GitHub Actions references.

## Requirements Coverage

The QA baseline covers:

- **REQ-001** — Process Pizza Order Data
- **REQ-002** — Normalize Topping Combinations
- **REQ-003** — Calculate Topping Combination Frequency
- **REQ-004** — Rank Topping Combinations
- **REQ-005** — Return Top 20 Topping Combinations
- **REQ-006** — Produce Ranked Results

Functional requirements and acceptance criteria are maintained in [`/docs/requirements.md`](../docs/requirements.md).

## Test Automation

Executable automated tests are maintained in the [`/tests`](../tests) directory using **Python and pytest**.

Current automated regression suite:

- **45 automated pytest tests**
- **45 passed**
- **0 failed**
- **100% passing**
- Executed automatically through **GitHub Actions CI**

The automated suite validates functional processing, normalization, frequency calculation, ranking, deterministic tie handling, Top-20 boundary behavior, invalid-data handling, and human-readable result formatting.

## Quality Engineering Workflow

The repository demonstrates the following end-to-end QE lifecycle:

**Requirements → Acceptance Criteria → Test Design → RTM Traceability → Python/pytest Automation → GitHub Actions CI → Test Results**

This structure provides auditable traceability from each business requirement through its associated acceptance criteria and formal test coverage while maintaining automated regression validation within the CI pipeline.
