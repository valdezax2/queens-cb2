# CSV Uploader - Queens CB2 Link Verification Pipeline

Complete automated workflow for scraping links, verifying their status, and uploading data to a remote server.

## 📋 Overview

This project consists of three integrated components:

### Step 1️⃣: Link Grabber
**File**: `01. all_link_grabber.ipynb`
- Scrapes all links from Queens CB2 website pages
- Exports to `links_table.csv`
- ~900+ links extracted

### Step 2️⃣: Link Verifier
**File**: `02. link_verify.ipynb`
- Validates HTTP status for each link
- Tests both HEAD and GET requests
- Exports to `links_table_with_status.csv`
- Rate limited: 1 second per 50 requests

### Step 3️⃣: CSV Uploader (NEW)
**Files**: 
- `03_csv_uploader.py` - Python script
- `03_csv_uploader.ipynb` - Jupyter notebook
- `test_uploader.sh` - Test harness

Sends verified CSV data to remote server via POST request.

---

## 🚀 Quick Start

### Prerequisites
```bash
# Install Python requests library
pip install requests
```

### Run the Upload Workflow

**Option 1: Using Python Script**
```bash
cd /workspaces/queens-cb2/homepage/link_grabber
python3 03_csv_uploader.py
```

**Option 2: Using Jupyter Notebook**
```bash
# Open in VS Code or Jupyter Lab
# Run cells in order
```

**Option 3: Using Test Harness**
```bash
cd /workspaces/queens-cb2/homepage/link_grabber
chmod +x test_uploader.sh
./test_uploader.sh
```

---

## 📊 Input/Output Files

| Step | Input | Output | Status |
|------|-------|--------|--------|
| 1️⃣ Link Grabber | Queens CB2 URLs | `links_table.csv` | ✅ Complete |
| 2️⃣ Link Verifier | `links_table.csv` | `links_table_with_status.csv` | ✅ Complete |
| 3️⃣ CSV Uploader | `links_table_with_status.csv` | HTTP 200 Response | 🔄 New |

---

## 🔧 Configuration

### Server Endpoint
Default: `http://127.0.0.1:8774`

To change, edit either file:
- **Python**: Line 3 of `03_csv_uploader.py`
- **Notebook**: Cell titled "Configuration"

```python
endpoint='http://127.0.0.1:8774'  # Change this URL
```

### Timeout
Default: 30 seconds

```python
self.timeout = 30  # Change in Python script
timeout_seconds = 30  # Change in notebook
```

---

## 📤 How It Works

### 1. CSV Validation
- Checks if `links_table_with_status.csv` exists
- Reports file size and row count

### 2. Data Loading
- Reads entire CSV into memory
- Parses header and sample rows

### 3. Server Upload
- Sends as multipart/form-data
- Includes metadata:
  - Timestamp (ISO 8601)
  - Source (queens-cb2-link-grabber)
  - Version (1.0)

### 4. Response Handling
- Success: HTTP 200, 201, 202
- Failure: Connection error, timeout, or server error
- Prints response status and body (first 500 chars)

---

## 🛠️ Testing

### Test 1: CSV File Validation
```bash
ls -lh links_table_with_status.csv
```

### Test 2: Python Dependencies
```bash
python3 -c "import requests; print('✅ requests available')"
```

### Test 3: Server Connectivity
```bash
# Check if server is running on port 8774
netstat -tuln | grep 8774

# Or test connection
curl -X POST http://127.0.0.1:8774 -d "test=true"
```

### Test 4: Full Workflow
```bash
./test_uploader.sh
```

---

## 🌐 Setting Up Server (Optional)

### Simple Test Server (NetCat)
```bash
# Terminal 1: Start server
nc -l 127.0.0.1 8774

# Terminal 2: Run uploader
python3 03_csv_uploader.py
```

### Python Test Server
```python
# save as simple_server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class UploadHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        print(f"✅ Received upload: {len(body)} bytes")
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        response = {
            'status': 'success',
            'bytes_received': len(body),
            'message': 'CSV uploaded successfully'
        }
        self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8774), UploadHandler)
    print("✅ Server listening on http://127.0.0.1:8774")
    server.serve_forever()
```

Run with:
```bash
python3 simple_server.py
```

---

## ⚠️ Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| CSV file not found | Step 2 not completed | Run `02. link_verify.ipynb` first |
| Connection Error | Server not running | Start server on port 8774 |
| Timeout | Server too slow | Increase `timeout_seconds` |
| HTTP 400/404 | Wrong endpoint | Check `endpoint` URL |
| HTTP 500 | Server error | Check server logs |

---

## 📝 API Contract

### Request
```
POST http://127.0.0.1:8774
Content-Type: multipart/form-data

file: (CSV file content)
metadata: {
  "timestamp": "2025-11-02T10:30:45.123456",
  "source": "queens-cb2-link-grabber",
  "version": "1.0"
}
```

### Expected Response (Success)
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "success",
  "records_received": 900,
  "timestamp": "2025-11-02T10:30:46.000000"
}
```

### Expected Response (Failure)
```
HTTP/1.1 400 Bad Request

{
  "status": "error",
  "message": "Invalid CSV format"
}
```

---

## 🐛 Troubleshooting

### Issue: "requests module not found"
```bash
pip install requests
# or
pip3 install requests
```

### Issue: "Connection refused"
```bash
# Check if port 8774 is in use
lsof -i :8774

# Kill existing process if needed
lsof -i :8774 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

### Issue: "CSV file empty"
Run `02. link_verify.ipynb` to generate data

### Issue: "Timeout after 30 seconds"
- Server is too slow
- Network is congested
- Increase timeout in code

---

## 📚 File Structure

```
link_grabber/
├── 01. all_link_grabber.ipynb          # Step 1: Scrape links
├── 02. link_verify.ipynb               # Step 2: Verify links
├── 03_csv_uploader.py                  # Step 3: Upload (NEW)
├── 03_csv_uploader.ipynb               # Step 3: Upload Notebook (NEW)
├── test_uploader.sh                    # Test harness (NEW)
├── links_table.csv                     # Step 1 output
├── links_table_with_status.csv         # Step 2 output
└── main.py                             # Legacy
```

---

## 🎯 Next Steps

1. ✅ Ensure `links_table_with_status.csv` exists
2. ✅ Start server on port 8774
3. ✅ Run `python3 03_csv_uploader.py`
4. ✅ Verify HTTP 200 response

---

## 📞 Support

For issues or questions:
1. Check error messages (printed to console)
2. Review troubleshooting section
3. Run test harness: `./test_uploader.sh`
4. Check server logs

---

## 📄 License

See LICENSE file in repository root

---

**Created**: November 2, 2025  
**Project**: queens-cb2  
**Module**: link_grabber
