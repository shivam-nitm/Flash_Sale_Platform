# 🛡️ `inventory-service` — High-Concurrency Stock Reservation Service

Welcome to the **`inventory-service`** repository! This microservice enforces inventory correctness and stock reservation logic under ultra-high concurrency.

> **GitHub Repository URL**: [https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/inventory-service](https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/inventory-service)

---

## 🎯 Core Invariants & Requirements

1. **Zero Overselling Invariant**: `available + reserved + sold == initial_stock` (**INV-1**).
2. **Locking Strategies**:
   - **Optimistic Locking**: JPA `@Version` column to catch race conditions (**T-003**).
   - **Pessimistic Locking**: `SELECT FOR UPDATE` for strict serializability under high conflict (**Phase 2**).
   - **Redis Atomic Counter**: Fast Lua scripts for fast pre-reservation (**FR-004**).
3. **Reservation Expiration Worker**: Expiration TTL task to release uncompleted checkout stock exactly once (**FR-005**).

---

## 📁 Repository Structure

```
inventory-service/
├── src/
│   ├── main/
│   │   ├── java/com/flashsale/inventory/
│   │   │   ├── InventoryServiceApplication.java
│   │   │   ├── domain/Inventory.java
│   │   │   ├── domain/Reservation.java
│   │   │   ├── repository/InventoryRepository.java
│   │   │   └── service/ReservationService.java
│   │   └── resources/
│   │       ├── application.yml
│   │       └── scripts/reserve_stock.lua
│   └── test/
├── Dockerfile
├── pom.xml
└── README.md
```

---

## ⚡ Redis Stock Reservation Lua Script (`reserve_stock.lua`)

```lua
local stock_key = KEYS[1]
local requested = tonumber(ARGV[1])
local current_stock = tonumber(redis.call('get', stock_key) or "0")

if current_stock >= requested then
    redis.call('decrby', stock_key, requested)
    return 1
else
    return 0
end
```
