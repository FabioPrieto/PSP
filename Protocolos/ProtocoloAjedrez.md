### Protocolo para Ajedrez Distribuido v1.0  

#### CONVENCIONES  
- Los valores literales se especifican en mayúscula y los variables en minúscula.  
- Se utiliza `#` como separador de campos. Este carácter no debe aparecer en los datos transferidos.  
- Cada movimiento está representado en notación algebraica estándar de ajedrez.  

---

### Mensajes del Protocolo  

---

#### **1. Registro de Jugadores**  
Permite que los jugadores se registren en el servidor.  

**Precondición**:  
- El servidor debe estar disponible.  
- No puede haber más de dos jugadores registrados en una partida.  

**Postcondición**:  
- Los jugadores quedan registrados con roles asignados: blancas (`B`) o negras (`N`).  

**Mensaje**:  
- Cliente ➔ Servidor:  
  `#INSCRIBIR#nombre#`  
  - `nombre`: Nombre del jugador (alfanumérico).  

- Servidor ➔ Cliente:  
  - En caso de éxito:  
    `#OK#rol#`  
    - `rol`: Rol asignado al jugador (`B` para blancas, `N` para negras).  
  - En caso de error:  
    `#NOK#texto#`  
    - `texto`: Descripción del error (e.g., "Partida completa", "Nombre duplicado").  

---

#### **2. Iniciar Partida**  
Se utiliza para que el servidor inicie la partida una vez que ambos jugadores estén registrados.  

**Precondición**:  
- Dos jugadores deben estar registrados.  

**Postcondición**:  
- El tablero inicial es establecido, y el jugador con blancas realiza el primer movimiento.  

**Mensaje**:  
- Servidor ➔ Clientes:  
  `#INICIO#turno#tablero#`  
  - `turno`: Indica quién juega primero (`B` para blancas).  
  - `tablero`: Representación del estado inicial del tablero en formato FEN.  

---

#### **3. Movimiento**  
Permite a un jugador realizar un movimiento en la partida.  

**Precondición**:  
- El jugador debe estar registrado.  
- Debe ser el turno del jugador que realiza el movimiento.  
- El movimiento debe ser válido según las reglas del ajedrez.  

**Postcondición**:  
- El tablero se actualiza con el nuevo estado.  
- Se cambia el turno al otro jugador.  

**Mensaje**:  
- Cliente ➔ Servidor:  
  `#MOVIMIENTO#codigo#movimiento#`  
  - `codigo`: Identificador único del jugador.  
  - `movimiento`: Movimiento en notación algebraica estándar (e.g., `e2e4`, `g1f3`).  

- Servidor ➔ Clientes:  
  - En caso de éxito:  
    `#OK#turno#tablero#estado#`  
    - `turno`: Indica el turno del siguiente jugador (`B` o `N`).  
    - `tablero`: Representación actual del tablero en formato FEN.  
    - `estado`: Estado de la partida (`EN_JUEGO`, `JAQUE`, `JAQUE_MATE`, `TABLAS`).  
  - En caso de error:  
    `#NOK#texto#`  
    - `texto`: Descripción del error (e.g., "Movimiento inválido", "No es tu turno").  

---

#### **4. Solicitar Tablero**  
Permite a un jugador consultar el estado actual del tablero.  

**Precondición**:  
- El jugador debe estar registrado.  

**Postcondición**:  
- El cliente recibe la representación del tablero actual.  

**Mensaje**:  
- Cliente ➔ Servidor:  
  `#CONSULTARTABLERO#codigo#`  
  - `codigo`: Identificador único del jugador.  

- Servidor ➔ Cliente:  
  - En caso de éxito:  
    `#OK#tablero#turno#`  
    - `tablero`: Representación actual del tablero en formato FEN.  
    - `turno`: Turno del jugador actual (`B` o `N`).  
  - En caso de error:  
    `#NOK#texto#`  

---

#### **5. Solicitar Rendición**  
Permite a un jugador rendirse y finalizar la partida.  

**Precondición**:  
- El jugador debe estar registrado.  

**Postcondición**:  
- La partida se da por concluida con victoria para el oponente.  

**Mensaje**:  
- Cliente ➔ Servidor:  
  `#RENDIRSE#codigo#`  
  - `codigo`: Identificador único del jugador.  

- Servidor ➔ Clientes:  
  - En caso de éxito:  
    `#OK#ganador#`  
    - `ganador`: Indica al jugador que ganó (`B` o `N`).  
  - En caso de error:  
    `#NOK#texto#`  

---

#### **6. Finalización de Partida**  
El servidor comunica el resultado final de la partida a ambos jugadores.  

**Precondición**:  
- La partida debe haber concluido (por jaque mate, tablas o rendición).  

**Postcondición**:  
- Se informa a ambos jugadores del resultado final.  

**Mensaje**:  
- Servidor ➔ Clientes:  
  `#FIN#resultado#`  
  - `resultado`: Resultado final de la partida (`GANADOR_B`, `GANADOR_N`, `TABLAS`).  

---

### EJEMPLO DE FLUJO  

1. **Registro de Jugadores**:  
   - Cliente1 ➔ Servidor: `#INSCRIBIR#Alice#`  
   - Servidor ➔ Cliente1: `#OK#B#`  
   - Cliente2 ➔ Servidor: `#INSCRIBIR#Bob#`  
   - Servidor ➔ Cliente2: `#OK#N#`  

2. **Inicio de Partida**:  
   - Servidor ➔ Clientes: `#INICIO#B#8/8/8/8/8/8/8/RNBQKBNR w KQkq - 0 1#`  

3. **Movimiento**:  
   - Cliente1 ➔ Servidor: `#MOVIMIENTO#12345#e2e4#`  
   - Servidor ➔ Clientes: `#OK#N#rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1#EN_JUEGO#`  

4. **Movimiento Invalido**:  
   - Cliente2 ➔ Servidor: `#MOVIMIENTO#67890#e7e5e5#`  
   - Servidor ➔ Cliente2: `#NOK#Movimiento inválido#`  

5. **Rendición**:  
   - Cliente2 ➔ Servidor: `#RENDIRSE#67890#`  
   - Servidor ➔ Clientes: `#OK#B#`  
   - Servidor ➔ Clientes: `#FIN#GANADOR_B#`  

---

### LIMITACIONES Y PROPUESTAS DE MEJORA  
1. **Soporte para Temporizadores**: Incorporar tiempos de juego por jugador (e.g., 10 minutos por jugador).  
2. **Soporte para Partidas Simultáneas**: Ampliar el protocolo para manejar múltiples partidas activas en paralelo.  
3. **Historial de Movimientos**: Permitir a los jugadores consultar los movimientos realizados en la partida.  
4. **Soporte para Espectadores**: Extender el protocolo para que terceros puedan observar las partidas en tiempo real.  