# fugle-workflow

The `fugle-workflow` project is designed to orchestrate and manage data pipelines efficiently. This project integrates several technologies to ensure seamless data flow, storage, and API access, making it ideal for handling intraday stock quotes and other financial data.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Introduction

`fugle-workflow` is a data pipeline orchestration codebase that integrates with multiple tools and services to manage data from collection to storage and retrieval. This workflow is particularly tailored for financial data, ensuring that data is processed efficiently and available for consumption through a RESTful API.

## Technologies Used

- **PostgreSQL**: The primary data storage system used for persisting data securely and efficiently.
- **Postgres REST**: A RESTful API built on top of PostgreSQL, allowing for easy data access and manipulation.
- **Kestra**: A modern data pipeline orchestration tool, enabling the seamless flow of data through various stages.
- **Fugle-FastAPI**: A custom component serving as the data source, integrated with FastAPI to handle intraday stock quotes and other data needs.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your machine (for running services in containers).
- Basic understanding of SQL and RESTful APIs.
- Python 3.9+ for running and modifying FastAPI services.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yitech/fugle-workflow.git
   cd fugle-workflow
   ```

2. Set up the environment by creating a `.env` file and configuring your environment variables as needed.

3. Start the services using Docker Compose:

   ```bash
   docker-compose up -d
   ```

### Configuration

Configure the `fugle-workflow` by modifying the `config.yaml` file to suit your data pipeline needs. Make sure to set the correct database credentials and API keys where necessary.

## Usage

After setting up the environment, you can interact with the data pipeline through the following:

- **Kestra UI**: Access the Kestra dashboard to monitor and manage data workflows.
- **Postgres REST API**: Use the REST API to interact with the data stored in PostgreSQL.
- **Fugle-FastAPI**: Utilize the FastAPI interface to retrieve intraday stock quotes and other financial data.

## Project Structure

```plaintext
fugle-workflow/
│
├── kestra/                # Kestra pipeline definitions
├── postgres-rest/         # Postgres REST API setup and configuration
├── config.yaml            # Main configuration file for the workflow
├── docker-compose.yml     # Docker Compose setup for all services
└── README.md              # Project documentation
```