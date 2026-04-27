# Anime Recommender System using RAG

## 🚀 Overview
This repository contains an **Anime Recommender System** powered by a Retrieval-Augmented Generation (RAG) architecture. By leveraging a vector database filled with anime synopses and metadata, the system can understand complex user queries, retrieve relevant anime profiles, and use a Large Language Model (LLM) to generate highly personalized and context-aware recommendations. 

## 📁 Project Structure
The project is organized in a modular and highly maintainable structure:

* **`app/`**: Contains the main application script (`app.py`) for interacting with the recommender system.
* **`chroma_db/`**: The local directory for the Chroma vector database, storing embedded anime data for fast semantic retrieval.
* **`config/`**: Configuration settings (`config.py`) containing environment and API variables.
* **`data/`**: Stores the raw CSV datasets, including `anime_with_synopsis.csv` and `anime_updated.csv`.
* **`pipeline/`**: Contains scripts (`pipeline.py`, `build_pipeline.py`) to manage the end-to-end flow of data ingestion, processing, and vectorization.
* **`src/`**: The core source code of the RAG system:
  * `data_loader.py`: Handles reading and pre-processing the anime CSV files.
  * `vector_store.py`: Manages embedding generation and interactions with ChromaDB.
  * `prompt_template.py`: Defines the system prompts that guide the LLM's conversational and recommendation responses.
  * `recommender.py`: The orchestrator that ties retrieval and generation together to produce the final recommendations.
* **`utils/`**: Helper scripts for custom exception handling (`custom_exception.py`) and robust system logging (`logger.py`).

## 🛠️ Technologies Used
* **Python** (Core language managed via `setup.py` and `requirements.txt`)
* **ChromaDB** (Vector Database for RAG)
* **Large Language Models (LLMs)** (Integrated via the `src/recommender.py` and prompt templates)
* **Pandas** (For dataset manipulation)

## ⚙️ Setup & Installation

### 1. Prerequisites
Ensure you have Python installed on your system. 

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/Anime-Recommender-System-using-RAG.git
cd Anime-Recommender-System-using-RAG
```

### 3. Install Dependencies
You can install the required packages using the provided requirements file:
```bash
pip install -r requirements.txt
```
*Alternatively, you can install the project as a package using `setup.py`:*
```bash
pip install -e .
```

## 🚀 Usage

### 1. Build the Pipeline
Before running the app, you need to ingest the CSV data and generate the vector embeddings. Run the pipeline script to process the data and populate `chroma_db`:
```bash
python pipeline/build_pipeline.py
```

### 2. Run the Application
Once the vector database is ready, you can start the recommender system application:
```bash
python app/app.py
```
Interact with the system by passing your anime preferences, themes, or queries, and the RAG model will return detailed, contextually relevant anime recommendations!
