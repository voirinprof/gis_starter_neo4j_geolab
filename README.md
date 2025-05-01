# GIS Starter – Neo4j + Python + Devcontainer

This repository provides a ready-to-use development environment for working with **Neo4j** and **Python**, especially suited for geospatial analysis and graph-based data modeling using **GitHub Codespaces** or **Devcontainers**.

## 🚀 Features

- 📦 **Devcontainer** support for GitHub Codespaces or local VS Code Remote Containers
- 🐍 **Python 3.11** with `neo4j`, `geopandas`, and other useful GIS libraries
- 🧠 **Neo4j 4.4** graph database in Docker
- ⚡ Easy configuration of environment variables and ports
- 🗃️ Volumes for data persistence

---

## 📁 Project Structure

```
gis_starter_neo4j_geolab/
├── .devcontainer/
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── devcontainer.json
│   └── Dockerfile
└── scripts/
    └── ...   # Your Python script to connect to Neo4j
```

---

## 🐳 Services (Docker Compose)

- **Python app**
  - Linked to Neo4j with environment variables
- **Neo4j**
  - Exposes ports `7474` (HTTP) and `7687` (Bolt)
  - Credentials: `neo4j / neo4j_pwd`
  - Volumes for persistent data and imports

---

## 🔧 Getting Started

### 📦 Prerequisites

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) + [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- OR use [GitHub Codespaces](https://github.com/features/codespaces)

### ▶️ Run the environment

1. Clone the repository:
   ```bash
   git clone https://github.com/voirinprof/gis_starter_neo4j_geolab.git
   cd gis_starter_neo4j_geolab
   ```

2. Open in **VS Code** and choose "Reopen in Container", or launch a **Codespace**.

3. Docker Compose will automatically start the Neo4j service.

---

## 🌐 Access Neo4j Browser (there is a bug on codespaces)

- In **local dev**: [http://localhost:7474](http://localhost:7474)
- In **Codespaces**: use the forwarded port `7474`, e.g.  
  `https://7474-<your-codespace-id>.preview.app.github.dev`

> ⚠️ You may need to use `bolt+ssc://localhost:7687` inside the Neo4j browser if `bolt://` is blocked.

---

## 📚 Useful Libraries

Installed via `requirements.txt`:

- `neo4j` – Neo4j Python driver
- `geopandas` – for geospatial data handling
- `pandas`, `shapely`, `pyproj`, `matplotlib`, ...

---

## 🤝 Contributing

Feel free to fork this repo, suggest improvements, or open issues for bug reports or feature ideas.