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
- **Add Tasks** — Queue new backtests with custom symbols, dates, and timeframes
- **Monitor Status** — Track task progress (Processing, Queued, Pending, Ready, Failed)
- **Batch Operations** — Execute all pending tasks or clean completed ones
- **File Management** — Save/load task configurations from CSV files

### Configuration Control
Manage panel settings via Claude:
- **Load/Save Configurations** — Save and load panel settings from text files
- **Query Folders** — Check data generation and task storage locations
- **System Information** — Access MT5 logs and system time

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

## Quick Start (With claude ai)

### 1. Install MCP Server

```bash
# Install from PyPI
pip install aidatataskrunner-mcp

# Or install in development mode
pip install -e .
```

### 2. Configure in Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aidatataskrunner": {
      "command": "python",
      "args": ["-m", "aidatataskrunner_mcp", "--host", "127.0.0.1", "--port", "9999"]
    }
  }
}
```

### 3. Configure your MT5
Navigate to the "Tools" section >> "Options" >> "Allowed URLs for WebRequest", add a new field with the host/address you will be using (in this case "127.0.0.1"), and click Accept.

### 4. Connect with AiDataTaskRunner Panel

Start your AiDataTaskRunner Panel in MT5 with the AI tab enabled:
- The panel will connect to the MCP server on port 9999
- Claude will automatically detect available tools

### 5. Use in Claude

```
Add a new EURUSD backtest from 2023.01.01 to 2024.01.01 on H1 timeframe
```

Claude will automatically translate this to the appropriate MCP call.

---

## Repository Structure

```
AiDataTaskRunerMcp/
└── aidatataskrunner_mcp/                      # Python MCP server source code
    └── __init__.py
 
```

---

## Requirements

### Python
- Python >= 3.10
- Dependencies listed in dependencies.json (or sub-dependencies of this repo)

### MetaTrader 5
- AiDataTaskRunner Panel installed and configured
- MCP connection enabled in the AI tab
- Network connectivity between Claude and MT5 (default: localhost:9999)

---

## Installation

```bash
cd "C:\Users\YOUR USER\AppData\Roaming\MetaQuotes\Terminal\YOUR ID\MQL5\Shared Projects"
tsndep install "https://forge.mql5.io/nique_372/FullMt5McpByLeo.git"
```
- For use tsndep command requerid tsndep pacakage (avaible in [pypi](https://pypi.org/project/tsndep)).. This command automatically downloads all dependencies and installs all requirements from the repositories.

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