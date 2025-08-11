# H.U.G.O-Chatbot 🎬


A simple Python-based chatbot that combines AIML (Artificial Intelligence Markup Language) with OMDB API integration to create a conversational AI that can discuss movies and engage in general conversation.

##  The Story Behind H.U.G.O

> **Built in 2016 by an inquisitive undergraduate with a passion for coding, movies and conversation** 🎓

This project represents a the general approach at the time to AI conversation - **built entirely without modern ML, NLP libraries, or dynamic APIs**. It instead uses the simplicity of AIML (Artificial Intelligence Markup Language) to create meaningful interactions.

### The Journey 📚

- **August,2016**: Conceived as a solution for movie enthusiasts who couldn't find like-minded people to discuss films with
- **Legacy**: Named after Martin Scorsese's film 'HUGO' - a beautiful movie about the love of movies and cinema
- **Evolution**: Further extended with GoodReads API for book discussions, weather integration, and more to become a fully capable assistant
- **College Project**: Later submitted for the annual college project where it was selected amongst top projects of the year


### 🏛️ GitHub Archive Program 2020

**This code is preserved for eternity!** H.U.G.O-Chatbot is archived under the GitHub Archive Program 2020, meaning this code lives in the **Doomsday Arctic Cold Vault in Svalbard, Norway** 🌍❄️. It may or may not be used to reconstruct human civilization from scratch if required! 😉

---

## ️ How It Works

### Core Architecture

H.U.G.O-Chatbot operates on a **pattern-matching paradigm** rather than modern neural networks:

1. **Input Processing**: User messages are received and normalized
2. **Pattern Matching**: AIML engine searches through 100+ knowledge files for matching patterns
3. **Response Generation**: Appropriate responses are selected and contextualized
4. **API Integration**: For movie queries, OMDB API provides real-time movie data
5. **Output**: Natural language responses are generated and returned

### Technical Flow

```
User Input → AIML Pattern Matching → Response Selection → API Calls (if needed) → Output
```

## 📁 How Each Python File Works

### 1. **`Python_Applications/first.py`** - The Core Chatbot
```python
# Main chatbot application - handles basic conversation
```
**Purpose**: Primary chatbot interface using AIML for conversation
**Key Functions**:
- Loads AIML knowledge base from `../Configuration/std-startup.xml`
- Manages brain file (`bot_brain.brn`) for performance optimization
- Handles user input/output in a continuous loop
- Uses pattern matching for response generation

### 2. **`Python_Applications/first (copy).py`** - Enhanced Movie Chatbot
```python
# Enhanced version with movie API integration
```
**Purpose**: Full-featured chatbot with movie information capabilities
**Key Functions**:
- All features of `first.py` plus movie API integration
- `mov()` function: Fetches movie data from OMDB API
- `att_check()`: Identifies movie-related attributes in user queries
- `title()`: Extracts movie titles from natural language
- Seamlessly switches between conversation and movie data retrieval

### 3. **`Python_Applications/omdb-api.py`** - Standalone Movie API Client
```python
# Standalone movie information retrieval
```
**Purpose**: Direct movie data access without chatbot interface
**Key Functions**:
- Direct OMDB API integration using `urllib`
- XML response parsing with `xml.etree.ElementTree`
- Interactive movie property lookup
- Useful for testing API functionality independently

### 4. **`Configuration/rename.py`** - Utility Script
```python
# AIML tag generator utility
```
**Purpose**: Generates AIML `<learn>` tags from file listings
**Key Functions**:
- Reads `list.txt` to get all AIML file names
- Generates proper AIML learning tags
- Helps maintain the knowledge base structure

## 🏛️ System Architecture

### High-Level Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│   AIML Engine    │───▶│  Response Gen   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Knowledge Base  │
                       │   (100+ AIML)    │
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │   API Gateway    │───▶│   OMDB API      │
                       └──────────────────┘    └─────────────────┘
```

### Component Architecture

#### **1. AIML Processing Layer**
- **Pattern Matching Engine**: Searches through AIML files for matching patterns
- **Context Management**: Maintains conversation context and user state
- **Response Selection**: Chooses appropriate responses based on patterns

#### **2. Knowledge Base Layer**
- **Core Conversation Files**: Basic chat, greetings, personality
- **Subject-Specific Knowledge**: Movies, technology, science, etc.
- **Standard AIML Set**: 40+ standardized response patterns
- **Reduction Patterns**: Text processing and normalization

#### **3. API Integration Layer**
- **OMDB API Client**: Movie information retrieval
- **XML Parser**: Response parsing and data extraction
- **Error Handling**: Graceful API failure management

#### **4. Configuration Layer**
- **Startup Configuration**: AIML file loading and initialization
- **Brain File Management**: Performance optimization through caching
- **Path Management**: File structure and reference handling


## 🎯 Usage Examples

### Basic Conversation
```
User: Hello
H.U.G.O: Well, hello! How are you today?

User: What's your favorite movie?
H.U.G.O: I love discussing movies! What genre interests you?
```

### Movie Information
```
User: What is the rating of the movie Inception?
H.U.G.O: [Fetches from OMDB API] Inception (2010) has a rating of 8.8/10 on IMDb.

User: Who directed The Matrix?
H.U.G.O: [Fetches from OMDB API] The Matrix was directed by Lana Wachowski and Lilly Wachowski.
```

## 🔧 Technical Specifications

### Dependencies
- **Core**: `aiml>=0.9.2` - AIML processing engine
- **HTTP**: `requests>=2.25.1` - API communication
- **Built-in**: `urllib`, `xml.etree.ElementTree`, `os`


### Compatibility
- **Python**: 2.7+ and 3.6+
- **OS**: Windows, macOS, Linux
- **Architecture**: x86, x64, ARM

## 🌟 Why This Approach?

### **Simplicity Over Complexity**
- **No Black Box**: Every response is traceable to specific AIML patterns
- **Transparent Logic**: Easy to understand and modify
- **Lightweight**: No heavy ML frameworks or GPU requirements
- **Reliable**: Pattern matching is deterministic and predictable

### **Educational Value**
- **Learning Tool**: Great for understanding conversational AI basics
- **Extensible**: Easy to add new topics and responses
- **Maintainable**: Clear structure and documentation
- **Portable**: Works on any system with Python

## 📁 File Structure

```
H.U.G.O-Chatbot/
├── 📁 Python_Applications
│   ├── first.py                    # Main chatbot application
│   ├── first (copy).py            # Enhanced version with movie API
│   └── omdb-api.py                # Standalone movie API client
│
├── 📁 AIML_Knowledge_Base (100+ files)
│   ├── 🎭 Core Conversation
│   │   ├── basic_chat.aiml        # Basic conversation patterns
│   │   ├── salutations.aiml       # Greetings and farewells
│   │   ├── bot_profile.aiml       # Bot personality and profile
│   │   └── movies.aiml            # Movie-related conversations
│   │
│   ├── 📚 Subject Knowledge
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

**File Categories:**
- **📁 Python Applications**: Main executable scripts
- **📁 AIML Knowledge Base**: Conversation patterns and responses
- **📁 Configuration & Setup**: System configuration files
- **📁 Documentation**: Project documentation
- **📁 Miscellaneous**: Utility and test files

**Key Statistics:**
- **Total Files**: 100+ AIML files + Python scripts
- **Knowledge Domains**: 15+ major subject areas
- **Standard Patterns**: 40+ std-*.aiml files
- **Generated Files**: 1 brain file for performance

## 📄 License

This project is based on the ALICE A.I. Foundation's AIML files, released under the GNU General Public License.


## 🙏 Acknowledgments

- **ALICE A.I. Foundation** for the comprehensive AIML knowledge base
- **OMDB API** for providing movie information
- **Python AIML library** developers
- **GitHub Archive Program** for preserving this code for future generations
- [**Python 2.7 Documentation for xml.etree.ElementTree**](https://docs.python.org/2/library/xml.etree.elementtree.html)

---



*This code is preserved in the Arctic Vault for future civilizations - a testament to human creativity and resillience* ❄️🏛️


