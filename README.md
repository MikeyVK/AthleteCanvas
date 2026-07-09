# Ypsia

> Personal AI-Driven Training, Nutrition & Weekly Rhythm Coach.

Ypsia is a personal AI coach platform that integrates Garmin/FIT training data, LiteLLM analysis (with Gemini as the primary engine), weekly rhythm planning, nutrition tracking, and meal planning into a single coherent weekly cycle.

The platform is designed as a privacy-respecting, local-first application that acts as an active sparring partner to help you align your training, recovery, and nutrition.

---

## ✨ Features

- **Training Fundament**: Import, normalize, and store Garmin FIT activity files.
- **Weekly Rhythm Planner**: Dynamic scheduling of training around fixed life rhythms (work, family) and recovery needs.
- **AI Coach Interface**: A streaming conversation interface with an AI coach that has context on your training and nutrition, with strict user-controlled data scoping.
- **Nutrition & Meal Engine**: Nutritional logging, menu creation, automated grocery lists, and personalized nutritional advice.

---

## 🛠 Technology Stack

- **Backend**: Python 3.11+, FastAPI, SQLite (local and privacy-first storage).
- **Frontend**: React, Vite, CSS.
- **AI Layer**: LiteLLM (provider-agnostic integration, Bring Your Own Key).

---

## 📚 Documentation & Onboarding

To quickly find the information you need, refer to these primary entry points:

### 1. Project & Vision
* **[Project Charter (docs/CHARTER.md)](docs/CHARTER.md)**: Read the *Constitution of Ypsia*, covering our core mission, product vision, design aesthetics, and the epics roadmap.

### 2. Development & Standards
* **[Developer Documentation Index (docs/README.md)](docs/README.md)**: The central entry point for developers, referencing:
  * **[Architecture Principles (docs/coding_standards/ARCHITECTURE_PRINCIPLES.md)](docs/coding_standards/ARCHITECTURE_PRINCIPLES.md)**: Our binding software architecture guidelines.
  * **[Quality Gates (docs/coding_standards/QUALITY_GATES.md)](docs/coding_standards/QUALITY_GATES.md)**: Quality checks and pre-merge checklist.
  * **[Documentation Standard (docs/coding_standards/DOCUMENTATION_STANDARD.md)](docs/coding_standards/DOCUMENTATION_STANDARD.md)**: Rules for writing clean, structured documentation.

### 3. Setup & Installation
* **[Setup & Installation Guide (.pgmcp/docs/setup/README.md)](.pgmcp/docs/setup/README.md)**: Step-by-step instructions to configure the environment and run the backend and frontend locally.

---

## 📁 Repository Structure

- `backend/` - FastAPI backend application and SQLite database.
- `frontend/` - React/Vite single-page application.
- `web/` - Static marketing/info site and charter web viewer.
- `docs/` - Project documentation, planning, and guidelines.
- `.agents/` - AI agent instruction sets and workflows.
