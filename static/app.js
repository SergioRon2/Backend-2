const card = document.getElementById('card');
const text = document.querySelectorAll('.text-center');

text.forEach(elem => {
    if (text.textContent.trim() === ''){
        card.style.display = 'none';
    }
})
