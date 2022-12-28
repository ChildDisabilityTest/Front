// SCROLL TO TOP ===============================================================================
$(function () {
  $(window).scroll(function () {
    if ($(this).scrollTop() != 0) {
      $("#toTop").fadeIn();
    } else {
      $("#toTop").fadeOut();
    }
  });

  $("#toTop").click(function () {
    $("body,html").animate({ scrollTop: 0 }, 500);
  });
});

if (window.innerWidth < 770) {
  $("button.forward, button.backward").click(function () {
    $("html, body").animate({ scrollTop: 115 }, "slow");
    return false;
  });
}

if (window.innerWidth < 500) {
  $("button.forward, button.backward").click(function () {
    $("html, body").animate({ scrollTop: 245 }, "slow");
    return false;
  });
}
if (window.innerWidth < 340) {
  $("button.forward, button.backward").click(function () {
    $("html, body").animate({ scrollTop: 280 }, "slow");
    return false;
  });
}
// WIZARD  ===============================================================================
jQuery(function ($) {
  //  Basic wizard with validation
  $("#survey_container")
    .wizard({
      stepsWrapper: "#wrapped",
      submit: ".submit",
      beforeSelect: function (event, state) {
        if (!state.isMovingForward) return true;
        var inputs = $(this).wizard("state").step.find(":input");
        return !inputs.length || !!inputs.valid();
      },
    })
    .validate({
      errorPlacement: function (error, element) {
        if (element.is(":radio") || element.is(":checkbox")) {
          error.insertBefore(element.next());
        } else {
          error.insertAfter(element);
        }
      },
    });

  //  progress bar
  $("#progressbar").progressbar();

  $("#survey_container").wizard({
    afterSelect: function (event, state) {
      $("#progressbar").progressbar("value", state.percentComplete);
      $("#location").text("(" + state.stepsComplete + "/" + state.stepsPossible + ")");
    },
  });
});

// OHTER ===============================================================================
$(document).ready(function () {
  //Menu mobile
  $(".btn-responsive-menu").click(function () {
    $("#top-nav").slideToggle(400);
  });

  //Check and radio input styles
  $("input.check_radio").iCheck({
    checkboxClass: "icheckbox_square-aero",
    radioClass: "iradio_square-aero",
  });

  //Pace holder
  $("input, textarea").placeholder();
});

// owl ===============================================================================
$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
    loop: false,
    nav: false,
    // margin: 10,
    items: 1,
    // autoplay: true,
    autoplayTimeout: 2000,
    autoplayHoverPause: false,
    autoWidth: false,
    autoHeight: false,
    // itemsDesktop: [1199, 3],
    // itemsDesktopSmall: [979, 3],
  });
});

// custom ===============================================================================
$(document).ready(function () {
  // 숫자만 받기(전화번호 입력 란)
  $("#testerPhone").keyup(function (event) {
    var inputVal = $(this).val();
    $(this).val(inputVal.replace(/[^0-9]/gi, ""));
  });

  // top area 타이틀 변경
  $("button.forward, button.backward").click(function () {
    var title = document.getElementById("complete");

    if (title.style.display === "block") {
      $("#main-title-text").html("검사 방법 안내");
    } else {
      $("#main-title-text").html("아동/검사자 정보 입력");
    }
  });
});

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
