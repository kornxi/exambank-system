#!/bin/bash

# Exam Bank System - Quick Deployment Script for Google Cloud Run
# ระบบคลังข้อสอบ - สคริปต์ Deploy รวดเร็วสำหรับ Google Cloud Run

set -e

echo "🚀 Exam Bank System - Cloud Run Deployment Script"
echo "=================================================="
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Error: gcloud CLI is not installed."
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Get project ID
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)

if [ -z "$PROJECT_ID" ]; then
    echo "❌ No project set. Please set your project ID:"
    read -p "Enter your Google Cloud Project ID: " PROJECT_ID
    gcloud config set project "$PROJECT_ID"
fi

echo "📋 Project: $PROJECT_ID"
echo ""

# Set default values
SERVICE_NAME="exambank-system"
REGION="asia-southeast1"

# Ask for confirmation
read -p "Deploy to region $REGION? (y/n): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    read -p "Enter region: " REGION
fi

echo ""
echo "🔧 Enabling required APIs..."
gcloud services enable run.googleapis.com --quiet
gcloud services enable cloudbuild.googleapis.com --quiet

echo ""
echo "📦 Building and deploying to Cloud Run..."
echo "This may take a few minutes..."
echo ""

gcloud run deploy "$SERVICE_NAME" \
    --source . \
    --region "$REGION" \
    --allow-unauthenticated \
    --port 8080 \
    --memory 512Mi \
    --cpu 1 \
    --min-instances 0 \
    --max-instances 10 \
    --quiet

echo ""
echo "✅ Deployment complete!"
echo ""

# Get service URL
SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" --region "$REGION" --format='value(status.url)')

echo "🌐 Your service is now available at:"
echo "   $SERVICE_URL"
echo ""
echo "📝 Test your deployment:"
echo "   curl $SERVICE_URL/"
echo "   curl $SERVICE_URL/health"
echo "   curl $SERVICE_URL/docs"
echo ""
echo "📊 View logs:"
echo "   gcloud run logs tail $SERVICE_NAME --region $REGION"
echo ""
echo "🗑️  Delete service:"
echo "   gcloud run services delete $SERVICE_NAME --region $REGION"
echo ""
