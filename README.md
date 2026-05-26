# Trapyador 🧹

Trapyador es un pequeño programa para desinstalar aplicaciones de una manera cómoda desde la consola.
Unicamente compatible con Windows.

## Descripción

El script escanea el registro de Windows para detectar programas instalados y muestra una lista interactiva para seleccionar cuáles deseas desinstalar.

Podes navegar por la lista usando:

- Flecha ARRIBA
- Flecha ABAJO
- ESPACIO para seleccionar programas
- ENTER para confirmar

Una vez confirmada la selección, el script ejecuta los comandos necesarios para desinstalar cada programa.

---

## Requisitos

- Python 3.x (para ejecutarlo desde Python)
- Windows
- Dependencias (para ejecutarlo desde Python):
  - `questionary`

---

## Instalación

1. **Mediante ejecutable**: Baja el ejecutable desde la pestaña [Releases](https://github.com/julpr833/trapyador/releases/tag/release)

2. **Mediante Python**

Clona el repositorio:

```bash
git clone https://github.com/julpr833/trapyador.git
cd trapyador
```

Instala las dependencias:

```bash
pip install questionary
```


---

## Uso

Ejecuta el script:

```bash
python main.py
```

### Controles

| Tecla | Acción |
|------|--------|
| ARRIBA / ABAJO | Navegar por la lista |
| ESPACIO | Seleccionar programa |
| ENTER | Confirmar selección |


