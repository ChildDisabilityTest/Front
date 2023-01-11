$(document).ready(function () {
  // 만 나이 계산, input date 제한
  const today = new Date(); // 오늘 날짜

  const ty = today.getFullYear();
  const tm = today.getMonth();
  const td = today.getDate();

  // 만 1세 기준 날짜 계산
  let minDate = new Date(ty - 7, tm, td);
  minDate.setDate(minDate.getDate() + 1);
  // alert(minDate);

  // max, min 날짜 구하기
  const maxy = ty - 1;
  let maxm = tm + 1;
  const maxd = td;
  const miny = minDate.getFullYear();
  let minm = minDate.getMonth() + 1;
  const mind = minDate.getDate();

  // yyyy-mm-dd 포맷에 맞추기 위해서 한 자릿수의 경우 0 붙이기
  if (maxm <= 9) {
    maxm = "0" + maxm.toString();
    // alert(maxm);
  }
  if (minm <= 9) {
    minm = "0" + minm.toString();
    // alert(minm);
  }

  let childBirth = document.getElementById("childBirthDate");
  childBirth.setAttribute("max", `${maxy}-${maxm}-${maxd}`);
  childBirth.setAttribute("min", `${miny}-${minm}-${mind}`);
});
