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
└── aidatataskrunner_mcp/                      # Python MCP server source code
    └── __init__.py
 
```

---

## Requirements

- For repo code
> - Check: [dependencies.json](./dependencies.json)

- For user use:
> - AiDataTaskRunner panel
> - McpServer requerid a EX5 Library, pucharse in: [TheBotPlace - McpServerByLeo](https://www.thebotplace.com/bot/mcpserverbyleo)

---
 

## Installation

```bash
cd "C:\Users\YOUR USER\AppData\Roaming\MetaQuotes\Terminal\YOUR ID\MQL5\Shared Projects"
tsndep install "https://forge.mql5.io/nique_372/AiDataTaskRunerMcp.git"
```
- For use tsndep command requerid tsndep pacakage (avaible in [pypi](https://pypi.org/project/tsndep)).. This command automatically downloads all dependencies and installs all requirements from the repositories.


---

## Quick Start (With claude ai) for final users

### 1. Install MCP Server

```bash
# Install from PyPI
pip install aidatataskrunner-mcp
```

### 2. Create a config json 

Open Common\\Files
And create a file with this structure:

```json
{
    "general_config": {
        "port": 9999,
        "host": "localhost",
        "mode": "fast_mcp"
    },
    "fast_mcp": {
        "name": "FastMcpServer"
    },
    "http": {
        "http_port": 8000,
        "name": "HTTP Server",
        "tools_namespace": "tools"
    }
}
```

### 3. Configure in Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aidatataskrunner": {
      "command": "python",
      "args": ["-m", 
      "aidatataskrunner_mcp", 
      "--config", 
      "PATH_TO_FILE", 
      "--config_encodig", 
      "utf-8"
      ]
    }
  }
}
```

- PATH_TO_FILE: Path to json config file 

### 4. Configure your MT5
Navigate to the "Tools" section >> "Options" >> "Allowed URLs for WebRequest", add a new field with the host/address you will be using (in this case "127.0.0.1"), and click Accept.

### 5. Connect with AiDataTaskRunner Panel

Start your AiDataTaskRunner Panel in MT5 with the AI tab enabled:
- The panel will connect to the MCP server on port 9999
- Claude will automatically detect available tools

### 6. Use in Claude

```md
- Add a new EURUSD task from 2023.01.01 to 2024.01.01 on H1 timeframe, and Symbol Folder = XAUUSD, Label id = 0
- Give me the total number of tasks I have
- Clean all task
- Run all task
```

Claude will automatically translate this to the appropriate MCP call.



--- 

## Available Tools

### Task Management
- `aidatataskrunner_add_task` — Add a new backtest task
- `aidatataskrunner_get_task_total` — Get total task count
- `aidatataskrunner_get_task_by_index` — Get task details by index
- `aidatataskrunner_get_task_status` — Get task execution status
- `aidatataskrunner_execute_all_tasks` — Execute all pending tasks
- `aidatataskrunner_clean_all_tasks` — Clean completed tasks

### File Operations
- `aidatataskrunner_save_tasks_to_file` — Export tasks to CSV
- `aidatataskrunner_load_tasks_from_file` — Import tasks from CSV
- `aidatataskrunner_save_config` — Save panel configuration
- `aidatataskrunner_load_config` — Load panel configuration

### Information Queries
- `aidatataskrunner_get_main_folder` — Get main data folder path
- `aidatataskrunner_get_task_folder` — Get tasks folder path
- `aidatataskrunner_is_in_commonfolder` — Check if using common MT5 folder

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