jQuery(document).ready(function ($) {
  $('input').on('click', function () {
    $('.has-error').hide();
  });

  $('input').on('keypress', function () {
    $('.has-error').hide();
  });
});
