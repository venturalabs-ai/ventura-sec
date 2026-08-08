import unittest

from ventura_sec import Event, anomaly_score, classify, precision_recall


class DefensiveTriageTests(unittest.TestCase):
    def test_low_risk_event_stays_below_threshold(self):
        event = Event(failed_logins=1, unique_sources=1, sensitive_actions=0, off_hours=False)
        self.assertLess(anomaly_score(event), 0.5)
        self.assertFalse(classify(event))

    def test_high_risk_event_is_flagged(self):
        event = Event(failed_logins=10, unique_sources=6, sensitive_actions=5, off_hours=True)
        self.assertEqual(anomaly_score(event), 1.0)
        self.assertTrue(classify(event))

    def test_precision_recall_on_versioned_fixture(self):
        labels = [False, True, True, False, True]
        predictions = [False, True, False, True, True]
        precision, recall = precision_recall(labels, predictions)
        self.assertAlmostEqual(precision, 2 / 3)
        self.assertAlmostEqual(recall, 2 / 3)

    def test_invalid_negative_counter_is_rejected(self):
        with self.assertRaises(ValueError):
            anomaly_score(Event(-1, 1, 0))


if __name__ == "__main__":
    unittest.main()
