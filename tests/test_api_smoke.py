import time
import unittest

from fastapi.testclient import TestClient

from app.main import app


class ApiSmokeTest(unittest.TestCase):
    def test_world_routes(self):
        # TestClient drives the FastAPI app in-process, so this covers routing,
        # lifespan startup/shutdown, and JSON request handling without a live server.
        with TestClient(app) as client:
            response = client.post("/world/print")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.text, '""')

            response = client.post(
                "/entity/create_npc",
                json={"name": "npc_a", "x": 2, "y": 3},
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"status": "ok"})

            response = client.post("/world/tick")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"status": "one tick"})

            world_text = client.post("/world/print").text
            self.assertIn("npc_a", world_text)
            self.assertIn("PositionData:x=2.0", world_text)
            self.assertIn("PositionData:y=3.0", world_text)

            response = client.post("/action/eat", json={"entity": 4999, "value": 7})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"status": "ok"})

            response = client.post("/world/tick")
            self.assertEqual(response.status_code, 200)

            world_text = client.post("/world/print").text
            self.assertIn("HungerData:value=37.0", world_text)
            self.assertIn("EmotionData:moods:MOOD.HAPPY=5.0", world_text)

            start_response = client.post("/world/start")
            self.assertEqual(start_response.status_code, 200)
            self.assertEqual(start_response.json(), {"status": "world started"})

            second_start_response = client.post("/world/start")
            self.assertEqual(second_start_response.status_code, 200)
            self.assertEqual(
                second_start_response.json(),
                {"status": "world already running"},
            )

            container = client.app.state.container
            before = container.world.time.tick_count
            time.sleep(0.45)
            mid = container.world.time.tick_count
            self.assertGreater(mid, before)

            stop_response = client.post("/world/stop")
            self.assertEqual(stop_response.status_code, 200)
            self.assertEqual(stop_response.json(), {"status": "world stopped"})

            # After stop() the background loop should no longer advance time.
            after_stop = container.world.time.tick_count
            time.sleep(0.3)
            self.assertEqual(container.world.time.tick_count, after_stop)


if __name__ == "__main__":
    unittest.main()
