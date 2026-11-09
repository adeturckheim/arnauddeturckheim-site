// Visionneuse : une photo en grand, pellicule de miniatures. Clavier, clic sur les côtés, swipe, ancre #slug.
document.querySelectorAll('[data-viewer]').forEach((v, vi) => {
  const slides = [...v.querySelectorAll('.slide')];
  const caps = [...v.querySelectorAll('.vcap')];
  const ths = [...v.querySelectorAll('.th')];
  const count = v.querySelector('.count b');
  const strip = v.querySelector('.strip');
  const n = slides.length;
  let i = -1;

  const load = k => {
    const img = slides[(k + n) % n].querySelector('img');
    if (img.dataset.src) {
      img.srcset = img.dataset.srcset; img.src = img.dataset.src;
      delete img.dataset.src; delete img.dataset.srcset;
    }
  };

  const show = (k, push = true) => {
    k = (k + n) % n;
    if (k === i) return;
    load(k); load(k + 1); load(k - 1);
    slides.forEach((s, j) => s.classList.toggle('on', j === k));
    caps.forEach((c, j) => c.classList.toggle('on', j === k));
    ths.forEach((t, j) => { t.classList.toggle('on', j === k); t.setAttribute('aria-current', j === k); });
    count.textContent = String(k + 1).padStart(2, '0');
    const th = ths[k];
    strip.scrollTo({ left: th.offsetLeft - strip.clientWidth / 2 + th.clientWidth / 2, behavior: i < 0 ? 'auto' : 'smooth' });
    i = k;
    if (push && vi === 0) history.replaceState(null, '', '#' + slides[k].dataset.slug);
  };

  v.querySelector('.nav.prev').onclick = v.querySelector('.a-prev').onclick = () => show(i - 1);
  v.querySelector('.nav.next').onclick = v.querySelector('.a-next').onclick = () => show(i + 1);
  ths.forEach((t, j) => t.onclick = () => show(j));

  // Clavier : actif pour la première visionneuse de la page, ou celle qui a le focus
  document.addEventListener('keydown', e => {
    if (e.target.closest && e.target.closest('input, textarea')) return;
    const mine = v.contains(document.activeElement) || (vi === 0 && !document.activeElement.closest?.('[data-viewer]'));
    if (!mine) return;
    if (e.key === 'ArrowLeft') { show(i - 1); e.preventDefault(); }
    if (e.key === 'ArrowRight') { show(i + 1); e.preventDefault(); }
  });

  // Swipe
  let x0 = null;
  const stage = v.querySelector('.stage');
  stage.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', e => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1));
    x0 = null;
  });

  const fromHash = () => {
    const k = slides.findIndex(s => '#' + s.dataset.slug === location.hash);
    return k < 0 ? 0 : k;
  };
  show(vi === 0 ? fromHash() : 0, false);
  if (vi === 0) addEventListener('hashchange', () => show(fromHash(), false));
});
