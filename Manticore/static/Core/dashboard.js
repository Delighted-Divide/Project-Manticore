console.log("pink");

var ctx = document.getElementById("line-graph").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Monthly Sales",
        data: [12, 19, 3, 5, 2, 3, 10],
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
        fill: false,
        tension: 0.4, // This makes the line curved
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
