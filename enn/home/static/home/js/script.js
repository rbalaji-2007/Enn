function changeSelected(n) {
  var element = document.getElementsByClassName("sideelements")[n];
  var oldElement = document.getElementById("sideselected");
  oldElement.id = "";
  element.id = "sideselected";
}

const ctx = document.getElementById("maingraph");

new Chart(ctx, {
  type: "bar", // 📊 Bar chart type

  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],

    datasets: [
      {
        label: "Expense",
        data: [2356, 3847, 1294, 2847, 1987, 1298],

        /* 🚀 FIXED: Use backgroundColor instead of borderColor to fill the bars! */
        backgroundColor: "#4A39FF",

        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          color: "#ffffff",
        },
      },
    },
    scales: {
      y: {
        ticks: { color: "#ffffff" },
      },
      x: {
        ticks: { color: "#ffffff" },
      },
    },
  },
});
function togglepopup(n, labelTxt){
    const element = document.getElementsByClassName("popup")[0];
    const popup_label = document.getElementById("popuplabel");
    popup_label.textContent = "Add "+labelTxt;
    if (n == 1){
        element.style.display = "flex";
    }
    else{
        element.style.display = "none";
    }
}
