# Changelog

Todas as mudanças notáveis do projeto serão registradas aqui.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-12 (ENGLISH)

### Overview

Complete refactoring of the Library Management System. The original codebase has been improved with better code organization, clear naming conventions, comprehensive documentation, and internationalization support (English).

### Added

- **Library Management System**: A command-line application for managing book loans and returns
- **Core Features**:
  - View all available books with their availability status
  - Loan books to registered users (with loan limit validation)
  - Return loaned books (with user tracking)
  
- **Project Structure**:
  - `main.py`: Entry point with menu-driven interface
  - `app/` module: Application-specific functions
    - `fetchFuncs.py`: Data retrieval operations
    - `modifyFuncs.py`: Data modification operations (loan and return)
  - `utils/` module: Utility helper functions
    - `helpers.py`: Common utilities (file I/O, constants, setup)
  - `db/` directory: Data persistence
    - `books.txt`: Book database with ID, title, author, and availability status
    - `users.txt`: User database with ID, name, and loan status
    
- **Documentation**:
  - Function docstrings explaining purpose and behavior
  - Clear code comments for complex logic
  - Comprehensive CHANGELOG and project documentation

### Changed

- **Code Internationalization**: Migrated all code and documentation from Portuguese to English
  - Function names now follow English naming conventions
  - Variable names are clear and descriptive
  - Comments and docstrings use English for international collaboration
  
- **Code Quality Improvements**:
  - Improved method naming: `fetchFuncs` instead of unclear abbreviations
  - Added type hints to function signatures
  - Refactored file handling with context managers (`with` statements)
  - Better separation of concerns between modules
  
- **Architecture**:
  - Implemented modular structure with separation of concerns
  - Utility functions centralized in `helpers.py`
  - Clear data flow between modules

### Technical Details

#### Data Model

**Books (db/books.txt)**
```
Format: ID;Title;Author;AvailabilityStatus
- ID: Unique book identifier
- Title: Book title
- Author: Author name
- AvailabilityStatus: "1" (Available) or "0" (Unavailable)
```

**Users (db/users.txt)**
```
Format: ID;Name;LoanStatus
- ID: Unique user identifier
- Name: User name
- LoanStatus: "1" (Has loaned a book) or "0" (No loaned books)
```

#### System Flow

1. **Initialization**: `setup()` creates dataset files with initial data
2. **User Interaction**: Menu-driven interface for book operations
3. **Book Operations**: 
   - View: Display all books with availability
   - Loan: Check user limit, mark book unavailable, update user status
   - Return: Mark book available, clear user loan status
4. **Data Persistence**: Changes written back to files immediately

#### Key Design Decisions

- **File-based Database**: Simple text files for development/learning purposes
- **Status Flags**: Binary flags (0/1) for simplicity and parsing
- **Loan Limit**: One book per user at a time
- **Immediate Persistence**: Changes saved to disk after each operation

### Fixed

- Removed debug print statements (e.g., `print(ROOT_DIR)` from helpers.py)
- Fixed unclear variable naming for better code readability
- Resolved confusing logic patterns with clearer structure

### Known Limitations

- File paths use Windows-style backslashes (requires cross-platform fix)
- No input validation for book/user IDs (assumes valid input)
- No encryption or security measures (development/learning purposes only)
- Single user session (no concurrent access handling)
- No error handling for file I/O exceptions
- Limited to one book loan per user

Overall, the core business logic wasn't changed, I've decided to keep it as it was not my task to do such rewrite.

### Future Improvements

- [ ] Implement proper database (SQLite/PostgreSQL)
- [ ] Add comprehensive input validation
- [ ] Implement error handling and logging
- [ ] Add user authentication system
- [ ] Support multiple loans per user
- [ ] Implement cross-platform file path handling
- [ ] Add unit tests
- [ ] Create API layer for external access
- [ ] Add data persistence with ORM
- [ ] Implement user roles and permissions