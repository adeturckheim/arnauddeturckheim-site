// Visionneuse : une photo en grand, pellicule de miniatures dans la barre du bas.
// Clavier (flèches, F pour plein écran), clic sur les moitiés de l'image, swipe, ancre #slug.
document.querySelectorAll('[data-viewer]').forEach((v, vi) => {
  const slides = [...v.querySelectorAll('.slide')];
  const caps = [...v.querySelectorAll('.vcap')];
  const ths = [...v.querySelectorAll('.th')];
  const count = v.querySelector('.count b');
  const strip = v.querySelector('.strip');
  const n = slides.length;
  let i = -1;
  const stageEl = v.querySelector('.stage');
  const mobile = matchMedia('(max-width: 820px)');
  // Sur mobile, la scène prend la hauteur de la photo affichée (sans bandes vides), plafonnée à 78 % de l'écran
  const fit = () => {
    if (!mobile.matches || i < 0) { stageEl.style.height = ''; return; }
    const r = parseFloat(slides[i].dataset.ratio);
    stageEl.style.height = Math.min(innerHeight * 0.78, stageEl.clientWidth / r) + 'px';
  };
  addEventListener('resize', fit);

  const load = k => {
    const img = slides[(k + n) % n].querySelector('img');
    if (img.dataset.src) {
      img.onload = () => img.classList.add('ready');
      img.srcset = img.dataset.srcset; img.src = img.dataset.src;
      delete img.dataset.src; delete img.dataset.srcset;
      if (img.complete) img.classList.add('ready');
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
    strip.scrollTo({ left: th.offsetLeft - strip.offsetLeft - strip.clientWidth / 2 + th.clientWidth / 2,
                     behavior: i < 0 ? 'auto' : 'smooth' });
    i = k;
    fit();
    if (push && vi === 0) history.replaceState(null, '', '#' + slides[k].dataset.slug);
  };

  v.querySelector('.nav.prev').onclick = () => show(i - 1);
  v.querySelector('.nav.next').onclick = () => show(i + 1);
  ths.forEach((t, j) => t.onclick = () => show(j));

  const fs = v.querySelector('.fs');
  const toggleFs = () => {
    if (document.fullscreenElement) document.exitFullscreen();
    else if (v.requestFullscreen) v.requestFullscreen();
    else if (v.webkitRequestFullscreen) v.webkitRequestFullscreen();
  };
  if (fs) fs.onclick = toggleFs;

  // Clavier : la visionneuse en plein écran ou qui a le focus, sinon la première de la page
  document.addEventListener('keydown', e => {
    if (e.target.closest && e.target.closest('input, textarea')) return;
    const active = document.fullscreenElement
      ? document.fullscreenElement === v
      : v.contains(document.activeElement) || (vi === 0 && !document.activeElement.closest?.('[data-viewer]'));
    if (!active) return;
    if (e.key === 'ArrowLeft') { show(i - 1); e.preventDefault(); }
    if (e.key === 'ArrowRight') { show(i + 1); e.preventDefault(); }
    if (e.key === 'f' || e.key === 'F') toggleFs();
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
