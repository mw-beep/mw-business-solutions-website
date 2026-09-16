// Screenshot links still open the original image when JavaScript is unavailable.
(() => {
    const links = document.querySelectorAll('.screenshot-link');
    if (!links.length || typeof HTMLDialogElement === 'undefined') return;

    const dialog = document.createElement('dialog');
    dialog.className = 'image-dialog';
    dialog.setAttribute('aria-labelledby', 'preview-title');
    dialog.innerHTML = `
        <div class="preview-toolbar">
            <h2 id="preview-title">Screenshot preview</h2>
            <button type="button" class="preview-zoom" aria-pressed="false">Zoom to full size</button>
            <button type="button" class="preview-close" autofocus>Close <span aria-hidden="true">×</span></button>
        </div>
        <div class="preview-scroll" tabindex="0" role="region" aria-label="Screenshot; scroll to explore when zoomed">
            <img class="preview-image" alt="">
        </div>
        <p class="preview-caption"></p>
        <a class="preview-original" target="_blank" rel="noopener">Open original image in a new tab ↗</a>`;
    document.body.append(dialog);
    const image = dialog.querySelector('.preview-image');
    const scroller = dialog.querySelector('.preview-scroll');
    const zoom = dialog.querySelector('.preview-zoom');
    let opener;
    let previousOverflow;

    for (const link of links) {
        link.addEventListener('click', (event) => {
            if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
            event.preventDefault();
            opener = link;
            image.src = link.href;
            image.alt = link.querySelector('img').alt;
            dialog.querySelector('.preview-caption').textContent = image.alt;
            dialog.querySelector('.preview-original').href = link.href;
            scroller.classList.remove('is-zoomed');
            zoom.setAttribute('aria-pressed', 'false');
            zoom.textContent = 'Zoom to full size';
            previousOverflow = document.body.style.overflow;
            document.body.style.overflow = 'hidden';
            dialog.showModal();
            scroller.scrollTo(0, 0);
        });
    }
    zoom.addEventListener('click', () => {
        const enlarged = scroller.classList.toggle('is-zoomed');
        zoom.setAttribute('aria-pressed', String(enlarged));
        zoom.textContent = enlarged ? 'Fit to screen' : 'Zoom to full size';
        scroller.scrollTo(0, 0);
    });
    dialog.querySelector('.preview-close').addEventListener('click', () => dialog.close());
    // Keep keyboard navigation within the preview, including at the tab-order edges.
    dialog.addEventListener('keydown', (event) => {
        if (event.key !== 'Tab') return;
        const controls = dialog.querySelectorAll('button, [tabindex="0"], a[href]');
        const first = controls[0];
        const last = controls[controls.length - 1];
        if (event.shiftKey && document.activeElement === first) {
            event.preventDefault();
            last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
            event.preventDefault();
            first.focus();
        }
    });
    dialog.addEventListener('click', (event) => {
        const bounds = dialog.getBoundingClientRect();
        if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right ||
            event.clientY < bounds.top || event.clientY > bounds.bottom)) dialog.close();
    });
    dialog.addEventListener('close', () => {
        document.body.style.overflow = previousOverflow;
        opener?.focus({ preventScroll: true });
    });
})();
