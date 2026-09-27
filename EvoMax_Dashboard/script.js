document.addEventListener('DOMContentLoaded', () => {
    // Calculator Logic
    const modelSelect = document.getElementById('model-select');
    const tokenVolumeSlider = document.getElementById('token-volume');
    const volumeDisplay = document.getElementById('volume-display');
    const rawCostDisplay = document.getElementById('raw-cost');
    const evomaxCostDisplay = document.getElementById('evomax-cost');
    const annualSavingsDisplay = document.getElementById('annual-savings');

    const COMPRESSION_RATE = 0.40; // 40% savings

    function updateCalculator() {
        const ratePerMillion = parseFloat(modelSelect.value);
        const volumeMillions = parseInt(tokenVolumeSlider.value);
        
        volumeDisplay.textContent = volumeMillions;

        const rawMonthlyCost = ratePerMillion * volumeMillions;
        const evomaxMonthlyCost = rawMonthlyCost * (1 - COMPRESSION_RATE);
        const annualSavings = (rawMonthlyCost - evomaxMonthlyCost) * 12;

        rawCostDisplay.textContent = formatCurrency(rawMonthlyCost);
        evomaxCostDisplay.textContent = formatCurrency(evomaxMonthlyCost);
        annualSavingsDisplay.textContent = formatCurrency(annualSavings);
    }

    function formatCurrency(value) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0
        }).format(value);
    }

    modelSelect.addEventListener('change', updateCalculator);
    tokenVolumeSlider.addEventListener('input', updateCalculator);
    
    // Initialize calculator
    updateCalculator();

    // Counter Animation
    const counters = document.querySelectorAll('.counter');
    
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const increment = target / 200;
        
        const updateCount = () => {
            const current = +counter.innerText.replace(/,/g, '');
            if (current < target) {
                counter.innerText = Math.ceil(current + increment).toLocaleString();
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target.toLocaleString();
            }
        };
        updateCount();
    });

    // Simulated Telemetry Stream
    const terminalOutput = document.getElementById('terminal-output');
    const actions = ['ROUTING', 'COMPRESSING', 'SCRUBBING', 'CACHING'];
    const statuses = ['[OK]', '[SUCCESS]', '[SECURE]', '[HIT]'];
    const piiTypes = ['EMAIL', 'SSN', 'NRIC', 'CREDIT_CARD', 'PHONE'];
    
    let lineCount = 0;
    const maxLines = 8;

    function addTerminalLine() {
        const now = new Date();
        const timeStr = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}.${now.getMilliseconds().toString().padStart(3, '0')}`;
        
        const actionType = Math.random();
        let message = '';
        
        if (actionType > 0.8) {
            const pii = piiTypes[Math.floor(Math.random() * piiTypes.length)];
            message = `<span class="timestamp">[${timeStr}]</span> <span class="warning">ALERT: PII DETECTED</span> -> Scrubbing ${pii} entity... <span class="status">[SECURE]</span>`;
        } else if (actionType > 0.5) {
            message = `<span class="timestamp">[${timeStr}]</span> <span class="action">COMPRESSING</span> Payload_ID_${Math.floor(Math.random() * 10000)} -> Removed ${Math.floor(Math.random() * 200 + 50)} tokens <span class="status">[SUCCESS]</span>`;
        } else if (actionType > 0.2) {
            message = `<span class="timestamp">[${timeStr}]</span> <span class="action">CACHING</span> Semantic match found -> Latency -150ms <span class="status">[HIT]</span>`;
        } else {
            message = `<span class="timestamp">[${timeStr}]</span> <span class="action">ROUTING</span> Request to external API (Sovereign Node #04) <span class="status">[OK]</span>`;
        }

        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.innerHTML = message;

        terminalOutput.appendChild(line);
        lineCount++;

        if (lineCount > maxLines) {
            terminalOutput.removeChild(terminalOutput.firstChild);
        }
    }

    // Add a new line every 600-1500ms
    function loopTelemetry() {
        addTerminalLine();
        setTimeout(loopTelemetry, Math.random() * 900 + 600);
    }

    loopTelemetry();
});
