# WeBugMate — AI-Powered Resolution Platform

<div align="center">

![WeBugMate Banner](https://img.shields.io/badge/WeBugMate-AI%20Workspace-6C3EF4?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19.x-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Supabase](https://img.shields.io/badge/Supabase-Backend-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)

**An enterprise-grade, AI-driven collaborative workspace platform built by We3vision Private Limited.**
WeBugMate combines real-time communication, RBAC-enforced AI chatbots, project management, and intelligent feedback systems into a single unified workspace.

[Features](#features) • [Architecture](#architecture) • [File Structure](#file-structure) • [Installation](#installation) • [API Reference](#api-reference) • [Workflow](#workflow)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [Execution Commands](#execution-commands)
- [API Reference](#api-reference)
- [Workflow](#workflow)
- [RBAC — Role-Based Access Control](#rbac--role-based-access-control)
- [AI & LLM Integration](#ai--llm-integration)
- [WebSocket & Real-Time Features](#websocket--real-time-features)
- [Feedback System](#feedback-system)
- [Security & Encryption](#security--encryption)
- [Frontend Pages](#frontend-pages)
- [Database Schema Overview](#database-schema-overview)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Company](#company)

---

## Features

### Core Platform Features
- **AI Chat (Common Mode)** — General-purpose chatbot accessible to all authenticated users, powered by LLMs via OpenRouter API.
- **AI Work Chat** — RBAC-enforced AI assistant that queries project-specific data filtered by user role.
- **Dual Chatbot** — Side-by-side AI responses; compares two AI outputs simultaneously.
- **Developer Chat** — Dedicated mode for technical team members with deeper code/technical context.
- **Real-Time Workspace Rooms** — WebSocket-based chat rooms scoped to workspaces and projects.
- **Broadcast & Announcements** — Company-wide or project-scoped broadcast messaging system.
- **Project Management** — Create, assign, and track projects with detailed tables and views.
- **Task Management** — Granular task tracking with assignment, status, and priority management.
- **User Role Management** — Admin-controlled role assignment with full permission matrix.
- **Feedback System** — Per-message thumbs up/down with tag-based scoring (complexity, relevance, clarity, length).
- **Settings & Avatar Customization** — Per-user settings, avatar selection, and profile management.
- **Organization View** — Visual organization hierarchy and member overview.

### AI & Intelligence Features
- Context-aware AI responses derived from ChromaDB vector embeddings.
- Retrieval-Augmented Generation (RAG) pipeline for document-based Q&A.
- Adaptive response tone based on user role (admin gets executive summaries, employees get task-level details).
- Intelligent deduplication to avoid surfacing redundant records.
- Semantic cleaning and normalization of AI-generated output.
- Canonical schema mapping to normalize structured AI responses.
- Cooldown-based AI rate limiting to prevent LLM overuse.

### Security Features
- JWT-based authentication via Supabase Auth.
- RSA key-pair encryption for sensitive data transmission.
- Fine-grained RBAC engine with per-table, per-role query filters.
- Encrypted route handlers for sensitive API calls.
- Session management with automatic online/offline status cleanup.

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | FastAPI (Python 3.13) |
| **ASGI Server** | Uvicorn / Gunicorn |
| **Frontend** | React 19, React Router DOM v7 |
| **UI Libraries** | MUI (Material UI) v7, Bootstrap 5, Framer Motion |
| **Database & Auth** | Supabase (PostgreSQL + Auth) |
| **Vector Store** | ChromaDB |
| **LLM Provider** | OpenRouter API (multi-model routing) |
| **Embeddings** | HuggingFace Sentence Transformers |
| **AI Framework** | LangChain, LangChain Community |
| **State/Data** | Axios, Supabase JS Client |
| **Visualization** | Recharts |
| **Notifications** | React Toastify |
| **Animation** | Lottie React |
| **Encryption** | RSA (PEM key pairs), Passlib/bcrypt |
| **Styling** | CSS Modules, Styled Components |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                      │
│           React 19 SPA — React Router DOM v7                 │
│   Pages: Dashboard / Chat / Projects / Workspace / RBAC     │
└───────────────────────────┬─────────────────────────────────┘
                            │  HTTP REST + WebSocket
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend (Python)                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐  │
│  │  Routers  │ │ Services │ │  RBAC    │ │   Security    │  │
│  │  /chat   │ │chat_svc  │ │ai_rbac   │ │ JWT / RSA     │  │
│  │  /work   │ │work_svc  │ │          │ │ Auth Utils    │  │
│  │  /llm    │ │dual_svc  │ │Role Gate │ │ Crypto Utils  │  │
│  │  /ws     │ │ws_utils  │ │          │ │               │  │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Pipeline: Ingestion → Cleaning → Embedding → Storage  │  │
│  └────────────────────────────────────────────────────────┘  │
└────────────┬─────────────────────────┬───────────────────────┘
             │                         │
             ▼                         ▼
┌────────────────────┐     ┌───────────────────────┐
│   Supabase         │     │   ChromaDB             │
│  (PostgreSQL +     │     │  (Vector Store)        │
│   Auth + RLS)      │     │  Semantic Embeddings   │
└────────────────────┘     └───────────────────────┘
             │
             ▼
┌────────────────────┐
│  OpenRouter API    │
│  (LLM Gateway)     │
│  Multiple Models   │
└────────────────────┘
```

---

## File Structure

```
WeBugMate/
│
├── backend/                          # FastAPI Python backend
│   │
│   ├── main.py                       # App entry point, router registration, CORS, startup tasks
│   ├── core.py                       # Supabase client init, shared DB utilities
│   ├── core_extensions.py            # Extended core helpers
│   ├── Procfile                      # Heroku/Render deployment process definition
│   ├── requirements.txt              # Python production dependencies
│   ├── requirements-auth.txt         # Auth-specific dependencies
│   │
│   ├── routers/                      # FastAPI route handlers (one file per domain)
│   │   ├── workspace_routes.py       # Workspace CRUD + WebSocket room management
│   │   ├── chat_routes.py            # Common AI chat (REST + WebSocket)
│   │   ├── work_routes.py            # Work/project-scoped AI chat
│   │   ├── dual_routes.py            # Dual chatbot comparison endpoints
│   │   ├── llm_routes.py             # Direct LLM interaction endpoints
│   │   ├── task_routes.py            # Task CRUD operations
│   │   ├── project_routes.py         # Project CRUD operations
│   │   ├── user_routes.py            # User profile management
│   │   ├── announcements_routes.py   # Company announcements
│   │   ├── broadcast_routes.py       # Broadcast messaging system
│   │   ├── feedback_routes.py        # Per-message AI feedback collection
│   │   ├── chat_id_routes.py         # Chat session/ID management
│   │   ├── records_routes.py         # Data records endpoints
│   │   ├── encryption_routes.py      # RSA encrypted API routes
│   │   └── session.py                # Session state management
│   │
│   ├── services/                     # Business logic layer
│   │   ├── chat_service.py           # Common AI chat logic
│   │   ├── work_service.py           # RBAC-filtered work chat logic
│   │   ├── dual_service.py           # Dual chatbot service
│   │   ├── chat_core.py              # Shared AI response building
│   │   ├── Workspace_service.py      # WebSocket room manager, AI config, OpenRouter calls
│   │   └── ws_utils.py               # WebSocket streaming utilities
│   │
│   ├── rbac/
│   │   └── ai_rbac.py                # Full RBAC engine: role definitions, permission map,
│   │                                 # query filters, tone gating, permission checks
│   │
│   ├── security/                     # Auth, encryption, JWT handling
│   │   ├── fastapi_routes.py         # Auth router (login, register, token)
│   │   ├── auth_utils.py             # JWT decode, get_current_user dependency
│   │   ├── crypto_utils.py           # RSA encrypt/decrypt utilities
│   │   ├── chat_security.py          # Chat-specific security guards
│   │   ├── rbac_utils.py             # Security-layer RBAC helpers
│   │   ├── avatar_utils.py           # Avatar management utilities
│   │   ├── encrypt.py                # Encryption helpers
│   │   ├── encrypt_utils.py          # Extended encryption utilities
│   │   ├── api_key.py                # API key management
│   │   ├── setup_auth.py             # Auth bootstrap
│   │   └── config/                   # RSA key pair storage
│   │       └── keys/
│   │           ├── private.pem       # RSA private key
│   │           └── public.pem        # RSA public key
│   │
│   ├── models/
│   │   └── schemas.py                # Pydantic request/response models
│   │
│   ├── pipeline/
│   │   └── pipeline.py               # Document ingestion pipeline orchestrator
│   │
│   ├── cleaning/
│   │   ├── engine.py                 # Text cleaning engine
│   │   └── rules.py                  # Cleaning rule definitions
│   │
│   ├── canonical/
│   │   ├── mapper.py                 # Maps raw AI output to canonical schema
│   │   └── schema.py                 # Canonical data schema definitions
│   │
│   ├── persistence/
│   │   └── deduplication.py          # Deduplication logic for records/embeddings
│   │
│   ├── feedback/
│   │   └── feedback_system.py        # Feedback processing & user preference scoring
│   │
│   ├── chroma_db/                    # ChromaDB vector store (local persistence)
│   │   └── chroma.sqlite3            # Vector database file
│   │
│   └── company_docs/                 # Company context documents for RAG
│       ├── about_company.txt         # We3vision company profile
│       ├── company_policies.txt      # HR / company policies
│       └── Webugmate.txt             # WeBugMate product description
│
└── frontend/                         # React 19 SPA
    │
    ├── public/                        # Static public assets
    ├── package.json                   # NPM dependencies and scripts
    │
    └── src/
        │
        ├── index.js                   # React DOM entry point
        ├── App.js                     # Root component + route definitions
        ├── reportWebVitals.js         # Performance reporting
        │
        ├── pages/                     # Page-level React components
        │   ├── Signin/                # Login / authentication page
        │   │   ├── index.js
        │   │   └── signin.css
        │   ├── Dashboard/             # Main dashboard with stats and overview
        │   │   ├── index.js
        │   │   └── Dashboard.css
        │   ├── chatbot/               # All AI chat interfaces
        │   │   ├── Communication.js   # Main communication hub
        │   │   ├── WorkChat.js        # RBAC work chat interface
        │   │   ├── DualChatbot.js     # Side-by-side dual AI chat
        │   │   ├── DeveloperChat.js   # Developer-mode chat
        │   │   ├── MessageFeedback.js # Per-message feedback widget
        │   │   └── feedback.js        # General feedback form
        │   ├── WorkspaceSetup/        # Workspace creation and room management
        │   │   ├── index.js
        │   │   └── room/
        │   │       └── Workspace.js   # Real-time workspace room component
        │   ├── project/               # Project detail and table views
        │   │   ├── ProjectDetails.js
        │   │   └── ProjectDetailsTable.js
        │   ├── Announcements/         # Company announcements page
        │   ├── Broadcasts/            # Broadcast message management
        │   ├── Role-management/       # Role assignment, email management
        │   │   ├── chooserole.js
        │   │   ├── ManageRoles.js
        │   │   └── ManageEmails.js
        │   ├── Organization/          # Organization/team view
        │   ├── Overview/              # Project overview page
        │   ├── Setting/               # User settings + avatar selection
        │   └── home/                  # Home landing page
        │
        ├── components/                # Reusable UI components
        │   └── Sidebar/               # Navigation sidebar
        │
        ├── contexts/
        │   └── messagecontext.js      # React context for messaging state
        │
        ├── services/                  # Frontend service layer
        │   ├── supabase.js            # Supabase client config + auth helpers
        │   └── projectDatabaseSupabase.js  # Project-specific DB operations
        │
        ├── rbac/                      # Frontend RBAC enforcement
        │   ├── rbacConfig.js          # Role-permission configuration
        │   ├── rbacService.js         # RBAC API calls
        │   ├── rbacUtils.js           # Utility functions for permission checks
        │   └── useRbac.js             # React hook for RBAC state
        │
        ├── utils/                     # Utility helpers
        │   ├── customUUID.js          # Custom UUID generator
        │   ├── structuredProjectId.js # Project ID formatting
        │   └── permissionUtils.js     # Permission check helpers
        │
        └── styles/
            └── responsive-global.css  # Global responsive styles
```

---

## Requirements

### Backend Requirements

```
Python >= 3.11 (tested on 3.13)

# Core
fastapi
uvicorn
gunicorn
pydantic
python-dotenv

# Database
supabase

# AI / LLM
groq
langchain
langchain-core
langchain-community
langchain-huggingface
chromadb
huggingface-hub
sentence-transformers
tiktoken
torch

# Document Processing
PyPDF2
python-docx

# Security
passlib[bcrypt]==1.7.4
numpy
```

### Frontend Requirements

```
Node.js >= 18.x
npm >= 9.x

# Core
react@^19.1.0
react-dom@^19.1.0
react-router-dom@^7.6.2

# UI
@mui/material@^7.1.1
@mui/icons-material@^7.1.1
bootstrap@^5.3.7
framer-motion@^12.23.24
styled-components@^6.1.19

# Data & API
axios@^1.13.5
@supabase/supabase-js@^2.90.1

# Utilities
react-toastify@^11.0.5
recharts@^2.15.4
lottie-react@^2.4.1
react-markdown@^10.1.0
lucide-react@^0.562.0
uuid@^13.0.0
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/we3vision/webugmate.git
cd webugmate
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend

# Install Node dependencies
npm install
```

### 4. Configure Environment Variables

Create a `.env` file inside the `backend/` directory (see [Environment Variables](#environment-variables) section below).

Create a `.env` file inside the `frontend/` directory for the React app.

---

## Environment Variables

### Backend — `backend/.env`

```env
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-service-role-key

# OpenRouter (LLM Gateway)
OPENROUTER_API_KEY=your-openrouter-api-key
OPENROUTER_MODEL=openai/gpt-4o-mini   # or any supported model

# Groq (optional fast inference)
GROQ_API_KEY=your-groq-api-key

# HuggingFace (embeddings)
HUGGINGFACEHUB_API_TOKEN=your-hf-token

# JWT / Security
SECRET_KEY=your-jwt-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# App Config
APP_ENV=development
DEBUG=True
```

### Frontend — `frontend/.env`

```env
REACT_APP_SUPABASE_URL=https://your-project.supabase.co
REACT_APP_SUPABASE_ANON_KEY=your-supabase-anon-key
REACT_APP_BACKEND_URL=http://localhost:8000
```

> ⚠️ **Never commit `.env` files to version control.** Both files are listed in `.gitignore`.

---

## Execution Commands

### Running the Backend

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment (if not already active)
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Start the development server (auto-reload enabled)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Start for production (multi-worker with Gunicorn)
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Using the Procfile (for Heroku/Render)
web: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

Backend will be live at: `http://localhost:8000`
Interactive API docs: `http://localhost:8000/docs`

### Running the Frontend

```bash
# Navigate to frontend directory
cd frontend

# Start the development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Eject from Create React App (irreversible, use with caution)
npm run eject
```

Frontend will be live at: `http://localhost:3000`

### Health Check

```bash
curl http://localhost:8000/
# Expected response: {"status": "WeBugMate Backend Running"}
```

---

## API Reference

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Login and receive JWT token |
| `GET` | `/auth/me` | Get current authenticated user |

### Chat

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/chat/common` | Send message to general AI chatbot |
| `WS` | `/chat/common/ws/{project_id}` | Stream AI responses via WebSocket |
| `POST` | `/work/chat` | RBAC-filtered work AI chat |
| `POST` | `/dual/chat` | Dual-mode side-by-side AI chat |

### Projects & Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/projects` | List all projects (RBAC-filtered) |
| `POST` | `/api/projects` | Create a new project |
| `GET` | `/api/tasks` | List tasks for a project |
| `POST` | `/api/tasks` | Create a task |
| `PATCH` | `/api/tasks/{task_id}` | Update task status/assignment |

### Workspace

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/workspaces` | List all workspaces |
| `POST` | `/api/workspaces` | Create or join a workspace |
| `GET` | `/api/projects/{project_id}/workspaces` | Get workspaces for a project |
| `POST` | `/api/workspaces/{workspace_id}/members` | Add member to workspace |
| `WS` | `/ws/{workspace_id}/{room_id}` | Real-time room WebSocket connection |

### Announcements & Broadcasts

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/announcements` | List announcements |
| `POST` | `/announcements` | Create announcement |
| `GET` | `/broadcasts` | List broadcasts |
| `POST` | `/broadcasts` | Create broadcast |

### Feedback

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/feedback/chat` | Submit per-message chat feedback |
| `POST` | `/feedback/general` | Submit general platform feedback |

---

## Workflow

### User Authentication Flow

```
1. User visits Sign In page
2. Enter email + password → Supabase Auth validates credentials
3. JWT access token returned and stored in browser
4. Token attached to every subsequent API request via Authorization header
5. FastAPI `get_current_user` dependency decodes token, extracts user email
6. RBAC engine resolves user role from `user_perms` table
```

### AI Chat Workflow

```
1. User types message in chat interface
2. Frontend sends POST to /chat/common (REST) or connects via WebSocket
3. Backend authenticates user + resolves role via RBAC engine
4. RBAC applies DB query filters (admin sees all, employee sees only assigned records)
5. Relevant records fetched from Supabase (RBAC-filtered)
6. Documents retrieved from ChromaDB via semantic similarity search
7. Context assembled: user role + filtered DB records + vector search results
8. Prompt sent to OpenRouter LLM with role-appropriate system tone
9. LLM response streamed back to frontend via WebSocket or REST
10. Response displayed; user can submit thumbs up/down feedback
```

### Feedback Learning Workflow

```
1. User clicks thumbs up/down on AI response
2. Optional tags selected: Complex / Not Relevant / Unclear / Too Long / Too Short
3. POST to /feedback/chat with message_id, is_positive, and tags array
4. Backend maps tags to scoring dimensions:
   - "Complex" → simplicity_score -= 1
   - "Not Relevant" → relevance_score -= 1
   - "Too Long" → length_score -= 1
5. user_preferences table updated in Supabase
6. Future AI responses adjust style/length/depth based on accumulated scores
```

### Workspace Real-Time Flow

```
1. User navigates to a workspace room
2. Frontend connects to WebSocket: ws://backend/ws/{workspace_id}/{room_id}
3. ConnectionManager registers the connection
4. Messages broadcast to all connected room members in real time
5. AI assistant available in rooms with cooldown-based rate limiting
6. Background task polls every 60s → marks users offline if last_seen > 20 minutes
```

---

## RBAC — Role-Based Access Control

WeBugMate implements a comprehensive RBAC system (`backend/rbac/ai_rbac.py`) as the single source of truth for all access control decisions.

### Roles

| Role | Level | Access |
|------|-------|--------|
| `admin` | Full Access | All projects, all users, all records |
| `hr` | Full Access | All records (HR context) |
| `manager` | High Access | All projects; self-only on employee_login |
| `project_manager` | Medium Access | Only assigned projects |
| `employee` | Restricted | Only records where their email appears in `assigned_to_emails` |

### How RBAC Works

1. Every API request resolves the user's role by querying the `user_perms` table.
2. `_apply_access_controls()` intercepts every Supabase query and appends `.contains("assigned_to_emails", [email])` filters for lower-privilege roles.
3. The LLM receives only the already-filtered dataset, so it cannot leak unauthorized information even if prompted to do so.
4. `get_response_tone()` returns a role-appropriate LLM system prompt tone — executive summaries for admins, task-level detail for employees.
5. `check_permission(role, action)` provides a clean boolean gate for any new feature permission checks.

---

## AI & LLM Integration

### RAG Pipeline

The Retrieval-Augmented Generation pipeline operates as follows:

1. **Ingestion** — Documents from `company_docs/` and project files are ingested via `pipeline/pipeline.py`.
2. **Cleaning** — Raw text passes through `cleaning/rules.py` for normalization.
3. **Embedding** — HuggingFace Sentence Transformers generate dense vector embeddings.
4. **Storage** — Embeddings persisted to ChromaDB local vector store.
5. **Retrieval** — At query time, the user's message is embedded and semantically matched against stored vectors.
6. **Augmentation** — Top-k retrieved chunks are injected into the LLM prompt context.
7. **Generation** — OpenRouter routes to the selected LLM model for final response.

### Canonical Schema Mapping

All structured AI output is normalized through `canonical/mapper.py` to ensure consistent response shapes regardless of which LLM model is active.

---

## WebSocket & Real-Time Features

The workspace room system uses FastAPI WebSockets with a `ConnectionManager` class in `services/Workspace_service.py`:

- **Room Isolation** — Each room maintains an independent set of active connections.
- **Broadcast** — Messages sent to one client are broadcast to all room members.
- **AI Integration** — Rooms can invoke the AI assistant with a cooldown guard (`AI_COOLDOWN_SECONDS`) to prevent flooding.
- **Disconnect Handling** — Clients are cleanly removed from the connection pool on disconnect.
- **Online Status** — A background async task (`cleanup_stuck_users`) runs every 60 seconds to mark users offline if their `last_seen` timestamp has exceeded 20 minutes.

---

## Feedback System

The adaptive feedback system (`feedback/feedback_system.py`) maintains a per-user preference profile in the `user_preferences` Supabase table with four scoring dimensions:

| Dimension | Field | Trigger Tag |
|-----------|-------|-------------|
| Simplicity | `simplicity_score` | "Complex" |
| Relevance | `relevance_score` | "Not Relevant" |
| Clarity | `clarity_score` | "Unclear" |
| Length | `length_score` | "Too Long" / "Too Short" |

These scores feed back into the LLM prompt construction to bias future responses toward the user's demonstrated preferences.

---

## Security & Encryption

- **JWT Authentication** — All protected routes use the `get_current_user` FastAPI dependency to validate Bearer tokens issued by Supabase Auth.
- **RSA Encryption** — Sensitive payloads transmitted through `encryption_routes.py` are encrypted using the RSA key pair stored in `config/keys/`.
- **CORS** — Configured to allow only specific origins (`localhost:3000`, `localhost:5173`) in development.
- **Bcrypt** — User passwords hashed with Passlib/bcrypt (`passlib[bcrypt]==1.7.4`).
- **RBAC Gate on LLM** — AI is only fed RBAC-pre-filtered data, preventing prompt injection from escalating privileges.

---

## Frontend Pages

| Page | Route | Description |
|------|-------|-------------|
| Sign In | `/` | Authentication entry point |
| Dashboard | `/dashboard` | KPIs, activity summary, quick navigation |
| Workspace | `/workspace` | Real-time collaborative workspace rooms |
| Work Chat | `/chat/work` | RBAC-scoped AI work assistant |
| Dual Chat | `/chat/dual` | Side-by-side AI response comparison |
| Projects | `/projects` | Project listing and management |
| Project Details | `/projects/:id` | Detailed project view with tasks table |
| Announcements | `/announcements` | Company-wide announcements feed |
| Broadcasts | `/broadcasts` | Broadcast message management |
| Organization | `/organization` | Team structure and member overview |
| Role Management | `/roles` | Assign/manage user roles and emails |
| Overview | `/overview` | High-level platform overview |
| Settings | `/settings` | User profile, avatar, preferences |

---

## Database Schema Overview

Key Supabase tables used by WeBugMate:

| Table | Purpose |
|-------|---------|
| `user_perms` | Stores user roles and numeric user IDs |
| `employee_login` | Employee profile records |
| `projects` | Project records with `assigned_to_emails` for RBAC |
| `tasks` | Task records linked to projects |
| `cw_workspaces` | Workspace definitions |
| `cw_rooms` | Chat rooms within workspaces |
| `cw_workspace_members` | Workspace membership + online status |
| `chat_history` | Persisted chat messages by session |
| `user_preferences` | Per-user AI feedback scoring |
| `announcements` | Company announcement records |
| `broadcasts` | Broadcast messages |

---

## Deployment

### Backend — Render / Heroku

The `Procfile` in `backend/` is pre-configured for platform deployments:

```
web: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

Set all environment variables from the [Environment Variables](#environment-variables) section in your platform's dashboard.

### Frontend — Vercel / Netlify

```bash
# Production build
cd frontend
npm run build

# The `build/` directory is ready to serve as a static site.
# Set REACT_APP_* environment variables in your deployment platform.
```

### Docker (Optional)

```dockerfile
# Backend Dockerfile (place in backend/)
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit changes: `git commit -m "feat: add your feature"`
4. Push to branch: `git push origin feature/your-feature-name`
5. Open a Pull Request against `main`.

Please follow existing code conventions and ensure all new routes include appropriate RBAC checks using `check_permission(role, action)` from `ai_rbac.py`.

---

## Company

**WeBugMate** is a product of **We3vision Private Limited** — a future-driven IT services and immersive technology company founded in 2019 and headquartered in Surat, Gujarat, India.

| | |
|---|---|
| **Company** | We3vision Private Limited |
| **Address** | 936 A, Ishwar Darshan, Bhim Kachchhi Mohallo, Nanpura, Surat – 395003, Gujarat, India |
| **Website** | [www.we3vision.com](https://www.we3vision.com) |
| **Email** | info@we3vision.com |
| **Phone** | +91 76007 72240 |
| **Founder/MD** | Mr. Harsh P Ramoliya |
| **Contact** | Parth Patel — parth@we3vision.com |

---

<div align="center">

© 2024–2026 We3vision Private Limited. All rights reserved.

*Built with ❤️ in Surat, Gujarat, India.*

</div>
