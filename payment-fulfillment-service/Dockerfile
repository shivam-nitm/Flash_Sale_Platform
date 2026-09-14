FROM eclipse-temurin:21-jdk-alpine
WORKDIR /app
COPY target/payment-fulfillment-service-1.0.0-SNAPSHOT.jar app.jar
EXPOSE 8084
ENTRYPOINT ["java", "-jar", "app.jar"]
