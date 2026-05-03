#+------------------------------------------------------------------+
#| Imports                                                          |
#+------------------------------------------------------------------+
import mcp_mt5_conection
from typing import Dict, Any 
import json
import argparse
from argparse import Namespace

#+------------------------------------------------------------------+
#| Args                                                             |
#+------------------------------------------------------------------+
g_parser : argparse.ArgumentParser = argparse.ArgumentParser()
g_parser.add_argument("--config", type=str, default="")
g_parser.add_argument("--config_encodig", type=str, default="utf-8")
g_args : Namespace = g_parser.parse_args()
 
# Leemos config 
g_config : dict = None 
with open(g_args.config, "r", encoding=g_args.config_encodig) as f:
    g_config = json.load(f)
    
    
# Config esperada:
"""
{
    "general_config" : {
        "port" : 9999,
        "host" : "localhost"
        "mode" : "fast_mcp"
    }
    "fast_mcp" : {
        "name" :  "FastMcpServer"
    }
    "http" : {
        "http_port" : 8000,
        "name" : "HTTP Server",
        "tools_namespace" : "tools"
    }
    
}
"""    
    
#+------------------------------------------------------------------+
#| General                                                          |
#+------------------------------------------------------------------+
g_conection : mcp_mt5_conection.CMt5McpConection = mcp_mt5_conection.CMt5McpConection(g_config["general_config"]["host"],g_config["general_config"]["port"]) 
g_registrador : mcp_mt5_conection.CToolRegister = mcp_mt5_conection.CToolRegisterMCP(g_config,g_conection) if g_config["general_config"]["mode"] == "fast_mcp" else mcp_mt5_conection.CToolRegisterFastApi(g_config,g_conection) 




#+------------------------------------------------------------------+
#| Funciones                                                        |
#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_add_task(payload: Dict[str, Any]) -> None:
    """
      "description": "Agrega una nueva tarea de backtest a la tabla de AiDataTaskRunner.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "timeframe": {
            "type": "string",
            "description": "Timeframe para el backtest | string:mt5:ENUM_TIMEFRAME | PERIOD_H1, PERIOD_D1, PERIOD_M15 | _Period (actual)"
          },
          "symbol": {
            "type": "string",
            "description": "Símbolo de trading | string | EURUSD, XAUUSD | requerido"
          },
          "set_file": {
            "type": "string",
            "description": "Archivo de configuración del set | string:ruta | config.set | vacío"
          },
          "start_date": {
            "type": "string",
            "description": "Fecha inicio del backtest | string:datetime | 2023.01.01 00:00 | requerido"
          },
          "end_date": {
            "type": "string",
            "description": "Fecha fin del backtest | string:datetime | 2024.01.01 00:00 | requerido"
          },
          "symbol_folder": {
            "type": "string",
            "description": "Carpeta destino para resultados | string:ruta | folder_name | vacío"
          },
          "label": {
            "type": "string",
            "description": "Etiqueta descriptiva de la tarea | string | test_001 | vacío"
          },
          "label_id": {
            "type": "string",
            "description": "ID numérico de la etiqueta | string:int | 1, 2, 3 | 0"
          }
        },
        "required": ["symbol", "start_date", "end_date"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_get_task_total(payload: Dict[str, Any]) -> None:
    """
      "description": "Retorna el número total de tareas actualmente en la tabla.",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_get_task_by_index(payload: Dict[str, Any]) -> None:
    """
      "description": "Retorna los detalles completos de una tarea según su índice en la tabla (timeframe|symbol|set_file|start|end|folder|label|label_id).",
      "inputSchema": {
        "type": "object",
        "properties": {
          "index": {
            "type": "integer",
            "description": "Índice de la tarea | integer:0+ | 0, 1, 2 | requerido"
          }
        },
        "required": ["index"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_get_task_status(payload: Dict[str, Any]) -> None:
    """
      "description": "Retorna el estado actual de una tarea. Estados: 0=Procesando, 1=En cola, 2=Pendiente, 3=Listo, 4=Fallo",
      "inputSchema": {
        "type": "object",
        "properties": {
          "index": {
            "type": "integer",
            "description": "Índice de la tarea | integer:0+ | 0, 1, 2 | requerido"
          }
        },
        "required": ["index"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_clean_all_tasks(payload: Dict[str, Any]) -> None:
    """
      "description": "Elimina todas las tareas que no estén en ejecución ni en cola (no elimina estado Procesando o En cola).",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_execute_all_tasks(payload: Dict[str, Any]) -> None:
    """
      "description": "Pone en cola de ejecución todas las tareas con estado Pendiente. Operación fire-and-forget (retorna inmediatamente).",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_save_tasks_to_file(payload: Dict[str, Any]) -> None:
    """
      "description": "Guarda las tareas en un archivo CSV. Ruta relativa a Common\\\\Files\\\\ o MQL5\\\\Files\\\\",
      "inputSchema": {
        "type": "object",
        "properties": {
          "file_name": {
            "type": "string",
            "description": "Ruta relativa del archivo CSV | string:ruta | tasks.csv, datos/export.csv | requerido"
          },
          "only_unfinished": {
            "type": "boolean",
            "description": "Guardar solo pendientes/cola/procesando | boolean | true, false | requerido"
          }
        },
        "required": ["file_name", "only_unfinished"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_load_tasks_from_file(payload: Dict[str, Any]) -> None:
    """
      "description": "Carga tareas desde un archivo CSV y las agrega a la tabla. Ruta relativa a Common\\\\Files\\\\ o MQL5\\\\Files\\\\",
      "inputSchema": {
        "type": "object",
        "properties": {
          "file_name": {
            "type": "string",
            "description": "Ruta relativa del archivo CSV | string:ruta | tasks.csv, datos/import.csv | requerido"
          }
        },
        "required": ["file_name"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_load_config(payload: Dict[str, Any]) -> None:
    """
      "description": "Carga la configuración del tab de generación de datos desde un archivo TXT. Ruta relativa a Common\\\\Files\\\\ o MQL5\\\\Files\\\\",
      "inputSchema": {
        "type": "object",
        "properties": {
          "file_name": {
            "type": "string",
            "description": "Ruta relativa del archivo TXT | string:ruta | config.txt, conf/setup.txt | requerido"
          }
        },
        "required": ["file_name"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_save_config(payload: Dict[str, Any]) -> None:
    """
      "description": "Guarda la configuración actual del tab de generación de datos en un archivo TXT. Ruta relativa a Common\\\\Files\\\\ o MQL5\\\\Files\\\\",
      "inputSchema": {
        "type": "object",
        "properties": {
          "file_name": {
            "type": "string",
            "description": "Ruta relativa del archivo TXT destino | string:ruta | config.txt, conf/setup.txt | requerido"
          }
        },
        "required": ["file_name"]
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_get_main_folder(payload: Dict[str, Any]) -> None:
    """
      "description": "Retorna la ruta de la carpeta base principal de AiDataTaskRunner (relativa a Common\\\\Files\\\\ o MQL5\\\\Files\\\\).",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_get_task_folder(payload: Dict[str, Any]) -> None:
    """
      "description": "Retorna la ruta de la carpeta donde se almacenan los archivos de tareas (relativa a Common\\\\Files\\\\ o MQL5\\\\Files\\\\).",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    """
    pass

#+------------------------------------------------------------------+
@g_registrador.register_tool_decorator()
def aidatataskrunner_is_in_commonfolder(payload: Dict[str, Any]) -> None:
    """
      "description": "Indica si AiDataTaskRunner usa carpeta común (1) o carpeta local del terminal (0). Necesario para construir rutas correctas.",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    """
    pass


#+------------------------------------------------------------------+
#| Main                                                             |
#+------------------------------------------------------------------+
def main():
    g_registrador.run()

if __name__ == "__main__":
    main()