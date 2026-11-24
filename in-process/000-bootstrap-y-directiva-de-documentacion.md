# 000 — Bootstrap del proyecto y directiva de documentación y flujo de tareas

## Objetivo
Dejar el proyecto listo para trabajar con la convención del equipo: repo, carpetas de tickets, docs vivos y CI. Sale del punto 0 de "Impacto estimado" en `docs/definiciones/canal-idiomas-es-en.md` (VoBo del PO del 2026-11-23). Cada ticket nace en `pending/`, pasa a `in-process/` al empezar y a `done/` al cerrarse con su sección "Hecho".

## Criterios de aceptación (TDD)
- El repo `64bitstudio/canal-idiomas` (público, por decisión del PO) tiene las ramas `dev`, `qa` y `prod`, con `dev` como rama por defecto, protección de ramas y webhook a Jenkins.
- Existen `pending/`, `in-process/`, `done/`, `docs/definiciones/` y los 5 docs vivos (`README`, `ARQUITECTURA`, `BASE_DE_DATOS`, `API`, `COMPONENTES`). Los que no aplican lo dicen explícitamente.
- `.gitignore` excluye secretos (`.env`, tokens OAuth), entornos, `MoneyPrinterTurbo/`, `pruebas/` y artefactos de audio y video. Se verifica con `git status`: ninguno de esos archivos aparece.
- Hay un `Jenkinsfile` placeholder (`deploy: false`) y el **pipeline de Jenkins pasa en verde** en el PR a `dev`.
- Están creados los tickets 001–010, cada uno referenciando la definición.
- SonarQube: se registra el proyecto cuando exista `SONARQUBE_CLI_TOKEN_VM`, que genera el PO.
