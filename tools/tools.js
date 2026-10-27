(() => {
  const controls = document.getElementById('demo-controls');
  const rows = document.getElementById('demo-rows');
  if (!controls || !rows) return;

  const stages = [
    ['new', 'New inquiry'],
    ['quoted', 'Quote sent'],
    ['scheduled', 'Scheduled'],
    ['completed', 'Completed']
  ];
  const initial = [
    { id: 'sample-100', name: 'Jamie Cole', request: 'Seasonal yard cleanup', source: 'Website form', stage: 'new' },
    { id: 'sample-101', name: 'Morgan Lee', request: 'Gutter clearing', source: 'Phone inquiry', stage: 'quoted' },
    { id: 'sample-102', name: 'Avery Reed', request: 'Small fence repair', source: 'Email inquiry', stage: 'scheduled' },
    { id: 'sample-103', name: 'Casey Brooks', request: 'Hedge trimming', source: 'Website form', stage: 'new' },
    { id: 'sample-104', name: 'Riley Quinn', request: 'Deck wash', source: 'Phone inquiry', stage: 'scheduled' },
    { id: 'sample-105', name: 'Taylor Lane', request: 'Leaf removal', source: 'Referral', stage: 'completed' }
  ];
  const extra = { id: 'sample-106', name: 'Jordan Ellis', request: 'Patio cleaning', source: 'Website form', stage: 'new' };
  let items = initial.map(item => ({ ...item }));
  const search = document.getElementById('demo-search');
  const filter = document.getElementById('demo-stage');
  const add = document.getElementById('demo-add');
  const reset = document.getElementById('demo-reset');
  const feedback = document.getElementById('demo-feedback');
  const stats = {
    total: document.getElementById('stat-total'),
    new: document.getElementById('stat-new'),
    scheduled: document.getElementById('stat-scheduled'),
    completed: document.getElementById('stat-completed')
  };

  function cell(tag, text) {
    const element = document.createElement(tag);
    element.textContent = text;
    return element;
  }

  function render(message = '') {
    const query = search.value.trim().toLocaleLowerCase();
    const visible = items.filter(item =>
      (filter.value === 'all' || item.stage === filter.value) &&
      [item.name, item.request, item.source].some(value => value.toLocaleLowerCase().includes(query))
    );
    const fragment = document.createDocumentFragment();
    visible.forEach(item => {
      const row = document.createElement('tr');
      const name = cell('th', item.name);
      name.scope = 'row';
      row.append(name, cell('td', item.request), cell('td', item.source));
      const stageCell = document.createElement('td');
      const select = document.createElement('select');
      select.dataset.inquiry = item.id;
      select.setAttribute('aria-label', 'Stage for ' + item.name);
      stages.forEach(([value, label]) => {
        const option = document.createElement('option');
        option.value = value;
        option.textContent = label;
        select.append(option);
      });
      select.value = item.stage;
      stageCell.append(select);
      row.append(stageCell);
      fragment.append(row);
    });
    if (!visible.length) {
      const row = document.createElement('tr');
      const empty = cell('td', 'No sample inquiries match. Try another search or reset the sample.');
      empty.colSpan = 4;
      empty.className = 'demo-empty';
      row.append(empty);
      fragment.append(row);
    }
    rows.replaceChildren(fragment);
    stats.total.textContent = String(items.length);
    ['new', 'scheduled', 'completed'].forEach(stage => {
      stats[stage].textContent = String(items.filter(item => item.stage === stage).length);
    });
    feedback.textContent = (message ? message + ' ' : '') + 'Showing ' + visible.length + ' of ' + items.length + ' fictional inquiries.';
  }

  search.addEventListener('input', () => render());
  filter.addEventListener('change', () => render());
  rows.addEventListener('change', event => {
    if (!(event.target instanceof HTMLSelectElement)) return;
    const select = event.target;
    const item = items.find(entry => entry.id === select.dataset.inquiry);
    const stage = stages.find(([value]) => value === select.value);
    if (!item || !stage) return;
    item.stage = stage[0];
    render(item.name + ' moved to ' + stage[1] + '.');
    const replacement = Array.from(rows.querySelectorAll('select')).find(entry => entry.dataset.inquiry === item.id);
    (replacement || filter).focus({ preventScroll: true });
  });
  add.addEventListener('click', () => {
    if (items.some(item => item.id === extra.id)) return;
    items.unshift({ ...extra });
    search.value = '';
    filter.value = 'all';
    add.disabled = true;
    add.textContent = 'Sample inquiry added';
    render('Jordan Ellis added to the board. Change their stage to try the next step.');
  });
  reset.addEventListener('click', () => {
    items = initial.map(item => ({ ...item }));
    search.value = '';
    filter.value = 'all';
    add.disabled = false;
    add.textContent = 'Add sample inquiry +';
    render('Sample reset.');
  });
  render();
  controls.hidden = false;
})();
