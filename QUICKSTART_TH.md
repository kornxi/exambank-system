# คู่มือเริ่มต้นใช้งาน (Quick Start Guide)

## 🚀 Deploy ไปยัง Google Cloud Run แบบง่าย ๆ

### ขั้นตอนที่ 1: เตรียมความพร้อม

1. **สร้างบัญชี Google Cloud**
   - ไปที่ https://cloud.google.com/
   - สมัครใช้งาน (ได้ credit ฟรี $300 สำหรับผู้ใช้งานใหม่)
   - เปิดใช้งาน Billing (ใส่ข้อมูลบัตรเครดิต)

2. **ติดตั้ง Google Cloud CLI**
   
   **สำหรับ Windows:**
   - ดาวน์โหลดจาก https://cloud.google.com/sdk/docs/install
   - รัน installer และติดตั้งตามขั้นตอน
   
   **สำหรับ Mac:**
   ```bash
   brew install --cask google-cloud-sdk
   ```
   
   **สำหรับ Linux:**
   ```bash
   curl https://sdk.cloud.google.com | bash
   exec -l $SHELL
   ```

### ขั้นตอนที่ 2: ตั้งค่า Google Cloud CLI

เปิด Terminal/Command Prompt และรันคำสั่งต่อไปนี้:

```bash
# 1. Login เข้า Google Cloud
gcloud auth login

# 2. สร้างโปรเจคใหม่ (หรือใช้โปรเจคที่มีอยู่)
gcloud projects create exambank-project-123 --name="Exam Bank System"

# 3. ตั้งค่าโปรเจค
gcloud config set project exambank-project-123

# 4. เปิดใช้งาน Billing (จำเป็น!)
# ไปที่ https://console.cloud.google.com/billing เพื่อเชื่อมโยง billing account กับโปรเจค

# 5. เปิดใช้งาน APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### ขั้นตอนที่ 3: Deploy!

มี 2 วิธีในการ deploy:

#### วิธีที่ 1: ใช้สคริปต์อัตโนมัติ (แนะนำ)

```bash
# รันสคริปต์ deploy
./deploy.sh
```

สคริปต์จะถามคำถามง่าย ๆ และ deploy ให้อัตโนมัติ!

#### วิธีที่ 2: Deploy ด้วยคำสั่งเดียว

```bash
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --allow-unauthenticated \
  --port 8080
```

**อธิบายคำสั่ง:**
- `exambank-system` = ชื่อ service ของเรา
- `--source .` = ใช้ source code ในโฟลเดอร์ปัจจุบัน
- `--region asia-southeast1` = deploy ที่ Singapore (ใกล้ไทยที่สุด)
- `--allow-unauthenticated` = เปิดให้ทุกคนเข้าถึงได้ (สำหรับ API สาธารณะ)
- `--port 8080` = ใช้ port 8080

### ขั้นตอนที่ 4: ทดสอบ

หลังจาก deploy เสร็จ คุณจะได้ URL มาประมาณนี้:
```
https://exambank-system-xxxxx-as.a.run.app
```

ทดสอบด้วยคำสั่ง:
```bash
# ทดสอบ API
curl https://YOUR-URL/
curl https://YOUR-URL/health
curl https://YOUR-URL/api/v1/exams

# หรือเปิดใน browser
# https://YOUR-URL/docs  <- ดู API documentation
```

## 📊 ค่าใช้จ่าย (Pricing)

Cloud Run คิดค่าบริการตามการใช้งานจริง:

- **2 ล้าน requests แรก/เดือน: ฟรี!**
- **360,000 GB-seconds แรก/เดือน: ฟรี!**
- ถ้าไม่มีคนใช้งาน = ไม่มีค่าใช้จ่าย (scale to zero)

สำหรับการใช้งานทั่วไป ถ้า traffic ไม่เยอะมาก มักจะอยู่ในขอบเขต free tier

## ⚙️ การตั้งค่าเพิ่มเติม

### เพิ่ม Memory
```bash
gcloud run deploy exambank-system \
  --source . \
  --memory 1Gi
```

### กำหนดจำนวน instances
```bash
gcloud run deploy exambank-system \
  --source . \
  --min-instances 1 \
  --max-instances 10
```

### ตั้งค่า Environment Variables
```bash
gcloud run deploy exambank-system \
  --source . \
  --set-env-vars "DB_HOST=xxxxx,API_KEY=yyyyy"
```

## 🔍 การดู Logs

```bash
# ดู logs แบบ real-time
gcloud run logs tail exambank-system --region asia-southeast1

# ดู logs ย้อนหลัง 100 บรรทัด
gcloud run logs read exambank-system --region asia-southeast1 --limit 100
```

## 🔄 Update แอพ

แก้ไข code แล้วต้องการ deploy version ใหม่:

```bash
# deploy version ใหม่ (รันคำสั่งเดิม)
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --allow-unauthenticated
```

Cloud Run จะ:
1. Build Docker image ใหม่
2. Deploy version ใหม่
3. ค่อย ๆ เปลี่ยนจาก version เก่าไปใหม่ (zero downtime!)

## ❌ ลบ Service

ถ้าต้องการลบ service:
```bash
gcloud run services delete exambank-system --region asia-southeast1
```

## 🆘 แก้ปัญหา

### ปัญหา: Build ล้มเหลว
```bash
# ดู build logs
gcloud builds list
gcloud builds log <BUILD_ID>
```

### ปัญหา: Service ไม่ start
```bash
# ดู logs
gcloud run logs read exambank-system --region asia-southeast1
```

### ปัญหา: 403 Forbidden
- ตรวจสอบว่าเปิดใช้งาน APIs แล้ว
- ตรวจสอบว่า billing เปิดใช้งานแล้ว

### ปัญหา: Authentication error
```bash
# Login ใหม่
gcloud auth login
gcloud auth application-default login
```

## 📚 ข้อมูลเพิ่มเติม

- [DEPLOYMENT.md](DEPLOYMENT.md) - คู่มือ deploy แบบละเอียด
- [README.md](README.md) - ข้อมูลโปรเจค
- [Google Cloud Run Docs](https://cloud.google.com/run/docs)

## 💡 เคล็ดลับ

1. **ประหยัดค่าใช้จ่าย**: ตั้ง `--min-instances 0` เพื่อให้ scale to zero
2. **เร็วขึ้น**: ตั้ง `--min-instances 1` เพื่อให้มี instance พร้อมเสมอ
3. **ปลอดภัย**: ลบ `--allow-unauthenticated` และใช้ IAM authentication
4. **Monitor**: ดู metrics ที่ Cloud Console

## 🎯 Next Steps

หลังจาก deploy เสร็จแล้ว:

1. ✅ เพิ่ม database (Cloud SQL, Firestore)
2. ✅ ใช้ Secret Manager สำหรับ sensitive data
3. ✅ ตั้งค่า custom domain
4. ✅ เพิ่ม CI/CD ด้วย Cloud Build triggers
5. ✅ เพิ่ม monitoring และ alerting

---

**สำเร็จแล้ว! 🎉 ระบบคลังข้อสอบของคุณพร้อมใช้งานบน Cloud แล้ว**

หากมีคำถามหรือปัญหา เปิด issue บน GitHub หรือดูเอกสารเพิ่มเติมใน [DEPLOYMENT.md](DEPLOYMENT.md)
