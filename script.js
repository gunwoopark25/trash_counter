document.addEventListener('DOMContentLoaded', () => {
    // 캘린더 생성
    const generateCalendar = () => {
        const calendar = document.getElementById('calendar');
        const today = new Date();
        const year = today.getFullYear();
        const month = today.getMonth(); // 0부터 시작 (0 = 1월)

        const daysInMonth = new Date(year, month + 1, 0).getDate();
        const firstDay = new Date(year, month, 1).getDay();

        calendar.innerHTML = '';

        // 빈칸 추가
        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            calendar.appendChild(emptyCell);
        }

        // 날짜 추가
        for (let day = 1; day <= daysInMonth; day++) {
            const dayCell = document.createElement('div');
            dayCell.textContent = day;

            const countSpan = document.createElement('span');
            countSpan.textContent = `(${Math.floor(Math.random() * 5)})`; // 예시 데이터
            dayCell.appendChild(countSpan);

            calendar.appendChild(dayCell);
        }
    };

    // 차트 생성
    const generateChart = () => {
        const ctx = document.getElementById('monthlyChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                datasets: [{
                    label: 'Trash Count',
                    data: Array.from({ length: 12 }, () => Math.floor(Math.random() * 20)),
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    };

    generateCalendar();
    generateChart();
});