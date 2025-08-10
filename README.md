# H.U.G.O-Chatbot

A comprehensive Python-based chatbot that combines AIML (Artificial Intelligence Markup Language) with OMDB API integration to create a conversational AI that can discuss movies and engage in general conversation.

## Project Overview

This is a sophisticated chatbot that successfully combines traditional AIML-based conversation with modern API integration. It demonstrates a practical approach to creating a conversational AI that can both engage in general discussion and provide specific information about movies. The extensive AIML knowledge base makes it capable of handling a wide variety of topics, while the OMDB integration adds practical utility for movie enthusiasts.

## Core Components

### 1. Main Application Files
- **`first.py`**: The primary chatbot application that loads AIML files and handles user interactions
- **`first (copy).py`**: An enhanced version that integrates movie API functionality with the chatbot
- **`omdb-api.py`**: Standalone movie information retrieval using the OMDB API

### 2. AIML Knowledge Base
The repository contains an extensive collection of AIML files (100+ files) covering various topics:

**Core Conversation Files:**
- `basic_chat.aiml` - Basic conversation patterns
- `salutations.aiml` - Greetings and farewells
- `bot_profile.aiml` - Bot personality and profile information
- `movies.aiml` - Movie-related conversations

**Subject-Specific Knowledge:**
- `ai.aiml`, `computers.aiml` - Technology topics
- `geography.aiml`, `history.aiml` - Educational content
- `humor.aiml`, `personality.aiml` - Personality and entertainment
- `math.aiml`, `science.aiml` - Academic subjects
- `sports.aiml`, `music.aiml` - Entertainment and hobbies

**Standard AIML Set:**
- Multiple `std-*.aiml` files providing standardized responses and patterns
- `std-startup.xml` - Main configuration file that loads all AIML modules

### 3. Configuration and Setup
- **`std-startup.xml`**: Central configuration file that loads all AIML knowledge files
- **`bot_brain.brn`**: Compiled brain file for faster loading (generated automatically)
- **`list.txt`**: List of all AIML files for reference
- **`rename.py`**: Utility script for generating AIML learn tags

## Key Features

### 1. AIML-Based Conversation
- Uses the AIML library for natural language processing
- Pattern matching and response generation
- Context awareness and conversation flow
- Personality traits and bot profile management

### 2. Movie Information Integration
- OMDB API integration for movie data
- Can retrieve movie details like:
  - Year, rating, release date
  - Runtime, genre, director
  - Writer, actors, plot
  - Language, country, awards
- Natural language parsing for movie queries

### 3. Multi-Topic Knowledge
The chatbot can discuss:
- Movies and entertainment
- Technology and computers
- Science and mathematics
- History and geography
- Sports and music
- Personal topics and humor
- And many other subjects

## Technical Architecture

### Dependencies
- `aiml` library for chatbot functionality
- `urllib` for API requests
- `xml.etree.ElementTree` for XML parsing

### API Integration
- OMDB API for movie information
- XML response parsing
- Error handling for API failures

### File Structure

```
H.U.G.O-Chatbot/
├── 📁 Python_Applications
│   ├── first.py                    # Main chatbot application
│   ├── first (copy).py            # Enhanced version with movie API
│   └── omdb-api.py                # Standalone movie API client
│
├── 📁 AIML_Knowledge_Base (100+ files)
│   ├──  Core Conversation
│   │   ├── basic_chat.aiml        # Basic conversation patterns
│   │   ├── salutations.aiml       # Greetings and farewells
│   │   ├── bot_profile.aiml       # Bot personality and profile
│   │   └── movies.aiml            # Movie-related conversations
│   │
│   ├──  Subject Knowledge
│   │   ├── ai.aiml                # Artificial Intelligence topics
│   │   ├── computers.aiml         # Computer and technology
│   │   ├── geography.aiml         # Geography and places
│   │   ├── history.aiml           # Historical topics
│   │   ├── humor.aiml             # Jokes and humor
│   │   ├── math.aiml              # Mathematics
│   │   ├── science.aiml           # Scientific topics
│   │   ├── sports.aiml            # Sports and athletics
│   │   └── music.aiml             # Music and entertainment
│   │
│   ├── 🎭 Personality & Social
│   │   ├── personality.aiml       # Personality traits
│   │   ├── emotion.aiml           # Emotional responses
│   │   ├── psychology.aiml        # Psychological topics
│   │   ├── gossip.aiml            # Social conversation
│   │   └── pickup.aiml            # Social interaction patterns
│   │
│   ├── 📚 Academic & Professional
│   │   ├── literature.aiml        # Literary topics
│   │   ├── politics.aiml          # Political discussions
│   │   ├── religion.aiml          # Religious topics
│   │   ├── philosophy.aiml        # Philosophical discussions
│   │   └── knowledge.aiml         # General knowledge
│   │
│   ├── 🏠 Lifestyle & Culture
│   │   ├── food.aiml              # Food and cuisine
│   │   ├── money.aiml             # Financial topics
│   │   ├── phone.aiml             # Communication devices
│   │   ├── date.aiml              # Dating and relationships
│   │   └── drugs.aiml             # Health and medicine
│   │
│   ├── 🔧 Standard AIML Set (std-*.aiml)
│   │   ├── std-startup.xml        # Main configuration loader
│   │   ├── std-hello.aiml         # Standard greetings
│   │   ├── std-botmaster.aiml     # Bot management
│   │   ├── std-errors.aiml        # Error handling
│   │   ├── std-srai.aiml          # Response redirection
│   │   └── [40+ more std-*.aiml files]
│   │
│   └── 🔄 Reduction & Processing
│       ├── reduction*.safe.aiml   # Text reduction patterns
│       ├── reduction.names.aiml   # Name processing
│       └── reductions-update.aiml # Update patterns
│
├── 📁 Configuration
│   ├── std-startup.xml            # Main AIML loader configuration
│   ├── bot_brain.brn              # Compiled brain file (auto-generated)
│   ├── list.txt                   # Complete file listing
│   └── rename.py                  # AIML tag generator utility
│
├── 📁 Documentation
│   └── README.md                  # This file
│
└── 📁 Miscellaneous
    ├── junktest.text              # Test file
    └── [other utility files]
```
