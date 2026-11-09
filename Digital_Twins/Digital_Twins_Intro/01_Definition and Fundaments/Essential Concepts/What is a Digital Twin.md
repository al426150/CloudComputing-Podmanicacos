---
type: concept_note
topic: Core Definitions
sources:
  - "[[IBM -  What is a Digital Twin]]"
  - "[[Draft Space Technology Roadmap Modeling, Simulation, Information Technology & Processing Roadmap]]"
  - "[[Digital Twin Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems]]"
tags:
  - digital-twins
  - architecture
  - definition
  - concepts
---
# What is a Digital Twin?

> [!summary] Core Takeaway
> A **Digital Twin** is a dynamic, virtual representation of a physical asset, process, or system that mirrors its real-world counterpart across its lifecycle. Unlike a static 3D model or an offline simulation, it relies on an **automated, continuous, and bidirectional data exchange** synchronized at a specified frequency and fidelity—allowing the virtual model to ingest real-time operational telemetry and return optimized control setpoints, predictive diagnostics, or operational commands directly to the physical entity.

## Technology Breakdown

### A. The Core Architectural Triad
A digital twin is not a single software application, but an active cyber-physical system operating across three structural components:

- **Real Space (The Physical Asset):** The operational physical entity—ranging from a single structural component (e.g., a turbine blade) to complex industrial facilities or spacecraft—instrumented with embedded sensors and physical actuators.
- **Virtual Space (The Computational Replica):** High-fidelity virtual models integrating structural geometry, kinematic logic, multiphysics simulations, and predictive AI/ML algorithms.
- **Bidirectional Data Connections:** 
  - *Upward Stream (Sensing):* Sensor networks and edge pipelines transmitting telemetry (temperature, vibration, pressure, wear) into the virtual model.
  - *Downward Stream (Actuation):* Optimized control setpoints, prescriptive operational thresholds, and emergency actuation commands executed directly back onto physical actuators.

### B. Lifecycle Archetypes
Digital twins evolve systematically across the product lifecycle:

- **Digital Twin Prototype (DTP):** The virtual archetype describing the intended physical asset prior to production, encompassing design tolerances, CAD geometries, and baseline material specifications.
- **Digital Twin Instance (DTI):** The individual virtual counterpart permanently paired with a specific serialized physical unit, continuously logging its operational hours, environmental exposure, and unique degradation profile.
- **Digital Twin Aggregate (DTA):** The composite multi-twin aggregation of all DTIs across an operating fleet, enabling fleet-wide predictive analytics and systemic fault recognition.

### C. Definitional Boundaries
Based on the degree of data automation:

- **Digital Model:** Characterized by manual data exchange in both directions (e.g., standard 3D CAD files or isolated engineering simulations).
- **Digital Shadow:** Characterized by automated one-way telemetry from the physical asset to the virtual model, but requiring manual human action to alter the physical machine (e.g., read-only SCADA dashboards).
- **Digital Twin:** Characterized by fully automated, bidirectional data exchange in a closed feedback loop.