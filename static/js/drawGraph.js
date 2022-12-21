// import { Chart } from "chart.js/auto";
// const data = [{ standard: "신체발달", count: 70 }]; // 데이터

var myOptions = {
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
      ticks: { padding: 10 },
      grid: {
        display: false,
      },
    },
  },
  responsive: true,
  maintainAspectRatio: false,
  animation: {
    duration: 2000,
  },
};

// 자폐경향성 차트
var autismBar = document.getElementById("autism-chart").getContext("2d");
var autismBarChart = new Chart(autismBar, {
  type: "bar",
  data: {
    labels: [""],
    datasets: [
      {
        label: "T점수",
        data: [Number($("#developValue").val())], // 데이터
        barThickness: 25,
      },
    ],
  },
  options: myOptions,
});

// ADHD경향성 차트
var adhdBar = document.getElementById("adhd-chart").getContext("2d");
var adhdBarChart = new Chart(adhdBar, {
  type: "bar",
  data: {
    labels: [""],
    datasets: [
      {
        label: "T점수",
        data: [Number($("#developValue").val())], // 데이터
        barThickness: 25,
      },
    ],
  },
  options: myOptions,
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
