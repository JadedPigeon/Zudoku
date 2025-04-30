document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell:not(.fixed)');

    cells.forEach(cell => {
        cell.addEventListener('keydown', (e) => {
            if (e.key >= '1' && e.key <= '9') {
                cell.innerText = e.key;
            } else if (e.key === 'Backspace' || e.key === 'Delete') {
                cell.innerText = '';
            }
            e.preventDefault(); // prevent newlines
        });
    });
});
