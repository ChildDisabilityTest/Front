// draw T score bar chart(발달지수, 자폐경향성, adhd경향성)

$(document).ready(function () {
  const myOptions = {
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

  // 발달지수 차트
  const developBar = document.getElementById("develop-chart").getContext("2d");
  const developValue = [Number($("#developValue").val())];

  let color1;
  if (developValue < 41) {
    color1 = "rgba(227, 112, 112, 1.0)"; // 빨
  } else if (developValue < 60) {
    color1 = "rgba(98, 96, 198, 1.0)"; // 파
  } else {
    color1 = "rgba(110, 167, 108, 1.0)"; // 초
  }

  const developBarChart = new Chart(developBar, {
    type: "bar",
    data: {
      labels: [""],
      datasets: [
        {
          label: "T점수",
          data: developValue,
          barThickness: 25,
          backgroundColor: color1,
        },
      ],
    },
    options: myOptions,
  });

  // 자폐경향성 차트
  const autismBar = document.getElementById("autism-chart").getContext("2d");
  const autismValue = [Number($("#autismValue").val())];

  let color2;
  if (autismValue < 41) {
    color2 = "rgba(110, 167, 108, 1.0)"; // 초
  } else if (autismValue < 60) {
    color2 = "rgba(98, 96, 198, 1.0)"; // 파
  } else {
    color2 = "rgba(227, 112, 112, 1.0)"; // 빨
  }

  const autismBarChart = new Chart(autismBar, {
    type: "bar",
    data: {
      labels: [""],
      datasets: [
        {
          label: "T점수",
          data: autismValue,
          barThickness: 25,
          backgroundColor: color2,
        },
      ],
    },
    options: myOptions,
  });

  // ADHD경향성 차트
  const adhdBar = document.getElementById("adhd-chart").getContext("2d");
  const adhdValue = [Number($("#adhdValue").val())];

  let color3;
  if (adhdValue < 41) {
    color3 = "rgba(110, 167, 108, 1.0)"; // 초
  } else if (adhdValue < 60) {
    color3 = "rgba(98, 96, 198, 1.0)"; // 파
  } else {
    color3 = "rgba(227, 112, 112, 1.0)"; // 빨
  }

  const adhdBarChart = new Chart(adhdBar, {
    type: "bar",
    data: {
      labels: [""],
      datasets: [
        {
          label: "T점수",
          data: adhdValue,
          barThickness: 25,
          backgroundColor: color3,
        },
      ],
    },
    options: myOptions,
  });
});
