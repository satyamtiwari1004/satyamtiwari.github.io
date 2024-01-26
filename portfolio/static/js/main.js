  const d = new Date();
  const hours = d.getHours();
  const night = hours >= 18 || hours <= 7; // between 7pm and 7am
  const body = document.querySelector('body');
  const toggle = document.getElementById('toggle');
  const input = document.getElementById('switch');
  const mediaQueryObj = window.matchMedia('(prefers-color-scheme: dark)');
  const isDarkMode = mediaQueryObj.matches; //to check if browser is in darkmode or not

  if (night || isDarkMode) {
    input.checked = true;
    body.classList.add('night');
  }

  toggle.addEventListener('click', function() {
    const isChecked = input.checked;
    if (isChecked) {
      body.classList.remove('night');
    } else {
      body.classList.add('night');
    }
  });

  const introHeight = document.querySelector('.intro').offsetHeight;
  const topButton = document.getElementById('top-button');

  // window.addEventListener(
  //   'scroll',
  //   function() {
  //     if (window.scrollY > introHeight) {
  //       topButton.fadeIn();
  //     } else {
  //       topButton.fadeOut();
  //     }
  //   },
  //   false
  // );

  topButton.addEventListener('click', function() {
    body.animate({ scrollTop: 0 }, 500);
  });

  const hand = document.querySelector('.emoji.wave-hand');

  function waveOnLoad() {
    hand.classList.add('wave');
    setTimeout(function() {
      hand.classList.remove('wave');
    }, 2000);
  }

  setTimeout(function() {
    waveOnLoad();
  }, 1000);

  hand.addEventListener('mouseover', function() {
    hand.classList.add('wave');
  });

  hand.addEventListener('mouseout', function() {
    hand.classList.remove('wave');
  });

//  var sr = {
//     reset: false,
//     duration: 600,
//     easing: 'cubic-bezier(.694,0,.335,1)',
//     scale: 1,
//     viewFactor: 0.3
//   };

//   ScrollReveal().reveal('.background',sr);
//   ScrollReveal().reveal('.skills',sr);
//   ScrollReveal().reveal('.experience',sr, { viewFactor: 0.2 });
//   ScrollReveal().reveal('.featured-projects',sr, { viewFactor: 0.1 });
//   ScrollReveal().reveal('.other-projects',sr, { viewFactor: 0.05 });

