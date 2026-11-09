---
type: concept_note
topic: Historical Foundations
sources:
  - "[[IBM -  What is a Digital Twin]]"
  - "[[History and Origin (Michael Grieves and NASA)]]"
tags:
  - digital-twins
  - history
  - nasa
  - michael-grieves
  - origins
  - concepts
---
# History and Origin (Michael Grieves and NASA)

> [!summary] Core Takeaway
> The conceptual foundation of the digital twin originated in 2002 when **Dr. Michael Grieves** introduced the "Conceptual Ideal for PLM" (later named the Mirrored Spaces Model), establishing the three-part triad of physical space, virtual space, and linking data channels. The formal terminology **"Digital Twin"** was explicitly coined and codified in 2010 by **NASA** (John Vickers and the TA11 Technology Roadmap team), shifting the paradigm from static aerospace simulation to dynamic, continuous, multiphysics mission assurance.

---
## Technology Breakdown

### A. The Conceptual Genesis: Dr. Michael Grieves (2002)
The structural framework of the digital twin emerged from research into Product Lifecycle Management (PLM):

- **The 2002 Presentation:** Dr. Michael Grieves introduced the model during an executive PLM course at the University of Michigan. Initially called the **Conceptual Ideal for PLM**, it addressed the fragmentation between physical manufacturing and virtual engineering design.
- **The Mirrored Spaces Triad:** Grieves formalized the architectural construct containing three essential components:
  1. *Real Space* containing the physical entity.
  2. *Virtual Space* containing the computational replica.
  3. *Information Links* connecting the two spaces (telemetry upward, control/actuation downward).
- **The Information-Resource Substitution Principle:** Grieves posited that organizations waste physical resources—energy, raw material, and human labor—because they lack perfect information. By creating high-fidelity virtual models in Virtual Space, computational tests and virtual adjustments replace costly physical trials and destructive failures.
- **Taxonomy of Prototypes and Instances (Grieves & Vickers, 2016):**
  - *Digital Twin Prototype (DTP):* Describes the prototypical physical artifact prior to manufacturing (variants, tolerances, specifications).
  - *Digital Twin Instance (DTI):* The dedicated virtual representation that corresponds to a unique, serialized physical item in service, continuously reflecting its operating history, localized wear, and maintenance events.
  - *Digital Twin Aggregate (DTA):* The composite multi-twin aggregation of all DTIs for fleet-wide monitoring and machine learning pattern recognition.

### B. The Terminology and Operational Expansion: NASA (2010)
While Grieves defined the structural triad, the term "Digital Twin" was officially born through aerospace engineering:

- **Historical Precursors (Apollo 13):** NASA originally used mirrored hardware simulators on Earth to test procedures, diagnose telemetry, and evaluate emergency reconfigurations for spacecraft thousands of miles away.
- **The 2010 Naming:** Working in collaboration with John Vickers (NASA's leading specialist in advanced materials and manufacturing), the term **"Digital Twin"** was formally authored in the *Draft Space Technology Roadmap: Modeling, Simulation, Information Technology & Processing (TA11)*.
- **The Multiphysics Definition:** NASA expanded the concept beyond CAD geometry, defining it as an integrated, multiscale, multiphysics, probabilistic simulation of an aerospace vehicle. It combined high-resolution physics solvers with real-time onboard sensor feeds, fleet data, and structural health monitoring (SHM).
- **Mission Assurance and Self-Correction:** For NASA, the digital twin was engineered to survive long-duration space flight by calculating Remaining Useful Life (RUL) in real time and enabling autonomous or commanded vehicle reconfigurations to mitigate unexpected anomalies.

### C. Evolution and Standardization: DTC and Kritzinger
The concept evolved from custom aerospace deployments into broader industrial standardization:

- **Integration Rigor:** Identified that the historical proliferation of the term caused semantic dilution, establishing the requirement for automated bidirectional data flow to differentiate true digital twins from static digital models and one-way digital shadows.
- **Consensus Standardization:** Established the modern cross-industry standard, defining digital twins as virtual representations synchronized at a *specified frequency and fidelity*, integrated across lifecycle horizons via digital threads.