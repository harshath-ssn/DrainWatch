-- DrainWatch PostgreSQL + PostGIS Spatial Schema

CREATE EXTENSION IF NOT EXISTS postgis;

-- Drainage Telemetry & Sensor Nodes Table
CREATE TABLE drain_nodes (
    id SERIAL PRIMARY KEY,
    ward_name VARCHAR(100) NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL,
    flow_capacity_lps NUMERIC,
    geom GEOMETRY(Point, 4326)
);

-- Real-time Risk Events Table
CREATE TABLE risk_telemetry_logs (
    log_id BIGSERIAL PRIMARY KEY,
    node_id INT REFERENCES drain_nodes(id),
    water_level_pct NUMERIC,
    rainfall_rate_mm_hr NUMERIC,
    stagnation_duration_hrs NUMERIC,
    vbp_risk_score DECIMAL(3,2),
    alert_status VARCHAR(20) DEFAULT 'NORMAL',
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);