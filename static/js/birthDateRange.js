$(document).ready(function () {
  // 만 나이 계산, input date 제한
  const today = new Date(); // 오늘 날짜

  const ty = today.getFullYear();
  const tm = today.getMonth();
  const td = today.getDate();

  let minDate = new Date(ty - 7, tm, td); // 만 1세 기준 날짜 계산
  minDate.setDate(minDate.getDate() + 1); // 만 6세 기준 날짜 계산
  // alert(minDate);

  const miny = minDate.getFullYear();
  const minm = minDate.getMonth();
  const mind = minDate.getDate();

  let childBirth = document.getElementById("childBirthDate");
  childBirth.setAttribute("max", `${ty - 1}-${tm + 1}-${td}`);
  childBirth.setAttribute("min", `${miny}-${minm + 1}-${mind}`);
});
