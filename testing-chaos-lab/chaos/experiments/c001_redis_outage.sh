#!/bin/bash
echo "Simulating Redis Outage..."
docker stop flashsale-redis
sleep 30
docker start flashsale-redis
echo "Redis restored."
