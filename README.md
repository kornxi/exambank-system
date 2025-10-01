# Exam Bank System / ระบบคลังข้อสอบ

A cloud-native exam bank management system built with FastAPI and designed for deployment on Google Cloud Run.

ระบบจัดการคลังข้อสอบที่พัฒนาด้วย FastAPI และออกแบบมาเพื่อ deploy บน Google Cloud Run

## Features / คุณสมบัติ

- ✅ RESTful API built with FastAPI
- ✅ Ready for Google Cloud Run deployment
- ✅ Docker containerization
- ✅ Health check endpoints
- ✅ CORS enabled
- ✅ Production-ready configuration

## Quick Start / เริ่มต้นใช้งาน

### Local Development / การพัฒนาในเครื่อง

1. **Install dependencies / ติดตั้ง dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application / รันแอปพลิเคชัน**
   ```bash
   python main.py
   ```
   
   หรือ / or
   
   ```bash
   uvicorn main:app --reload --port 8080
   ```

3. **Access the API / เข้าถึง API**
   - API: http://localhost:8080
   - Interactive docs: http://localhost:8080/docs
   - Alternative docs: http://localhost:8080/redoc

### Docker Development / การพัฒนาด้วย Docker

1. **Build image**
   ```bash
   docker build -t exambank-system .
   ```

2. **Run container**
   ```bash
   docker run -p 8080:8080 exambank-system
   ```

## Deployment to Google Cloud Run / การ Deploy ไปยัง Google Cloud Run

📖 **See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions**

📖 **ดู [DEPLOYMENT.md](DEPLOYMENT.md) สำหรับคำแนะนำการ deploy แบบละเอียด**

### Quick Deploy / Deploy แบบรวดเร็ว

```bash
# Login to Google Cloud
gcloud auth login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Deploy
gcloud run deploy exambank-system \
  --source . \
  --region asia-southeast1 \
  --allow-unauthenticated
```

## API Endpoints / ปลายทาง API

### Base Endpoints

- `GET /` - Root endpoint, returns service info
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

### API v1 Endpoints

- `GET /api/v1/exams` - List all exams (placeholder)

## Project Structure / โครงสร้างโปรเจค

```
exambank-system/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── .dockerignore       # Docker ignore rules
├── cloudbuild.yaml     # Google Cloud Build configuration
├── .env.example        # Environment variables example
├── README.md           # This file
├── DEPLOYMENT.md       # Deployment documentation
└── LICENSE            # MIT License
```

## Environment Variables / ตัวแปรสภาพแวดล้อม

Copy `.env.example` to `.env` and configure:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | 8080 |
| `ENVIRONMENT` | Environment name | production |

## Development / การพัฒนา

### Prerequisites / สิ่งที่ต้องมี

- Python 3.11 or higher
- pip
- Docker (optional)
- Google Cloud CLI (for deployment)

### Installing Dependencies / ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### Running Tests / รันการทดสอบ

```bash
# Add tests here when implemented
pytest
```

## Technologies Used / เทคโนโลยีที่ใช้

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Docker** - Containerization
- **Google Cloud Run** - Serverless container platform

## Contributing / การมีส่วนร่วม

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License / ใบอนุญาต

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support / การสนับสนุน

For issues and questions, please open an issue on GitHub.

สำหรับปัญหาและคำถาม กรุณาเปิด issue บน GitHub

## Links / ลิงก์

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Docker Documentation](https://docs.docker.com/)

---

**Made with ❤️ for education / สร้างด้วย ❤️ เพื่อการศึกษา**
