<!-- mcp-name: io.github.TradeSystemsNique/aidatataskrunner-mcp -->
<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776ab?style=flat-square"/>
  <img src="https://img.shields.io/badge/Protocol-MCP-1B6CA8?style=flat-square"/>
  <img src="https://img.shields.io/badge/Platform-MetaTrader%205-0D1B2A?style=flat-square"/>
  <img src="https://img.shields.io/badge/Author-nique__372%20and%20Leo-C9D6DF?style=flat-square"/>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-Nique%26Leo%20NL--ND-red.svg"/>
  </a>
</p>

<p align="center">
  <strong>Control AiDataTaskRunner Panel directly via MCP</strong>
</p>

---

## Main features

### Task Management
Control your backtesting queue directly from Claude:
- **Add Tasks:** Queue new backtests with custom symbols, dates, and timeframes
- **Monitor Status:** Track task progress (Processing, Queued, Pending, Ready, Failed)
- **Batch Operations:** Execute all pending tasks or clean completed ones
- **File Management:** Save/load task configurations from CSV files

### Configuration Control
Manage panel settings via Claude:
- **Load/Save Configurations:** Save and load panel settings from text files
- **Query Folders:** Check data generation and task storage locations
- **System Information:** Access MT5 logs and system time

### Natural Language Integration
Use Claude to automate your trading data pipeline:
- Query task counts and details
- Add multiple backtests in batch
- Organize and manage task configurations
- Monitor real-time execution status

### Real-Time Updates
- Asynchronous operations delivered directly to chat
- Non-blocking task execution (fire-and-forget support)
- Instant status feedback from the panel

---

## Repository Structure

```
AiDataTaskRunerMcp/
└── aidatataskrunner_mcp/                      # JSON Tools definition
 
```

---

## Requirements
- AiDataTaskRunner panel functional.
- License for McpServer requerid a EX5 Library, and EXE for McpServer, pucharse in: [TheBotPlace - McpServerByLeo](https://www.thebotplace.com/bot/mcpserverbyleo)

---
 
## Installation

```bash
cd "C:\Users\YOUR USER\AppData\Roaming\MetaQuotes\Terminal\YOUR ID\MQL5\Shared Projects"
tsndep install "https://forge.mql5.io/nique_372/AiDataTaskRunerMcp.git"
```
- For use tsndep command requerid tsndep pacakage (avaible in [pypi](https://pypi.org/project/tsndep)).. This command automatically downloads all dependencies and installs all requirements from the repositories.


---

## Quick Start (With claude ai) for final users


 
### 1. Create a config json 

Open Common\\Files
And create a json file with this structure:

```json
{
  "general": {
    "type_reg": "stdio_stdin",
    "json_tools_fpath": "JSON_TOOL_PATH"
  },
  "mt5_conn": {
    "host": "127.0.0.1",
    "port": 9999
  },
  "http_lib": {
    "name": "McpMt5Server",
    "version": "1.0.0",
    "host": "127.0.0.1",
    "port": 8080,
    "endpoint": "/"
  },
  "stdio_stdin": {
    "name": "MT5 MCP Server",
    "version": "1.0.0"
  }
}
```

- JSON_TOOL_PATH: Path to the tools configuration json (you can download the json from the aidatataskrunner_mcp folder and place it in documents for example and put the path to said file here...) Or if you have the repository cloned, you can use the path to tools.json

### 2. Configure in Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aidatataskrunner_mcp": {
      "command": "PATH_TO_EXE",
      "args": ["PATH_TO_FILE", "YOUR_TBP_ID", "YOUR_MT5_ACCOUNT_LOGIN_ID" 
      ]
    }
  }
}
```

- PATH_TO_EXE: Path to exe McpServer file
- PATH_TO_FILE: Path to json config file
- YOUR_TBP_ID: Your The Bot Place user ID
- YOUR_MT5_ACCOUNT_LOGIN_ID: ACCOUNT_LOGGIN of your mt5 account where AiDataTaskRunner Panel EA is running

### 3. Configure your MT5
In MT5: **Tools** → **Options** → **Allowed URLs for WebRequest**
- Add `127.0.0.1` or host you configured.
- Click **Accept**
- Enable AutoTrading and DLL imports

### 4. Open claude desktop 
Open Claude Desktop. At that moment, a Python script is running in the background until it establishes a connection with the EA McpServer.ex5.

### 5. Connect with AiDataTaskRunner Panel

Start your AiDataTaskRunner Panel in MT5, then go to the Ai tab and then to Mcp, finally configure the server and launch it. A new chart will open with a new EA.
 
### 6. Use in Claude

```md
- Add a new EURUSD task from 2023.01.01 to 2024.01.01 on H1 timeframe, and Symbol Folder = XAUUSD, Label id = 0
- Give me the total number of tasks I have
- Clean all task
- Run all task
```

Claude will automatically translate this to the appropriate MCP call.

Note:
> You can also use HTTP Remote with the help of "mcp-remote" (see: https://forge.mql5.io/nique_372/McpServer/wiki/Running-HTTP)


--- 

## Available Tools

Check: [Tools definition.](./aidatataskrunner_mcp/tools.json)

---
## License

**[Read Full License](./LICENSE)**
By downloading or using this repository, you accept the license terms.

---

## Documentation

Full documentation is available in the main repository:
- [AiDataTaskRunner Wiki](https://forge.mql5.io/nique_372/AiDataTaskRuner/wiki)
- [MCP Integration Guide](https://forge.mql5.io/nique_372/AiDataTaskRuner/wiki/AiMCP)
- [MCP Integration Guide with claude](https://forge.mql5.io/nique_372/AiDataTaskRuner/wiki/AiMcpClaude)

---

## Contact
- **Platform:** [MQL5 Community](https://www.mql5.com/es/users/nique_372)
- **Profile:** https://www.mql5.com/es/users/nique_372/news
 
---

<p align="center">Copyright © 2026 Nique-Leo.</p>