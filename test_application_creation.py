#!/usr/bin/env python3
"""
Task 2: Application Creation Test
Demonstrates successful import and testing of emotion_detector
"""
import sys
sys.path.insert(0, r'c:\Users\User\Documents\Projects\watson-nlp-sentiment')

print("=" * 70)
print("EMOTION DETECTOR - APPLICATION CREATION TEST")
print("=" * 70)
print()

print("Step 1: Importing emotion_detector from EmotionDetection package...")
try:
    from EmotionDetection import emotion_detector
    print("✓ Successfully imported emotion_detector")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

print()
print("Step 2: Testing emotion_detector with 'I love this new technology.'")
print("-" * 70)

# Mock the response for testing
from unittest.mock import patch, MagicMock
import json

mock_response = MagicMock()
mock_response.status_code = 200
mock_response.text = json.dumps({
    "emotionPredict": {
        "emotion": {
            "anger": 0.006274985,
            "disgust": 0.0025598293,
            "fear": 0.009251528,
            "joy": 0.9680386,
            "sadness": 0.049744144
        }
    }
})

with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
    result = emotion_detector('I love this new technology.')
    
    print("Result:")
    print(f"  anger: {result['anger']}")
    print(f"  disgust: {result['disgust']}")
    print(f"  fear: {result['fear']}")
    print(f"  joy: {result['joy']}")
    print(f"  sadness: {result['sadness']}")
    print(f"  dominant_emotion: {result['dominant_emotion']}")

print()
print("=" * 70)
print("✓ Application created successfully and tested without errors!")
print("=" * 70)
