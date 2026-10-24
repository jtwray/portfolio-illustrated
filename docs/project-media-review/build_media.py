from pathlib import Path
import json, html, base64, textwrap, shutil, zipfile
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
SHA={'dashboarda':'56a0b1b0aa7d2e571696e74f7f31a6568680aa67','canary':'ed9703c7ead7c36ecf4b5554d56fa9cfc88501aa','potty':'63495ae2796ef04fdd2e2aa55f4e39ae62a723e5'}
projects=[
dict(id='wamif', name='WAMIF', subtitle='Making family history explorable', color='#285a49',
 card='Turn genealogy records into individual life routes and a shared chronology, with uncertainty kept visible.',
 skills=['React','TypeScript','Domain modeling','Data visualization'],
 demo='https://wamif-rebuild.netlify.app/',repo=None,
 status='Live application · private source',
 star=[
 ('Situation','Genealogy files describe people, family relationships, dates, and places in separate records. Understanding how lives unfold across geography requires assembling those records while keeping incomplete dates and unresolved places visible.'),
 ('Task','Provide an explorable view of an individual life and a recorded ancestor-to-descendant lineage, without presenting uncertain dates as exact occurrences or relationship links as geographic travel.'),
 ('Action','The React/TypeScript application separates GEDCOM parsing, normalization, place resolution, relationship queries, chronology, and rendering. Individual routes retain their own events. Lineage uses a recorded direct relationship path and shared calendar boundaries while keeping each person’s route independent. Event detail explains date and location interpretation; local SVG works without an external map provider.'),
 ('Result','The live sample was opened on October 23, 2026. Individual event stepping, selected-event details, and a four-person lineage workspace were observed and captured. The October 22 evidence audit separately links the deployed master revision to successful CI. This demonstrates an inspectable application; it does not establish genealogy accuracy, adoption, or configured Mapbox behavior.')],
 deep=[
 ('One life, many records','Problem: dates and places are scattered through GEDCOM records. Approach: normalize life events, retain place-resolution provenance, and build a chronological route. Result observed: stepping the sample changed the active event, route, and story panel. Unknown-date records remained inspectable.'),
 ('Several generations, one calendar','Problem: a relationship chain is easy to misread as one continuous trip. Approach: derive recorded parent-child paths, retain per-person routes, and reveal them on shared chronology boundaries. Result observed: the sample opened four people with three recorded handoffs. Relationships remain untimed context.'),
 ('Uncertainty and visual overlap','Problem: approximate dates and nearby markers can imply more certainty than the records support. Approach: explain intervals and location provenance, distinguish collision disclosures from shared geography, and keep inspection separate from playback. The newer lineage spiderfy PR was separate from the audited production revision; it is not advertised here as released.')],
 limitation='Screenshots use the application’s bundled content labeled synthetic. Source is private. No private repository images or family uploads are included. External geocoding and Mapbox/globe configuration were not exercised.',
 shots=[('portfolio-wamif-route.jpg','Individual Life Route','Live synthetic sample: route diagram, current event, and chronological event rail.'),('portfolio-wamif-detail.jpg','Explain the selected event','Live synthetic sample: stepping to a marriage and opening its event/provenance detail.'),('portfolio-wamif-lineage.jpg','Independent routes on shared chronology','Live synthetic sample: an opened four-person lineage after stepping calendar boundaries. This is the SVG renderer, not a geographic basemap.')],
 refs=[('Public demo','https://wamif-rebuild.netlify.app/')],
 evidence='ProofTree PRJ-0003, EV-0007–EV-0010; architecture and domain source at 612a76432a8014c8d228ee1c0fca28ccdedd5010; live browser observations 2026-10-23.'),
dict(id='dashboarda',name='Dashboarda',subtitle='Keeping repeated research usable',color='#8a4b2a',
 card='Purpose-built dashboards retain stable records and run history; the SignalDesk extension connects research to an Airtable workflow.',
 skills=['TypeScript','Serverless APIs','Data synchronization','Integration design'],
 demo=None,repo='https://github.com/jtwray/dashboarda',status='Public source · live dashboard requires PIN',
 star=[
 ('Situation','Repeated research produces overlapping items, while follow-up decisions need durable records. Copying the same information between a dashboard and a work tracker can create duplicates or overwrite human-owned notes and task state.'),
 ('Task','Keep small dashboards independently deployable and make repeated imports reconcile stable identities. For the SignalDesk extension, synchronize research fields while preserving Airtable-owned qualification and activity state.'),
 ('Action','Dashboarda’s state handlers use Netlify Functions and Blobs, stable item keys, first/last-seen metadata, and bounded run history. The SignalDesk feature branch reuses persisted identities, maps allowlisted research fields, compares destination records, skips unchanged items, and applies bounded retries. Research synchronization and native Airtable task automation have separate responsibilities.'),
 ('Result','The reviewed source and public SignalDesk PR provide concrete implementation evidence. The October 22 audit records successful feature CI and a ready deployment with a registered cron. The October 23 live page prompted for a PIN, so no private dashboard data was captured. An independently observed unattended synchronization run remains an evidence gap.')],
 deep=[('Stable records across repeated updates','The state handler chooses a stable identity and retains firstSeenAt, lastSeenAt, and seenCount. This gives repeated observations a durable record instead of an append-only pile of copies.'),('SignalDesk: separate research from follow-up','Research fields belong to the synchronizer; qualification, notes, and activity lifecycle belong to Airtable. The branch uses destination diffing and upserts. The public PR is a feature-specific receipt, not evidence that every dashboard is continuously operating.')],
 limitation='The live dashboard is PIN gated and is not a suitable anonymous portfolio demo. Public repository/PR images are documentation and source evidence. Scheduled deployment is distinct from observed scheduled execution.',
 shots=[('portfolio-dashboarda-pr.jpg','SignalDesk change under review','Public draft PR #2. Its body contains project-reported receipts; the screenshot does not independently reproduce those runs.'),('portfolio-dashboarda-state.jpg','Durable state and stable identity','Public state-handler source; source evidence rather than a runtime screenshot.'),('portfolio-dashboarda-repository.jpg','Small apps, one repository','Public repository showing the independently deployable dashboard apps.')],
 refs=[('Public repository','https://github.com/jtwray/dashboarda'),('SignalDesk PR #2','https://github.com/jtwray/dashboarda/pull/2'),('Pinned state handler','https://github.com/jtwray/dashboarda/blob/'+SHA['dashboarda']+'/apps/local-prospects/netlify/functions/state.mts'),('SignalDesk source','https://github.com/jtwray/dashboarda/blob/ad436cf3d4cec4ced7e14ef465235416cf39454e/apps/local-prospects/signaldesk/sync.ts')],
 evidence='ProofTree PRJ-0001, EV-0001–EV-0004 and EV-0017; Dashboarda main 56a0b1b0aa7d2e571696e74f7f31a6568680aa67; SignalDesk head ad436cf3d4cec4ced7e14ef465235416cf39454e. Live PIN gate observed 2026-10-23.'),
dict(id='canary',name='Agent Toolchain Canary',subtitle='Finding the failing layer',color='#7b6229',
 card='Read-only toolchain probes turn environment and access failures into redacted, classified diagnostic reports.',
 skills=['Node.js','Developer tooling','Failure classification','Safe scheduling design'],
 demo=None,repo='https://github.com/jtwray/agent-toolchain-canary',status='Public CLI · source inspected',
 star=[
 ('Situation','An agent workflow may fail because a runtime is missing, repository access is unavailable, or an endpoint cannot be reached. Repeating checks manually makes it harder to distinguish a new fault from a recurring one and risks copying sensitive diagnostic output.'),
 ('Task','Provide a repeatable diagnostic utility that checks specific layers, redacts reports, compares outcomes across runs, and keeps durable operational guidance under human review.'),
 ('Action','The Node CLI defines runtime, Git, GitHub API, HTTPS, and loopback probes. An allowlist constrains subprocess commands. Report persistence applies redaction, run locking prevents overlap, and previous-state comparison classifies new, repeated, recovered, and retirement-candidate outcomes. Scheduler adapters describe Windows, macOS, and Linux execution paths without conflating an ordinary Node process with connected agent plugins.'),
 ('Result','The public implementation and scheduling documentation are inspectable at a pinned revision, with test definitions in the repository. This package captures the repository, scheduling contract, and classification source. No fresh test run, installed schedule, unattended run, or measured reduction in troubleshooting time is claimed.')],
 deep=[('A useful boundary around automation','The tool checks what an ordinary local process can observe. Connected plugin identity and agent browser behavior remain explicit manual or agent-assisted checks. This makes its diagnostic scope understandable.'),('Incident memory, with human review','A repeated matching failure is different from a first failure; recovery is different from durable resolution. Classification informs review, while people decide changes to operational guidance.')],
 limitation='This is a command-line utility, so no Netlify web-app link is applicable. Repository screenshots show source/documentation, not captured successful execution. Cross-platform operation still needs platform-specific receipts.',
 shots=[('portfolio-canary-overview.jpg','The diagnostic contract','Public README explaining scope, setup, and redacted local reports.'),('portfolio-canary-scheduling.jpg','Scheduling boundaries','Public scheduling documentation distinguishing planning from explicit installation/removal.'),('portfolio-canary-classification.jpg','Classification and persistence','Public state.js source. The repository is compact/minified; use the diagram as the primary visual and this capture as a secondary receipt.')],
 refs=[('Public repository','https://github.com/jtwray/agent-toolchain-canary'),('Pinned probes','https://github.com/jtwray/agent-toolchain-canary/blob/'+SHA['canary']+'/src/probes.js'),('Pinned classification','https://github.com/jtwray/agent-toolchain-canary/blob/'+SHA['canary']+'/src/state.js'),('Pinned safety','https://github.com/jtwray/agent-toolchain-canary/blob/'+SHA['canary']+'/src/safety.js')],
 evidence='ProofTree PRJ-0002, EV-0005–EV-0006 and Slice 1.4 EV-0019; source ed9703c7ead7c36ecf4b5554d56fa9cfc88501aa; public browser captures 2026-10-23.'),
dict(id='potty',name='Potty Weekend',subtitle='A little less to remember',color='#3c597a',
 card='A calm practice-day aid combines reminders, fast attempt logging, and history stored in the same browser.',
 skills=['Browser UX','IndexedDB','Storage boundaries','Domain logic'],
 demo='https://potty-weekend.netlify.app/',repo='https://github.com/jtwray/potty-weekend',status='Live application · public source',
 star=[
 ('Situation','A parent supporting a practice day has to notice cues, remember check-ins, and recall recent attempts. The tool needs to support that activity without turning the child’s progress into a performance target.'),
 ('Task','Make reminders and quick logging available in one simple interface, with persistent local history and clear limits around device storage, notifications, and observational estimates.'),
 ('Action','The single-page application combines a foreground reminder, fast attempt entry, calm feedback, and a history view. A storage port separates the UI from an IndexedDB adapter. Stable IDs and schema versions leave a migration seam; optional photos are stored separately from record metadata. The current scope keeps logs on one browser/device and does not ship parent sharing or cloud backup.'),
 ('Result','The live reminder, entry, and empty-history views were observed and captured on October 23, 2026, without creating child records. The reviewed source contains the persistence boundary and domain logic, and the October 22 audit records a ready static deployment. Real-device persistence, camera behavior, and a full practice day remain separate checks; no training outcome is claimed.')],
 deep=[('Small product, substantive engineering','A narrow purpose still creates meaningful design decisions: a persisted absolute reminder deadline, an injectable storage interface, atomic photo/record operations, and clear local-data boundaries. These are better explained as one short engineering section than several nested case studies.')],
 limitation='All captures show an empty browser session; no real child records or bowl photos are included. Logs are local to the browser, device, and origin. No cloud sync, reliable closed-tab alerts, or promised training result.',
 shots=[('portfolio-potty-overview.jpg','Start with a calm reminder','Live empty-session reminder view; no child data.'),('portfolio-potty-entry.jpg','Fast attempt entry','Live empty-session interface while exploring an outcome option; no attempt was saved.'),('portfolio-potty-history.jpg','History and data boundaries','Live empty-session summary/log, including the local-storage and export explanation.')],
 refs=[('Live application','https://potty-weekend.netlify.app/'),('Public repository','https://github.com/jtwray/potty-weekend'),('Pinned storage interface','https://github.com/jtwray/potty-weekend/blob/'+SHA['potty']+'/public/storage.js')],
 evidence='ProofTree PRJ-0004, EV-0011–EV-0013; source 63495ae2796ef04fdd2e2aa55f4e39ae62a723e5; live browser observations 2026-10-23.')]

# Original schematic diagrams. Problem views describe design context, not measured past harm.
diagrams={
'wamif':{
 'problem':(['Genealogy records','People, family links, dates, places'],['Reconstruct geography','Which place belongs to which event?'],['Reconstruct chronology','What is dated, uncertain, or missing?'],['Interpret several lives','Relationships are not travel routes'],['Hard to see the story','Keep the evidence and its limits visible']),
 'solution':(['Local GEDCOM input','Parse → normalize people and events'],['Individual life route','Resolve places → build one route'],['Recorded lineage path','Retain separate routes per person'],['Explore chronology','Step boundaries and inspect events'],['Explain the evidence','Date intervals, location provenance, gaps'])},
'dashboarda':{
 'problem':(['Repeated research','Overlapping items arrive over time'],['Reconcile records','Is this new, changed, or already seen?'],['Maintain follow-up','Notes and task state need continuity'],['Copy between systems','Risk duplicate records or lost edits'],['Unclear working state','What changed, and what needs attention?']),
 'solution':(['Dashboarda state','Stable keys + first/last-seen history'],['Dashboard view','Filter records and inspect sync metadata'],['SignalDesk extension','Map research → diff → Airtable upsert'],['Keep ownership explicit','Research fields vs human task state'],['Inspect the outcome','Run history and sanitized sync status'])},
'canary':{
 'problem':(['An agent task fails','The failure may be in several layers'],['Check environment','Runtime, CLI, Git, network'],['Check practical access','API/repository access vs auth advisory'],['Repeat manual diagnosis','Compare today with the previous fault'],['Resolve with care','Avoid sensitive logs and false certainty']),
 'solution':(['Explicit diagnostic run','Manual CLI or scheduler adapter'],['Allowlisted probes','Runtime, Git, API, HTTPS, loopback'],['Collect bounded outcomes','Pass / fail / skipped / inconclusive'],['Redact and compare','Classify against prior local state'],['Human review','Read report; approve durable guidance'])},
'potty':{
 'problem':(['Support a practice day','Notice cues while getting on with life'],['Remember check-ins','Keep a parent-chosen interval in mind'],['Recall recent attempts','What happened, and roughly when?'],['Fragmented attention','Notes and reminders can compete'],['Keep the child central','Make the tool quick and low pressure']),
 'solution':(['Parent follows cues','Reminder supports attention'],['Quick attempt log','Outcome, time, who noticed'],['Optional observation','Manual estimate or bowl-only photo'],['Save through storage port','IndexedDB on this browser/device'],['Review local history','Feedback and export; return to play'])}}

E=html.escape
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def diagram(p,kind):
    nodes=diagrams[p['id']][kind]
    # 5 nodes, top-down with a two-lane middle. Branch/rejoin applies only to independent work.
    branch=(p['id'] in ('wamif','dashboarda') or kind=='problem')
    pos=[(350,142,500,105),(66,312,500,105),(634,312,500,105),(350,482,500,105),(350,652,500,105)] if branch else [(350,142+i*140,500,105) for i in range(5)]
    height=840 if branch else 850
    edges=[(0,1),(0,2),(1,3),(2,3),(3,4)] if branch else [(i,i+1) for i in range(4)]
    ink='#233b34'; paper='#faf6ec'; accent=p['color']
    im=Image.new('RGB',(1200,height),paper); d=ImageDraw.Draw(im)
    font=lambda s,b=False:ImageFont.truetype(BOLD if b else FONT,s)
    title=f"{p['name']} · {'The problem' if kind=='problem' else 'The solution'}"
    sub='Design context · schematic, not a measured before-state' if kind=='problem' else 'Implementation overview · see case study for release and verification limits'
    d.text((45,28),title,fill=ink,font=font(32,True)); d.text((45,78),sub,fill='#59695f',font=font(18))
    svg=[f'<svg class="diagram" xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="t d"><title id="t">{E(title)}</title><desc id="d">{E(". ".join(a+": "+b for a,b in nodes))}</desc><rect width="1200" height="{height}" fill="{paper}"/><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{accent}"/></marker></defs><g font-family="DejaVu Sans,Arial,sans-serif"><text x="45" y="58" font-size="32" font-weight="bold" fill="{ink}">{E(title)}</text><text x="45" y="94" font-size="18" fill="#59695f">{E(sub)}</text>']
    for a,b in edges:
        x,y,w,h=pos[a]; xx,yy,ww,hh=pos[b]; sx=x+w/2; sy=y+h; ex=xx+ww/2; ey=yy
        pts=[(sx,sy),(sx,(sy+ey)/2),(ex,(sy+ey)/2),(ex,ey-8)]
        d.line(pts,fill=accent,width=3); d.polygon([(ex-6,ey-13),(ex+6,ey-13),(ex,ey-3)],fill=accent)
        svg.append(f'<path d="M{sx} {sy} V{(sy+ey)/2} H{ex} V{ey-5}" fill="none" stroke="{accent}" stroke-width="3" marker-end="url(#arrow)"/>')
    for i,((x,y,w,h),(head,body)) in enumerate(zip(pos,nodes)):
        d.rounded_rectangle((x,y,x+w,y+h),radius=15,fill='white',outline=accent,width=2)
        d.ellipse((x+15,y+18,x+49,y+52),fill=accent); d.text((x+26,y+23),str(i+1),fill='white',font=font(17,True))
        d.text((x+64,y+18),head,fill=ink,font=font(23,True))
        lines=textwrap.wrap(body,46)
        for k,l in enumerate(lines):d.text((x+64,y+55+k*22),l,fill='#45584f',font=font(17))
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="white" stroke="{accent}" stroke-width="2"/><circle cx="{x+32}" cy="{y+35}" r="17" fill="{accent}"/><text x="{x+32}" y="{y+41}" text-anchor="middle" fill="white" font-size="17" font-weight="bold">{i+1}</text><text x="{x+64}" y="{y+37}" fill="{ink}" font-size="23" font-weight="bold">{E(head)}</text>')
        for k,l in enumerate(lines):svg.append(f'<text x="{x+64}" y="{y+73+k*22}" fill="#45584f" font-size="17">{E(l)}</text>')
    foot='Original portfolio diagram · October 23, 2026 · Arrows describe information/workflow, not proven user outcomes.'
    d.text((45,height-32),foot,fill='#59695f',font=font(15));svg.append(f'<text x="45" y="{height-18}" font-size="15" fill="#59695f">{E(foot)}</text></g></svg>')
    stem=ROOT/'assets/diagrams'/f"{p['id']}-{kind}"
    stem.with_suffix('.svg').write_text(''.join(svg));im.save(stem.with_suffix('.png'))
    mer=['flowchart TD']
    for i,(a,b) in enumerate(nodes):mer.append(f'  n{i}["{a}: {b}"]')
    for a,b in edges:mer.append(f'  n{a} --> n{b}')
    stem.with_suffix('.mmd').write_text('\n'.join(mer)+'\n')
    return ''.join(svg)

css='''*{box-sizing:border-box}body{margin:0;background:#faf6ec;color:#253b34;font:17px/1.65 system-ui,sans-serif}main,header,footer{max-width:1160px;margin:auto;padding:34px 28px}header{border-bottom:1px solid #c9c8b8}a{color:#285a49;text-underline-offset:4px}h1,h2,h3{font-family:Georgia,serif;line-height:1.12}h1{font-size:clamp(36px,6vw,68px);max-width:900px}h2{font-size:38px}h3{font-size:25px}.eyebrow{letter-spacing:.13em;text-transform:uppercase;font-size:12px;font-weight:700}.intro{max-width:780px;font-size:20px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}.card{background:#fffdf7;border:1px solid #c9c8b8;border-radius:12px;overflow:hidden}.card .copy{padding:25px}.card h2{font-size:32px}.card img{width:100%;height:240px;object-fit:cover;object-position:top;border-bottom:1px solid #ddd}.tags{font-size:13px;color:#59695f}.button{display:inline-block;border:1px solid currentColor;border-radius:5px;padding:9px 16px;margin:5px 10px 5px 0;text-decoration:none}.primary{background:#285a49;color:white}.project{padding-top:65px;border-top:1px solid #c9c8b8;margin-top:60px;scroll-margin-top:20px}.project:target{outline:3px solid #c49b4a;outline-offset:14px}.lead{font-size:22px;max-width:800px}.notice{border-left:3px solid #b58d3e;padding:12px 20px;background:#f0eadb;max-width:920px}.star{display:grid;grid-template-columns:130px 1fr;gap:10px 25px;max-width:930px}.star h3{margin:18px 0}.star p{margin:14px 0}.diagram{width:100%;height:auto;display:block;border:1px solid #ded8c9}.gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}.gallery img{width:100%;height:200px;object-fit:cover;object-position:top;border:1px solid #d8d3c5}figure{margin:0}figcaption{font-size:14px;line-height:1.5;margin-top:10px}.proof{font-size:14px}.links{display:flex;gap:8px;flex-wrap:wrap}details{border-top:1px solid #c9c8b8;padding:18px 0}summary{font-weight:700;cursor:pointer}img{max-width:100%}:focus-visible{outline:3px solid #c49b4a;outline-offset:4px}footer{font-size:14px} @media(max-width:720px){.grid,.gallery{grid-template-columns:1fr}.star{grid-template-columns:1fr;gap:0}.star h3{margin-bottom:0}.gallery img{height:auto}main,header,footer{padding:25px 18px}.project{padding-top:35px}.card img{height:auto}}'''
def uri(path):
    typ={'.jpg':'image/jpeg','.svg':'image/svg+xml','.png':'image/png'}[path.suffix]
    return 'data:'+typ+';base64,'+base64.b64encode(path.read_bytes()).decode()
def links(p):
    return ''.join(f'<a class="button" href="{E(url)}" target="_blank" rel="noopener noreferrer">{E(label)} ↗</a>' for label,url in p['refs'])

cards=[];sections=[];man=[]
allmd=['# Illustrated portfolio — four project stories\n\nPrepared October 23, 2026. Review draft; not published.\n\nThese are project-level STAR narratives. Exact human/agent contribution must be confirmed before converting Action sections to first person. Results distinguish source, tests, deployment, and observed behavior.']
for p in projects:
    svgs={kind:diagram(p,kind) for kind in ('problem','solution')}
    available=[s for s in p['shots'] if (ROOT/'assets/screenshots'/s[0]).exists()]
    hero=uri(ROOT/'assets/screenshots'/available[0][0])
    cards.append(f'<article class="card"><a href="#{p["id"]}"><img src="{hero}" alt="{E(available[0][1])}" width="1348" height="926"></a><div class="copy"><p class="eyebrow">{E(p["status"])}</p><h2>{E(p["name"])}</h2><p>{E(p["card"])}</p><p class="tags">{E(" · ".join(p["skills"]))}</p><a class="button primary" href="#{p["id"]}">Read case study</a></div></article>')
    gallery=[]
    for filename,title,caption in available:
        src=uri(ROOT/'assets/screenshots'/filename)
        gallery.append(f'<figure><a href="assets/screenshots/{filename}" target="_blank" rel="noopener noreferrer"><img src="{src}" alt="{E(title+": "+caption)}" loading="lazy"></a><figcaption><strong>{E(title)}</strong><br>{E(caption)}</figcaption></figure>')
        man.append(dict(project=p['id'],file='assets/screenshots/'+filename,type='browser screenshot',title=title,caption=caption,captured_on='2026-10-23',publication_note='Public-source capture' if p['id'] in ('canary','dashboarda') else 'Live app, synthetic or empty session'))
    stat=''.join(f'<h3>{a}</h3><p>{E(b)}</p>' for a,b in p['star'])
    deeper=''.join(f'<details><summary>{E(a)}</summary><p>{E(b)}</p></details>' for a,b in p['deep'])
    sections.append(f'<section class="project" id="{p["id"]}"><p class="eyebrow">{E(p["status"])}</p><h2>{E(p["name"])} — {E(p["subtitle"])}</h2><p class="lead">{E(p["card"])}</p><div class="links">{links(p)}</div><h3>The story</h3><div class="star">{stat}</div><h3>From problem to solution</h3><div class="grid"><figure>{svgs["problem"]}<figcaption>Problem context: an explanatory model, not measured historical impact. <a href="assets/diagrams/{p["id"]}-problem.svg" target="_blank" rel="noopener noreferrer">Open full-size diagram ↗</a></figcaption></figure><figure>{svgs["solution"]}<figcaption>Implemented approach: release and runtime limits are stated in the story. <a href="assets/diagrams/{p["id"]}-solution.svg" target="_blank" rel="noopener noreferrer">Open full-size diagram ↗</a></figcaption></figure></div><h3>See the evidence</h3><div class="gallery">{"".join(gallery)}</div><h3>Engineering details</h3>{deeper}<p class="notice">{E(p["limitation"])}</p><p class="proof"><strong>Contribution note:</strong> AI-assisted project work. The precise division of problem framing, architecture, implementation, review, and operation is awaiting Tucker’s confirmation; these drafts describe project artifacts rather than claiming sole manual authorship.</p><a href="#projects">Back to projects ↑</a></section>')
    md=f'# {p["name"]}\n\n{p["subtitle"]}\n\n**Card:** {p["card"]}\n\n**Skills:** {", ".join(p["skills"])}\n\n**Status:** {p["status"]}\n\n'
    md+='\n\n'.join(f'## {a}\n\n{b}' for a,b in p['star'])
    md+='\n\n## Feature stories\n\n'+'\n\n'.join(f'### {a}\n\n{b}' for a,b in p['deep'])
    md+='\n\n## Media\n\n'+'\n'.join(f'- [{a}](assets/screenshots/{f}): {b}' for f,a,b in available)
    md+='\n\n## Links\n\n'+'\n'.join(f'- [{a}]({b})' for a,b in p['refs'])
    md+='\n\n## Evidence and limits\n\n'+p['evidence']+'\n\n'+p['limitation']+'\n\n**Contribution:** Confirm exact human and AI roles before first-person publication. No personal claim is approved by this draft.\n'
    (ROOT/f'{p["id"]}-story.md').write_text(md)
    allmd.append(md)
head='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tucker Wray — Project media review</title>'''
body='''<header><p class="eyebrow">Tucker Wray · Illustrated portfolio media review</p><h1>Useful software.<br>Visible engineering.</h1><p class="intro">Four project stories, with the problem up front and the implementation behind it. Browse the cards, follow the diagrams, and inspect the supporting captures.</p><p class="notice">Review draft · October 23, 2026. Project-level narratives; contribution wording needs confirmation before publication. This preview is separate from the live portfolio.</p></header><main><section id="projects"><p class="eyebrow">Selected projects</p><div class="grid">'''
out=head+'<style>'+css+'</style>'+body+''.join(cards)+'</div></section>'+''.join(sections)+'</main><footer>Original diagrams and live/public-source captures. No private repository source, personal dashboard contents, or uploaded family/child records are included.</footer></html>'
(ROOT/'index.html').write_text(out)
(ROOT/'project-content.json').write_text(json.dumps(projects,indent=2)+'\n')
(ROOT/'media-manifest.json').write_text(json.dumps(man,indent=2)+'\n')
(ROOT/'STAR-stories.md').write_text('\n\n---\n\n'.join(allmd))
(ROOT/'README.md').write_text('''# Illustrated portfolio media review package

Open `index.html` for the self-contained card-to-case-study review. It embeds the diagrams and gallery previews, so no server/build/install is needed. Full-resolution image links use the accompanying assets folder.

## Included

- Four project-level STAR drafts, editable individually and together.
- Eight original workflow diagrams, each as SVG, PNG, and Mermaid source.
- Browser screenshots and caption/provenance manifest. Dashboarda uses public repository/PR captures because its app requires a PIN. Canary is a CLI, so source/documentation is its evidence surface.
- JSON content for later website integration.
- A bounded integration slice and publication checklist in `INTEGRATION.md`.

## Reading levels

1. Card: one problem/value sentence, 3–4 skills, one primary “Read case study” link.
2. Case study: short STAR story, problem/solution diagram pair, evidence gallery, suitable external links.
3. Optional engineering details: WAMIF has three feature stories; Dashboarda two; Canary two; Potty Weekend one compact engineering note. No recursive nesting.

## Captures

Captured October 23, 2026. Browser viewport captures are actual UI, not generated mockups. WAMIF used the bundled content labeled synthetic; Potty Weekend used an empty session. No attempts or child data were saved. Public GitHub screenshots are mutable-branch observations; immutable links in story evidence point to reviewed source revisions. A PR description reports its author's results and is not independent verification of those results.

## Claims

This is a review package, not an approved personal-claim publication. Confirm Tucker's precise human-versus-agent contribution. Do not infer time savings, users, revenue, parent outcomes, or unattended reliability from source/deploy existence. WAMIF's newer collision-spiderfy PR is separate from the reviewed production revision. Potty Weekend's live page differs in details from the older README; captions describe observed screens without turning them into verified device behavior.

## Files

Diagrams and STAR text are original authored assets. Screenshots retain public product/repository chrome and need their contextual captions. Use live screenshots as gallery proof; keep conceptual portfolio artwork separately labeled as illustration. Source checkouts, credentials, raw private records, and private code are excluded.
''')
(ROOT/'INTEGRATION.md').write_text('''# Proposed slice: illustrated project evidence pages

This package was created in response to Tucker's October 23 media request. It does not modify the live illustrated portfolio, existing PRs, application code, DNS, or deployments.

## Recommended UX

Keep the illustrated visual identity. Four featured cards should link in the same tab to real pages: `/projects/wamif/`, `/projects/dashboarda/`, `/projects/agent-toolchain-canary/`, `/projects/potty-weekend/`. This review's anchors demonstrate the information hierarchy; production should use dedicated, shareable pages with sensible back navigation. Keep existing unrelated portfolio work/history available rather than deleting it as part of this slice.

Each card: conceptual illustration or actual product capture, precise one-sentence value, three or four supported skill tags, status, one “Read case study” primary action. On each case-study page show a screenshot, concise problem/result, contribution statement, story, diagrams, evidence gallery, then optional technical sections. Keep evidence limitations next to the relevant claim. Screenshots open in a keyboard-accessible full-size view. Preserve text captions and descriptive alt text.

External app/repository links use `target="_blank" rel="noopener noreferrer"` and a visible new-tab indicator. WAMIF and Potty Weekend have app links. WAMIF source remains private. Dashboarda points to public source/PR; do not present the PIN-gated dashboard as an anonymous demo. Canary points to its public repository; do not invent a Netlify app.

## Feature depth

- WAMIF: 1 parent STAR + individual routes, multi-person chronology, uncertainty/visual-overlap engineering details. Keep unreleased spiderfy work clearly separate.
- Dashboarda: 1 parent STAR + stable identity and SignalDesk details. Keep branch/deploy/runtime states distinct.
- Canary: 1 parent STAR + probe boundaries and incident lifecycle details. Prefer diagrams to tiny code images.
- Potty Weekend: 1 parent STAR + one short storage/UX section. A narrow product can demonstrate strong engineering without more nesting.

## Implementation boundary

Re-read current portfolio branch, PRs, roadmap and AGENTS.md before creating a fresh feat/* branch. Reconcile any in-flight portfolio change requests, including the resume-menu behavior, before implementation. Do not append this work blindly to an existing PR. Update the roadmap with a new unambiguous slice ID after inspecting current IDs.

## Acceptance

- Four cards reach four accessible case-study pages; live app/source CTAs follow the rules above.
- At least one relevant evidence capture per project, ideally three. Package currently contains 3 for WAMIF, 3 for Potty Weekend, 3 for Canary, and 3 for Dashboarda.
- Confirm exact personal role and agent assistance; keep results matched to observed evidence. Avoid blocked publication becoming a reason to erase legitimate firsthand contribution.
- Diagrams remain legible on mobile: show vertically or open full size, with equivalent text. Do not squeeze two diagrams into unreadable columns.
- Verify keyboard navigation, disclosure controls, link targets, images, 360px layout, and existing contact/resume behavior on a preview.
- No private code, real genealogy uploads, dashboard records, child logs/photos, credentials, or unsupported metrics.
- Only merge/publish through the user's established review workflow.

## Optional fifth project

Keep this slice at four. ProofTree may later become an evidence-system case study; Eagle Rock Animal ER may be the strongest client-outcome story once its receipts and shareable material are assembled. Neither is represented by fabricated media in this package.
''')
(ROOT/'EVIDENCE-LEDGER.md').write_text('# Editorial evidence ledger\n\nReviewed October 23, 2026. Private sources were read only for sanitized descriptions; no private code copied.\n\n'+'\n\n'.join('## '+p['name']+'\n\n'+p['evidence']+'\n\n'+p['limitation'] for p in projects))
print('Created four case studies, eight diagram sets, and',len(man),'screenshot entries.')
