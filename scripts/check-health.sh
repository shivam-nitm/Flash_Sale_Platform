#!/bin/bash
echo "Checking Docker container health..."
docker ps --format "table {{.Names}}	{{.Status}}	{{.Ports}}"
