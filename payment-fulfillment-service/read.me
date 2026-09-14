# 💳 `payment-fulfillment-service` — Payment Processing & Saga Orchestration

Welcome to **`payment-fulfillment-service`**! This repository handles payment transactions, shipment dispatch simulation, and Saga Workflow Orchestration with automated compensations.

> **GitHub Repository URL**: [https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/payment-fulfillment-service](https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/payment-fulfillment-service)

---

## 🎯 Distributed Workflows (Saga Pattern)

### Happy Path:
1. `OrderCreated` ➔ Reserve Stock ➔ Charge Payment ➔ Create Shipment ➔ Mark `Order FULFILLED`.

### Compensation Path (Payment Success, Shipment Failure - T-009):
1. Payment succeeds ➔ Shipment API returns HTTP 500.
2. Saga Orchestrator triggers **Compensating Action**:
   - Issue Payment Refund
   - Release Reserved Inventory
   - Mark Order `CANCELLED` (**FR-012**).
