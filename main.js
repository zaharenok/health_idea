// Автоматическая загрузка метрик с backend и обновление DOM
async function loadMetrics() {
    try {
        const response = await fetch('/api/metrics');
        if (!response.ok) throw new Error('Ошибка загрузки метрик');
        const data = await response.json();
        // Обновляем значения на странице
        document.getElementById('weight-value').innerHTML = `${data.weight}<span class="metric-unit">kg</span>`;
        document.getElementById('sleep-value').innerHTML = `${data.sleep}<span class="metric-unit">h</span>`;
        document.getElementById('steps-value').textContent = data.steps.toLocaleString('ru-RU');
        if (data.recommendation) {
            document.getElementById('recommendation-text').textContent = data.recommendation;
        }
    } catch (error) {
        console.error('Ошибка загрузки метрик:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadMetrics();
    setInterval(loadMetrics, 300000); // 5 минут = 300 000 мс
});
