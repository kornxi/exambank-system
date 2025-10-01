# การ Deploy ระบบไปยัง Google Cloud Run / Deploying to Google Cloud Run

## ภาษาไทย (Thai)

### ความต้องการเบื้องต้น (Prerequisites)

1. **Google Cloud Account**: สร้างบัญชี Google Cloud และเปิดใช้งาน billing
2. **Google Cloud CLI**: ติดตั้ง gcloud CLI จาก https://cloud.google.com/sdk/docs/install
3. **Docker**: ติดตั้ง Docker สำหรับการ build image ในเครื่อง (ถ้าต้องการทดสอบ)

### ขั้นตอนการ Deploy

#### วิธีที่ 1: Deploy ด้วย gcloud CLI (แนะนำ)

1. **ติดตั้งและตั้งค่า gcloud CLI**
   ```bash
   # ล็อกอินเข้า Google Cloud
   gcloud auth login
   
   # ตั้งค่า project
   gcloud config set project YOUR_PROJECT_ID
   
   # ตั้งค่า region (แนะนำ asia-southeast1 สำหรับประเทศไทย)
   gcloud config set run/region asia-southeast1
   ```

2. **เปิดใช้งาน APIs ที่จำเป็น**
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   gcloud services enable containerregistry.googleapis.com
   ```

3. **Deploy จาก Source Code โดยตรง**
   ```bash
   # Cloud Run จะ build และ deploy อัตโนมัติ
   gcloud run deploy exambank-system \
     --source . \
     --region asia-southeast1 \
     --allow-unauthenticated \
     --port 8080
   ```

4. **รอให้ deployment เสร็จสิ้น** - จะได้ URL ของแอปพลิเคชันที่ deploy แล้ว

#### วิธีที่ 2: Deploy ด้วย Cloud Build (สำหรับ CI/CD)

1. **สร้าง trigger ใน Cloud Build**
   ```bash
   # เชื่อมต่อ repository กับ Cloud Build
   gcloud builds submit --config cloudbuild.yaml
   ```

2. **ตั้งค่า Continuous Deployment** (ถ้าต้องการ)
   - ไปที่ Cloud Build console
   - สร้าง trigger ที่เชื่อมกับ GitHub repository
   - ตั้งค่าให้ trigger ทำงานเมื่อมี push ไปยัง main branch

#### วิธีที่ 3: Deploy ด้วย Docker Image

1. **Build Docker image ในเครื่อง**
   ```bash
   docker build -t gcr.io/YOUR_PROJECT_ID/exambank-system:latest .
   ```

2. **Push image ไปยัง Google Container Registry**
   ```bash
   docker push gcr.io/YOUR_PROJECT_ID/exambank-system:latest
   ```

3. **Deploy จาก image**
   ```bash
   gcloud run deploy exambank-system \
     --image gcr.io/YOUR_PROJECT_ID/exambank-system:latest \
     --region asia-southeast1 \
     --allow-unauthenticated \
     --port 8080
   ```

### การตั้งค่าเพิ่มเติม

#### การกำหนด Environment Variables
```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --set-env-vars "ENVIRONMENT=production,PORT=8080"
```

#### การตั้งค่า Memory และ CPU
```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --memory 512Mi \
  --cpu 1
```

#### การกำหนดจำนวน instances
```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --min-instances 0 \
  --max-instances 10
```

### การทดสอบ

หลังจาก deploy เสร็จแล้ว ทดสอบการทำงานด้วย:
```bash
# ดู service URL
gcloud run services describe exambank-system --region asia-southeast1

# ทดสอบ API
curl https://YOUR_SERVICE_URL/
curl https://YOUR_SERVICE_URL/health
curl https://YOUR_SERVICE_URL/api/v1/exams
```

### การดู Logs
```bash
# ดู logs แบบ real-time
gcloud run logs tail exambank-system --region asia-southeast1

# ดู logs ย้อนหลัง
gcloud run logs read exambank-system --region asia-southeast1 --limit 50
```

### การลบ Service
```bash
gcloud run services delete exambank-system --region asia-southeast1
```

---

## English

### Prerequisites

1. **Google Cloud Account**: Create a Google Cloud account and enable billing
2. **Google Cloud CLI**: Install gcloud CLI from https://cloud.google.com/sdk/docs/install
3. **Docker**: Install Docker for local image building (optional, for testing)

### Deployment Steps

#### Method 1: Deploy with gcloud CLI (Recommended)

1. **Install and configure gcloud CLI**
   ```bash
   # Login to Google Cloud
   gcloud auth login
   
   # Set your project
   gcloud config set project YOUR_PROJECT_ID
   
   # Set region (asia-southeast1 recommended for Thailand)
   gcloud config set run/region asia-southeast1
   ```

2. **Enable required APIs**
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   gcloud services enable containerregistry.googleapis.com
   ```

3. **Deploy directly from source code**
   ```bash
   # Cloud Run will build and deploy automatically
   gcloud run deploy exambank-system \
     --source . \
     --region asia-southeast1 \
     --allow-unauthenticated \
     --port 8080
   ```

4. **Wait for deployment to complete** - You'll receive the URL of your deployed application

#### Method 2: Deploy with Cloud Build (for CI/CD)

1. **Create a Cloud Build trigger**
   ```bash
   # Connect repository to Cloud Build
   gcloud builds submit --config cloudbuild.yaml
   ```

2. **Set up Continuous Deployment** (optional)
   - Go to Cloud Build console
   - Create a trigger connected to your GitHub repository
   - Configure it to trigger on push to main branch

#### Method 3: Deploy with Docker Image

1. **Build Docker image locally**
   ```bash
   docker build -t gcr.io/YOUR_PROJECT_ID/exambank-system:latest .
   ```

2. **Push image to Google Container Registry**
   ```bash
   docker push gcr.io/YOUR_PROJECT_ID/exambank-system:latest
   ```

3. **Deploy from image**
   ```bash
   gcloud run deploy exambank-system \
     --image gcr.io/YOUR_PROJECT_ID/exambank-system:latest \
     --region asia-southeast1 \
     --allow-unauthenticated \
     --port 8080
   ```

### Additional Configuration

#### Setting Environment Variables
```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --set-env-vars "ENVIRONMENT=production,PORT=8080"
```

#### Configuring Memory and CPU
```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --memory 512Mi \
  --cpu 1
```

#### Setting Instance Count
```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --min-instances 0 \
  --max-instances 10
```

### Testing

After deployment, test your application:
```bash
# Get service URL
gcloud run services describe exambank-system --region asia-southeast1

# Test API endpoints
curl https://YOUR_SERVICE_URL/
curl https://YOUR_SERVICE_URL/health
curl https://YOUR_SERVICE_URL/api/v1/exams
```

### Viewing Logs
```bash
# Tail logs in real-time
gcloud run logs tail exambank-system --region asia-southeast1

# Read historical logs
gcloud run logs read exambank-system --region asia-southeast1 --limit 50
```

### Deleting the Service
```bash
gcloud run services delete exambank-system --region asia-southeast1
```

## Cost Optimization Tips

1. **Use minimum instances wisely**: Set `--min-instances 0` to scale to zero when not in use
2. **Set appropriate memory limits**: Start with 512Mi and adjust based on actual usage
3. **Monitor usage**: Use Cloud Monitoring to track requests and adjust scaling settings
4. **Set timeout limits**: Configure appropriate timeout values to avoid hanging requests

## Security Best Practices

1. **Enable authentication**: Remove `--allow-unauthenticated` for production if API should be private
2. **Use Secret Manager**: Store sensitive data in Google Secret Manager, not in environment variables
3. **Configure CORS properly**: Update CORS settings in main.py for your specific domains
4. **Use HTTPS**: Cloud Run provides HTTPS by default, ensure clients use secure connections
5. **Implement rate limiting**: Add rate limiting to prevent abuse

## Troubleshooting

### Build fails
- Check Dockerfile syntax
- Ensure all dependencies are in requirements.txt
- Check Cloud Build logs: `gcloud builds log <BUILD_ID>`

### Service won't start
- Verify PORT environment variable is set correctly
- Check application logs: `gcloud run logs read exambank-system`
- Ensure health check endpoint responds correctly

### Deployment timeouts
- Increase deployment timeout: `--timeout 300s`
- Check that application starts within 10 minutes

For more information, visit [Google Cloud Run documentation](https://cloud.google.com/run/docs)
