const artGallery = {
    'Dog': {
        art: `   //  \\___
  (((  @@@\\___
  //      OO
 //__((__//`,
        color: 'yellow'
    },
    'Cat': {
        art: `   /\\_/\\
  ( o.o )
   > ^ <
  /|   |\\`,
        color: 'white'
    },
    'Bird': {
        art: `    ____
  >(o )__
   (  ._>
    \`--`,
        color: 'blue'
    },
    'Fish': {
        art: `>>><<<(((((((°°°>>>`,
        color: 'cyan'
    },
    'Butterfly': {
        art: `  (\\_/)
 (o.o)
  >*<`,
        color: 'magenta'
    },
    'Rabbit': {
        art: `    ((\\((\\
    ((  -.- ))
    oo__("")("")`,
        color: 'white'
    },
    'Snake': {
        art: `      ,,,---
,,,---'''
\`\`\`===eee`,
        color: 'green'
    },
    'Frog': {
        art: `   @..@
  (----)
 ( >__< )
 ^^  ~~  ^^`,
        color: 'green'
    },
    'Owl': {
        art: `   ,___,
  (O,O)
  (   )
   ---`,
        color: 'yellow'
    }
};

const menuEl = document.getElementById('menu');
const artEl = document.getElementById('ascii-art');

// Populate menu
Object.keys(artGallery).forEach((name, index) => {
    const item = document.createElement('div');
    item.className = 'menu-item' + (index === 0 ? ' active' : '');
    item.textContent = `🎨 ${name}`;
    item.onclick = () => selectArt(name, item);
    menuEl.appendChild(item);
});

function selectArt(name, element) {
    // Remove active class from all items
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('active');
    });

    // Add active class to selected item
    element.classList.add('active');

    // Update art
    const selected = artGallery[name];
    artEl.textContent = selected.art;
    artEl.className = `ascii-art color-${selected.color}`;
}

// Show first item by default
const firstName = Object.keys(artGallery)[0];
artEl.textContent = artGallery[firstName].art;
artEl.className = `ascii-art color-${artGallery[firstName].color}`;
