# This script sets up a local development environment for the browser-use project (PowerShell version)
# Usage:
#   PS> ./bin/setup.ps1

# Enable strict mode
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Get the script directory
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $SCRIPT_DIR

# Check if we're in the right directory
if (Test-Path "$SCRIPT_DIR/lint.sh") {
    Write-Host "[√] already inside a cloned browser-use repo"
} else {
    Write-Host "[+] Cloning browser-use repo into current directory: $SCRIPT_DIR"
    git clone https://github.com/browser-use/browser-use
    Set-Location "$SCRIPT_DIR/browser-use"
}

Write-Host "[+] Installing uv..."
# Install uv (requires curl and sh, or use the Windows installer if available)
# This uses the same method as the bash script, but adapted for PowerShell
Invoke-Expression ([System.Text.Encoding]::UTF8.GetString((Invoke-WebRequest -Uri "https://astral.sh/uv/install.ps1" -UseBasicParsing).Content))

Write-Host ""
Write-Host "[+] Setting up venv"
uv venv
Write-Host ""
Write-Host "[+] Installing packages in venv"
uv sync --dev --all-extras
Write-Host ""
Write-Host "[i] Tip: make sure to set BROWSER_USE_LOGGING_LEVEL=debug and your LLM API keys in your .env file"
Write-Host ""
uv pip show browser-use

Write-Host "Usage:"
Write-Host "  PS> browser-use               # use the CLI"
Write-Host "  or"
Write-Host "  PS> . .venv/Scripts/Activate.ps1"
Write-Host "  PS> ipython                   # use the library"
Write-Host "  >>> from browser_use import BrowserSession, Agent"
Write-Host "  >>> await Agent(task='book me a flight to fiji', browser=BrowserSession(headless=$false)).run()"
Write-Host "" 