Create a **FastAPI** application for managing crypto market metadata with the following requirements:

#### 1. **Project Structure**
- Follow a modular project structure:
  ```
  app/
  ├── api/
  │   ├── __init__.py
  │   ├── v1/
  │       ├── __init__.py
  │       ├── crypto_metadata_endpoints.py
  ├── core/
  │   ├── __init__.py
  │   ├── config.py
  │   ├── logging_config.py
  ├── db/
  │   ├── __init__.py
  │   ├── base.py
  │   ├── session.py
  ├── models/
  │   ├── __init__.py
  │   ├── metadata_models.py
  ├── services/
  │   ├── __init__.py
  │   ├── crypto_metadata_service.py
  ├── main.py
  └── alembic/
      ├── versions/
      ├── env.py
      ├── script.py.mako
  ```
- Use **Alembic** for database migrations.

#### 2. **Database Configuration**
- Use **SQLAlchemy** ORM with **PostgreSQL**.
- Provide reusable database session management.
- Implement the given table structures for crypto metadata entities.

#### 3. **Configuration**
- Add a `config.py` to handle application settings (e.g., database URL, environment, debugging mode).
- Use **Pydantic** models for configuration validation.

#### 4. **Logging**
- Implement centralized and configurable logging using **Python's logging module**.
- Include a `logging_config.py` file for setting up log format, handlers, and levels.

#### 5. **API Design**
- Implement versioned APIs (e.g., `/api/v1/`).
- Create CRUD operations for the `CryptoMetadata` table.
- Example API endpoints for `CryptoMetadata`:
  - `POST /api/v1/crypto-metadata/`: Create a new crypto metadata record.
  - `GET /api/v1/crypto-metadata/`: Retrieve a list of crypto metadata.
  - `GET /api/v1/crypto-metadata/{crypto_metadata_id}/`: Get a single crypto metadata record by ID.
  - `PUT /api/v1/crypto-metadata/{crypto_metadata_id}/`: Update crypto metadata by ID.
  - `DELETE /api/v1/crypto-metadata/{crypto_metadata_id}/`: Delete crypto metadata by ID.

#### 6. **Service Layer**
- Implement a `CryptoMetadataService` class under `services/crypto_metadata_service.py`:
  - Define methods for creating, reading, updating, and deleting `CryptoMetadata`.
  - Abstract business logic from the API layer for better maintainability.

#### 7. **Validation**
- Use **Pydantic** models for request and response validation.
- Ensure the API adheres to a consistent contract.

#### 8. **Test Coverage**
- Add unit tests for:
  - Database models.
  - Service layer methods.
  - API endpoints using `TestClient` from FastAPI.

#### 9. **First Implementation**
- Provide a working implementation for the `CryptoMetadata` API.
- Use the `CryptoMetadata` table structure provided below:
  ```python
  class CryptoMetadata(Base):
      __tablename__ = "crypto_metadata"
      __table_args__ = {'schema': 'reporting_schema'}

      crypto_metadata_id = Column(UUID, primary_key=True, default=uuid.uuid4)
      crypto_name = Column(String(255), nullable=False)
      crypto_symbol = Column(String(10), nullable=False, unique=True)
      market_cap_rank = Column(Integer)
      circulating_supply = Column(Integer)
      max_supply = Column(Integer)
      listed_exchange = Column(String(255), nullable=False)
      created_at = Column(DateTime(timezone=True), server_default=func.current_timestamp(), nullable=False)
      updated_at = Column(DateTime(timezone=True), server_default=func.current_timestamp(), nullable=False)
      notes = Column(Text)

      class Config:
          orm_mode = True
  ```

#### 10. **Documentation**
- Use FastAPI's built-in **OpenAPI** support to auto-generate API documentation.
- Add meaningful descriptions and examples to API endpoints for clarity.

#### 11. **Extra Features**
- Ensure all database interactions are handled within transactions.
- Make the application configurable for deployment in different environments (e.g., `dev`, `prod`).
- Include instructions for setting up the database and running migrations with Alembic.

#### Deliverables
- Full project structure as outlined.
- Working implementation for `CryptoMetadata` API endpoints.
- Clear and concise documentation for setting up and running the application.

---