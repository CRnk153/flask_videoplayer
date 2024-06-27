document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById('menu-button');
    const menu = document.getElementById('menu');

    menuButton.addEventListener('click', function() {
      rect = menuButton.getBoundingClientRect();
      menu.style.top = `${rect.bottom + window.scrollY - 1}px`;
      menu.style.left = `${rect.right + window.scrollX - 96}px`;
      if (menu.style.display === 'none' || menu.style.display === '') {
        menu.style.display = 'block';
      } else {
        menu.style.display = 'none';
      }
    });

    const closeButtons = document.getElementsByClassName('close-button');

    if (closeButtons.length != 0) {
    for (let i = 0; i < closeButtons.length; i++) {
      closeButtons[i].addEventListener('click', function() {
        this.parentElement.remove();
      });
    }
    }

  });
