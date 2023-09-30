var ctx = document.getElementById("line").getContext("2d");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May"],
    datasets: [
      {
        label: "Monthly Sales",
        data: [10, 15, 7, 12, 8],
        borderColor: "rgba(75, 192, 192, 1)",
        fill: true,
      },
    ],
  },
  options: {
    layout: {
      padding: 150,
    },
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
