const ctx = document.getElementById("maingraph");

let chartLabels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
let chartExpenses = [0, 0, 0, 0, 0, 0];
let chartIncome = [0, 0, 0, 0, 0, 0];

try {
    const labelsEl = document.getElementById("chart-labels-data");
    const expenseEl = document.getElementById("chart-expense-data");
    const incomeEl = document.getElementById("chart-income-data");
    if (labelsEl && labelsEl.textContent.trim()) chartLabels = JSON.parse(labelsEl.textContent);
    if (expenseEl && expenseEl.textContent.trim()) chartExpenses = JSON.parse(expenseEl.textContent);
    if (incomeEl && incomeEl.textContent.trim()) chartIncome = JSON.parse(incomeEl.textContent);
} catch (e) {
    console.warn("Could not parse dynamic chart data, using defaults.", e);
}

if (ctx) {
    const chartCtx = ctx.getContext("2d");

    const incomeGradient = chartCtx.createLinearGradient(0, 0, 0, 300);
    incomeGradient.addColorStop(0, "rgba(76, 175, 80, 0.95)");
    incomeGradient.addColorStop(1, "rgba(76, 175, 80, 0.3)");

    const expenseGradient = chartCtx.createLinearGradient(0, 0, 0, 300);
    expenseGradient.addColorStop(0, "rgba(120, 90, 255, 0.95)");
    expenseGradient.addColorStop(1, "rgba(120, 90, 255, 0.3)");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: chartLabels,
            datasets: [
                {
                    label: "Income (₹)",
                    data: chartIncome,
                    backgroundColor: incomeGradient,
                    borderColor: "#4CAF50",
                    borderWidth: 1.5,
                    borderRadius: 6,
                    borderSkipped: false,
                },
                {
                    label: "Expense (₹)",
                    data: chartExpenses,
                    backgroundColor: expenseGradient,
                    borderColor: "#785AFF",
                    borderWidth: 1.5,
                    borderRadius: 6,
                    borderSkipped: false,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: "index",
                intersect: false,
            },
            plugins: {
                legend: {
                    position: "top",
                    labels: {
                        color: "#e0e0e0",
                        font: {
                            family: "'Segoe UI', sans-serif",
                            size: 13,
                            weight: "600",
                        },
                        usePointStyle: true,
                        pointStyle: "rectRounded",
                        padding: 16,
                    },
                },
                tooltip: {
                    backgroundColor: "rgba(20, 15, 35, 0.9)",
                    titleColor: "#ffffff",
                    bodyColor: "#e0e0e0",
                    borderColor: "rgba(255, 255, 255, 0.1)",
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function (context) {
                            let label = context.dataset.label || "";
                            if (label) {
                                label += ": ";
                            }
                            if (context.parsed.y !== null) {
                                label += "₹" + context.parsed.y.toLocaleString("en-IN", { minimumFractionDigits: 2 });
                            }
                            return label;
                        },
                    },
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: "rgba(255, 255, 255, 0.07)",
                    },
                    ticks: {
                        color: "#b0b0b0",
                        font: { size: 11 },
                        callback: function (value) {
                            return "₹" + value.toLocaleString("en-IN");
                        },
                    },
                },
                x: {
                    grid: {
                        display: false,
                    },
                    ticks: {
                        color: "#b0b0b0",
                        font: { size: 12, weight: "500" },
                    },
                },
            },
        },
    });
}

function togglepopup(n, labelTxt) {
    const element = document.getElementsByClassName("popup")[0];
    const popup_label = document.getElementById("popuplabel");
    const savebtn = document.getElementsByClassName("savebtn")[0];
    if (popup_label) popup_label.textContent = "Add " + labelTxt;
    if (savebtn) savebtn.name = labelTxt;
    if (element) {
        if (n == 1) {
            element.style.display = "flex";
            const dateInput = document.querySelector('input[name="date"]');
            if (dateInput && !dateInput.value) {
                dateInput.value = new Date().toISOString().split('T')[0];
            }
        } else {
            element.style.display = "none";
        }
    }
}

