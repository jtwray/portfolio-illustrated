(() => {
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
  const menu = document.querySelector('.menu-toggle');
  const links = document.querySelector('.nav-links');
  if (menu && links) {
    const close = () => { menu.setAttribute('aria-expanded', 'false'); menu.setAttribute('aria-label', 'Open navigation'); links.classList.remove('open'); };
    menu.addEventListener('click', () => {
      const expanded = menu.getAttribute('aria-expanded') === 'true';
      menu.setAttribute('aria-expanded', String(!expanded));
      menu.setAttribute('aria-label', expanded ? 'Open navigation' : 'Close navigation');
      links.classList.toggle('open', !expanded);
    });
    links.querySelectorAll('a').forEach(link => link.addEventListener('click', close));
    document.addEventListener('keydown', event => { if (event.key === 'Escape') close(); });
    document.addEventListener('click', event => { if (!menu.contains(event.target) && !links.contains(event.target)) close(); });
  }
  const filters = [...document.querySelectorAll('.filter')];
  const projects = [...document.querySelectorAll('.project')];
  filters.forEach(button => button.addEventListener('click', () => {
    const category = button.dataset.filter;
    filters.forEach(item => { const active = item === button; item.classList.toggle('active', active); item.setAttribute('aria-pressed', String(active)); });
    projects.forEach(project => { project.hidden = category !== 'all' && project.dataset.category !== category; });
  }));
  const revealEls = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('in-view'); observer.unobserve(entry.target); }
    }), { threshold: .1, rootMargin: '0px 0px -20px 0px' });
    revealEls.forEach(el => observer.observe(el));
  } else revealEls.forEach(el => el.classList.add('in-view'));
  const status = document.querySelector('.form-status');
  const form = document.querySelector('form[name="reachout"]');
  // Only known tool/action names become an editable inquiry draft. No data is sent here.
  if (form) {
    const toolNames = {
      dashboarda: 'the customer and job board',
      signaldesk: 'connected records and tool synchronization',
      'email-action': 'inbox follow-up',
      pdf: 'business document generation',
      canary: 'technical diagnostics and maintenance',
      'saas-starter': 'a custom business application',
      reminders: 'customer confirmations and reminders'
    };
    const requests = {
      setup: "I'd like help setting up ",
      repair: "I'd like help fixing a workflow similar to ",
      walkthrough: "I'd like to discuss ",
      'follow-up': 'Please follow up with me about '
    };
    const params = new URLSearchParams(location.search);
    const tool = params.get('tool');
    const request = params.get('request');
    const message = form.querySelector('textarea[name="message"]');
    if (Object.hasOwn(toolNames, tool) && Object.hasOwn(requests, request) && message && !message.value.trim()) {
      message.value = requests[request] + toolNames[tool] + ' for my business.\n\nMy business and what I need:\n';
      if (status) status.textContent = 'Your tool inquiry is drafted above. Edit it, then submit when you are ready.';
    }
  }
  if (form && location.protocol === 'file:') form.addEventListener('submit', event => {
    event.preventDefault();
    if (status) status.textContent = 'The form needs Netlify hosting to send. Please use the email link for now.';
  });
})();
