# 🚌 `event-bus` — Async Messaging Schemas, Outbox Relay & DLQ Handler

Welcome to **`event-bus`**! This repository defines Kafka event schemas, the Outbox Relay poller worker, consumer idempotency libraries, and poison message Dead Letter Queue (DLQ) retry routers.

> **GitHub Repository URL**: [https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/event-bus](https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/event-bus)

---

## 🎯 Features

1. **Event Schemas**: Defined in Avro / JSON Schema (`OrderCreatedEvent`, `StockReservedEvent`).
2. **Consumer Idempotency**: Deduplication using explicit event message IDs (**FR-009**, **T-006**).
3. **Poison Message Router**: Exponential backoff retries ➔ DLQ routing (**FR-010**, **T-007**).
