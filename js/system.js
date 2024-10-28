// Pyodideの初期化
async function initPyodide() {
    return await loadPyodide();
}
let pyodideInstance;

// ページ読み込み時にPyodideを初期化
window.addEventListener('load', async () => {
    console.log("Loading Pyodide...");
    pyodideInstance = await initPyodide();
    console.log("Pyodide loaded!");
});

// Pythonコードを実行する関数
async function runPython() {
    try {
        const code = document.getElementById('inputBox').value;
        const result = await pyodideInstance.runPython(code);
        document.getElementById('result').innerText = "実行結果: " + result;
    } catch (error) {
        document.getElementById('result').innerText = "エラー: " + error.message;
    }
}