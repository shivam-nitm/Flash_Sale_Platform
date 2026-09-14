# ADR-002: Inventory Stock Locking Strategy

## Status
Accepted

## Context
High concurrent purchase requests hit limited inventory simultaneously.

## Decision
1. Redis Lua scripts for fast pre-reservation atomic decrement.
2. PostgreSQL optimistic locking (`version` field) as source-of-truth backup.
