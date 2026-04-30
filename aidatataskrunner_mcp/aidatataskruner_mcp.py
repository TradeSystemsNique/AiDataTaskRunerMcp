import socket
import json
import threading
import argparse
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

#+------------------------------------------------------------------+
#| Args                                                             |
#+------------------------------------------------------------------+
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="127.0.0.1")
parser.add_argument("--port", type=int, default=9999)
args = parser.parse_args()

HOST = args.host
PORT = args.port

#+------------------------------------------------------------------+
#| General                                                          |
#+------------------------------------------------------------------+
mcp = FastMCP("AiDataTaskRunerMT5 MCP")

# Conexion de MT5 (se llena cuando MT5 conecta)
mt5_conn = None

def esperar_mt5():
    global mt5_conn
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    mt5_conn, _ = server_sock.accept()  # espera a que MT5 conecte
    mt5_conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# Arranca en hilo separado, no bloquea el MCP
# La idea esq ue exista mientras que se termine por fin de conectar con mt5
threading.Thread(target=esperar_mt5, daemon=True).start()

#+------------------------------------------------------------------+
#| Send                                                             |
#+------------------------------------------------------------------+
def send(name: str, payload: Dict[str, Any]) -> str:
    if mt5_conn is None:
        return json.dumps({"ok": False, "error": "mt5_no_conectado"})
    
    try:
        payload_clean = json.dumps(payload, separators=(',', ':'))
        msg = f'{{"name":"{name}","data":{payload_clean}}}\n'
        
        # Enviamos
        mt5_conn.sendall( msg.encode("utf-8"))
        
        # Esperamos la repuesta
        response = b""
        while not response.endswith(b"\n"):
            chunk = mt5_conn.recv(4096)
            if not chunk:
                return json.dumps({"ok": False, "error": "mt5_desconectado"})
            response += chunk
        
        return response.decode("utf-8").strip()
    
    except Exception as e:
        return json.dumps({"ok": False, "error": str(e)})

#+------------------------------------------------------------------+
#| Funciones                                                        |
#+------------------------------------------------------------------+
# Funciones
@mcp.tool()
def aidatataskrunner_add_task(payload: Dict[str, Any]) -> str:
    """
    Agrega una nueva tarea de backtest a la tabla de AiDataTaskRunner.

    Parametros (DICT):
      - symbol        (string, requerido): Simbolo de trading. Ej: "EURUSD", "XAUUSD"
      - start_date    (string, requerido): Fecha inicio. Formato: "YYYY.MM.DD HH:MM"
      - end_date      (string, requerido): Fecha fin.   Formato: "YYYY.MM.DD HH:MM"
      - timeframe     (string, opcional): Temporalidad MQL5. Ej: "PERIOD_H1", "PERIOD_M15". Default: "_Period"
      - set_file      (string, opcional): Ruta al archivo .set de parametros del EA. Default: ""
      - symbol_folder (string, opcional): Subcarpeta para agrupar datos. Ej: "XAUUSD". Default: ""
      - label         (string, opcional): Nombre de la estrategia. Ej: "BosChoch". Default: ""
      - label_id      (string, opcional): ID variante del label. Ej: "0", "1". Default: "0"

    Retorna (JSON):
      - ok     (boolean): true si se agrego correctamente
      - result (string):  mensaje de confirmacion o error

    Ejemplo llamada: {"symbol": "EURUSD", "start_date": "2023.01.01 00:00", "end_date": "2024.01.01 00:00"}
    Ejemplo retorno: {"ok": true, "result": "Task added successfully"}
    """
    return send("aidatataskrunner_add_task", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_get_task_total(payload: Dict[str, Any]) -> str:
    """
    Retorna el numero total de tareas actualmente en la tabla.

    Parametros: ninguno, pasar DICT vacio "{}"

    Retorna (JSON):
      - ok     (boolean): true si la consulta fue exitosa
      - result (integer como string): numero total de tareas

    Ejemplo llamada: {}
    Ejemplo retorno: {"ok": true, "result": "5"}
    """
    return send("aidatataskrunner_get_task_total", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_get_task_by_index(payload: Dict[str, Any]) -> str:
    """
    Retorna los detalles completos de una tarea segun su indice en la tabla.
    Usar aidatataskrunner_get_task_total para conocer el total antes de llamar.

    Parametros (DICT):
      - index (integer, requerido): Indice base 0 de la tarea

    Retorna (JSON):
      - ok     (boolean): true si el indice es valido
      - result (string):  datos de la tarea separados por | (timeframe|symbol|set_file|start|end|folder|label|label_id)

    Ejemplo llamada: {"index": 0}
    Ejemplo retorno: {"ok": true, "result": "16385|EURUSD||2023.01.01 00:00|2024.01.01 00:00|||0"}
    """
    return send("aidatataskrunner_get_task_by_index", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_get_task_status(payload: Dict[str, Any]) -> str:
    """
    Retorna el estado actual de una tarea segun su indice en la tabla.

    Parametros (DICT):
      - index (integer, requerido): Indice base 0 de la tarea

    Retorna (JSON):
      - ok     (boolean): true si el indice es valido
      - result (integer como string):
          "0" = Procesando
          "1" = En cola
          "2" = Pendiente
          "3" = Listo
          "4" = Fallo

    Ejemplo llamada: {"index": 0}
    Ejemplo retorno: {"ok": true, "result": "2"}
    """
    return send("aidatataskrunner_get_task_status", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_clean_all_tasks(payload: Dict[str, Any]) -> str:
    """
    Elimina de la tabla todas las tareas que no esten en ejecucion ni en cola.
    Las tareas con estado Procesando o En cola no se eliminan.

    Parametros: ninguno, pasar DICT vacio "{}"

    Retorna (JSON):
      - ok     (boolean): true si se limpio al menos una tarea
      - result (string):  mensaje de confirmacion o indicacion de que no habia nada que limpiar

    Ejemplo llamada: {}
    Ejemplo retorno: {"ok": true, "result": "All tasks cleaned"}
    """
    return send("aidatataskrunner_clean_all_tasks", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_execute_all_tasks(payload: Dict[str, Any]) -> str:
    """
    Pone en cola de ejecucion todas las tareas con estado Pendiente.
    Operacion fire-and-forget: retorna inmediatamente sin esperar resultado.

    Parametros: ninguno, pasar DICT vacio "{}"

    Retorna (JSON):
      - ok     (boolean): siempre true
      - result (string):  "queued"

    Ejemplo llamada: {}
    Ejemplo retorno: {"ok": true, "result": "queued"}
    """
    return send("aidatataskrunner_execute_all_tasks", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_save_tasks_to_file(payload: Dict[str, Any]) -> str:
    """
    Guarda las tareas de la tabla en un archivo CSV.
    La ruta es relativa a la carpeta de trabajo de MT5.
    Consultar aidatataskrunner_is_in_commonfolder para saber si es Common\\Files\\ o MQL5\\Files\\.

    Parametros (DICT):
      - file_name       (string,  requerido): Ruta relativa del archivo .csv destino
      - only_unfinished (boolean, requerido): true = guardar solo pendientes/en cola/procesando | false = guardar todas

    Retorna (JSON):
      - ok     (boolean): true si se guardo correctamente
      - result (string):  mensaje de confirmacion o error

    Ejemplo llamada: {"file_name": "tasks.csv", "only_unfinished": false}
    Ejemplo retorno: {"ok": true, "result": "Successfully saving all tasks to file tasks.csv"}
    """
    return send("aidatataskrunner_save_tasks_to_file", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_load_tasks_from_file(payload: Dict[str, Any]) -> str:
    """
    Carga tareas desde un archivo CSV y las agrega a la tabla.
    La ruta es relativa a la carpeta de trabajo de MT5.
    Consultar aidatataskrunner_is_in_commonfolder para saber si es Common\\Files\\ o MQL5\\Files\\.

    Parametros (DICT):
      - file_name (string, requerido): Ruta relativa del archivo .csv a cargar

    Retorna (JSON):
      - ok     (boolean): true si se cargo correctamente
      - result (string):  mensaje de confirmacion o error

    Ejemplo llamada: {"file_name": "tasks.csv"}
    Ejemplo retorno: {"ok": true, "result": "Tasks loaded successfully"}
    """
    return send("aidatataskrunner_load_tasks_from_file", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_load_config(payload: Dict[str, Any]) -> str:
    """
    Carga la configuracion del tab de generacion de datos desde un archivo .txt.
    La ruta es relativa a la carpeta de trabajo de MT5.
    Consultar aidatataskrunner_is_in_commonfolder para saber si es Common\\Files\\ o MQL5\\Files\\.

    Parametros (DICT):
      - file_name (string, requerido): Ruta relativa del archivo .txt a cargar

    Retorna (JSON):
      - ok     (boolean): true si se cargo correctamente
      - result (string):  mensaje de confirmacion o error

    Ejemplo llamada: {"file_name": "config.txt"}
    Ejemplo retorno: {"ok": true, "result": "Config loaded successfully"}
    """
    return send("aidatataskrunner_load_config", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_save_config(payload: Dict[str, Any]) -> str:
    """
    Guarda la configuracion actual del tab de generacion de datos en un archivo .txt.
    La ruta es relativa a la carpeta de trabajo de MT5.
    Consultar aidatataskrunner_is_in_commonfolder para saber si es Common\\Files\\ o MQL5\\Files\\.

    Parametros (DICT):
      - file_name (string, requerido): Ruta relativa del archivo .txt destino

    Retorna (JSON):
      - ok     (boolean): true si se guardo correctamente
      - result (string):  mensaje de confirmacion o error

    Ejemplo llamada: {"file_name": "config.txt"}
    Ejemplo retorno: {"ok": true, "result": "Config saved successfully"}
    """
    return send("aidatataskrunner_save_config", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_get_main_folder(payload: Dict[str, Any]) -> str:
    """
    Retorna la ruta de la carpeta base principal usada por AiDataTaskRunner.
    Relativa a Common\\Files\\ o MQL5\\Files\\ segun aidatataskrunner_is_in_commonfolder.

    Parametros: ninguno, pasar DICT vacio "{}"

    Retorna (JSON):
      - ok     (boolean): true siempre
      - result (string):  ruta de la carpeta principal

    Ejemplo llamada: {}
    Ejemplo retorno: {"ok": true, "result": "AiDataTaskRunerPro\\"}
    """
    return send("aidatataskrunner_get_main_folder", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_get_task_folder(payload: Dict[str, Any]) -> str:
    """
    Retorna la ruta de la carpeta donde se almacenan los archivos de tareas.
    Relativa a Common\\Files\\ o MQL5\\Files\\ segun aidatataskrunner_is_in_commonfolder.

    Parametros: ninguno, pasar DICT vacio "{}"

    Retorna (JSON):
      - ok     (boolean): true siempre
      - result (string):  ruta de la carpeta de tareas

    Ejemplo llamada: {}
    Ejemplo retorno: {"ok": true, "result": "AiDataTaskRunerPro\\Tasks\\"}
    """
    return send("aidatataskrunner_get_task_folder", payload)

#+------------------------------------------------------------------+
@mcp.tool()
def aidatataskrunner_is_in_commonfolder(payload: Dict[str, Any]) -> str:
    """
    Indica si AiDataTaskRunner esta operando sobre la carpeta comun de MT5 (Common\\Files\\)
    o sobre la carpeta local del terminal (MQL5\\Files\\).
    Util para construir rutas correctas antes de llamar a otras funciones.

    Parametros: ninguno, pasar DICT vacio "{}"

    Retorna (JSON):
      - ok     (boolean): true siempre
      - result (string):  "1" = usa Common\\Files\\ | "0" = usa MQL5\\Files\\

    Ejemplo llamada: {}
    Ejemplo retorno: {"ok": true, "result": "1"}
    """
    return send("aidatataskrunner_is_in_commonfolder", payload)


#+------------------------------------------------------------------+
#| Main                                                             |
#+------------------------------------------------------------------+
def main():
    mcp.run()

if __name__ == "__main__":
    main()