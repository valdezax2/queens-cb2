#!/bin/bash

echo "=========================================="
echo "CSV Uploader Test Suite"
echo "=========================================="

# Test 1: Check if CSV exists
echo -e "\n[TEST 1] Checking for links_table_with_status.csv..."
if [ -f "links_table_with_status.csv" ]; then
    SIZE=$(wc -c < links_table_with_status.csv)
    ROWS=$(wc -l < links_table_with_status.csv)
    echo "✅ CSV file found"
    echo "   Size: $((SIZE / 1024)) KB"
    echo "   Rows: $ROWS"
else
    echo "❌ CSV file not found - Run link verifier first"
    exit 1
fi

# Test 2: Check if Python dependencies exist
echo -e "\n[TEST 2] Checking Python dependencies..."
python3 -c "import requests" 2>/dev/null && echo "✅ requests module available" || echo "⚠️ requests module missing"

# Test 3: Test server connectivity
echo -e "\n[TEST 3] Testing server connectivity..."
if timeout 2 bash -c 'echo > /dev/tcp/127.0.0.1/8774' 2>/dev/null; then
    echo "✅ Server is reachable on port 8774"
else
    echo "⚠️ Server not found on port 8774"
    echo "   Start server with: nc -l 127.0.0.1 8774"
fi

# Test 4: Run uploader script
echo -e "\n[TEST 4] Running CSV uploader..."
python3 03_csv_uploader.py

echo -e "\n=========================================="
echo "Tests Complete"
echo "=========================================="
