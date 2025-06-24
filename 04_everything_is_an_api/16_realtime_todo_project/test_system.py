#!/usr/bin/env python3
"""
Simple test script to verify the todo system is working
"""
import requests
import json
import time

def test_api():
    base_url = "http://localhost:8000"
    
    print("Testing Todo API...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return
    
    # Test create todo
    try:
        todo_data = {"task": "Test todo from script", "completed": False}
        response = requests.post(f"{base_url}/todos", json=todo_data)
        print(f"Create todo: {response.status_code}")
        if response.status_code == 200:
            created_todo = response.json()
            print(f"Created todo: {created_todo}")
    except Exception as e:
        print(f"Create todo failed: {e}")
    
    # Test get todos
    try:
        response = requests.get(f"{base_url}/todos")
        print(f"Get todos: {response.status_code}")
        if response.status_code == 200:
            todos = response.json()
            print(f"Found {len(todos)} todos")
            for todo in todos:
                print(f"  - {todo}")
    except Exception as e:
        print(f"Get todos failed: {e}")

if __name__ == "__main__":
    print("Waiting for system to start...")
    time.sleep(5)  # Give the system time to start
    test_api() 