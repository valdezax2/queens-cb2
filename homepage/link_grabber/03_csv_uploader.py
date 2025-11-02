import requests
import pathlib
import json
import sys
from datetime import datetime

class CSVUploader:
    def __init__(self, csv_file='links_table_with_status.csv', endpoint='http://127.0.0.1:8774'):
        self.csv_path = pathlib.Path(csv_file)
        self.endpoint = endpoint
        self.timeout = 30
        self.upload_success = False
        
    def validate_csv_exists(self):
        """Verify CSV file exists before upload"""
        if not self.csv_path.exists():
            print(f"❌ Error: {self.csv_path} not found")
            return False
        print(f"✅ CSV file found: {self.csv_path}")
        print(f"   File size: {self.csv_path.stat().st_size / 1024:.2f} KB")
        return True
    
    def read_csv_data(self):
        """Read CSV and return data"""
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                content = f.read()
            lines = content.split('\n')
            print(f"✅ CSV loaded successfully")
            print(f"   Total bytes: {len(content)}")
            print(f"   Data rows: {len(lines) - 2}")
            return content
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return None
    
    def upload_csv(self, csv_content):
        """Send CSV to endpoint via POST"""
        try:
            print(f"\n📤 Uploading to {self.endpoint}...")
            
            files = {
                'file': ('links_table_with_status.csv', csv_content, 'text/csv')
            }
            
            metadata = {
                'timestamp': datetime.now().isoformat(),
                'source': 'queens-cb2-link-grabber',
                'version': '1.0'
            }
            
            data = {
                'metadata': json.dumps(metadata)
            }
            
            response = requests.post(
                self.endpoint,
                files=files,
                data=data,
                timeout=self.timeout
            )
            
            print(f"📊 Response Status: {response.status_code}")
            
            if response.status_code in [200, 201, 202]:
                print("✅ Upload successful!")
                print(f"Response: {response.text[:200]}")
                self.upload_success = True
                return True
            else:
                print(f"⚠️ Server returned: {response.status_code}")
                print(f"Response: {response.text[:500]}")
                return False
                
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection Error: Cannot reach {self.endpoint}")
            print("   Ensure server is running on port 8774")
            print("   Try: nc -l 127.0.0.1 8774")
            return False
        except requests.exceptions.Timeout:
            print(f"❌ Timeout: Server not responding within {self.timeout}s")
            return False
        except Exception as e:
            print(f"❌ Error uploading: {e}")
            return False
    
    def upload(self):
        """Main upload workflow"""
        print("=" * 60)
        print("CSV UPLOADER - Queens CB2 Link Verification Data")
        print("=" * 60)
        
        # Step 1: Validate
        if not self.validate_csv_exists():
            return False
        
        # Step 2: Read
        csv_content = self.read_csv_data()
        if not csv_content:
            return False
        
        # Step 3: Upload
        success = self.upload_csv(csv_content)
        
        print("\n" + "=" * 60)
        if success:
            print("✅ Upload workflow completed successfully")
        else:
            print("❌ Upload workflow failed")
        print("=" * 60)
        
        return success

if __name__ == '__main__':
    uploader = CSVUploader(
        csv_file='links_table_with_status.csv',
        endpoint='http://127.0.0.1:8774'
    )
    exit_code = 0 if uploader.upload() else 1
    sys.exit(exit_code)
