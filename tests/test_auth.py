"""Authentication Tests"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAuthentication:
    """Test authentication endpoints"""

    def test_register_user(self):
        """Test user registration"""
        response = client.post(
            "/api/v1/auth/register",
            json={
                "email": "test@example.com",
                "username": "testuser",
                "password": "securepassword123",
                "full_name": "Test User",
                "phone": "+1234567890",
                "address": "123 Main St",
                "city": "New York",
                "country": "USA",
                "postal_code": "10001"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "test@example.com"
        assert data["username"] == "testuser"
        assert "hashed_password" not in data

    def test_register_duplicate_email(self):
        """Test registration with duplicate email"""
        email = "duplicate@example.com"
        
        # Register first user
        client.post(
            "/api/v1/auth/register",
            json={
                "email": email,
                "username": "user1",
                "password": "password123"
            }
        )
        
        # Try to register with same email
        response = client.post(
            "/api/v1/auth/register",
            json={
                "email": email,
                "username": "user2",
                "password": "password123"
            }
        )
        assert response.status_code == 400
        assert "already registered" in response.json()["detail"]

    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


class TestApi:
    """Test API endpoints"""

    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "docs" in data

    def test_api_v1_endpoint(self):
        """Test API v1 endpoint"""
        response = client.get("/api/v1")
        assert response.status_code == 200
        data = response.json()
        assert data["version"] == "1.0.0"
        assert "endpoints" in data
