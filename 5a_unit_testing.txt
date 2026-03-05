import unittest
from unittest import TestCase
from emotion_detection import emotion_detector

class TestEmotionDetection(TestCase):
    def test_emotion_detection_integration(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected_emotion in test_cases:
            with self.subTest(text=text, expected_emotion=expected_emotion):
                result = emotion_detector(text)
                self.assertIsNotNone(result)
                self.assertIn("dominant_emotion", result)
                self.assertEqual(result["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    unittest.main()
