# 🛒 `order-service` — Order Management & Transactional Outbox Engine

Welcome to **`order-service`**! This repository handles purchase order placement, explicit lifecycle state transitions, and guaranteed event publishing using the Transactional Outbox pattern.

> **GitHub Repository URL**: [https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/order-service](https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/order-service)

---

## 🎯 Domain Requirements & Invariants

1. **State Machine Transitions**:
   - `CREATED` ➔ `RESERVED` ➔ `PAID` ➔ `FULFILLED`
   - Failure states: `CANCELLED`, `REFUNDED` (**FR-003**).
2. **Transactional Outbox Pattern**:
   - Save Order to `orders` table AND message payload to `outbox_messages` table within the **SAME local DB transaction** (**FR-011**, **T-010**).
   - Prevents lost events if the server crashes after DB commit but before Kafka publication.

---

## 📁 Repository Structure

```
order-service/
├── src/
│   ├── main/
│   │   ├── java/com/flashsale/order/
│   │   │   ├── OrderServiceApplication.java
│   │   │   ├── domain/Order.java
│   │   │   ├── domain/OrderStatus.java
│   │   │   ├── domain/OutboxMessage.java
│   │   │   └── service/OrderService.java
│   │   └── resources/application.yml
├── Dockerfile
├── pom.xml
└── README.md
```
