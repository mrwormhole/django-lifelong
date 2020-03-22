(function ($) {
  $.fn.counter = function() {
    const $this = $(this),
    numberFrom = parseInt($this.attr('data-from')),
    numberTo = parseInt($this.attr('data-to')),
    delta = numberTo - numberFrom,
    deltaPositive = delta > 0 ? 1 : 0,
    time = parseInt($this.attr('data-time')),
    changeTime = 10;
  
    let currentNumber = numberFrom,
    value = delta*changeTime/time;
    var interval1;
    const changeNumber = () => {
      currentNumber += value;
      //checks if currentNumber reached numberTo
      (deltaPositive && currentNumber >= numberTo) || (!deltaPositive &&currentNumber<= numberTo) ? currentNumber=numberTo : currentNumber;
      this.text(parseInt(currentNumber));
      currentNumber == numberTo ? clearInterval(interval1) : currentNumber;  
    }

    interval1 = setInterval(changeNumber,changeTime);
  }
}(jQuery));

$(document).ready(function() {

  // Home page counter
  $('.counter-location').counter();
  $('.counter-patient').counter();
  $('.counter-satisfaction').counter();
  
  new WOW().init();
  // Home page counter

  // Home page testimonial
  $('.testimonial').carousel({
    interval: 3000
  });
  // Home page testimonial

  var pattern = GeoPattern.generate('LIFELONG COUNSELLING');
  $('#geopattern').css('background-image', pattern.toDataUrl());

});