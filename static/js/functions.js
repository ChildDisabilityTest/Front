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
  // ????????? ??????(???????????? ?????? ???)
  $("#testerPhone").keyup(function (event) {
    var inputVal = $(this).val();
    $(this).val(inputVal.replace(/[^0-9]/gi, ""));
  });

  // top area ????????? ??????
  $("button.forward, button.backward").click(function () {
    var title = document.getElementById("complete");

    if (title.style.display === "block") {
      $("#main-title-text").html("?????? ?????? ??????");
    } else {
      $("#main-title-text").html("??????/????????? ?????? ??????");
    }
  });
});
