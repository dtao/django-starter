import './index.scss';

document.addEventListener('DOMContentLoaded', () => {
  const HEXADECIMAL = '0123456789abcdef';

  function getRandomColor() {
    let value = '#';
    while (value.length < 7) {
      value += HEXADECIMAL[Math.floor(Math.random() * HEXADECIMAL.length)];
    }
    return value;
  }

  function contrastingColor(color) {
    let contrast = '#';
    for (let i = 1; i < color.length; ++i) {
      let colorIndex = HEXADECIMAL.indexOf(color.charAt(i));
      contrast += HEXADECIMAL[(colorIndex + 8) % HEXADECIMAL.length];
    }
    return contrast;
  }

  document.querySelector('h1').addEventListener('click', () => {
    const color = getRandomColor();
    document.body.style.backgroundColor = color;
    document.body.style.color = contrastingColor(color);
  });
});
