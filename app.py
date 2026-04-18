"""
=============================================================================
SOURCE   : Algo_Visual_Web_v6.py
VERSION  : 6.6.6 [Stable Build]
DEV      : Nosrat Jahan
ACADEMIC : BSc in CSE
-----------------------------------------------------------------------------
CORE     : Web-based Sorting Engine with Dynamic Mode Switching.
LOGIC    : Async-driven visualization for real-time complexity analysis.
=============================================================================
"""

from flask import Flask, render_template_string
import webbrowser

app = Flask(__name__)

# Single-file Web Architecture (HTML/CSS/JS)
UI_INTEGRATION = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Algo-Visualizer Engine v6.6.6</title>
    <style>
        :root {
            --bg: #1e272e;
            --panel: #2f3640;
            --text: #d2dae2;
            --accent: #05c46b;
            --bar: #485460;
            --footer-text: #ffffff;
        }

        .gray-mode {
            --bg: #dfe4ea;
            --panel: #ced6e0;
            --text: #2f3542;
            --accent: #27ae60;
            --bar: #747d8c;
            --footer-text: #2f3542;
        }

        body { 
            background-color: var(--bg); 
            color: var(--text); 
            font-family: 'Consolas', 'Segoe UI', sans-serif; 
            margin: 0; 
            transition: background-color 0.4s, color 0.4s;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        header {
            width: 100%;
            background: var(--panel);
            padding: 25px 0;
            text-align: center;
            border-bottom: 3px solid var(--accent);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .nav-controls {
            margin-top: 15px;
            display: flex;
            justify-content: center;
            gap: 12px;
        }

        button {
            padding: 10px 18px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            font-size: 13px;
            transition: 0.2s ease;
            text-transform: uppercase;
        }

        .btn-gen { background: var(--accent); color: white; }
        .btn-sort { background: #3498db; color: white; }
        .btn-mode { background: #57606f; color: white; }
        
        button:hover { filter: brightness(1.2); transform: translateY(-1px); }

        #visual-portal {
            display: flex;
            align-items: flex-end;
            justify-content: center;
            height: 400px;
            width: 90%;
            max-width: 1000px;
            margin: 40px 0;
            padding: 20px;
            background: rgba(0,0,0,0.2);
            border-radius: 8px;
            gap: 2px;
            border: 1px solid var(--bar);
        }

        .node {
            flex: 1;
            background: var(--bar);
            transition: height 0.1s ease-in-out;
        }

        footer {
            margin-top: auto;
            width: 100%;
            background: var(--panel);
            padding: 15px 0;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            color: var(--footer-text);
            border-top: 2px solid var(--accent);
            letter-spacing: 1px;
        }
    </style>
</head>
<body>

    <header>
        <span style="font-size: 1.8rem; font-weight: bold; color: var(--accent);">ALGO-VISUALIZER CORE v6.6.6</span>
        <div class="nav-controls">
            <button class="btn-gen" onclick="refreshNodes()">Refresh Array</button>
            <button class="btn-sort" onclick="executeBubbleSort()">Execute Bubble Sort</button>
            <button class="btn-mode" onclick="toggleTheme()">Switch Dark / Gray Mode</button>
        </div>
    </header>

    <div id="visual-portal"></div>

    <footer>
        v6.6.6 | Engineered by Nosrat Jahan | BSc in CSE | 2026
    </footer>

    <script>
        let nodes = [];
        const portal = document.getElementById('visual-portal');

        function refreshNodes(size = 50) {
            portal.innerHTML = '';
            nodes = [];
            for (let i = 0; i < size; i++) {
                let val = Math.floor(Math.random() * 350) + 20;
                nodes.push(val);
                const bar = document.createElement('div');
                bar.classList.add('node');
                bar.style.height = `${val}px`;
                bar.setAttribute('id', `node-${i}`);
                portal.appendChild(bar);
            }
        }

        async function executeBubbleSort() {
            const domNodes = document.getElementsByClassName('node');
            const n = nodes.length;
            
            for (let i = 0; i < n; i++) {
                for (let j = 0; j < n - i - 1; j++) {
                    domNodes[j].style.background = "#f1c40f"; // Yellow for comparison
                    domNodes[j+1].style.background = "#f1c40f";

                    if (nodes[j] > nodes[j+1]) {
                        await performSwap(j, j + 1);
                    }

                    domNodes[j].style.background = ""; 
                    domNodes[j+1].style.background = "";
                }
                domNodes[n - i - 1].style.background = "#05c46b"; // Green for sorted
            }
        }

        function performSwap(a, b) {
            return new Promise(resolve => {
                setTimeout(() => {
                    let temp = nodes[a];
                    nodes[a] = nodes[b];
                    nodes[b] = temp;

                    const barA = document.getElementById(`node-${a}`);
                    const barB = document.getElementById(`node-${b}`);
                    
                    barA.style.height = `${nodes[a]}px`;
                    barB.style.height = `${nodes[b]}px`;
                    
                    resolve();
                }, 20); 
            });
        }

        function toggleTheme() {
            document.body.classList.toggle('gray-mode');
        }

        refreshNodes();
    </script>
</body>
</html>
"""

@app.route("/")
def entry_point():
    return render_template_string(UI_INTEGRATION)

if __name__ == "__main__":
    local_host = "127.0.0.1"
    port = 5050
    session_id = "Nosrat_Jahan_Algo_9.9.9"
    
    print("\\n" + "="*60)
    print("  ENGINE: ALGO-VISUALIZER CORE [v6.6.6]")
    print(f"  LINK  : {session_id} (http://{local_host}:{port})")
    print("  STATUS: ACTIVE - SERVER RUNNING")
    print("="*60 + "\\n")
    
    webbrowser.open(f"http://{local_host}:{port}")
    app.run(host=local_host, port=port, debug=False)
