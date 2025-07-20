# MCP-PROJECT: Learning Path Generator

A Streamlit-based web application that generates personalized learning paths using the Model Context Protocol (MCP) to integrate with YouTube and Google Drive/Notion APIs.

## 🚀 Features

- **AI-Powered Learning Path Generation**: Creates structured, day-wise learning paths based on user goals
- **YouTube Integration**: Automatically searches and curates relevant YouTube videos for each learning topic
- **Document Creation**: Generates comprehensive learning documents in Google Drive or Notion
- **Playlist Creation**: Creates public YouTube playlists with curated learning videos
- **Real-time Progress Tracking**: Visual progress indicators during generation
- **Multi-tool Integration**: Seamlessly coordinates between YouTube, Drive, and Notion APIs

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Protocol**: Model Context Protocol (MCP)
- **APIs**: YouTube, Google Drive, Notion (via Pipedream)
- **Framework**: LangChain with LangGraph

## 📋 Prerequisites

Before running this application, you'll need:

1. **Google API Key**: For Gemini AI model access
2. **Pipedream URLs**: For YouTube, Google Drive, and/or Notion integrations
3. **Python 3.8+**: Required for all dependencies

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MCP-PROJECT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Keys and URLs

You'll need to configure the following in the application:

- **Google API Key**: Required for AI model access
- **YouTube Pipedream URL**: Required for video search and playlist creation
- **Google Drive Pipedream URL**: Optional, for document creation
- **Notion Pipedream URL**: Optional, for page creation

### 4. Run the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📖 Usage Guide

### 1. Configuration Setup

1. Open the application in your browser
2. In the sidebar, enter your **Google API Key**
3. Enter your **YouTube Pipedream URL** (required)
4. Select your secondary tool: **Drive** or **Notion**
5. Enter the corresponding Pipedream URL for your selected tool

### 2. Generate Learning Path

1. Enter your learning goal in the main input field
   - Example: "I want to learn python basics in 3 days"
   - Example: "I want to learn data science basics in 10 days"

2. Click **"Generate Learning Path"**

3. Monitor the progress as the AI:
   - Sets up the agent with tools
   - Integrates with selected APIs
   - Generates your personalized learning path
   - Creates documents and playlists

### 3. Access Your Learning Path

Once generation is complete, you'll receive:
- **Document Link**: Access your structured learning path in Drive/Notion
- **YouTube Playlist Link**: Access curated videos for your learning journey

## 🏗️ Project Structure

```
MCP-PROJECT/
├── app.py              # Main Streamlit application
├── utils.py            # Core functionality and MCP integration
├── prompt.py           # AI prompt templates
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🔧 Core Components

### `app.py`
- Streamlit web interface
- User input handling
- Progress tracking and display
- Configuration management

### `utils.py`
- MCP client initialization
- Agent setup and configuration
- Tool integration (YouTube, Drive, Notion)
- Asynchronous execution handling

### `prompt.py`
- AI prompt templates for learning path generation
- Step-by-step execution instructions
- Output formatting guidelines

## 🔌 API Integrations

### YouTube API
- **Search**: Find relevant educational videos
- **Playlist Creation**: Create curated learning playlists
- **Video Selection**: Identify core learning resources

### Google Drive API
- **Document Creation**: Generate structured learning documents
- **Content Formatting**: Organize day-wise learning paths
- **Link Management**: Embed YouTube links in documents

### Notion API
- **Page Creation**: Generate learning path pages
- **Content Organization**: Structure learning materials
- **Rich Text Formatting**: Enhanced document presentation

## 🎯 Learning Path Features

### Structured Content
- **Day-wise Organization**: Logical progression through topics
- **Topic Breakdown**: Core concepts for each learning day
- **Resource Links**: Direct access to curated videos

### Quality Assurance
- **Video Curation**: Hand-picked educational content
- **Progressive Learning**: Builds from basics to advanced topics
- **Resource Diversity**: Multiple learning approaches

### Output Formats
- **Document Structure**: Clear headers and sections
- **Clickable Links**: Direct access to YouTube videos
- **Additional Resources**: Suggested channels and institutes

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your Google API key is valid and has proper permissions
   - Check that the key is entered correctly in the sidebar

2. **Pipedream URL Issues**
   - Verify your Pipedream URLs are active and accessible
   - Ensure proper authentication is configured in Pipedream

3. **Generation Failures**
   - Check your internet connection
   - Verify all required URLs are provided
   - Ensure your learning goal is clear and specific

### Error Messages

- **"Please enter your Google API key"**: Add your API key in the sidebar
- **"YouTube URL is required"**: Provide your YouTube Pipedream URL
- **"Please enter your learning goal"**: Specify what you want to learn

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Model Context Protocol (MCP)**: For enabling seamless tool integration
- **LangChain**: For AI agent orchestration
- **Streamlit**: For the web interface framework
- **Google Gemini**: For AI model capabilities

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review the project documentation

---

**Happy Learning! 🎓** 