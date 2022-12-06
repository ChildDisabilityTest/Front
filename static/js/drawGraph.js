import { Chart } from "chart.js/auto";

const data = [{ standard: "신체발달", count: 70 }]; // 데이터

var myBar = document.getElementById("bar-chart").getContext("2d");
var myBarChart = new Chart(myBar, {
  type: "bar",
  data: {
    labels: ["계산 값"], // 데이터
    datasets: [
      {
        label: "신체발달", // 데이터
        data: [54], // 데이터
        barThickness: 50,
      },
    ],
  },
  options: {
    indexAxis: "y",
    plugins: {
      legend: {
        // 범례(상단)
        display: false,
      },
      datalabels: {
        display: false,
      },
      tooltip: {
        boxWidth: 25,
      },
    },
    scales: {
      x: {
        min: 0,
        max: 100,
      },
      y: {
        ticks: {},
        grid: {
          display: false,
        },
      },
    },
    responsive: true,
    maintainAspectRatio: false,
    animation: {
      duration: 4000,
    },
  },
});

// new Chart(document.getElementById("acquisitions"), {
//   type: "bar",
//   data: {
//     labels: data.map((col) => col.standard), // 데이터
//     datasets: [
//       {
//         label: "신체발달", // 데이터
//         data: data.map((row) => row.count), // 데이터
//         barThickness: 50,
//       },
//     ],
//   },
//   options: {
//     indexAxis: "y",
//     plugins: {
//       legend: {
//         // 범례(상단)
//         display: false,
//       },
//       datalabels: {
//         display: false,
//       },
//       tooltip: {
//         boxWidth: 25,
//       },
//     },
//     scales: {
//       x: {
//         min: 0,
//         max: 100,
//       },
//       y: {
//         ticks: {},
//         grid: {
//           display: false,
//         },
//       },
//     },
//     responsive: true,
//     maintainAspectRatio: false,
//     animation: {
//       duration: 2000,
//     },
//   },
// });
