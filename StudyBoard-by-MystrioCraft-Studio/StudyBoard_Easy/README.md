# StudyBoard Easy — Live Server friendly

## Important: this version fixes the Live Server issue
`index.html`, `style.css`, and `script.js` are in the same root folder. Do not open `templates/index.html`; this version has no templates folder. This is the key difference that lets VS Code Live Server find the CSS and JavaScript files.

## Run in VS Code
1. Extract this ZIP to a normal folder.
2. In VS Code, choose **File → Open Folder** and select `StudyBoard_Easy`.
3. Open the root `index.html` file (the one beside `style.css` and `script.js`).
4. Click **Go Live** in the VS Code status bar.
5. The website should open in your browser with styling and interactive controls.

You do not need to install Python to use Live Server. Python is included as an optional alternative server (`app.py`), because the primary goal is easy, zero-terminal usage.

## For your teacher's PC
- Simplest: share/extract the folder and double-click `index.html` or `Start StudyBoard.bat`.
- No terminal, VS Code, Python, or internet is required for core website functions.
- `Start StudyBoard.bat` opens the page in the default browser. (It does not start a Python server.)
- The Google Fonts import is optional; without internet, system fonts are used.

## Included features
- Class → Subject → Chapter → Pages structure
- Add, rename, edit, delete items from Teacher tools
- Notes editor with heading, bold, bullets, and important-note helpers (HTML content)
- Upload diagrams (images smaller than 1.5 MB)
- Soft color, Light, and Dark themes
- Student feedback comments
- Six-digit editing passcode (demo default `123456`), three wrong attempts → two-minute lock
- Export and import JSON backup to move content between computers
- Content saved in this browser's local storage

## Critical data/security limitations
This is a static offline-friendly demo. Content is stored in the current browser profile on the current computer. To transfer content, use **Teacher tools → Export backup**, then on the other PC use **Teacher tools → Import backup**. Keep backups regularly.
The passcode is a convenience lock, NOT real security: anyone with access to the browser developer tools or the computer's files may bypass it. Comments and content are stored locally, not shared live between different computers. Google login and cloud sync are not included.
For a multi-user hosted website where students' comments and teacher edits sync across devices, a proper backend/database and secure authentication will be required.

## Optional Python
`app.py` is included as requested, but not needed for Live Server. If using it, install Python and Flask first, then run it from a terminal. For your intended workflow, prefer Go Live.
