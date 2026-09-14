# 📦 `catalog-service` — Flash Sale Product Catalog Microservice

Welcome to the **`catalog-service`** repository! This service manages product metadata, pricing, flash sale window definitions, and high-performance Redis cache-aside reads.

> **GitHub Repository URL**: [https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/catalog-service](https://github.com/shivam-nitm/Flash_Sale_Platform/tree/main/catalog-service)

---

## 🎯 Purpose & Scope

The `catalog-service` is responsible for:
1. **Product Metadata CRUD**: Creating, reading, and updating product catalogs, pricing, and sale schedules (**FR-001**).
2. **Redis Cache-Aside**: Offloading read traffic from PostgreSQL to Redis for hot flash sale items (**FR-006**).
3. **Cache Stampede & Hot Key Protection**: Utilizing probabilistic early expiration and mutex locks to prevent database overload during cache key expiration (**T-005**).
4. **Resilience & Fallbacks**: Returning graceful degraded product views if Redis or DB is degraded (**FR-007**, **T-015**).

---

## ⚙️ Tech Stack

- **Language**: Java 21 (Virtual Threads enabled)
- **Framework**: Spring Boot 3.2+
- **Database**: PostgreSQL 16 (JPA / Hibernate)
- **Cache**: Redis 7 (Lettuce client)
- **Resilience**: Resilience4j (Circuit Breaker & Rate Limiter)
- **Observability**: OpenTelemetry, Micrometer, Prometheus

---

## 📁 Repository Structure

```
catalog-service/
├── src/
│   ├── main/
│   │   ├── java/com/flashsale/catalog/
│   │   │   ├── CatalogServiceApplication.java
│   │   │   ├── controller/ProductController.java
│   │   │   ├── domain/Product.java
│   │   │   ├── dto/ProductDto.java
│   │   │   ├── repository/ProductRepository.java
│   │   │   └── service/ProductService.java
│   │   └── resources/
│   │       ├── application.yml
│   │       └── db/migration/V1__init_catalog.sql
│   └── test/
├── Dockerfile
├── pom.xml
└── README.md
```

---

## 🔌 API Endpoints

### 1. Create Product
- **POST** `/api/v1/products`
```json
{
  "name": "Flagship Smartphone Pro 15",
  "description": "Flash sale special edition",
  "price": 999.99,
  "initialStock": 1000,
  "saleStartTime": "2026-09-14T12:00:00Z",
  "saleEndTime": "2026-09-14T13:00:00Z"
}
```

### 2. Get Product by ID (Cached)
- **GET** `/api/v1/products/{id}`
- **Headers**: `X-Correlation-ID: <uuid>`

---

## 🏃 Getting Started for Developers

### Prerequisites
- JDK 21+
- Maven 3.9+
- Docker running PostgreSQL and Redis (via root `docker-compose.yml`)

### Run Locally
```bash
mvn clean spring-boot:run
```
