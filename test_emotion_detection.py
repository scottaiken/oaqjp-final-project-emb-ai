import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        res = emotion_detector('I am glad this happened')
        assert 'dominant_emotion' in res
        self.assertEqual(res['dominant_emotion'], 'joy')

        res = emotion_detector('I am really mad about this')
        assert 'dominant_emotion' in res
        self.assertEqual(res['dominant_emotion'], 'anger')
        
        res = emotion_detector('I feel disgusted just hearing about this')
        assert 'dominant_emotion' in res
        self.assertEqual(res['dominant_emotion'], 'disgust')
        
        res = emotion_detector('I am so sad about this')
        assert 'dominant_emotion' in res
        self.assertEqual(res['dominant_emotion'], 'sadness')
        
        res = emotion_detector('I am really afraid that this will happen')
        assert 'dominant_emotion' in res
        self.assertEqual(res['dominant_emotion'], 'fear')

unittest.main()
