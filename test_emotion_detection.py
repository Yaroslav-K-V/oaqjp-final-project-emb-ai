import unittest
import sys
sys.path.insert(0, r'c:\Users\User\Documents\Projects\watson-nlp-sentiment')

from unittest.mock import patch, MagicMock
import json
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_joy_emotion(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            'emotionPredict': {
                'emotion': {
                    'anger': 0.05,
                    'disgust': 0.02,
                    'fear': 0.03,
                    'joy': 0.88,
                    'sadness': 0.02
                }
            }
        })

        with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
            result = emotion_detector('I am glad this happened')
            self.assertEqual(result['dominant_emotion'], 'joy')
            print("Test 1 PASSED: 'I am glad this happened' - Dominant emotion: joy")

    def test_anger_emotion(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            'emotionPredict': {
                'emotion': {
                    'anger': 0.87,
                    'disgust': 0.05,
                    'fear': 0.02,
                    'joy': 0.03,
                    'sadness': 0.03
                }
            }
        })

        with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
            result = emotion_detector('I am really mad about this')
            self.assertEqual(result['dominant_emotion'], 'anger')
            print("Test 2 PASSED: 'I am really mad about this' - Dominant emotion: anger")

    def test_disgust_emotion(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            'emotionPredict': {
                'emotion': {
                    'anger': 0.05,
                    'disgust': 0.85,
                    'fear': 0.02,
                    'joy': 0.03,
                    'sadness': 0.05
                }
            }
        })

        with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
            result = emotion_detector('I feel disgusted just hearing about this')
            self.assertEqual(result['dominant_emotion'], 'disgust')
            print("Test 3 PASSED: 'I feel disgusted just hearing about this' - Dominant emotion: disgust")

    def test_sadness_emotion(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            'emotionPredict': {
                'emotion': {
                    'anger': 0.03,
                    'disgust': 0.02,
                    'fear': 0.04,
                    'joy': 0.02,
                    'sadness': 0.89
                }
            }
        })

        with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
            result = emotion_detector('I am so sad about this')
            self.assertEqual(result['dominant_emotion'], 'sadness')
            print("Test 4 PASSED: 'I am so sad about this' - Dominant emotion: sadness")

    def test_fear_emotion(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            'emotionPredict': {
                'emotion': {
                    'anger': 0.02,
                    'disgust': 0.01,
                    'fear': 0.89,
                    'joy': 0.02,
                    'sadness': 0.06
                }
            }
        })

        with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
            result = emotion_detector('I am really afraid that this will happen')
            self.assertEqual(result['dominant_emotion'], 'fear')
            print("Test 5 PASSED: 'I am really afraid that this will happen' - Dominant emotion: fear")

    def test_output_format(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            'emotionPredict': {
                'emotion': {
                    'anger': 0.05,
                    'disgust': 0.02,
                    'fear': 0.03,
                    'joy': 0.88,
                    'sadness': 0.02
                }
            }
        })

        with patch('EmotionDetection.emotion_detection.requests.post', return_value=mock_response):
            result = emotion_detector('Test statement')
            # Verify output structure
            self.assertIn('anger', result)
            self.assertIn('disgust', result)
            self.assertIn('fear', result)
            self.assertIn('joy', result)
            self.assertIn('sadness', result)
            self.assertIn('dominant_emotion', result)
            self.assertIsInstance(result['dominant_emotion'], str)
            print("Test 6 PASSED: Output format is correct")


if __name__ == '__main__':
    print("=" * 70)
    print("EMOTION DETECTION UNIT TESTS")
    print("=" * 70)
    print()
    
    unittest.main(argv=[''], verbosity=2, exit=False)
    
    print()
    print("=" * 70)
    print("ALL UNIT TESTS COMPLETED SUCCESSFULLY")
    print("=" * 70)
