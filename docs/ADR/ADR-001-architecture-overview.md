# ADR-001: Architecture Overview & Service Decomposition

## Status
Accepted

## Context
We are building a Flash Sale Platform capable of supporting 100k+ RPS under extreme stock contention.

## Decision
We decompose the domain into event-driven microservices:
1. `catalog-service`
2. `inventory-service`
3. `order-service`
4. `payment-fulfillment-service`
5. `event-bus`

## Consequences
- Pros: Cohesive domain boundaries, independent scaling.
- Cons: Requires distributed transaction handling (Saga/Outbox).
