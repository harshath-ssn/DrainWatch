"""
DrainWatch Ingestion: IMD Radar and Civic Stream Ingestor
"""
import json

def fetch_radar_telemetry(city="Chennai"):
    # Simulated IMD / OpenWeather radar ingestion
    sample_payload = {
        "city": city,
        "radar_reflectivity_dbz": 48.5,
        "precipitation_rate_mm_hr": 24.2,
        "nlp_civic_flags": ["waterlogged", "drain_overflow"],
        "status": "INGESTED"
    }
    return sample_payload

if __name__ == "__main__":
    payload = fetch_radar_telemetry()
    print("🛰️ Ingestion Pipeline Active:")
    print(json.dumps(payload, indent=2))